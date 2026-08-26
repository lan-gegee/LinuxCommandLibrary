# TAGLINE

拦截并记录进程调用的动态库函数

# TLDR

**跟踪程序的库调用**

```ltrace [path/to/program]```

**统计库调用次数并在退出时打印摘要**

```ltrace -c [path/to/program]```

**跟踪特定的库函数**

```ltrace -e malloc+free [path/to/program]```

**跟踪调用并同时显示系统调用**

```ltrace -S [path/to/program]```

**附加到正在运行的进程**

```ltrace -p [pid]```

**将跟踪输出写入文件**

```ltrace -o [path/to/file] [path/to/program]```

**跟踪 fork 创建的子进程**

```ltrace -f [path/to/program]```

**显示每次库调用耗时**

```ltrace -T [path/to/program]```

# SYNOPSIS

**ltrace** [_options_] [_command_ [_arg ..._]]

# DESCRIPTION

**ltrace** 拦截并记录进程发出的动态库调用以及它收到的信号。它可用于调试和理解程序如何与共享库交互。

# PARAMETERS

**-a**, **--align** _column_
> 将返回值对齐到指定列（默认为屏幕宽度的 5/8）。

**-A** _maxelts_
> 在用省略号抑制其余元素之前打印的数组元素最大数量。

**-b**, **--no-signals**
> 禁止打印被跟踪进程收到的信号。

**-c**
> 统计每次库调用的耗时和次数，并在程序退出时打印摘要。

**-C**, **--demangle**
> 将低层 C++ 符号名解码（demangle）为用户级名称。

**-D**, **--debug** _mask_
> 显示 ltrace 自身的调试输出。

**-e** _filter_
> 用于选择要跟踪哪些库调用的限定表达式。

**-f**
> 跟踪由 fork(2) 或 clone(2) 创建的子进程。

**-F**, **--config** _pathlist_
> 原型库配置文件的路径列表，以冒号分隔。

**-i**
> 打印库调用发生时的指令指针。

**-l**, **--library** _library_pattern_
> 只显示匹配模式的库中的函数调用。

**-L**
> 不显示库调用（配合 -x 使用可只跟踪符号入口点）。

**-n**, **--indent** _nr_
> 跟踪输出的每一层嵌套调用缩进 nr 个空格。

**-o**, **--output** _filename_
> 将跟踪输出写入文件而非 stderr。

**-p** _pid_
> 附加到具有给定进程 ID 的进程。

**-r**
> 为跟踪的每一行加上相对时间戳。

**-s** _strsize_
> 可打印的最大字符串长度（默认：32）。

**-S**
> 同时显示系统调用和库调用。

**-t**
> 为每行加上当天时刻前缀。

**-tt**
> 带微秒的当天时刻。

**-ttt**
> 自纪元起的微秒数。

**-T**
> 显示每次调用内部的耗时。

**-u** _username_
> 以指定用户的用户 ID 和组 ID 运行命令。

**-w**, **--where** _nr_
> 为每个被跟踪的函数显示 nr 层栈帧的回溯信息。

**-x** _filter_
> 用于跟踪符号表入口点的限定表达式。

**-V**, **--version**
> 显示版本号并退出。

**-h**, **--help**
> 显示帮助并退出。

# CAVEATS

可能显著拖慢被跟踪的程序。并非所有架构都能拦截所有库调用。**-w** 选项在编译时需要 elfutils 或 libunwind 支持。

# INSTALL

```apt: sudo apt install ltrace```

```dnf: sudo dnf install ltrace```

```pacman: sudo pacman -S ltrace```

```apk: sudo apk add ltrace```

```zypper: sudo zypper install ltrace```

```nix: nix profile install nixpkgs#ltrace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[strace](/man/strace)(1), [ldd](/man/ldd)(1), [gdb](/man/gdb)(1), [nm](/man/nm)(1), [objdump](/man/objdump)(1)
