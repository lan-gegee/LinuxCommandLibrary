# TAGLINE

应用 KDE Plasma 光标主题

# TLDR

按名称**应用**光标主题

```plasma-apply-cursortheme [breeze_cursors]```

**列出**已安装的光标主题

```plasma-apply-cursortheme --list-themes```

显示**帮助**

```plasma-apply-cursortheme --help```

# SYNOPSIS

**plasma-apply-cursortheme** [**--list-themes**] [_theme_name_]

# PARAMETERS

**--list-themes**
> 列出所有可用的光标主题

**theme_name**
> 要应用的光标主题名称

**--help**
> 显示帮助信息

# DESCRIPTION

**plasma-apply-cursortheme** 通过命令行更改 KDE Plasma 桌面的光标主题。它提供与系统设置中光标配置相同的功能，但以可脚本化的形式呈现。

光标主题影响整个桌面和应用程序中的鼠标指针外观。更改立即生效，无需重启会话。

# CAVEATS

需要正在运行的 Plasma 会话。某些应用程序可能需要重启才能显示新光标。主题名称区分大小写。

# HISTORY

**plasma-apply-cursortheme** 是 **KDE Plasma Workspace** 的一部分，通过命令行控制光标外观，便于脚本编写和自动化。

# INSTALL

```apt: sudo apt install plasma-workspace```

```dnf: sudo dnf install plasma-workspace```

```pacman: sudo pacman -S plasma-workspace```

```apk: sudo apk add plasma-workspace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[plasma-apply-colorscheme](/man/plasma-apply-colorscheme)(1), [plasma-apply-desktoptheme](/man/plasma-apply-desktoptheme)(1)
