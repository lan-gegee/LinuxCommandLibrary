# TAGLINE

SMART 磁盘监控守护进程

# TLDR

在**前台启动 smartd**

```smartd -d```

**使用指定配置文件启动**

```smartd -c [/etc/smartd.conf]```

**检查配置文件语法**

```smartd -q onecheck```

**运行一次后退出**（非守护模式）

```smartd -q onecheck -d```

以秒为单位**设置轮询间隔**

```smartd -i [1800]```

# SYNOPSIS

**smartd** [_-d_] [_-c configfile_] [_-i interval_] [_-l facility_] [_-p pidfile_] [_-q opt_]

# PARAMETERS

**-d**
> 在前台运行（调试模式）；不 fork 到后台

**-c** _file_
> 使用指定的配置文件而不是 /etc/smartd.conf

**-i** _N_
> 设置磁盘检查间隔（秒）（默认：1800）

**-l** _facility_
> 日志使用指定的 syslog facility

**-p** _file_
> 将 PID 写入指定文件

**-q** _option_
> 安静模式选项：errors、nodev、nodev0、never、onecheck、showtests

**-r** _type_
> 按指定类型报告 ATA 错误（ioctl、bpt）

# DESCRIPTION

**smartd** 是一个守护进程，用于监控来自 ATA/SATA 和 SCSI/SAS 硬盘与 SSD 的 SMART（Self-Monitoring, Analysis and Reporting Technology，自我监控、分析及报告技术）数据。它能检测性能退化的硬盘，并在数据丢失发生之前预测故障。

该守护进程以可配置的间隔（默认 30 分钟）轮询设备，并通过 syslog 记录 SMART 属性的变化。检测到问题时，它可以发送电子邮件警报、运行自定义脚本或执行测试。

配置保存在 **/etc/smartd.conf** 中，列出要监控的设备及其选项。没有配置文件时，smartd 会扫描并监控所有支持 SMART 的设备。

# CONFIGURATION

**/etc/smartd.conf**
> 主配置文件，列出要监控的设备及其检查选项、告警操作和测试计划。

**/etc/default/smartmontools**
> 在基于 Debian 的系统上 smartd 守护进程的启动选项。

# CAVEATS

smartd 监控磁盘健康，但不是备份方案。某些 USB 硬盘盒不透传 SMART 数据。虚拟硬盘和 RAID 控制器可能不向主机暴露 SMART。通过 systemd 启动 smartd：**systemctl enable --now smartd**。

# HISTORY

smartd 是 **smartmontools** 的一部分，最初由 Bruce Allen 自 **2002 年**起开发。该软件包为各类硬盘和操作系统提供开源的 SMART 数据监控工具。

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

[smartctl](/man/smartctl)(8), [hddtemp](/man/hddtemp)(8)
