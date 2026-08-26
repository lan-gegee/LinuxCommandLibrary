# TAGLINE

为 Linux 内核熵池补充随机数的随机数生成守护进程

# TLDR

**启动** haveged 守护进程

```sudo haveged```

以**前台方式**运行 haveged

```sudo haveged -F```

设置输出的**文件路径**

```sudo haveged -f [path/to/file]```

设置守护进程的**运行级别**

```sudo haveged -r [runlevel]```

设置采集**缓冲区大小**（KiB 字）

```sudo haveged -b [buffersizeinKW]```

设置**缓存大小**（KiB 字）

```sudo haveged -d [cachesizeinKW]```

设置写入输出文件的**字节数**

```sudo haveged -n [byteamount]```

# SYNOPSIS

**haveged** [_options_]

# PARAMETERS

**-F**, **--Foreground**
> 在前台运行（不守护进程化）

**-f**, **--file** _PATH_
> 将随机数据写入文件而不是 /dev/random

**-r**, **--run** _LEVEL_
> 设置运行级别（0=作为守护进程运行，1=显示结果）

**-b**, **--buffer** _SIZE_
> 采集缓冲区大小（KiB 字）

**-d**, **--data** _SIZE_
> 缓存大小（KiB 字）

**-n**, **--number** _BYTES_
> 要写入输出的字节数

**-w**, **--write** _BYTES_
> 每次向 /dev/random 写入 _BYTES_ 字节

**-v**, **--verbose** _LEVEL_
> 详细程度

# DESCRIPTION

**haveged** 是一个随机数生成守护进程，为 Linux 内核的熵池（/dev/random）补充随机数。它采用 HAVEGE（HArdware Volatile Entropy Gathering and Expansion）算法，从 CPU 计时变化中采集熵。

该守护进程在以下场景特别有用：
- 缺少传统熵源（键盘、鼠标）的无头服务器
- 硬件熵有限的虚拟机
- 需要高吞吐量随机数生成的系统
- 防止加密操作期间 /dev/random 阻塞

haveged 监视内核熵池，并在熵量下降时自动补充。

# CAVEATS

部分安全研究者质疑 HAVEGE 在虚拟化环境或计时行为一致的现代 CPU 上产生的熵质量。若硬件 RNG（rngd）可用，建议优先考虑。在现代内核上，/dev/random 已不再阻塞，这降低了对 haveged 的需求。

# HISTORY

haveged 由 Gary Wuertz 开发，基于 André Seznec 和 Nicolas Sendrier 提出的 HAVEGE 算法。它在解决 Linux 服务器和虚拟机的熵饥饿问题方面广受欢迎。

# INSTALL

```apt: sudo apt install haveged```

```dnf: sudo dnf install haveged```

```pacman: sudo pacman -S haveged```

```apk: sudo apk add haveged```

```zypper: sudo zypper install haveged```

```nix: nix profile install nixpkgs#haveged```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[random](/man/random)(4), [getrandom](/man/getrandom)(2)
