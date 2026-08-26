# TAGLINE

列出 CUPS 已知的可用打印机和打印机驱动

# TLDR

**列出可用的打印机**

```lpinfo -v```

**列出可用的打印机驱动**

```lpinfo -m```

**列出匹配关键字的驱动**

```lpinfo -m | grep -i [keyword]```

**显示完整打印机名称**

```lpinfo -l -v```

**列出特定厂商的驱动**

```lpinfo --make-and-model "[HP LaserJet]" -m```

**排除指定的 scheme**

```lpinfo -v --exclude-schemes [dnssd]```

**只包含指定的 scheme**

```lpinfo -v --include-schemes [usb,parallel]```

# SYNOPSIS

**lpinfo** [_-l_] [_-m_] [_-v_] [_--make-and-model pattern_] [_options_]

# PARAMETERS

**-l**
> 显示包含设备详情的长列表。

**-m**
> 列出可用的打印机驱动（PPD 文件）。

**-v**
> 列出可用的打印机设备。

**--device-id** _ID_
> 只显示匹配 IEEE-1284 设备 ID 的设备。

**--make-and-model** _PATTERN_
> 按厂商与型号字符串筛选。

**--exclude-schemes** _SCHEMES_
> 排除匹配这些 scheme 的设备 URI。

**--include-schemes** _SCHEMES_
> 只包含匹配这些 scheme 的设备 URI。

**-h** _SERVER_
> 连接到 CUPS 服务器。

**--timeout** _SECONDS_
> 设备发现的超时时间。

# DESCRIPTION

**lpinfo** 列出 CUPS 已知的可用打印机和打印机驱动。它向 CUPS 服务器查询设备以及 PPD（PostScript Printer Description）文件。

设备列表（-v）显示所有检测到的打印机连接，包括 USB、网络和并行端口。每个条目都带有设备 URI，可在用 lpadmin 添加打印机时使用。

驱动列表（-m）显示描述打印机能力的 PPD 文件。PPD 定义纸张尺寸、分辨率、彩色选项等特性。免驱打印使用通用的 IPP Everywhere 或 AirPrint 驱动。

厂商与型号过滤器有助于查找特定打印机的驱动。配合 grep 可以搜索适配你硬件的兼容驱动。

网络打印机发现结果可能包括通过 DNS-SD（Bonjour/Avahi）发现的打印机。可使用 scheme 过滤器聚焦特定的连接类型。

# CAVEATS

需要 CUPS 处于运行状态。网络发现可能较慢。某些打印机需要 CUPS 未附带的专有驱动。免驱打印要求打印机支持 IPP Everywhere 或 AirPrint。

# HISTORY

**lpinfo** 属于 **CUPS**（Common UNIX Printing System）套件，由 Easy Software Products 的 **Michael Sweet** 开发。CUPS 发布于 **1999 年**，于 **2007 年**被 **Apple** 收购。lpinfo 提供打印配置工具所依赖的发现机制。

# INSTALL

```apt: sudo apt install cups-client```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lpadmin](/man/lpadmin)(1), [lpstat](/man/lpstat)(1), [lp](/man/lp)(1), [lpr](/man/lpr)(1), [cupsd](/man/cupsd)(8)
