# TAGLINE

支持动画的 Wayland 壁纸守护进程

# TLDR

**启动壁纸守护进程**

```swww-daemon```

**设置壁纸图片**

```swww img [path/to/image]```

**在特定显示器上设置壁纸**

```swww img -o [output1,output2] [path/to/image]```

**恢复上次设置的壁纸**

```swww restore```

**查询当前输出与壁纸信息**

```swww query```

**停止守护进程**

```swww kill```

**带过渡效果设置壁纸**

```swww img --transition-type [wipe] --transition-duration [1] [path/to/image]```

**用纯色清空屏幕**

```swww clear [RRGGBB]```

# SYNOPSIS

**swww** _command_ [_OPTIONS_]

**swww-daemon**

# COMMANDS

**img** _path_
> 设置壁纸图片

**restore**
> 恢复上次的壁纸

**query**
> 显示输出信息

**kill**
> 停止守护进程

**clear** _color_
> 用 RGB 颜色清空屏幕

# PARAMETERS

**-o, --outputs** _names_
> 指定目标显示器（逗号分隔）

**--transition-type** _type_
> 效果：simple、center、outer、wipe、left、right、top、bottom、any、random

**--transition-step** _n_
> 平滑度（1-255）

**--transition-fps** _n_
> 帧率（1-255，默认：30）

**--transition-duration** _seconds_
> 过渡时长

**--resize** _mode_
> 缩放模式：crop、fit、no

**--fill-color** _color_
> 未覆盖区域的颜色

# DESCRIPTION

**swww** 是一个面向 Wayland 合成器的高效动画壁纸守护进程。它支持动画 GIF 和多种图片格式（JPEG、PNG、WebP、AVIF、SVG 等），并可在不同壁纸之间实现平滑的过渡效果。守护进程可以在运行时控制，无需重启。

必须先启动守护进程（**swww-daemon**），然后由 **swww** 客户端控制壁纸设置。按输出的壁纸控制允许在多个显示器上显示不同的图片。

# ENVIRONMENT

**SWWW_TRANSITION**: 默认过渡类型
**SWWW_TRANSITION_FPS**: 默认帧率
**SWWW_TRANSITION_STEP**: 默认步长

# CAVEATS

需要 wlr-layer-shell 协议（基于 wlroots 的合成器）。不支持 GNOME。设置壁纸前守护进程必须已在运行。动画壁纸比静态图片消耗更多资源。

# HISTORY

**swww** 由 **LGFae** 创建，作为其他 Wayland 壁纸方案的轻量替代。它专注于高效和流畅的动画，同时保持较低的 CPU 和内存占用。该项目已于 **2025 年 10 月**更名为 **awww** 并迁移至 Codeberg。以 GPL-3.0 发布。

# SEE ALSO

[swaybg](/man/swaybg)(1), [hyprpaper](/man/hyprpaper)(1), [feh](/man/feh)(1)
