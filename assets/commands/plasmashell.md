# TAGLINE

KDE Plasma 桌面外壳与面板

# TLDR

通过 systemd **重启** plasmashell

```systemctl restart --user plasma-plasmashell```

**不使用 systemd** 重启 plasmashell

```plasmashell --replace & disown```

显示**帮助**

```plasmashell -h```

显示包含 **Qt 选项**的帮助

```plasmashell --help-all```

# SYNOPSIS

**plasmashell** [**--replace**] [**-h**|**--help**] [**--help-all**]

# PARAMETERS

**--replace**
> 替换当前正在运行的 plasmashell 实例

**-h, --help**
> 显示帮助信息

**--help-all**
> 显示包含 Qt 选项的帮助

# DESCRIPTION

**plasmashell** 是 KDE Plasma 的桌面外壳，提供桌面、面板、系统托盘和小部件。它是 Plasma 桌面环境的核心视觉组件。

该外壳通常由 Plasma 会话自动启动。崩溃后或应用某些配置更改时可能需要手动重启。

# CAVEATS

杀死 plasmashell 会移除桌面和面板。请使用 --replace 进行优雅重启。现代系统上优先使用 systemd 方式。后台进程应脱离终端（disown）。

# HISTORY

**plasmashell** 是 KDE 4 中 plasma-desktop 的继任者。它基于 Qt 5 和 KDE Frameworks 5 为 KDE Plasma 5 重写，提供了更好的性能和现代化特性。

# INSTALL

```apt: sudo apt install plasma-workspace```

```dnf: sudo dnf install plasma-workspace```

```pacman: sudo pacman -S plasma-workspace```

```apk: sudo apk add plasma-workspace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kwin](/man/kwin)(1), [startplasma-wayland](/man/startplasma-wayland)(1), [startplasma-x11](/man/startplasma-x11)(1)
