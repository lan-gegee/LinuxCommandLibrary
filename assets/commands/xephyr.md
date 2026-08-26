# TAGLINE

窗口中的嵌套 X 服务器

# TLDR

**启动嵌套 X 服务器**

```Xephyr :1```

**指定分辨率**

```Xephyr -screen [800x600] :1```

**全屏**

```Xephyr -fullscreen :1```

**多个屏幕**

```Xephyr -screen [800x600] -screen [800x600] :1```

**可调整大小**

```Xephyr -resizeable :1```

# SYNOPSIS

**Xephyr** [_-screen WxH_] [_-fullscreen_] [_options_] _:display_

# PARAMETERS

**-screen** _WxH_
> 屏幕尺寸。

**-fullscreen**
> 全屏模式。

**-resizeable**
> 允许调整大小。

**-no-host-grab**
> 不抓取键盘。

_:display_
> display 编号。

# DESCRIPTION

**Xephyr** 是一款基于 kdrive 的 X 服务器，作为现有 X 会话中的一个窗口运行。它创建一个功能完整、相互隔离的 X display，在桌面上显示为普通窗口，让你可以在其中运行完整的 X 环境。

Xephyr 的主要用途是在沙箱环境中测试和开发窗口管理器、桌面环境和 X11 应用程序。开发者可以在 Xephyr 内启动新的窗口管理器而不影响当前的桌面会话，从而安全地进行配置实验和测试更改。

Xephyr 支持可配置的屏幕分辨率、全屏模式、多个虚拟屏幕和可调整大小的窗口。它与宿主 X 服务器完全隔离显示，因此 Xephyr 中运行的应用程序无法与宿主显示交互。

# CAVEATS

仅支持 X11。不支持 Wayland。display 编号必须空闲。

# HISTORY

**Xephyr** 的定位是一款在窗口中运行的现代 kdrive X 服务器，用于开发和测试。

# SEE ALSO

[Xnest](/man/Xnest)(1), [Xvfb](/man/Xvfb)(1), [startx](/man/startx)(1)
