# TAGLINE

系统负载平均值的图形化表示

# TLDR

**在当前终端上显示实时 ASCII 图表**

```tload```

**在特定 tty 上显示图表**（如辅助虚拟控制台）

```tload [/dev/tty2]```

**设置纵向刻度**（图表刻度之间的字符数——数值越小刻度越大）

```tload -s [1]```

**每 5 秒刷新一次图表**而非默认值

```tload -d [5]```

**组合刻度与刷新间隔**

```tload -s 2 -d 2```

# SYNOPSIS

**tload** [_options_] [_tty_]

# PARAMETERS

**-s** _NUMBER_, **--scale** _NUMBER_
> 纵向刻度，以图表刻度之间的字符数表示。数值越小，图表越高、越灵敏。

**-d** _SECONDS_, **--delay** _SECONDS_
> 重绘间隔的秒数。设置 **-d 0** 会禁用定时器并冻结显示。

**-h**, **--help**
> 显示帮助文本并退出。

**-V**, **--version**
> 输出版本信息并退出。

# DESCRIPTION

**tload** 将从 **/proc/loadavg** 读取的 **1 分钟、5 分钟和 15 分钟负载平均值**以滚动的 ASCII 图表打印到指定的 tty——若未指定则为启动 tload 的终端。图表中每一列代表一次采样，因此随着新值的到来，显示会从右向左滚动。

当前负载平均值还会以常见的 **uptime** 格式打印在屏幕顶部。tload 特别适用于无头服务器、串口控制台和 tmux 窗格等场合，在这些场景下使用 **top** 或 **htop** 这类完整的 curses 监控器有些大材小用。

按任意键（**q**、**Ctrl-C** 等）即可退出；终端尺寸变化时会在收到 SIGWINCH 后干净地重绘。

# FILES

**/proc/loadavg**
> 每次刷新周期读取三个负载平均值的来源文件。

# CAVEATS

传入 **-d 0** 会将内部的 **alarm(2)** 定时器设为零，它永远不会触发；因此显示会保持静止，直到进程被终止。纵向刻度以整字符为单位，非常空闲的系统可能只显示一条平线，除非使用 **-s 1**。

# HISTORY

**tload** 起源于 Linux 早期的 **procps** 工具集（1990 年代中期），是在没有 X11 的系统上对应 **xload** 的轻量替代品。如今它作为 **procps-ng** 套件的一部分与 **ps**、**top**、**uptime** 和 **w** 一同维护。

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

[uptime](/man/uptime)(1), [top](/man/top)(1), [htop](/man/htop)(1), [w](/man/w)(1), [ps](/man/ps)(1)
