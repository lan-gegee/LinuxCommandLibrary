# TAGLINE

控制 Intel RAID 控制器和存储系统的机箱 LED

# TLDR

为设备点亮 **Locate** LED

```sudo ledctl locate=[/dev/sda,/dev/sdb]```

**熄灭** Locate LED

```sudo ledctl locate_off=[/dev/sda,/dev/sdb]```

熄灭 **Status** 和 **Failure** LED

```sudo ledctl off=[/dev/sda,/dev/sdb]```

熄灭**所有** LED（恢复正常状态）

```sudo ledctl normal=[/dev/sda,/dev/sdb]```

# SYNOPSIS

**ledctl** [_options_] _pattern_=_device_list_ ...

# PATTERNS

**locate**=_DEVICES_
> 点亮 Locate LED（蓝色闪烁）

**locate_off**=_DEVICES_
> 熄灭 Locate LED

**off**=_DEVICES_
> 熄灭 Status 和 Failure LED

**normal**=_DEVICES_
> 熄灭所有 LED，恢复正常状态

**rebuild**=_DEVICES_
> 设置重建指示模式（RAID 重建期间使用）

**failure**=_DEVICES_, **disk_failed**=_DEVICES_
> 设置故障指示模式（红色常亮）

**ica**=_DEVICES_, **degraded**=_DEVICES_
> 处于临界状态的阵列。

**ifa**=_DEVICES_, **failed_array**=_DEVICES_
> 处于失效状态的阵列。

**hotspare**=_DEVICES_
> 标记为热备盘。

**pfa**=_DEVICES_
> 预测性故障分析。

设备既可以用逗号分隔给出（如 **locate=/dev/sda,/dev/sdb**），也可以放进花括号中（如 **locate={ /dev/sda /dev/sdb }**）。

# OPTIONS

**-L**, **--list-controllers**
> 列出检测到的控制器及其类型。

**-x**, **--listed-only**
> 只对列出的设备应用更改；其他设备保持不变。

**-l** _FILE_, **--log**=_FILE_
> 将日志输出写入给定的文件。

**--quiet**, **--error**, **--warning**, **--info**, **--debug**, **--all**
> 设置日志详细程度。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**ledctl** 控制 Intel RAID 控制器和存储系统的机箱 LED。它可以借助闪烁的 Locate LED 在物理上识别磁盘，并管理磁盘状态指示灯。

这在拥有大量磁盘的数据中心尤为有用，管理员可以在机房内实地找到需要关注、更换或正处于重建操作的特定硬盘。

# CAVEATS

需要支持 LED 的 Intel 硬件（AHCI、ISCI、VMD 机箱）。需要 root 权限。并非所有机箱都支持全部 LED 指示模式。

# HISTORY

ledctl 是 ledmon 软件包的一部分，由 Intel 开发，用于在其 RAID 和存储硬件平台上管理存储机箱 LED。

# INSTALL

```apt: sudo apt install ledmon```

```dnf: sudo dnf install ledmon```

```zypper: sudo zypper install ledmon```

```nix: nix profile install nixpkgs#ledmon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mdadm](/man/mdadm)(8), [smartctl](/man/smartctl)(8)
