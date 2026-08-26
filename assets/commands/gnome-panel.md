# TAGLINE

传统的 GNOME 桌面面板和任务栏

# TLDR

**启动 GNOME Panel**

```gnome-panel```

**替换正在运行的面板**

```gnome-panel --replace```

# SYNOPSIS

**gnome-panel** [_options_]

# PARAMETERS

**--replace**
> 替换正在运行的面板。

**--version**
> 打印版本信息并退出

**--help**
> 显示帮助信息

# DESCRIPTION

**gnome-panel** 提供 **GNOME Flashback** 会话使用的经典 GNOME 2 风格面板。它承载应用程序菜单、窗口列表、系统托盘、时钟、通知区域、工作区切换器以及任意数量的小程序（PanelApplet），分布在一条或多条屏幕边缘面板上。布局、小程序及其偏好设置存储在 **dconf** 的 **/org/gnome/gnome-panel/** 之下。

用户登录 GNOME Flashback 会话时，该面板会自动启动；**--replace** 会停止正在运行的实例并启动新的实例，在修改配置或安装新小程序后很有用。

# CAVEATS

属于 GNOME Flashback 的一部分。现代 GNOME（3.x 及更高版本）改用 **gnome-shell**，后者不加载 gnome-panel 小程序。需要可用的 DBus 会话总线、**gnome-settings-daemon** 以及面板的 GSettings schema。

# HISTORY

gnome-panel 曾是 **GNOME 2** 的主面板，现在作为 GNOME Flashback 的一部分维护，供偏好经典桌面范式的用户使用。

# INSTALL

```apt: sudo apt install gnome-panel```

```dnf: sudo dnf install gnome-panel```

```pacman: sudo pacman -S gnome-panel```

```apk: sudo apk add gnome-panel```

```nix: nix profile install nixpkgs#gnome-panel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnome-calculator](/man/gnome-calculator)(1), [gnome-screenshot](/man/gnome-screenshot)(1), [gsettings](/man/gsettings)(1)
