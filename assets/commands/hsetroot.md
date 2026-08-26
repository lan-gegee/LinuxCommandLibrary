# TAGLINE

设置 X11 根窗口背景

# TLDR

**设置纯色背景**

```hsetroot -solid "[#1a1b26]"```

**设置壁纸（填充）**

```hsetroot -fill [wallpaper.jpg]```

**设置壁纸（居中）**

```hsetroot -center [wallpaper.png]```

**设置壁纸（平铺）**

```hsetroot -tile [pattern.png]```

**设置渐变**

```hsetroot -add "[#1a1b26]" -add "[#24283b]" -gradient [0]```

**以 cover 模式设置**

```hsetroot -cover [wallpaper.jpg]```

# SYNOPSIS

**hsetroot** [_options_]

# PARAMETERS

**-solid** _color_
> 纯色背景。

**-fill** _image_
> 缩放至填满屏幕。

**-center** _image_
> 居中显示图像。

**-tile** _image_
> 平铺图像。

**-cover** _image_
> 覆盖屏幕，保持宽高比。

**-add** _color_
> 向渐变添加颜色。

**-gradient** _angle_
> 以指定角度创建渐变。

**-screens** _n_
> 应用到 n 个屏幕。

**-brightness** _value_
> 调整亮度。

**-contrast** _value_
> 调整对比度。

# DESCRIPTION

**hsetroot** 用于设置 X11 根窗口背景。它常与不自带壁纸功能的极简窗口管理器一起使用，如 dwm、bspwm 或 i3。

该工具支持纯色、多种缩放模式的图像以及渐变。它轻量且易于脚本化。

# CAVEATS

仅支持 X11；不适用于 Wayland。某些合成器可能会覆盖设置。需要 Imlib2。颜色格式：#RRGGBB 或颜色名称。

# HISTORY

hsetroot 是各种根窗口背景设置工具的分支/重写。它在需要专门壁纸处理的极简/平铺窗口管理器社区中很常用。

# INSTALL

```apt: sudo apt install hsetroot```

```dnf: sudo dnf install hsetroot```

```pacman: sudo pacman -S hsetroot```

```zypper: sudo zypper install hsetroot```

```nix: nix profile install nixpkgs#hsetroot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[feh](/man/feh)(1), [nitrogen](/man/nitrogen)(1), [xwallpaper](/man/xwallpaper)(1), [xsetroot](/man/xsetroot)(1)
