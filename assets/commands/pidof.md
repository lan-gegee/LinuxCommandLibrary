# TAGLINE

查找指定名称程序的进程 ID 并输出到标准输出

# TLDR

列出具有指定名称的所有**进程 ID**

```pidof bash```

列出具有指定名称的**单个**进程 ID

```pidof -s bash```

列出进程 ID，包括**脚本**

```pidof -x script.py```

**杀死**具有指定名称的所有进程

```kill $(pidof name)```

显示**线程 ID** 而不是进程 ID

```pidof -t process_name```

# SYNOPSIS

**pidof** [_-s_] [_-c_] [_-q_] [_-w_] [_-x_] [_-o omitpid_] [_-t_] [_-S separator_] _program_...

# DESCRIPTION

**pidof** 查找指定名称程序的进程 ID (PID) 并输出到标准输出。它适用于脚本编写和按名称识别正在运行的进程。

# PARAMETERS

**-s**
> 单次返回——只返回一个 PID

**-c**
> 只返回在同一根目录下运行的进程 ID

**-q**
> 静默模式——抑制输出，只设置退出状态

**-w**
> 显示没有可见命令行的进程（如内核线程）

**-x**
> 同时返回运行指定脚本的 shell 的 PID

**-o omitpid**
> 省略具有指定 PID 的进程；父进程可用 %PPID 表示

**-t**
> 显示线程 ID 而不是 PID

**-S separator**
> 在 PID 之间使用指定的分隔符（默认为空格）

# CAVEATS

退出状态 0 表示至少找到一个匹配的程序；退出状态 1 表示未找到匹配的程序。对脚本使用 **-x** 时，脚本名必须完全匹配。

# HISTORY

**pidof** 是 **sysvinit** 软件包的一部分，提供按名称查找进程 ID 的方式，与 pgrep 等命令相辅相成。

# INSTALL

```apt: sudo apt install sysvinit-utils```

```dnf: sudo dnf install procps-ng```

```pacman: sudo pacman -S procps-ng```

```apk: sudo apk add procps-ng```

```brew: brew install pidof```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pgrep](/man/pgrep)(1), [pkill](/man/pkill)(1), [killall](/man/killall)(1), [ps](/man/ps)(1)
