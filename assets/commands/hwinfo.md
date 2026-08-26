# TAGLINE

探测系统中存在的硬件并提供详细信息

# TLDR

显示**所有**硬件信息

```hwinfo```

显示**特定组件**的信息

```hwinfo --cpu```

**简略**显示组件信息

```hwinfo --disk --short```

将所有信息**写入**文件

```hwinfo --all --log hardware.txt```

显示**内存**信息

```hwinfo --memory```

显示**网络**设备

```hwinfo --network```

# SYNOPSIS

**hwinfo** [_--component_] [_--short_] [_--log file_]

# DESCRIPTION

**hwinfo** 探测系统中存在的硬件，并提供检测到的设备的详细信息。它可以报告单个组件或一次报告全部硬件。

# PARAMETERS

**--short**
> 显示简略摘要而非完整细节

**--all**
> 探测所有硬件

**--log FILE**
> 将输出写入指定文件

**--debug LEVEL**
> 设置调试级别（0-255）

**--dump-db LEVEL**
> 转储硬件数据库

# HARDWARE COMPONENTS

**--cpu**：处理器信息
**--memory**：RAM 与内存
**--disk**：硬盘和 SSD
**--partition**：磁盘分区
**--network**：网络适配器
**--gfxcard**：显卡
**--sound**：音频设备
**--usb**：USB 设备
**--pci**：PCI 设备
**--keyboard**：键盘
**--mouse**：指针设备
**--monitor**：显示器
**--framebuffer**：帧缓冲设备
**--cdrom**：CD/DVD 驱动器
**--bios**：BIOS 信息
**--fingerprint**：指纹读取器
**--bluetooth**：蓝牙设备

# CAVEATS

部分硬件检测需要 root 权限。完整探测（--all）可能耗时较长。该工具主要为 openSUSE 开发，但也能在其他发行版上运行。

# HISTORY

**hwinfo** 由 SUSE 为 Linux 的硬件检测而开发。它是现有最全面的硬件探测工具之一。

# INSTALL

```apt: sudo apt install hwinfo```

```dnf: sudo dnf install hwinfo```

```pacman: sudo pacman -S hwinfo```

```apk: sudo apk add hwinfo```

```zypper: sudo zypper install hwinfo```

```nix: nix profile install nixpkgs#hwinfo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lshw](/man/lshw)(1), [lspci](/man/lspci)(8), [lsusb](/man/lsusb)(8), [dmidecode](/man/dmidecode)(8)

# RESOURCES

```[Source code](https://github.com/openSUSE/hwinfo)```

<!-- verified: 2026-07-19 -->
