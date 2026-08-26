# TAGLINE

KDE Plasma 的 Wayland 合成器与窗口管理器

# TLDR

**启动**带 Xwayland 的嵌套 KWin Wayland 会话

```kwin_wayland --xwayland```

**嵌套启动**并使用自定义 Wayland 套接字名称

```kwin_wayland --xwayland --socket [wayland-1]```

使用 DRM 后端在 TTY 上**运行**（默认）

```kwin_wayland --drm --xwayland```

**启动后**在会话命令结束时退出

```kwin_wayland --xwayland --exit-with-session=[kwrite]```

**启动完整的 Plasma** Wayland 会话（优先于单独调用 kwin_wayland）

```startplasma-wayland```

# SYNOPSIS

**kwin_wayland** [_options_] [_applications_...]

# PARAMETERS

**--xwayland**
> 启动一个 Xwayland 服务器，使 X11 应用能在此合成器下运行。

**--socket** _name_
> Wayland 套接字名称（默认通常为 `wayland-0`）。嵌套于另一个 Wayland 会话之下时应使用不同的名称。

**--drm**
> 使用 DRM/KMS 后端（全屏接管，通常运行在 TTY 上）。提供 OpenGL 加速。

**--framebuffer**
> 使用帧缓冲后端（无 OpenGL 加速）。

**--x11-display** _display_
> 在嵌套模式下显式指定目标 X11 显示。

**--wayland-display** _display_
> 在嵌套模式下显式指定父级 Wayland 显示。

**--exit-with-session=**_command_
> 将 _command_ 作为会话客户端运行，并在其退出时一并退出。

**--lock**
> 以锁屏状态启动。

**--replace**
> 在适用的情况下替换正在运行的窗口管理器。

**applications...**
> 可选的要启动的应用程序，作为此合成器实例的客户端运行。

# DESCRIPTION

**kwin_wayland** 是 KDE Plasma 所使用的 Wayland 合成器和窗口管理器。它在同一进程内实现 Wayland 显示服务器：客户端通过 Unix 套接字连接，由 KWin 合成窗口、装饰、虚拟桌面和桌面特效。

它是 **kwin_x11** 的 Wayland 对应版本。在正常的 Plasma Wayland 登录流程中，显示管理器和会话脚本会启动 **kwin_wayland**（通常经由 **startplasma-wayland**），用户很少需要手动调用它。

在开发和测试场景中，你可以在 X11 或另一个 Wayland 会话下用 **--xwayland** 运行一个**嵌套**实例，然后通过将 `WAYLAND_DISPLAY` 和/或 `DISPLAY` 指向嵌套套接字来启动客户端。在空闲的 TTY 上，**--drm**（未设置父显示时的默认值）会接管图形硬件。

# CAVEATS

单独启动 **kwin_wayland** 并不是受支持的 Plasma 登录方式；请使用显示管理器会话或 **startplasma-wayland**。嵌套模式和 TTY 模式主要面向测试用途。Xwayland 能支持许多 X11 应用，但剪贴板管理器、屏幕捕获以及部分全局快捷键的行为可能与纯 X11 下不同。硬件和驱动的兼容性问题（尤其是 NVIDIA）可能需要额外的环境配置。

# HISTORY

KWin 起源于 **20 世纪 90 年代**末的 KDE X11 窗口管理器。Wayland 支持在 Plasma 5 期间逐步开发；自 **Plasma 5.4** 起，KWin 已能管理 Wayland 客户端，Plasma Wayland 会话也以 **kwin_wayland** 作为合成器。Plasma 6 继续将其作为 KDE 主要的 Wayland 技术栈发布。

# INSTALL

```apt: sudo apt install kwin-wayland```

```dnf: sudo dnf install kwin```

```pacman: sudo pacman -S kwin```

```apk: sudo apk add kwin```

<!-- packages: 2026-08-01 -->

# SEE ALSO

[kwin](/man/kwin)(1), [plasmashell](/man/plasmashell)(1), [startplasma-wayland](/man/startplasma-wayland)(1), [wayland-info](/man/wayland-info)(1), [Xwayland](/man/Xwayland)(1)

# RESOURCES

```[Source code](https://invent.kde.org/plasma/kwin)```

```[Homepage](https://kde.org/plasma-desktop/)```

```[Documentation](https://community.kde.org/KWin/Wayland)```

<!-- verified: 2026-08-01 -->
