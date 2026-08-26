# TAGLINE

查看和配置无线 PHY（物理设备）设置

# TLDR

**列出所有**无线设备的**能力**

```iw phy```

**显示指定 PHY 的详细信息**

```iw phy [phy0] info```

**设置 PHY 的信道**

```iw phy [phy0] set channel [6]```

**设置固定的发射功率**（单位 mBm）

```iw phy [phy0] set txpower fixed [1500]```

**添加指定类型的虚拟接口**

```iw phy [phy0] interface add [mon0] type [monitor]```

**重命名**无线 PHY

```iw phy [phy0] set name [newname]```

# SYNOPSIS

**iw** **phy** [_phyname_] _command_

# DESCRIPTION

**iw phy** 操作的是无线 PHY，即承载一个或多个网络接口的物理射频设备。不带参数时，它会列出每个 wiphy 及其能力：支持的频段和信道、比特率、加密算法、天线配置，以及硬件允许的接口模式和特性。

针对命名的 PHY（例如 **phy0**），可以用 **info** 进行查询，或更改整个射频范围的设置，如工作信道、发射功率、重试限制和天线掩码。**interface add** 形式可以在同一射频设备上创建额外的虚拟接口（managed、monitor、AP、mesh 等）。

# PARAMETERS

**info**
> 打印该 PHY 的完整能力列表。

**set channel** _N_ _[HT/VHT]_
> 设置工作信道，可选带宽说明符。

**set freq** _FREQ_
> 直接设置工作频率。

**set txpower** _auto_|_fixed_|_limit_ _[mBm]_
> 控制发射功率，固定或限制在给定电平。

**set name** _NAME_
> 重命名无线 PHY。

**set antenna** _TX_ _RX_
> 配置 TX 和 RX 天线位掩码。

**interface add** _NAME_ **type** _TYPE_
> 在此 PHY 上创建 _TYPE_ 类型的新虚拟接口。

# CAVEATS

大多数 **set** 操作需要 root 权限，有些只能在接口处于 down 或未使用状态时执行。支持的信道、功率和接口类型的准确集合取决于驱动程序和当前生效的管制域。

# INSTALL

```apt: sudo apt install iw```

```dnf: sudo dnf install iw```

```pacman: sudo pacman -S iw```

```apk: sudo apk add iw```

```zypper: sudo zypper install iw```

```nix: nix profile install nixpkgs#iw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iw](/man/iw)(8), [iwconfig](/man/iwconfig)(8), [nmcli](/man/nmcli)(1)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/linux/kernel/git/jberg/iw.git)```

```[Documentation](https://wireless.wiki.kernel.org/en/users/documentation/iw)```

<!-- verified: 2026-06-10 -->
