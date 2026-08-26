# TAGLINE

支持动画效果的 Wayland 壁纸管理器

# TLDR

**设置壁纸图片**

```awww img [path/to/image]```

**在指定显示器上设置壁纸**

```awww img -o [output1,output2] [path/to/image]```

**带过渡效果设置壁纸**

```awww img --transition-type [wipe] --transition-duration [1] [path/to/image]```

**恢复上次设置的壁纸**

```awww restore```

**用纯色清空屏幕**

```awww clear [RRGGBB]```

**查询当前输出与壁纸信息**

```awww query```

**停止守护进程**

```awww kill```

# SYNOPSIS

**awww** _command_ [_options_]

# COMMANDS

**img** _path_
> 设置壁纸图片或动画 GIF。使用 **-** 可从 stdin 读取。

**restore**
> 在输出上重新显示之前显示的图片。

**clear** _color_
> 用纯色填充指定的输出。

**clear-cache**
> 删除 awww 的缓存目录。

**query**
> 请求守护进程的输出详情（名称和尺寸）。

**kill**
> 终止守护进程。

# PARAMETERS

**-o, --outputs** _names_
> 指定目标显示器（逗号分隔）。

**-f, --filter** _filter_
> 缩放滤镜：Nearest、Bilinear、CatmullRom、Mitchell、Lanczos3。

**--resize** _mode_
> 缩放模式：no、crop、fit、stretch。

**--no-resize**
> 禁用缩放；改为居中显示图片。

**--fill-color** _RRGGBB_
> 未填充区域的填充色（默认：000000）。

**-t, --transition-type** _type_
> 过渡效果：none、simple、fade、left、right、top、bottom、wipe、wave、grow、center、any、outer、random。

**--transition-step** _n_
> 每帧的 RGB 增量（0-255）。

**--transition-duration** _seconds_
> 过渡完成时间，以秒为单位。

**--transition-fps** _n_
> 过渡帧率（最大 255）。

**--transition-angle** _degrees_
> wipe 和 wave 过渡的角度。

**--transition-pos** _position_
> grow 和 outer 效果的圆心位置。

**--transition-bezier** _curve_
> 自定义 cubic-bezier 动画曲线。

**--transition-wave** _width,height_
> wave 过渡的波浪尺寸。

**-n, --namespace** _name_
> 指定某个 Wayland namespace。

**-a, --all**
> 面向所有活动的 namespace。

# DESCRIPTION

**awww**（"An Answer to your Wayland Wallpaper Woes"）是一款面向 Wayland 合成器的壁纸管理器。它在运行时控制 **awww-daemon** 来更换显示器背景，支持动画 GIF、多种图片格式，以及壁纸之间平滑的过渡效果。

必须先用 **awww-daemon** 启动守护进程，然后由 **awww** 客户端发送命令来控制壁纸设置。它支持按输出分别控制壁纸，可在多台显示器上显示不同图片。处理过的图片会被缓存以优化性能。

# CAVEATS

需要实现 wlr-layer-shell 协议的合成器（通常是基于 wlroots 的合成器，如 Sway 或 Hyprland）。不支持 GNOME 或 KDE。设置壁纸前必须先运行守护进程。动画壁纸比静态图片消耗更多资源。

# HISTORY

**awww** 是 **swww** 更名后的后继项目，由 **LGFae** 创建。项目名称从 "A Solution to your Wayland Wallpaper Woes" 改为 "An Answer to your Wayland Wallpaper Woes"，并于 **2025** 年 **10** 月从 GitHub 迁移到 Codeberg。它专注于高效和流畅的动画，同时保持较低的资源占用。采用 GPL-3.0 许可证发布。

# INSTALL

```pacman: sudo pacman -S awww```

```apk: sudo apk add awww```

```zypper: sudo zypper install awww```

```nix: nix profile install nixpkgs#awww```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[swww](/man/swww)(1), [swaybg](/man/swaybg)(1), [hyprpaper](/man/hyprpaper)(1), [feh](/man/feh)(1)
