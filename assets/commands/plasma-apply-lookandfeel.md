# TAGLINE

应用 KDE Plasma 全局主题

# TLDR

列出**可用的**全局主题

```plasma-apply-lookandfeel --list```

**应用**全局主题

```plasma-apply-lookandfeel --apply [org.kde.breeze.desktop]```

在无显示服务器的情况下运行

```plasma-apply-lookandfeel --platform offscreen```

显示**帮助**

```plasma-apply-lookandfeel --help```

# SYNOPSIS

**plasma-apply-lookandfeel** [**--list**] [**--apply** _theme_] [**--platform** _platform_]

# PARAMETERS

**--list**
> 列出所有可用的全局主题

**--apply _theme_**
> 应用指定的全局主题

**--platform _platform_**
> 平台插件（无头环境使用 offscreen）

**--help**
> 显示帮助信息

# DESCRIPTION

**plasma-apply-lookandfeel** 用于应用 KDE Plasma 全局主题（Look and Feel 包）。全局主题将配色方案、桌面主题、光标主题、图标和其他外观设置打包成统一的整体。

该工具可以使用 offscreen 平台在没有运行显示服务器的情况下工作，支持自动化主题部署。

# CAVEATS

全局主题可能覆盖单独的主题设置。主题 ID 采用反向域名记法。offscreen 模式仅限于配置更改。

# HISTORY

**plasma-apply-lookandfeel** 是 **KDE Plasma Workspace** 的一部分，为 KDE 模块化的外观系统提供统一的主题应用方式。

# INSTALL

```apt: sudo apt install plasma-workspace```

```dnf: sudo dnf install plasma-workspace```

```pacman: sudo pacman -S plasma-workspace```

```apk: sudo apk add plasma-workspace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[plasma-apply-colorscheme](/man/plasma-apply-colorscheme)(1), [plasma-apply-desktoptheme](/man/plasma-apply-desktoptheme)(1)
