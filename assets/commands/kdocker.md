# TAGLINE

让任意应用停靠到系统托盘

# TLDR

**点击选择要停靠的窗口**

```kdocker```

**启动应用并将其停靠到托盘**

```kdocker [application]```

**停靠当前获得焦点的窗口**

```kdocker -f```

**以自定义图标停靠**

```kdocker -i [/path/to/icon.png] [application]```

**启动应用、停靠并在启动时最小化**

```kdocker -o [application]```

**停靠窗口并在其失去焦点时最小化**

```kdocker -l [application]```

# SYNOPSIS

**kdocker** [_options_] [_command_] [_args_]

# PARAMETERS

**-f**
> 停靠当前获得焦点的窗口。

**-i** _ICON_
> 为被停靠的应用使用自定义图标。

**-l**
> 窗口失去焦点时最小化到托盘。

**-m**
> 保持应用窗口映射（可见）；最小化时不隐藏。

**-o**
> 启动后立即最小化到托盘。

**-p** _SECONDS_
> 停靠前等待指定的秒数。

**-t**
> 应用窗口关闭时移除托盘图标。

**-q**
> 禁用通知气泡消息。

**-w** _WINDOW_ID_
> 停靠具有指定 X11 窗口 ID 的窗口。

**--version**
> 显示版本信息。

# DESCRIPTION

**kdocker** 允许将任意应用停靠到系统托盘。应用被停靠后，点击其托盘图标即可切换窗口的可见性，从而为原生不支持系统托盘的应用提供托盘功能。

该工具的工作方式是选中一个窗口（通过鼠标点击交互选择或自动选择），并通过系统托盘管理其可见性。它在任何 X11 桌面环境中都适用于 Qt 和 GTK 应用。

# CAVEATS

需要系统托盘（大多数桌面环境都提供）。仅支持 X11；不支持 Wayland。行为可能因窗口管理器而异。由于窗口管理的特殊性，某些应用可能无法正确停靠。当应用创建窗口需要时间时，**-p** 延迟选项会有帮助。

# HISTORY

KDocker 最初是一个 KDE 专用工具，后来演变为可在任何 X11 桌面环境中工作。它提供不依赖工具包的通用系统托盘功能。

# INSTALL

```apt: sudo apt install kdocker```

```zypper: sudo zypper install kdocker```

```nix: nix profile install nixpkgs#kdocker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[alltray](/man/alltray)(1), [trayer](/man/trayer)(1)
