# TAGLINE

在 X11 上启动 KDE Plasma

# TLDR

**从控制台在 X11 上启动 KDE Plasma**

```startplasma-x11```

**通过 xinit 启动**

```xinit /usr/bin/startplasma-x11```

**通过 startx 启动**（添加到 ~/.xinitrc）

```echo "exec startplasma-x11" > ~/.xinitrc && startx```

# SYNOPSIS

**startplasma-x11**

# DESCRIPTION

**startplasma-x11** 使用 X11 显示服务器启动 KDE Plasma 桌面环境。它会初始化 KWin X11 窗口管理器、Plasma shell 以及相关的桌面服务。

选择"Plasma (X11)"会话时，此命令通常由显示管理器（SDDM、GDM、LightDM）自动调用。在没有显示管理器的最小化环境中，也可以通过 **startx** 或 **xinit** 手动启动。

X11 提供广泛的应用程序兼容性和成熟的驱动支持。当 Wayland 在你的硬件上出现问题，或运行需要 X11 特有功能的应用程序时，可以使用此会话类型。

# CAVEATS

需要 X 服务器已在运行，或通过 xinit/startx 启动。与 Wayland 相比，X11 存在固有的安全局限（任何应用程序都可以捕获输入/屏幕）。一些现代特性（如逐显示器缩放）在 Wayland 上效果更好。从 Plasma 6 开始，Wayland 是推荐的默认会话。

# HISTORY

**startplasma-x11** 取代了旧的 **startkde** 脚本，是 KDE Plasma 5 现代化改造的一部分。X11 会话仍保留，以便兼容旧硬件、专有驱动以及需要 X11 特有功能的应用程序。随着 **2024 年** Plasma 6 的发布，Wayland 成为默认选项，但 X11 仍受支持。

# INSTALL

```apt: sudo apt install plasma-workspace```

```dnf: sudo dnf install plasma-workspace```

```pacman: sudo pacman -S plasma-workspace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[startplasma-wayland](/man/startplasma-wayland)(1), [plasmashell](/man/plasmashell)(1), [startx](/man/startx)(1), [xinit](/man/xinit)(1)
