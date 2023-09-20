import os
import network
from flashbdev import bdev


def fwupdate(fn, erase_all=False, safe_check=True, verbose=True):
    import esp

    fw_size = rem_fs = os.stat(fn)[6]
    esp.set_dfu(0, fw_size)
    with open(fn, "rb") as fp:
        while fp.read(4096):
            pass

    if safe_check:
        blks = esp.get_blks()
        if blks is None:
            raise Exception(f"No blocks data found for the file {fn}")
        blks, offs = blks
        esp.set_dfu(-1, fw_size)
        if verbose:
            print(f"Verifying sector data:{blks} {offs}")
        with open(fn, "rb") as fp:
            for ii, blkid in enumerate(blks):
                sz = min(rem_fs, 4096 - offs[ii])
                L2 = esp.flash_read(esp.flash_user_start() + blkid * 4096 + offs[ii], sz)
                L1 = fp.read(sz)
                if L1 != L2:
                    raise Exception("Data is different at N={ii} blkid={blkid}")
                del L1, L2
                rem_fs -= sz
                if verbose:
                    print(f"{ii}/{len(blks)}", end="\r")
        esp.set_dfu(len(blks), fw_size)
        del blks, offs
        if verbose:
            print("Success, starting firmware update ...")

    esp.DFU(erase_all)


def wifi():
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(True)
    # ssid = 'MicroPython-' + ap_if.config("mac")[-3:].hex()
    # ap_if.config(ssid=ssid, security=network.AUTH_WPA_WPA2_PSK, key=b"micropythoN")


def check_bootsec():
    buf = bytearray(bdev.SEC_SIZE)
    bdev.readblocks(0, buf)
    empty = True
    for b in buf:
        if b != 0xFF:
            empty = False
            break
    if empty:
        return True
    fs_corrupted()


def fs_corrupted():
    import time
    import micropython

    # Allow this loop to be stopped via Ctrl-C.
    micropython.kbd_intr(3)

    while 1:
        print(
            """\
The filesystem starting at sector %d with size %d sectors looks corrupt.
You may want to make a flash snapshot and try to recover it. Otherwise,
format it with os.VfsLfs2.mkfs(bdev), or completely erase the flash and
reprogram MicroPython.
"""
            % (bdev.start_sec, bdev.blocks)
        )
        time.sleep(3)


def setup():
    check_bootsec()
    print("Performing initial setup")
    wifi()
    os.VfsLfs2.mkfs(bdev)
    vfs = os.VfsLfs2(bdev)
    os.mount(vfs, "/")
    with open("boot.py", "w") as f:
        f.write(
            """\
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import os, machine
#os.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()
"""
        )
    return vfs
