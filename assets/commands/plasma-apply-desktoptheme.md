# TAGLINE

应用 KDE Plasma 桌面主题

# TLDR

按名称**应用** Plasma 桌面主题

```plasma-apply-desktoptheme [default]```

**列出**可用的桌面主题

```plasma-apply-desktoptheme --list-themes```

显示**帮助**

```plasma-apply-desktoptheme --help```

# SYNOPSIS

**plasma-apply-desktoptheme** [**--list-themes**] [_theme_name_]

# PARAMETERS

**--list-themes**
> 列出所有可用的桌面主题

**theme_name**
> 要应用的桌面主题名称

**--help**
> 显示帮助信息

# DESCRIPTION

**plasma-apply-desktoptheme** 通过命令行更改 Plasma 桌面主题。桌面主题控制面板、小部件和其他 Plasma 特有 UI 元素的外观。

该工具支持自动切换主题，适合日/夜主题或脚本化的桌面自定义。

# CAVEATS

需要正在运行的 Plasma 会话。桌面主题与配色方案和图标主题相互独立。更改立即应用到 Plasma 组件。

# HISTORY

**plasma-apply-desktoptheme** 是 **KDE Plasma Workspace** 的一部分，作为 KDE 全面的外观定制工具之一，提供命令行主题控制。

# INSTALL

```apt: sudo apt install plasma-workspace```

```dnf: sudo dnf install plasma-workspace```

```pacman: sudo pacman -S plasma-workspace```

```apk: sudo apk add plasma-workspace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[plasma-apply-colorscheme](/man/plasma-apply-colorscheme)(1), [plasma-apply-lookandfeel](/man/plasma-apply-lookandfeel)(1)
