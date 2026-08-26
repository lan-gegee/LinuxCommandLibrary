# TAGLINE

应用 KDE Plasma 配色方案

# TLDR

**列出**可用的配色方案

```plasma-apply-colorscheme --list-schemes```

**应用**配色方案

```plasma-apply-colorscheme BreezeLight```

应用**深色**主题

```plasma-apply-colorscheme BreezeDark```

显示**帮助**

```plasma-apply-colorscheme --help```

# SYNOPSIS

**plasma-apply-colorscheme** [_options_] [_scheme_name_]

# DESCRIPTION

**plasma-apply-colorscheme** 用于切换 KDE Plasma 桌面的配色方案。它允许通过命令行更换主题，无需打开系统设置。

# PARAMETERS

**--list-schemes**
> 列出所有可用的配色方案

**scheme_name**
> 要应用的配色方案名称

**--help**
> 显示帮助信息

# CAVEATS

需要正在运行的 Plasma 桌面会话。配色方案名称区分大小写。更改立即生效，无需注销。

# HISTORY

**plasma-apply-colorscheme** 是 **KDE Plasma** 桌面环境的一部分，为外观设置提供命令行访问方式。

# INSTALL

```apt: sudo apt install plasma-workspace```

```dnf: sudo dnf install plasma-workspace```

```pacman: sudo pacman -S plasma-workspace```

```apk: sudo apk add plasma-workspace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[plasma-apply-wallpaperimage](/man/plasma-apply-wallpaperimage)(1), [plasma-apply-cursortheme](/man/plasma-apply-cursortheme)(1)
