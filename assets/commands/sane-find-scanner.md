# TAGLINE

检测 SCSI 和 USB 扫描仪设备

# TLDR

**查找所有 SCSI 和 USB 扫描仪**

```sane-find-scanner```

**详细输出**，包含设备细节

```sane-find-scanner -v```

**非常详细**，包含 SCSI inquiry 和 USB 描述符

```sane-find-scanner -vv```

**安静模式**，只显示设备名称

```sane-find-scanner -q```

**探测并口扫描仪**

```sane-find-scanner -p```

**强制检查指定设备**

```sane-find-scanner -f [/dev/sg0] [/dev/usb/scanner0]```

# SYNOPSIS

**sane-find-scanner** [_-hvqpf_] [_-F filename_] [_devname_...]

# PARAMETERS

**-h**, **-?**
> 打印用法信息

**-v**
> 详细输出；使用两次可显示 SCSI inquiry 和 USB 描述符

**-q**
> 安静模式；只打印设备名称，不显示注释

**-p**
> 探测并口扫描仪

**-f**
> 强制将指定设备视为 SCSI 或 USB 扫描仪

**-F** _filename_
> 从文件读取 USB 描述符（Linux /proc/bus/usb/devices 格式）

# DESCRIPTION

**sane-find-scanner** 检测 SCSI 和 USB 扫描仪并报告其设备文件。它有助于验证扫描仪已正确连接并且 SANE 后端可以访问。

对于 SCSI 扫描仪，它会向 /dev/sg0 等通用设备文件发送 inquiry 命令，寻找扫描仪或处理器类型的设备。对于 USB 扫描仪，它会检查内核的扫描仪设备文件并使用 libusb 检测设备，识别厂商 ID、产品 ID 以及 USB 芯片类型。

即使扫描仪不被任何 SANE 后端支持，该工具也能找到它们，因此适用于初步硬件检测和故障排查。

# CAVEATS

除部分 Mustek 型号外（使用 **-p**），无法检测大多数并口扫描仪。专有接口的扫描仪无法检测。USB 支持需要带 libusb 的 Linux、FreeBSD、NetBSD 或 OpenBSD。

# HISTORY

sane-find-scanner 是 **SANE**（Scanner Access Now Easy）项目的一部分，该项目为类 Unix 系统上的扫描仪硬件提供标准化访问。项目始于 **1996 年**，目标是创建通用的扫描仪 API。

# INSTALL

```apt: sudo apt install sane-utils```

```apk: sudo apk add sane-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scanimage](/man/scanimage)(1), [saned](/man/saned)(8)
