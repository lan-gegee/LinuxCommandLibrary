# TAGLINE

显示详细系统信息的 KDE 信息中心应用

# TLDR

打开**图形界面**

```kinfocenter```

**列出**所有可用的 KCM 模块

```kinfocenter --list```

显示**版本**信息

```kinfocenter -v```

# SYNOPSIS

**kinfocenter** [_options_]

# PARAMETERS

**--list**
> 列出所有可用的 KCM（KDE Control Module）模块。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**kinfocenter** 是 KDE Plasma 的信息中心。它提供硬件和软件配置的集中视图，包括 CPU、内存、显卡、音频、网络和 USB 设备等。

该应用加载各种 KCM 模块，每个模块提供系统不同方面的信息。它对故障排查和了解系统能力很有用。

# CAVEATS

仅在 KDE Plasma 桌面上可用。部分信息模块可能需要额外的软件包。硬件检测依赖于内核和驱动支持。

# HISTORY

kinfocenter 自 KDE 3 早期就是 KDE 的组成部分，随每个主要 KDE 版本不断演进，在友好的界面中提供全面的系统信息。

# INSTALL

```apt: sudo apt install kinfocenter```

```dnf: sudo dnf install kinfocenter```

```pacman: sudo pacman -S kinfocenter```

```apk: sudo apk add kinfocenter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[inxi](/man/inxi)(1), [lshw](/man/lshw)(1), [systemctl](/man/systemctl)(1)
