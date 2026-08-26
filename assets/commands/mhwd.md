# TAGLINE

Manjaro Linux 上用于自动硬件检测和驱动管理的工具

# TLDR

列出**可用**驱动

```mhwd --list```

列出**已安装**驱动

```mhwd --listinstalled```

**安装**驱动

```mhwd --install pci [driver_name]```

**卸载**驱动

```mhwd --remove pci [driver_name]```

显示**详细**硬件信息

```mhwd --list --detail```

**自动安装**最佳显卡驱动

```mhwd --auto pci free 0300```

# SYNOPSIS

**mhwd** [_options_]

# DESCRIPTION

**mhwd**（Manjaro Hardware Detection）是 Manjaro Linux 上用于自动硬件检测和驱动管理的工具。它简化了专有驱动和开源驱动的安装过程。

# PARAMETERS

**-l, --list**
> 列出可用驱动

**-li, --listinstalled**
> 列出已安装驱动

**-i, --install pci|usb DRIVER**
> 安装驱动

**-r, --remove pci|usb DRIVER**
> 卸载驱动

**-a, --auto pci|usb free|nonfree HWCLASS**
> 自动安装最佳驱动（0300 为显卡）

**-d, --detail**
> 显示详细信息

**-f, --force**
> 强制重装驱动

**-h, --help**
> 显示帮助消息

**-v, --version**
> 显示版本

# CAVEATS

仅适用于 Manjaro Linux。显卡类别为 0300。开源驱动选择 'free'，专有驱动选择 'nonfree'。

# SEE ALSO

[mhwd-kernel](/man/mhwd-kernel)(8), [pacman](/man/pacman)(8)
