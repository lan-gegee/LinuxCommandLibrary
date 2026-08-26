# TAGLINE

动画式版本控制历史可视化工具

# TLDR

**可视化当前仓库**

```gource```

**可视化特定仓库**

```gource [/path/to/repo]```

**以全屏模式运行**

```gource -f```

**输出 PPM 流并通过管道传给 ffmpeg 生成视频**

```gource -1280x720 -o - | ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i - -vcodec libx264 -pix_fmt yuv420p [output.mp4]```

**设置时间缩放**

```gource --seconds-per-day [0.1]```

**隐藏特定元素**

```gource --hide filenames,mouse,progress```

**按日期范围可视化**

```gource --start-date "[2024-01-01]" --stop-date "[2024-12-31]"```

# SYNOPSIS

**gource** [_options_] [_path_]

# PARAMETERS

_PATH_
> 仓库路径（默认为当前目录）。

**-o**, **--output-ppm-stream** _FILE_
> 将 PPM 图像流输出到文件（'-' 表示标准输出）。与 ffmpeg 配合用于制作视频。

**-r**, **--output-framerate** _FPS_
> 输出帧率（25、30、60）。需与 --output-ppm-stream 配合使用。

**-WIDTHxHEIGHT**, **--viewport** _WIDTHxHEIGHT_
> 设置视口大小（例如 1280x720）。

**--seconds-per-day** _SEC_
> 历史中每一天对应的时间（秒）（默认：10）。

**--hide** _ELEMENTS_
> 隐藏显示元素（逗号分隔）：bloom、date、dirnames、files、filenames、mouse、progress、root、tree、users、usernames。

**--start-date** _DATE_
> 从指定日期开始（YYYY-MM-DD 格式）。

**--stop-date** _DATE_
> 在指定日期停止。

**-f**, **--fullscreen**
> 全屏模式。

**--title** _TITLE_
> 设置标题。

**--load-config** _FILE_
> 加载配置文件。

**--save-config** _FILE_
> 将当前选项保存到配置文件。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**gource** 将版本控制历史可视化为动画树。开发者以化身的形式出现并进行修改，文件和目录在实时动画中从中心向外分支生长。

该工具支持 Git、SVN、Mercurial 和 Bazaar 仓库。输出可以通过管道传给 ffmpeg 等视频编码器，以创建便于分享的项目历史录像。

# CAVEATS

需要 OpenGL。包含大量文件或提交的大型仓库渲染速度可能较慢。输出流使用未压缩的 PPM 格式，因此编码前通过管道传输的视频文件可能非常大。对于大型仓库，可使用 --seconds-per-day 和 --hide 进行优化。

# HISTORY

gource 由 **Andrew Caudwell** 创建，旨在将软件开发历史可视化为引人入胜的动画。

# INSTALL

```apt: sudo apt install gource```

```dnf: sudo dnf install gource```

```pacman: sudo pacman -S gource```

```apk: sudo apk add gource```

```zypper: sudo zypper install gource```

```brew: brew install gource```

```nix: nix profile install nixpkgs#gource```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-log](/man/git-log)(1), [ffmpeg](/man/ffmpeg)(1)
