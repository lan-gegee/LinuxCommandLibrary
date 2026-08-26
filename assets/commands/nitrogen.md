# TAGLINE

X Window 桌面的壁纸浏览器与设置工具

# TLDR

**浏览**某个目录下的壁纸

```nitrogen [path/to/directory]```

以自动尺寸**设置**壁纸

```nitrogen --set-auto [path/to/file]```

**恢复**上次的壁纸

```nitrogen --restore```

设置壁纸并**缩放**以适配屏幕

```nitrogen --set-scaled [path/to/file]```

设置壁纸**居中**显示

```nitrogen --set-centered [path/to/file]```

设置壁纸**平铺**

```nitrogen --set-tiled [path/to/file]```

# SYNOPSIS

**nitrogen** [**--restore**] [**--set-auto**|**--set-scaled**|**--set-centered**|**--set-tiled**|**--set-zoom** _file_] [_directory_]

# PARAMETERS

**--restore**
> 恢复之前设置的壁纸

**--set-auto _file_**
> 以自动尺寸设置壁纸

**--set-scaled _file_**
> 设置壁纸缩放以填满屏幕

**--set-centered _file_**
> 设置壁纸在屏幕上居中

**--set-tiled _file_**
> 设置壁纸平铺整个屏幕

**--set-zoom _file_**
> 设置壁纸缩放填充

**--set-zoom-fill _file_**
> 设置壁纸缩放并裁剪至填满

**--save**
> 保存当前设置

**--head _n_**
> 在指定的显示器上设置壁纸（Xinerama）

# DESCRIPTION

**nitrogen** 是面向 X Window 桌面的壁纸浏览器和设置工具。它提供图形界面来浏览和挑选壁纸，并支持多显示器配置。

该工具会保存壁纸设置，登录后可用 --restore 标志恢复。它支持多种缩放模式，兼容 Xinerama/RandR 多显示器环境。

# CAVEATS

仅支持 X Window System，不支持 Wayland。设置保存在 ~/.config/nitrogen/ 中。如需开机自动恢复，请将 "nitrogen --restore &" 添加到自启动脚本。

# HISTORY

**nitrogen** 的定位是为不含内置壁纸功能的窗口管理器提供轻量的壁纸设置工具。它常与 i3、bspwm、openbox 等平铺式窗口管理器配合使用。

# INSTALL

```apt: sudo apt install nitrogen```

```dnf: sudo dnf install nitrogen```

```zypper: sudo zypper install nitrogen```

```nix: nix profile install nixpkgs#nitrogen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[feh](/man/feh)(1), [xwallpaper](/man/xwallpaper)(1), [hsetroot](/man/hsetroot)(1)
