# TAGLINE

周期性执行命令并显示输出

# TLDR

**每 2 秒执行一次命令**（默认）

```watch [command]```

**以自定义间隔执行命令**

```watch -n [5] [command]```

**高亮显示**各次更新之间的差异

```watch -d [command]```

**输出变化时退出**

```watch -g [command]```

**隐藏**显示时间和命令的**头部**

```watch -t [command]```

**命令出错时发出蜂鸣**

```watch -b [command]```

**保留 ANSI 颜色**

```watch -c [ls --color=always]```

**命令出错时退出**

```watch -e [command]```

# SYNOPSIS

**watch** [_options_] _command_

# PARAMETERS

**-n**, **--interval** _SECS_
> 更新间隔，以秒为单位（默认：2，最小：0.1，最大：2678400）

**-d**, **--differences** [=_permanent_]
> 高亮显示差异；permanent 会显示自启动以来的所有变化

**-g**, **--chgexit**
> 输出变化时退出

**-e**, **--errexit**
> 出错时冻结，按键后退出

**-b**, **--beep**
> 退出码非零时发出蜂鸣

**-c**, **--color**
> 解析 ANSI 颜色序列

**-C**, **--no-color**
> 不解析 ANSI 颜色序列

**-t**, **--no-title**
> 隐藏头部（间隔、命令、时间）

**-w**, **--no-wrap**
> 禁用自动换行

**-p**, **--precise**
> 从开始时刻起按精确间隔运行命令

**-f**, **--follow**
> 像 tail -f 一样滚动输出，而不是清屏

**-q**, **--equexit** _CYCLES_
> 输出在给定周期数内无变化时退出

**-x**, **--exec**
> 将命令传给 exec 而不是 sh -c

**-h**, **--help**
> 显示帮助

**-v**, **--version**
> 显示版本

# DESCRIPTION

**watch** 反复执行命令，并以全屏模式显示输出。这样无需手动重复执行命令即可监视不断变化的数据，例如磁盘用量、正在运行的进程或日志文件。

默认情况下命令每 2 秒运行一次。头部显示间隔、命令和当前时间。使用 **-d** 可以高亮各次更新之间的变化——便于在大输出中发现改动。

命令会传给 **sh -c** 执行，因此管道和重定向等 shell 特性可用，但可能需要加引号。不可打印字符会被剔除；可在管道中使用 **cat -v** 来查看它们。

# CAVEATS

由于 shell 的解释机制，含特殊字符的命令可能需要额外的引号。POSIX 选项处理在第一个非选项参数处停止，因此命令之后的标志不会被 watch 处理。极快的间隔可能导致较高的 CPU 占用。要显示 **ls --color** 等命令的彩色输出，需要 **-c** 选项。

# HISTORY

watch 命令由 **Tony Rems** 编写，后来成为 Linux 上 **procps** 软件包（后为 **procps-ng**）的一部分。它为监视命令输出提供了一种简单的替代方案，无需自行编写循环。周期性执行并显示命令输出的这一概念在各种 Unix 系统上都有不同形式的实现。

# INSTALL

```apt: sudo apt install procps```

```dnf: sudo dnf install procps-ng```

```pacman: sudo pacman -S procps-ng```

```apk: sudo apk add procps-ng```

```zypper: sudo zypper install procps```

```brew: brew install procps```

```nix: nix profile install nixpkgs#procps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tail](/man/tail)(1), [top](/man/top)(1), [htop](/man/htop)(1), [while](/man/while)(1)
