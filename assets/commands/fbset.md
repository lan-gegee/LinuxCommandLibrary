# TAGLINE

配置 framebuffer 设备设置

# TLDR

显示当前 **framebuffer 设置**

```sudo fbset [-i|--info]```

从 fb.modes 设置 framebuffer **模式**

```sudo fbset "[800]x[600]-[60]"```

设置**任意** framebuffer 模式

```sudo fbset [-g|--geometry] [TTY_horizontal] [TTY_vertical] [monitor_horizontal] [monitor_vertical] [color_depth]```

# SYNOPSIS

**fbset** [_options_] [_mode_]

# DESCRIPTION

**fbset** 用于查看和修改 Linux framebuffer 设备的设置。它可以更改分辨率、颜色深度、时序和其他显示参数。

用于在使用 framebuffer 的系统上配置控制台显示。

# PARAMETERS

**-i, --info**
> 显示 framebuffer 信息

**-g, --geometry** _params_
> 设置几何参数（xres、yres、vxres、vyres、depth）

**-t, --timings** _params_
> 设置显示时序

**-fb** _device_
> 使用指定的 framebuffer 设备

# CONFIGURATION

**/etc/fb.modes**
> 定义预置的视频模式，包含分辨率、时序和颜色深度设置。

# CAVEATS

需要内核支持 framebuffer。可能需要 root 权限。错误的设置可能导致显示问题。

# INSTALL

```apt: sudo apt install fbset```

```pacman: sudo pacman -S fbset```

```nix: nix profile install nixpkgs#fbset```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fbi](/man/fbi)(1)
