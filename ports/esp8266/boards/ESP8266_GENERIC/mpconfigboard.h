#if defined(MICROPY_ESP8266_2M)

#define MICROPY_HW_BOARD_NAME "ESP module"
#define MICROPY_HW_MCU_NAME "ESP8266"

#define MICROPY_PERSISTENT_CODE_LOAD    (1)
#define MICROPY_EMIT_XTENSA             (1)
#define MICROPY_EMIT_INLINE_XTENSA      (1)

#define MICROPY_DEBUG_PRINTERS          (1)
#define MICROPY_ERROR_REPORTING         (MICROPY_ERROR_REPORTING_NORMAL)

#define MICROPY_READER_VFS              (MICROPY_VFS)
#define MICROPY_VFS                     (1)

#define MICROPY_PY_CRYPTOLIB            (1)
#define MICROPY_DFU                     (1)

#elif defined(MICROPY_ESP8266_1M)

#define MICROPY_HW_BOARD_NAME "ESP module (1M)"
#define MICROPY_HW_MCU_NAME "ESP8266"

#define MICROPY_PERSISTENT_CODE_LOAD    (1)
#define MICROPY_EMIT_XTENSA             (1)
#define MICROPY_EMIT_INLINE_XTENSA      (1)

#define MICROPY_DEBUG_PRINTERS          (1)
#define MICROPY_ERROR_REPORTING         (MICROPY_ERROR_REPORTING_NORMAL)

#define MICROPY_READER_VFS              (MICROPY_VFS)
#define MICROPY_VFS                     (1)


#define MICROPY_PY_CRYPTOLIB            (1)

#elif defined(MICROPY_ESP8266_512K)

#define MICROPY_HW_BOARD_NAME "ESP module (512K)"
#define MICROPY_HW_MCU_NAME "ESP8266"

#define MICROPY_ERROR_REPORTING         (MICROPY_ERROR_REPORTING_TERSE)

#define MICROPY_PY_FSTRINGS             (0)
#define MICROPY_PY_BUILTINS_SLICE_ATTRS (0)
#define MICROPY_PY_ALL_SPECIAL_METHODS  (0)
#define MICROPY_PY_REVERSE_SPECIAL_METHODS (0)
#define MICROPY_PY_SYS_STDIO_BUFFER     (0)
#define MICROPY_PY_ASYNCIO              (0)
#define MICROPY_PY_RE_SUB               (0)
#define MICROPY_PY_FRAMEBUF             (0)

#endif
