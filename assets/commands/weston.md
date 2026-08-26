# TAGLINE

参考实现的 Wayland 合成器

# TLDR

**启动 Weston 合成器**（需要 seat 访问权限）

```weston```

**使用指定的后端启动**

```weston --backend=[drm|wayland|x11]```

**使用指定的 shell 启动**

```weston --shell=[desktop|fullscreen|kiosk]```

在 X11 下**以窗口模式启动**

```weston --backend=x11```

在另一个 Wayland 合成器内**嵌套启动**

```weston --backend=wayland```

**启用 Xwayland** 以兼容 X11 客户端

```weston --xwayland```

**指定 display 套接字名称**

```weston -S [wayland-1]```

**使用指定配置文件启动**

```weston -c [path/to/weston.ini]```

# SYNOPSIS

**weston** [**-B**=_backend_] [**--shell**=_shell_] [**-S**=_name_] [**-c**=_file_] [_options_]

# PARAMETERS

**-B**, **--backend**=_backend_
> 合成器后端：drm（原生）、x11、wayland、headless、rdp、vnc、pipewire。

**--shell**=_shell_
> Shell 插件：desktop（默认）、fullscreen、kiosk、ivi。

**-S**, **--socket**=_name_
> 供客户端连接的 Wayland 套接字名称。

**-c**, **--config**=_file_
> 配置文件路径。默认为 $XDG_CONFIG_HOME/weston.ini 或 ~/.config/weston/weston.ini。

**--no-config**
> 不读取配置文件。

**--modules**=_module_
> 加载额外模块（逗号分隔）。

**--renderer**=_name_
> 选择渲染引擎（gl、pixman、vulkan、noop）。

**--xwayland**
> 通过 Xwayland 启用 X11 应用支持。

**-i**, **--idle-time**=_seconds_
> 进入屏幕保护前的空闲超时。

**--log**=_file_
> 日志文件路径。

**-l**, **--logger-scopes**=_scopes_
> 要启用的日志范围（逗号分隔）。

**--debug**
> 启用调试协议扩展。

**--width**=_pixels_
> 初始输出宽度（窗口类后端）。

**--height**=_pixels_
> 初始输出高度（窗口类后端）。

**--scale**=_factor_
> 输出缩放因子。

**-h**, **--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**Weston** 是参考实现的 Wayland 合成器，同时充当显示服务器和窗口管理器。它演示了 Wayland 协议的各项能力，并为测试和嵌入式系统提供一个功能完备的桌面环境。

Weston 支持多种后端以适应不同部署场景：DRM 用于原生访问 Linux framebuffer；X11 和 Wayland 后端用于嵌套在其他显示服务器中运行；headless/RDP/VNC 后端用于远程或测试用途。

不同的 shell 提供不同的用户界面风格：desktop shell 面向传统工作站，fullscreen shell 用于单应用的 kiosk 模式，IVI shell 则面向车载信息娱乐系统。配置通过 weston.ini 完成。

Weston 需要通过 seat 管理器（seatd 或 elogind）访问输入设备和显示硬件。在原生模式下，用户必须通过 seat 机制拥有适当的权限。

# CAVEATS

原生运行需要 Linux 内核模式设置（KMS）。直接运行需要 seat 管理配置（seatd 或 elogind）。部分功能依赖 GPU 对 EGL 和 DRM 的驱动支持。自 10.0.0 版本起 weston-launch 已弃用。

# HISTORY

**Weston** 与 **Wayland** 协议一同在 **freedesktop.org** 开发，最初由 **Kristian Høgsberg** 于 **2010 年**前后主导。它是 Wayland 概念的试验场，至今仍是参考实现。虽然生产环境的桌面通常使用 GNOME 的 Mutter 或 KDE 的 KWin 等合成器，Weston 仍在持续开发，服务于测试、嵌入式系统和车载应用。

# INSTALL

```apt: sudo apt install weston```

```dnf: sudo dnf install weston```

```pacman: sudo pacman -S weston```

```apk: sudo apk add weston```

```zypper: sudo zypper install weston```

```nix: nix profile install nixpkgs#weston```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sway](/man/sway)(1), [Xwayland](/man/Xwayland)(1), [xrandr](/man/xrandr)(1)
