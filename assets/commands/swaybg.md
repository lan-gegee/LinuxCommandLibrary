# TAGLINE

Sway 的 Wayland 壁纸设置工具

# TLDR

**设置壁纸**

```swaybg -i [wallpaper.jpg]```

**指定输出**

```swaybg -o [HDMI-A-1] -i [wallpaper.jpg]```

**填充模式**

```swaybg -i [wallpaper.jpg] -m fill```

**平铺模式**

```swaybg -i [wallpaper.jpg] -m tile```

**纯色背景**

```swaybg -c "[#1a1a2e]"```

**居中显示图像**

```swaybg -i [wallpaper.jpg] -m center```

# SYNOPSIS

**swaybg** [_-o output_] [_-i image_] [_-m mode_] [_-c color_]

# PARAMETERS

**-i**, **--image** _FILE_
> 壁纸图像。

**-o**, **--output** _OUTPUT_
> 目标输出。

**-m**, **--mode** _MODE_
> 缩放模式。

**-c**, **--color** _COLOR_
> 背景颜色。

# MODES

**stretch** - 拉伸以填满
**fill** - 填充并裁剪超出部分
**fit** - 适配，可能出现黑边
**center** - 居中，不缩放
**tile** - 平铺图像

# DESCRIPTION

**swaybg** 为 Sway 及其他基于 wlroots 的 Wayland 合成器设置桌面壁纸。它支持以多种缩放模式（stretch、fill、fit、center、tile）显示图像文件，也可以使用十六进制代码设置纯色背景。

通过指定输出名称，可以为不同输出分配不同的壁纸，在多显示器环境中实现每个显示器独立的背景。该工具作为常驻后台进程运行；要更换壁纸，必须先结束正在运行的实例，再用所需的设置启动新实例。

swaybg 通常在 Sway 配置文件中用 `exec` 指令启动，以确保合成器启动时自动设置壁纸。

# CAVEATS

仅支持 Wayland。适用于 Sway/wlroots 合成器。每张壁纸一个实例。

# HISTORY

**swaybg** 是 **Sway** 项目（一个 Wayland 合成器）的组成部分，为基于 wlroots 的合成器提供简单的背景管理。

# INSTALL

```apt: sudo apt install swaybg```

```dnf: sudo dnf install swaybg```

```pacman: sudo pacman -S swaybg```

```apk: sudo apk add swaybg```

```zypper: sudo zypper install swaybg```

```nix: nix profile install nixpkgs#swaybg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sway](/man/sway)(1), [swaylock](/man/swaylock)(1), [feh](/man/feh)(1)
