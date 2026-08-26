# TAGLINE

KDE Plasma 系统设置图形界面

# TLDR

打开设置的**图形界面**

```systemsettings```

**列出**所有 KCM 模块

```systemsettings --list```

显示**帮助**

```systemsettings -h```

# SYNOPSIS

**systemsettings** [_OPTIONS_] [_MODULE_]

# PARAMETERS

**--list**
> 列出所有可用的 KCM（KDE Control Module，KDE 控制模块）

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**systemsettings** 是 KDE Plasma 桌面的核心配置程序。它提供图形界面来配置系统设置，包括外观、工作区行为、硬件、网络和应用程序。

设置按类别组织，由各个 KCM 模块分别处理特定的配置领域。

# CAVEATS

需要 KDE Plasma 桌面环境。某些模块在进行系统级更改时需要 root 权限。更改立即生效或注销后生效，取决于具体设置项。

# HISTORY

自 KDE 4 以来，**systemsettings** 一直是 KDE 的主要配置工具，取代了更早的 KControl 程序。它延续为 KDE Plasma 5 和 6 的设置界面。

# INSTALL

```apt: sudo apt install systemsettings```

```pacman: sudo pacman -S systemsettings```

```apk: sudo apk add systemsettings```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kwriteconfig5](/man/kwriteconfig5)(1)
