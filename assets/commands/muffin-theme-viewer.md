# TAGLINE

预览 Muffin 窗口管理器主题

# TLDR

**按名称预览主题（区分大小写）**

```muffin-theme-viewer [theme-name]```

**预览默认主题（Atlanta）**

```muffin-theme-viewer```

# SYNOPSIS

**muffin-theme-viewer** [_theme_]

# PARAMETERS

_THEME_
> 要预览的主题名称或路径。

**--help**
> 显示帮助信息。

# DESCRIPTION

**muffin-theme-viewer** 通过在测试窗口中渲染窗口装饰来预览 Muffin 窗口管理器主题。它可用于测量某个窗口边框选项的性能，并预览其外观效果。主题名称区分大小写；若未指定则默认为 Atlanta。

适用于 Cinnamon 桌面环境中的主题开发、测试和挑选。

# CAVEATS

仅适用于 Cinnamon/Muffin。需要正在运行的显示服务器。只能预览 Metacity 兼容的窗口装饰主题。

# HISTORY

muffin-theme-viewer 是 **Muffin** 的一部分，后者是 GNOME 的 Mutter 窗口管理器的分支，由 Linux Mint 项目维护，适配 Cinnamon 桌面环境。

# SEE ALSO

[muffin](/man/muffin)(1), [muffin-window-demo](/man/muffin-window-demo)(1), [cinnamon](/man/cinnamon)(1)
