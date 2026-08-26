# TAGLINE

监控内核路由表变化

# TLDR

将所有**网络状态变化**保存到文件

```sudo rtmon file path/to/file```

指定要记录的**变化类型**

```sudo rtmon file link```

# SYNOPSIS

**rtmon** [_options_] file _path_

# PARAMETERS

**file** _path_
> 网络状态变化的输出文件

_type_
> 按变化类型过滤（link、address、route）

# DESCRIPTION

**rtmon** 监控网络状态变化并将其记录到文件。它捕获链路变化、地址修改和路由表更新，供后续分析使用。

输出可以被回放或分析，用于了解网络配置的历史。

# CAVEATS

需要 root 权限。若变化频繁，输出文件会随时间不断变大。

# HISTORY

属于 **iproute2** 软件包的一部分，提供网络监控与日志记录功能。

# INSTALL

```apt: sudo apt install iproute2```

```pacman: sudo pacman -S iproute2```

```apk: sudo apk add iproute2```

```zypper: sudo zypper install iproute2```

```brew: brew install iproute2```

```nix: nix profile install nixpkgs#iproute2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip](/man/ip)(8), [ip-monitor](/man/ip-monitor)(8)
