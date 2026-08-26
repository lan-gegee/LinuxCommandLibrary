# TAGLINE

监控和控制 SMART 磁盘健康数据

# TLDR

**显示硬盘信息**

```smartctl -i /dev/[sda]```

**显示全部 SMART 数据**

```smartctl -a /dev/[sda]```

**检查硬盘健康状况**

```smartctl -H /dev/[sda]```

**运行短自检**

```smartctl -t short /dev/[sda]```

**运行长自检**

```smartctl -t long /dev/[sda]```

**查看自检结果**

```smartctl -l selftest /dev/[sda]```

**查看错误日志**

```smartctl -l error /dev/[sda]```

在硬盘上**启用 SMART**

```smartctl -s on /dev/[sda]```

**扫描硬盘**

```smartctl --scan```

# SYNOPSIS

**smartctl** [_options_] _device_

# DESCRIPTION

**smartctl** 是一个用于监控和控制硬盘与 SSD 上 SMART（Self-Monitoring, Analysis and Reporting Technology，自我监控、分析及报告技术）数据的命令行工具。SMART 数据可以在故障发生之前预测硬盘损坏。

该工具可以显示硬盘身份信息、健康状态、属性、错误日志和自检结果。它还能发起自检并控制 SMART 特性。不同厂商对 SMART 的实现不同，因此属性解读存在差异。

smartctl 是 smartmontools 的一部分，对于监控磁盘健康并在故障前规划更换的系统管理员来说必不可少。

# PARAMETERS

**-i**, **--info**
> 显示设备识别信息。

**-a**, **--all**
> 显示所有 SMART 信息。

**-H**, **--health**
> 显示 SMART 健康状态。

**-A**, **--attributes**
> 显示 SMART 属性。

**-l** _type_, **--log=** _type_
> 显示日志（error、selftest、selective）。

**-t** _test_, **--test=** _test_
> 运行测试（short、long、conveyance、selective、offline）。

**-s** _on|off_
> 启用/禁用 SMART。

**-d** _type_
> 指定设备类型。

**--scan**
> 扫描设备。

**-x**, **--xall**
> 显示所有扩展信息（全部 SMART 与非 SMART 数据）。

**-c**, **--capabilities**
> 显示设备的 SMART 能力。

**-C**, **--captive**
> 以 captive 模式运行自检（完成前阻塞设备）。

**-X**, **--abort**
> 中止进行中的自检。

**-n** _POWERMODE_, **--nocheck=** _POWERMODE_
> 若设备处于低功耗模式则跳过检查（standby、sleep、idle、never）。

**-q** _type_, **--quietmode=** _type_
> 安静输出（errorsonly、silent、noserial）。

# KEY ATTRIBUTES

**Reallocated Sector Count**: 已迁移到备用区的坏扇区数
**Current Pending Sector Count**: 等待重映射的扇区数
**Offline Uncorrectable**: 无法纠正的扇区
**Power-On Hours**: 总通电时间
**Temperature**: 硬盘温度

# CAVEATS

多数操作需要 root 权限。硬盘必须支持并启用 SMART。属性解读因厂商而异。自检运行期间可能影响性能。

# HISTORY

**smartmontools** 由 **Bruce Allen** 于 **2002 年**创建，是 smartsuite 软件包的一个分支。它在 Linux、BSD、macOS 和 Windows 上提供跨平台的 SMART 监控。项目仍在积极开发中，是类 Unix 系统上的标准 SMART 监控工具。

# INSTALL

```apt: sudo apt install smartmontools```

```dnf: sudo dnf install smartmontools```

```pacman: sudo pacman -S smartmontools```

```apk: sudo apk add smartmontools```

```zypper: sudo zypper install smartmontools```

```brew: brew install smartmontools```

```nix: nix profile install nixpkgs#smartmontools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smartd](/man/smartd)(8), [hdparm](/man/hdparm)(1), [nvme](/man/nvme)(1), [lsblk](/man/lsblk)(1)
