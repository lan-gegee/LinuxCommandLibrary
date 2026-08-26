# TAGLINE

在 Wayland 上启动 KDE Plasma

# TLDR

**从控制台在 Wayland 上启动 KDE Plasma**

```startplasma-wayland```

**需要时通过 DBus 会话**包装器启动

```dbus-run-session startplasma-wayland```

**使用推荐的包装脚本启动**

```/usr/lib/plasma-dbus-run-session-if-needed startplasma-wayland```

**显式指定会话类型启动**

```XDG_SESSION_TYPE=wayland startplasma-wayland```

# SYNOPSIS

**startplasma-wayland** [_options_]

# DESCRIPTION

**startplasma-wayland** 使用 Wayland 显示协议启动 KDE Plasma 桌面环境。它会初始化 KWin Wayland 合成器、Plasma shell 以及相关的桌面服务。

当选择"Plasma (Wayland)"会话时，此命令通常由显示管理器（SDDM、GDM）自动调用，但也可以从虚拟控制台（TTY）手动启动，用于调试或最小化配置。

与 X11 相比，Wayland 提供了更好的安全性、更完善的 HiDPI 支持和更流畅的图形表现。旧式 X11 应用程序会自动通过 XWayland 兼容层运行。

# CAVEATS

从控制台启动可能需要 DBus 会话包装器，具体取决于系统配置。某些仅限 X11 的特性（如部分应用程序的全局键盘快捷键）可能无法工作。屏幕录制和远程桌面需要 portal 支持。GPU 驱动必须正确支持 Wayland。并非所有应用程序都原生支持 Wayland；它们会通过 XWayland 运行。

# HISTORY

**startplasma-wayland** 随着 KDE Plasma 获得 Wayland 支持而引入。KDE 自 **2014 年**起开始 KWin 合成器的 Wayland 开发，并在 **2020 年** KDE Plasma 5.20 前后达到可用于生产的水平。**2024 年**发布的 Plasma 6 将 Wayland 设为默认会话。该命令取代了旧的仅限 X11 的启动方式，是 KDE 向 Wayland 过渡的一部分。

# INSTALL

```apt: sudo apt install plasma-workspace```

```dnf: sudo dnf install plasma-workspace```

```pacman: sudo pacman -S plasma-workspace```

```apk: sudo apk add plasma-workspace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[startplasma-x11](/man/startplasma-x11)(1), [plasmashell](/man/plasmashell)(1)
