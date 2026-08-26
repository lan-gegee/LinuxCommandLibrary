# TAGLINE

在你该离开的时候提醒你

# TLDR

**30 分钟后提醒离开**

```leave +30```

**在指定时间离开**（HHMM，12 或 24 小时制）

```leave [1730]```

**交互模式**（提示 "When do you have to leave?"）

```leave```

**取消离开提醒**

```kill $(pgrep leave)```

# SYNOPSIS

**leave** [[+]_hhmm_]

# PARAMETERS

_hhmm_
> 当天需要离开的时刻。时间按 12 小时制解释，并被假定位于接下来的 12 小时之内。

**+**_hhmm_
> 相对时间；leave 将在 _hh_ 小时 _mm_ 分钟后触发提醒。

# DESCRIPTION

**leave** 等待到指定时刻，然后提醒你离开。在实际时间前 5 分钟和 1 分钟、到达该时刻时以及此后的每一分钟都会提醒你。它会派生自身并在后台运行，当你注销时自动退出。

如果不带参数运行，**leave** 会提示 "When do you have to leave?"；空回复会使其退出。

# CAVEATS

经典的 BSD 实用工具，可在 macOS 和大多数 *BSD 系统上使用；在 Linux 上通常默认不安装。除了杀掉后台进程之外，没有取消正在运行的提醒的其他办法。

# HISTORY

leave 起源于 **BSD Unix**，是一个面向终端用户的简单提醒工具。

# HISTORY

leave 起源于 **BSD Unix**，是一个面向终端用户的简单提醒工具。

# INSTALL

```apt: sudo apt install leave```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[at](/man/at)(1), [calendar](/man/calendar)(1), [sleep](/man/sleep)(1)
