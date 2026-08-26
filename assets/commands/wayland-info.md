# TAGLINE

显示 Wayland 合成器的相关信息

# TLDR

**显示**合成器通告的所有全局对象

```wayland-info```

**过滤**输出，只显示单个接口

```wayland-info -i [wl_output]```

**连接**到指定的 Wayland display

```wayland-info -d [wayland-1]```

**保存**报告到文件

```wayland-info > [path/to/file.txt]```

# SYNOPSIS

**wayland-info** [**-d** _display_] [**-i** _interface_]...

# DESCRIPTION

**wayland-info** 连接到正在运行的 **Wayland** 合成器，并打印其通过 registry 公开的全局对象，包括各自的接口名称和版本。对于常见的接口，它还会解码并打印更多细节，例如每个 **wl_output** 的显示模式、几何参数、缩放比例和变换方式，**wl_shm** 支持的格式，以及可用的 seat 及其能力。

它相当于 X11 下的 **xrandr** 或 **glxinfo** 等工具在 Wayland 上的对应物，可用于检查合成器支持哪些协议及协议版本、调试多显示器配置，以及确认会话确实运行在 Wayland 下。该工具属于 **wayland-utils** 软件包，取代了较旧的 **weston-info**。

# PARAMETERS

**-d** _display_, **--display** _display_

> 连接到指定的 Wayland display，而不是 **WAYLAND_DISPLAY** 环境变量指定的那个。

**-i** _interface_, **--interface** _interface_

> 只打印匹配给定接口名称的全局对象信息。可以重复使用以选择多个接口。

**-h**, **--help**

> 显示用法信息。

# CAVEATS

必须在 Wayland 会话中运行该工具（或让 **WAYLAND_DISPLAY**/**-d** 指向一个可访问的合成器套接字）；它无法报告 X11 会话的信息。实际能解码的接口集合取决于所安装的 wayland-utils 版本。

# INSTALL

```apt: sudo apt install wayland-utils```

```dnf: sudo dnf install wayland-utils```

```pacman: sudo pacman -S wayland-utils```

```apk: sudo apk add wayland-utils```

```zypper: sudo zypper install wayland-utils```

```nix: nix profile install nixpkgs#wayland-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[swaymsg](/man/swaymsg)(1), [weston](/man/weston)(1), [drm_info](/man/drm_info)(1), [glxinfo](/man/glxinfo)(1), [xrandr](/man/xrandr)(1)

# RESOURCES

```[Source code](https://gitlab.freedesktop.org/wayland/wayland-utils)```

```[Homepage](https://wayland.freedesktop.org)```

<!-- verified: 2026-06-16 -->
