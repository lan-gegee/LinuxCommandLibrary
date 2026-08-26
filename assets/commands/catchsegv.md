# TAGLINE

捕获段错误并打印回溯信息

# TLDR

**运行程序并捕获段错误**

```catchsegv [./program]```

**带参数运行**

```catchsegv [./program] [arg1] [arg2]```

# SYNOPSIS

**catchsegv** _program_ [_args_...]

# DESCRIPTION

**catchsegv** 是一个调试包装器，它会拦截程序中的段错误并打印符号化的回溯信息，帮助诊断崩溃。它的工作原理是通过 LD_PRELOAD 注入 libSegFault.so，为 SIGSEGV 和其他致命信号安装信号处理函数。

被包装的程序崩溃时，catchsegv 会显示包含函数名、源文件位置（如果有调试符号）和内存映射信息的堆栈跟踪。当你只需要崩溃诊断时，它是在完整调试器下运行程序的轻量替代方案。

该工具曾是 glibc 调试工具的一部分，但已从 glibc 2.35 及之后版本中移除。现代替代方案包括 AddressSanitizer 以及使用 GDB 进行核心转储分析。

# ENVIRONMENT

**SEGFAULT_OUTPUT_NAME**
> 输出文件（默认：stderr）

**SEGFAULT_SIGNALS**
> 要处理的信号：segv、ill、bus、stkflt、abrt、fpe

**SEGFAULT_USE_ALTSTACK**
> 处理函数使用备用栈

# DEBUG SYMBOLS

编译时加上 -g 标志，回溯中才会出现函数名和行号：

```gcc -g -o program program.c```

没有调试符号时，只会显示内存地址。

# CAVEATS

已从 glibc 2.35+ 中移除。现代替代方案包括进程外调试器和事后分析工具。其处理函数使用了非异步信号安全的函数。

# ALTERNATIVES

- GDB 配合核心转储
- AddressSanitizer（-fsanitize=address）
- 使用 backtrace() 的自定义信号处理函数
- Valgrind

# SEE ALSO

[gdb](/man/gdb)(1), [addr2line](/man/addr2line)(1)
