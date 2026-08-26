# TAGLINE

用于浏览和搜索 Arch Linux 软件包的 TUI

# TLDR

**启动软件包浏览器**

```pacseek```

# SYNOPSIS

**pacseek** [_options_]

# DESCRIPTION

**pacseek** 是一个终端用户界面，可用于浏览和搜索 Arch Linux 软件包数据库以及 AUR。你可以直接在界面中安装或移除软件包。它支持按名称或描述搜索、自动建议、结果排序、PKGBUILD 查看、升级检测以及新闻源。

# CAVEATS

仅适用于 Arch Linux 及基于 Arch 的发行版。默认使用 yay 作为 AUR 助手，但可配置为其他助手。

# HISTORY

**pacseek** 由 **moson-mo** 开发，使用 **Go** 编写。

# INSTALL

```aur: yay -S pacseek```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pacsea](/man/pacsea)(1), [paru](/man/paru)(1), [yay](/man/yay)(1)
