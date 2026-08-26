# TAGLINE

访问 SCSI 设备模式页信息

# TLDR

**显示 SCSI 设备的 INQUIRY 数据**

```sudo sginfo [/dev/sda]```

**列出设备支持的所有模式页**

```sudo sginfo -u 63 [/dev/sda]```

**显示特定模式页**

```sudo sginfo -t [0x08] [/dev/sda]```

**显示可修改字段**而非当前值

```sudo sginfo -m -t [0x08] [/dev/sda]```

**显示厂商默认值**

```sudo sginfo -M -t [0x08] [/dev/sda]```

**显示保存的默认值**

```sudo sginfo -S -t [0x08] [/dev/sda]```

**以可编辑列表格式输出值**

```sudo sginfo -X -t [0x08] [/dev/sda]```

# SYNOPSIS

**sginfo** [_options_] [_DEVICE_]

# PARAMETERS

**-a**
> 显示设备报告的所有模式页。

**-A**
> 显示设备报告的所有模式页和子页。

**-c**
> 显示缓存页信息。

**-C**
> 显示控制模式页。

**-d**
> 显示断开重连页。

**-D**
> 显示缺陷列表（需要磁盘支持）。

**-e**
> 显示错误恢复页。

**-f**
> 显示格式化页。

**-g**
> 显示几何参数页。

**-i**
> 显示 INQUIRY 数据和序列号。

**-m**
> 显示可修改字段而非当前值。

**-M**
> 显示厂商默认值。

**-S**
> 显示已保存的值。

**-t** _PN_
> 显示模式页编号 PN。

**-u** _PN_
> 以未处理的十六进制格式显示模式页 PN。

**-X**
> 以适合编辑并配合 **-R** 写回的列表格式输出值。

**-R**
> 用输入文件中的值替换模式页的值。

**-v**
> 显示版本信息。

# DESCRIPTION

**sginfo** 访问 SCSI 和 ATAPI 设备的模式页信息。它可以显示和修改 SCSI 模式页，这些页面控制着缓存、错误恢复和电源管理等各类设备行为。

每个 SCSI 设备为模式页维护四组值：**current**（当前生效值）、**default**（厂商设置）、**saved**（断电后仍保留的值）和 **changeable**（可修改字段的掩码）。

其主要用途是通过模式页读取和修改设备配置。模式页可以原始十六进制或解码后的格式显示，修改后的值可以写回设备。

# CAVEATS

此工具处于遗留维护状态，仅接受关键缺陷修复。用于列出设备的 **-l** 选项在 Linux 2.6 及更高版本上已损坏；请改用 **lsscsi**。处理模式页时，推荐使用更现代的替代品 **sdparm**。随着 T10 SCSI 标准的演进，模式页定义不再更新。

# HISTORY

**sginfo** 是 Eric Youngdale 编写的 Linux **scsiinfo** 程序的一个移植版本。它由 Douglas Gilbert 重写，Kurt Garloff 参与贡献，是 **sg3_utils** 软件包的一部分。该工具自 Linux 2.4 内核系列起就已存在，目前仍以 GPL 第 2 版发布，不过如今已被视为遗留软件。

# INSTALL

```apt: sudo apt install sg3-utils```

```dnf: sudo dnf install sg3_utils```

```pacman: sudo pacman -S sg3_utils```

```apk: sudo apk add sg3_utils```

```zypper: sudo zypper install sg3_utils```

```nix: nix profile install nixpkgs#sg3_utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sg_inq](/man/sg_inq)(8), [lsscsi](/man/lsscsi)(1)
