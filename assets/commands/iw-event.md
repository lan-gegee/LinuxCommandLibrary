# TAGLINE

监视来自内核的无线（nl80211）事件

# TLDR

**监视**所有无线事件

```iw event```

每个事件**打印时间戳**

```iw event -t```

每个事件**打印相对时间戳**

```iw event -r```

同时**显示事件的频率**信息

```iw event -f```

# SYNOPSIS

**iw** **event** [_-t_] [_-r_] [_-f_]

# DESCRIPTION

**iw event** 监听 nl80211 多播组，并在内核发出无线事件时将其打印出来。典型的事件包括扫描结果就绪、（断开）连接、认证与关联状态变化、管制域更新以及接口状态转换。

它会持续运行直到被中断，因此可用于观察连接尝试期间发生了什么，或实时调试驱动和 supplicant 的行为。

# PARAMETERS

**-t**
> 为每个事件加上绝对时间戳前缀。

**-r**
> 为每个事件加上相对于上一个事件的时间戳前缀。

**-f**
> 在事件输出中包含频率信息。

# INSTALL

```apt: sudo apt install iw```

```dnf: sudo dnf install iw```

```pacman: sudo pacman -S iw```

```apk: sudo apk add iw```

```zypper: sudo zypper install iw```

```nix: nix profile install nixpkgs#iw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iw](/man/iw)(8), [iwconfig](/man/iwconfig)(8), [wpa_supplicant](/man/wpa_supplicant)(8)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/linux/kernel/git/jberg/iw.git)```

```[Documentation](https://wireless.wiki.kernel.org/en/users/documentation/iw)```

<!-- verified: 2026-06-10 -->
