# TAGLINE

以客户端窗口形式运行的嵌套 X 服务器

# TLDR

**在显示 :1 上启动嵌套 X 服务器**

```Xnest :1```

**以指定窗口大小启动**

```Xnest :1 -geometry [800x600]```

**以多屏幕方式启动**

```Xnest :1 -scrns [2]```

**连接到指定的父显示服务器**

```Xnest :1 -display [:0]```

**全屏启动**

```Xnest :1 -fullscreen```

# SYNOPSIS

**Xnest** [:_display_] [_options_]

# PARAMETERS

**-display** _name_
> 要连接的父 X 服务器。默认取 DISPLAY 环境变量。

**-geometry** _WxH+X+Y_
> 嵌套服务器的窗口几何尺寸。

**-scrns** _num_
> 要创建的屏幕数量。

**-depth** _n_
> 默认颜色深度。

**-fullscreen**
> 在父显示服务器上全屏运行。

**-bw** _n_
> 边框宽度，单位为像素。

**-name** _string_
> 嵌套服务器的窗口名。

**-sss**
> 为每个屏幕启用独立的屏幕保护程序。

**-sync**
> 将窗口和图形操作与父服务器同步。对调试有用，但会显著降低性能。

# DESCRIPTION

**Xnest** 既是 X 客户端又是 X 服务器。它作为另一个 X 服务器（父服务器）中的一个窗口运行；对父服务器而言它表现为普通的 X 客户端，同时又为它自己的客户端提供完整的 X 服务器环境。

应用程序使用 Xnest 的显示号（如 `:1`）连接到它，并获得功能完备的 X 环境。多个屏幕可通过显示名中点号后的数字引用（例如用 `xterm -display :1.1` 表示第二个屏幕）。这使得测试窗口管理器、运行隔离的 X 会话或在受控窗口中显示远程 X 应用成为可能。

Xnest 通过在本地加载字体并将字体名传给真实服务器来管理字体。为了获得更好的性能和对现代 X 扩展的支持，建议改用 **Xephyr**。

# CAVEATS

缺少现代 X 扩展（XRender、Composite、RandR）。没有硬件加速。资源消耗较大。多数使用场景建议改用 Xephyr。需要使用与父服务器不同的显示号。

# HISTORY

**Xnest** 是作为 X11 的调试和测试工具开发的。它让开发者可以测试应用程序和窗口管理器，而不必拿自己的主桌面冒险。虽然它仍然可用，但在现代使用中，能力更强的 Xephyr 服务器已在很大程度上取代了它。

# INSTALL

```apt: sudo apt install xnest```

```pacman: sudo pacman -S xorg-server-xnest```

```apk: sudo apk add xorg-server-xnest```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[Xvfb](/man/Xvfb)(1), [Xorg](/man/Xorg)(1), [startx](/man/startx)(1)
