# TAGLINE

显示系统中 PCI 总线及其连接设备的信息

# TLDR

显示设备的**简要列表**

```lspci```

显示**详细**信息

```lspci -v```

显示**内核驱动**和模块

```lspci -k```

选择**特定设备**

```lspci -s 00:18.3```

机器**可读**输出

```lspci -vm```

同时以**编号和名称**显示厂商/设备

```lspci -nn```

以**树状**显示

```lspci -t```

# SYNOPSIS

**lspci** [_options_]

# DESCRIPTION

**lspci** 显示系统中 PCI 总线及所连设备的信息，提供 PCI 设备的硬件、驱动和能力等细节。

# PARAMETERS

**-v**
> 详细输出，包含设备细节

**-vv**
> 非常详细的输出

**-vvv**
> 最大详细程度

**-k**
> 显示内核驱动程序和可用模块

**-n**
> 仅以数字形式显示厂商/设备代码

**-nn**
> 同时显示编号和名称

**-m**
> 机器可读的输出格式

**-mm**
> 供脚本使用的机器可读格式

**-t**
> 以树状图显示

**-s SLOT**
> 只显示指定插槽中的设备

**-d VENDOR:DEVICE**
> 只显示具有指定 ID 的设备

**-x**
> 配置空间的十六进制转储

**-xxx**
> 完整的 PCI 配置空间（仅限 root）

**-D**
> 始终显示 PCI 域编号

**-P**
> 按桥接路径显示设备

**-A** _METHOD_
> 使用指定的 PCI 访问方式（列表见 -A help）

**-M**
> 总线映射模式；彻底扫描包括配置错误的桥（仅限 root）

**-q**
> 向中央数据库查询未知设备

**-i** _FILE_
> 使用备用的 PCI ID 文件

# CAVEATS

部分信息需要 root 权限。**-xxx** 选项会显示完整的配置空间，但需要 root 权限。

# HISTORY

**lspci** 属于 **pciutils**，为 Linux 系统提供 PCI 设备信息和配置工具。

# INSTALL

```apt: sudo apt install pciutils```

```dnf: sudo dnf install pciutils```

```pacman: sudo pacman -S pciutils```

```apk: sudo apk add pciutils```

```zypper: sudo zypper install pciutils```

```brew: brew install pciutils```

```nix: nix profile install nixpkgs#pciutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsusb](/man/lsusb)(8)
