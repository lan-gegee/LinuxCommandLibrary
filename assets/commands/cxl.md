# TAGLINE

Compute Express Link 设备管理工具

# TLDR

列出 CXL 内存设备

```cxl list```

显示设备详细信息

```cxl list -vvv```

列出内存区域

```cxl list -R```

显示设备健康状况

```cxl list -H```

启用内存设备

```cxl enable-memdev [mem0]```

创建内存区域

```cxl create-region -d [decoder0.0] -m [mem0]```

# SYNOPSIS

**cxl** _command_ [_options_] [_device_]

# PARAMETERS

**list**
> 列出 CXL 设备、区域或解码器。

**enable-memdev** _device_
> 启用内存设备。

**disable-memdev** _device_
> 禁用内存设备。

**create-region**
> 创建内存区域。

**destroy-region** _region_
> 销毁内存区域。

**enable-region** _region_
> 启用内存区域。

**disable-region** _region_
> 禁用内存区域。

**-m**, **--memdev** _device_
> 指定内存设备。

**-d**, **--decoder** _decoder_
> 指定解码器。

**-R**, **--regions**
> 列出区域。

**-H**, **--health**
> 包含健康信息。

**-v**, **--verbose**
> 增加输出详细度（可重复使用）。

# DESCRIPTION

**cxl** 是 Compute Express Link（CXL）设备的管理工具。CXL 是一种将内存和加速器连接到 CPU 的新型互连标准。该工具管理 CXL 内存扩展设备、配置内存区域并监控设备健康状况。

CXL 支持分离式内存架构，内存可以集中成池并动态分配给不同的主机。cxl 工具通过区域和解码器配置这些内存呈现给操作系统的方式。

常见操作包括列出可用的 CXL 设备、检查健康状态、创建可供系统使用的内存区域以及管理设备生命周期。

# CAVEATS

需要内核 5.15+ 且启用了 CXL 支持。硬件必须支持 CXL（Intel 第四代 Xeon、AMD EPYC 等）。配置更改可能需要重启系统。CXL 是仍在演进中的技术；某些功能依赖于特定的内核版本。

# HISTORY

CXL 由 **CXL 联盟**开发，该联盟由 Intel 于 **2019 年**创立，主要硬件厂商均参与了规范制定。Linux 的 **cxl** 工具是 **ndctl** 项目的一部分，由 Intel 的 **Dan Williams** 开发。CXL 1.1 支持出现在 Linux 5.12（2021 年）中，持续的开发为更新的 CXL 规范（2.0、3.0）增加了特性。

# INSTALL

```apt: sudo apt install cxl```

```dnf: sudo dnf install ndctl```

```pacman: sudo pacman -S ndctl```

```apk: sudo apk add ndctl```

```zypper: sudo zypper install ndctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ndctl](/man/ndctl)(1), [daxctl](/man/daxctl)(1), [lspci](/man/lspci)(8)

# RESOURCES

```[Source code](https://github.com/pmem/ndctl)```

```[Documentation](https://docs.pmem.io/ndctl-user-guide/)```

<!-- verified: 2026-06-26 -->
