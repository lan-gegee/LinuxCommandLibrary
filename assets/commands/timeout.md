# TAGLINE

限时运行命令

# TLDR

**限时运行命令**（30 秒）

```timeout 30s [command]```

以分钟为单位**限时运行**

```timeout 5m [command]```

超时时**发送指定信号**

```timeout --signal=SIGKILL 10s [command]```

若命令未终止，**再等一段时间后强制杀死**

```timeout --kill-after=10s 30s [command]```

**保留超时命令的退出状态**

```timeout --preserve-status 5s [command]```

在前台**限时运行**（适用于交互式命令）

```timeout --foreground 30s [command]```

# SYNOPSIS

**timeout** [_options_] _duration_ _command_ [_args_...]

# PARAMETERS

**-k** _duration_, **--kill-after**=_duration_
> 若命令仍在运行，则在额外时长后发送 SIGKILL

**-s** _signal_, **--signal**=_signal_
> 超时时发送的信号（默认：SIGTERM）

**--preserve-status**
> 即使超时也返回命令自身的退出状态

**--foreground**
> 不创建新进程组（用于终端交互场景）

**-v**, **--verbose**
> 将所发送信号的诊断信息输出到 stderr

# DURATION FORMAT

**s**：秒（默认）
**m**：分钟
**h**：小时
**d**：天

数字可以用浮点数：**1.5m** = 90 秒

# DESCRIPTION

**timeout** 以指定时限运行命令。如果命令未在时限内完成，timeout 会发送信号（默认 SIGTERM）将其终止。是 GNU coreutils 的一部分。

默认信号（SIGTERM）允许进程在退出前进行清理。对于忽略 SIGTERM 的进程，可以使用 **--kill-after** 在额外宽限期后发送 SIGKILL。

如果命令超时，退出状态为 124；被 SIGKILL 杀死则为 137；在时限内正常完成则为命令自身的退出状态。配合 **--preserve-status** 可在超时时返回信号编号 + 128。

# CAVEATS

Timeout 默认创建新的进程组，这可能干扰交互式命令或终端 I/O。此类情况请使用 **--foreground**。

会派生子进程的命令可能留下孤儿进程。Timeout 只向直接子进程发信号，不会作用于孙进程。

极短的时限（亚秒级）由于调度开销可能不可靠。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[time](/man/time)(1), [watch](/man/watch)(1), [kill](/man/kill)(1), [sleep](/man/sleep)(1)
