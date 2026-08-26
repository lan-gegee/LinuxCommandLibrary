# TAGLINE

显示运行中的 coreutils 命令的进度

# TLDR

**显示运行中的 coreutils 命令的进度**

```progress```

**持续监视**

```progress -M```

**等待进程结束**

```progress -w```

**监视特定命令**

```progress -c [cp]```

**监视特定 PID**

```progress -p [12345]```

**每 N 秒更新一次**

```progress -i [1]```

**只显示特定进程**

```progress -p $(pidof [dd])```

# SYNOPSIS

**progress** [_-M_] [_-w_] [_-c command_] [_-p pid_] [_-i interval_]

# PARAMETERS

**-M**, **--monitor**
> 持续监视模式。

**-w**, **--wait**
> 等待进程完成。

**-c** _CMD_, **--command** _CMD_
> 只监视指定的命令。

**-p** _PID_, **--pid** _PID_
> 监视特定 PID。

**-i** _SEC_, **--interval** _SEC_
> 更新间隔（秒）。

**-a**, **--additional-command** _CMD_
> 添加要监视的自定义命令。

**-o**, **--open-mode**
> 监视所有已打开的文件（实验性）。

**-q**, **--quiet**
> 更安静的输出。

**-v**, **--version**
> 显示版本。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**progress**（原名 cv，coreutils viewer）显示运行中的 coreutils 命令的进度。它为 cp、mv、dd、tar、gzip 以及其他没有内置进度指示的类似工具显示文件操作进度。

该工具通过读取 /proc 文件系统来查找文件描述符和位置信息。它通过比较当前位置与文件总大小来计算进度，然后显示百分比和吞吐量。

支持的命令包括：cp、mv、dd、tar、cat、rsync、gzip、gunzip、bzip2、xz、lzma 等。-a 标志可添加要监视的自定义命令。

监视模式（-M）像 top 一样持续更新显示。等待模式（-w）会阻塞直到所有被监视的进程完成——在脚本中用于获知操作何时结束非常有用。

对于 dd 来说，progress 提供了 dd 传统上缺乏的预计剩余时间和吞吐量信息（在 dd 原生的 status=progress 选项出现之前）。

# CAVEATS

仅适用于通过标准系统调用读写文件的命令。网络操作可能无法正确显示。需要对 /proc 的读取权限。某些压缩工具不暴露进度信息。必须已知文件大小才能计算百分比。

# HISTORY

**progress** 由 **Xfennec** 于 **2013 年**前后创建，最初名为 "cv"（coreutils viewer）。它解决了 cp 和 dd 不显示进度这一长期抱怨。该工具变得广受欢迎，尤其用于在磁盘操作期间监视 dd。为清晰起见更名为 "progress"。

# INSTALL

```apt: sudo apt install progress```

```dnf: sudo dnf install progress```

```pacman: sudo pacman -S progress```

```apk: sudo apk add progress```

```zypper: sudo zypper install progress```

```brew: brew install progress```

```nix: nix profile install nixpkgs#progress```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pv](/man/pv)(1), [dd](/man/dd)(1), [rsync](/man/rsync)(1), [watch](/man/watch)(1)
