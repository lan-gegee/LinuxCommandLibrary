# TAGLINE

编译后程序的交互式调试器

# TLDR

**调试程序**

```gdb [program]```

**配合 core 文件调试**

```gdb [program] [core]```

**附加到进程**

```gdb -p [pid]```

**带参数运行**

```gdb --args [program] [arg1] [arg2]```

**执行命令脚本**

```gdb -x [commands.gdb] [program]```

# SYNOPSIS

**gdb** [_options_] [_program_] [_core_|_pid_]

# PARAMETERS

_PROGRAM_
> 要调试的可执行文件。

_CORE_
> 核心转储文件。

**-p** _PID_
> 附加到正在运行的进程。

**--args**
> 向程序传递参数。

**-x** _FILE_
> 执行文件中的 GDB 命令。

**-q**, **--quiet**
> 抑制启动消息。

**--tui**
> 启用文本用户界面。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.gdbinit**
> 用户专属的 GDB 初始化命令，启动时执行。

**/etc/gdb/gdbinit**
> 面向所有用户的系统级初始化文件。

**.gdbinit**
> 项目本地的初始化文件，用于目录特定的命令。

# DESCRIPTION

**gdb**（GNU Debugger）是类 Unix 系统上 C、C++ 及其他编译型语言的标准调试器。它提供了全面的功能，可在程序执行期间检查程序状态、设置断点、单步执行代码、查看变量以及分析内存内容。

调试器通过控制程序执行来工作，允许开发者在特定位置暂停、检查调用栈、修改变量值以及跟踪执行流程。它可以通过附加的方式调试运行中的进程，分析崩溃程序的核心转储，甚至可以通过 gdbserver 跨网络连接进行远程调试。

gdb 通过其命令语言和 Python 集成支持脚本化，可实现自动化调试会话和自定义命令。文本用户界面（TUI）模式提供源代码、汇编、寄存器和命令提示符的分屏视图。调试符号（使用 -g 标志编译）对于有效的源码级调试至关重要，不过 gdb 在汇编级别仍可处理剥离了符号的二进制文件。

常见工作流包括：在函数或行号处设置断点、用 print 和 display 命令查看变量、用 next/step/continue 单步执行代码，以及通过 backtrace 分析崩溃。该工具是诊断原生应用程序中段错误、内存损坏、竞态条件和复杂逻辑错误的必备利器。

# CAVEATS

需要调试符号（-g）。优化后的代码可能出现意外行为。命令学习曲线较陡。

# HISTORY

gdb 由 **Richard Stallman** 于 1986 年编写，是 GNU 计划的一部分。它成为 Unix 上的标准调试器，支持众多架构和语言。

# INSTALL

```apt: sudo apt install gdb```

```dnf: sudo dnf install gdb```

```pacman: sudo pacman -S gdb```

```apk: sudo apk add gdb```

```zypper: sudo zypper install gdb```

```brew: brew install gdb```

```nix: nix profile install nixpkgs#gdb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcore](/man/gcore)(1), [gdbserver](/man/gdbserver)(1), [lldb](/man/lldb)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/gdb/)```

```[Documentation](https://sourceware.org/gdb/current/onlinedocs/gdb/)```

<!-- verified: 2026-07-15 -->
