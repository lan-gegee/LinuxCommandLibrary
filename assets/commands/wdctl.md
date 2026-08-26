# TAGLINE

显示硬件看门狗定时器状态

# TLDR

**显示**看门狗状态

```wdctl```

**以单行键值对格式显示**看门狗状态

```wdctl -O```

**只显示**指定的看门狗标志

```wdctl -f [flag_list]```

# SYNOPSIS

**wdctl** [_options_] [_device_]

# PARAMETERS

**-O, --oneline**
> 以单行键值对格式输出

**-f, --flags _list_**
> 只显示指定的标志

**-s, --settimeout _seconds_**
> 设置看门狗超时

**-x, --flags-only**
> 仅显示标志

**-o, --output _list_**
> 定义输出列

**-r, --raw**
> 原始输出格式

**-n, --noheadings**
> 不打印表头

# DESCRIPTION

**wdctl** 显示硬件看门狗定时器的状态。看门狗是一种硬件或软件定时器，如果主程序未能定期重置它，就会触发系统重启，从而防止系统死锁。

输出包括看门狗设备的信息、超时值和支持的特性。不同的硬件看门狗支持不同的能力。

# CAVEATS

需要对看门狗设备（通常是 **/dev/watchdog**）的读取权限。可用标志因驱动而异。并非所有系统都支持硬件看门狗。属于 util-linux 软件包的一部分。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[watchdog](/man/watchdog)(8)
