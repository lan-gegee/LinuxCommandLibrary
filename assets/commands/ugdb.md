# TAGLINE

GDB 调试器的替代 TUI

# TLDR

**调试程序**

```ugdb [./myprogram]```

**带参数调试**

```ugdb [./myprogram] -- [arg1] [arg2]```

**按 PID 附加到运行中的进程**

```ugdb -p [pid]```

**使用自定义 GDB 可执行文件**

```ugdb --gdb [/path/to/gdb] [./myprogram]```

**从单独的文件读取符号**

```ugdb -s [symbols.elf] [./myprogram]```

**作为 rr 回放的界面启动**

```ugdb --rr [./myprogram]```

**跳过所有 .gdbinit 初始化文件**

```ugdb -n [./myprogram]```

# SYNOPSIS

**ugdb** [_options_] [_program_] [-- _args_...]

# PARAMETERS

**--gdb** _path_
> 替代 gdb 二进制文件的路径（默认：gdb）。

**-p**, **--pid** _pid_
> 附加到具有给定 PID 的运行中进程。

**-s**, **--symbols** _file_
> 从指定文件读取调试符号。

**-d**, **--directory** _dir_
> 向源文件搜索路径添加一个目录。

**-c**, **--core** _file_
> 使用 core dump 文件进行检查分析。

**-x**, **--command** _file_
> 启动时执行来自文件的 GDB 命令。

**-e**, **--initial-expression** _expr_
> 预先在表达式表中填充一个条目。

**--layout** _string_
> 定义初始窗格布局（默认：(1s-1c)|(1e-1t)）。窗格字母含义：s=源代码，c=控制台，e=表达式，t=终端。

**-n**, **--nx**
> 不执行任何 .gdbinit 文件中的命令。

**--nh**
> 不执行 ~/.gdbinit 中的命令。

**-q**, **--quiet**
> 不显示开场和版权信息。

**--rr**
> 将 ugdb 作为 rr 的界面启动；末尾参数会传给 rr replay。

**--rr-path** _path_
> 替代 rr 二进制文件的路径。

**--log_dir** _dir_
> 日志文件所在目录（默认：/tmp）。

# DESCRIPTION

**ugdb** 是基于 unsegen 库构建的 GDB 终端用户界面。它提供四个交互窗格：GDB 控制台、源代码分页器、用于监视变量的表达式表，以及显示被调试程序输出的虚拟终端。窗格布局可通过 **--layout** 配置。

支持类 Vim 按键绑定以及通过 IPC 进行远程控制。**--rr** 标志可将其与 Mozilla rr 录制回放调试器配合使用，作为即插即用的界面。

# HISTORY

**ugdb** 由 **ftilde** 开发，使用 **Rust** 编写。

# INSTALL

```nix: nix profile install nixpkgs#ugdb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdb](/man/gdb)(1), [lldb](/man/lldb)(1)
