# TAGLINE

控制台网络流量监视器

# TLDR

**监视所有接口**

```nload```

**监视特定接口**

```nload [eth0]```

**监视多个接口**

```nload [eth0] [wlan0]```

**设置刷新间隔**

```nload -t [500]```

**以比特为单位显示**而非字节

```nload -u b```

# SYNOPSIS

**nload** [_options_] [_devices_...]

# DESCRIPTION

**nload** 是一个控制台网络流量监视器。它以图形方式显示流入和流出的流量，并提供实时的带宽使用信息。

该工具会显示当前、平均、最小和最大流量速率，便于监控网络活动。

# PARAMETERS

**-a** _period_
> 平均值计算周期（秒）。

**-t** _interval_
> 刷新间隔（毫秒）。

**-u** _unit_
> 显示单位（h=自适应，b=比特，B=字节，k=KB，m=MB，g=GB）。

**-U** _unit_
> 总流量的单位。

**-m**
> 不使用多种单位。

**devices**
> 要监视的设备。

# KEYS

**Left/Right**: 切换设备
**F2**: 选项
**F5**: 保存选项
**F6**: 重新加载选项
**q**: 退出

# CAVEATS

显示的是可能波动的瞬时速率。总流量计数在重启后归零。设备名必须完全匹配。VPN 接口可能需要额外配置。

# HISTORY

**nload** 由 **Roland Riegel** 创建，是一个简单的网络负载监视器。它填补了快速可视化带宽需求的空白，又没有完整网络分析器的复杂度。

# INSTALL

```apt: sudo apt install nload```

```dnf: sudo dnf install nload```

```pacman: sudo pacman -S nload```

```apk: sudo apk add nload```

```zypper: sudo zypper install nload```

```brew: brew install nload```

```nix: nix profile install nixpkgs#nload```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iftop](/man/iftop)(1), [bmon](/man/bmon)(1), [vnstat](/man/vnstat)(1), [nethogs](/man/nethogs)(1)
