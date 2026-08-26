# TAGLINE

Wayland 的 X11 兼容层

# TLDR

以 rootless 模式**启动**（合成器的典型用法）

```Xwayland :0 -rootless```

以 rootful 模式**启动用于测试**

```Xwayland :1 -geometry [1920x1080]```

以全屏 rootful 模式**启动**

```Xwayland :1 -fullscreen```

带窗口装饰**启动**

```Xwayland :1 -decorate```

强制使用共享内存后端

```Xwayland :0 -rootless -shm```

启用详细输出

```Xwayland :0 -rootless -verbose [2]```

# SYNOPSIS

**Xwayland** [:_display_] [_options_]

# PARAMETERS

**-rootless**
> 以 rootless 模式运行，将 X 客户端融入 Wayland 桌面。

**-fullscreen**
> 全屏运行 rootful 窗口。

**-geometry** _WxH_
> 设置 rootful 窗口的几何尺寸。

**-decorate**
> 为 rootful 窗口添加装饰。

**-output** _name_
> 全屏 rootful 模式使用的输出。

**-host-grab**
> 禁用宿主快捷键并捕获指针（按 Ctrl+Shift 释放）。

**-shm**
> 强制使用共享内存后端。

**-glamor**
> 强制使用 OpenGL 渲染（而非 GL ES）。

**-hidpi**
> 在 rootful 模式下适配输出缩放。

**-noTouchPointerEmulation**
> 禁用触摸指针模拟。

**-nokeymap**
> 忽略合成器的键盘映射。

**-listenfd** _fd_
> 添加监听套接字（由合成器使用）。

**-wm** _fd_
> 窗口管理器套接字（由合成器使用）。

**-verbose** _n_
> 设置详细程度。

**-version**
> 显示版本。

# DESCRIPTION

**Xwayland** 是一种 X 服务器，用于在 Wayland 合成器下运行 X11 应用程序。它把 X11 协议翻译为 Wayland，让传统的 X 应用能够在现代 Wayland 桌面中工作。

在 rootless 模式（默认）下，X 窗口与 Wayland 窗口无缝融合，由合成器统一管理。在 rootful 模式下，Xwayland 运行在自己的窗口中，适合测试或隔离使用。

当 X11 应用启动时，Wayland 合成器（GNOME、KDE Plasma、Sway 等）通常会自动拉起 Xwayland。

输入、剪贴板和拖放在 X11 与 Wayland 上下文之间互通。

# CAVEATS

部分 X11 特有功能可能不可用（屏幕捕获、全局热键）。性能可能低于原生 Wayland。rootful 模式主要用于测试。HiDPI 缩放需要合成器支持。

# HISTORY

**Xwayland** 作为 X.Org 服务器项目的组成部分而开发，旨在向 Wayland 过渡期间保持 X11 兼容性。对于尚未移植为原生 Wayland 的应用而言，它已成为不可或缺的组件。

# INSTALL

```apt: sudo apt install xwayland```

```apk: sudo apk add xwayland```

```zypper: sudo zypper install xwayland```

```nix: nix profile install nixpkgs#xwayland```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[Xorg](/man/Xorg)(1), [sway](/man/sway)(1)
