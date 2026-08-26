# TAGLINE

把终端录制转换为动画 GIF

# TLDR

**将 asciinema 录制转换为 GIF**

```agg [recording.cast] [output.gif]```

设置**字号**

```agg --font-size [20] [recording.cast] [output.gif]```

设置**播放速度**

```agg --speed [2] [recording.cast] [output.gif]```

使用**自定义主题**

```agg --theme [monokai] [recording.cast] [output.gif]```

设置输出**尺寸**

```agg --cols [80] --rows [24] [recording.cast] [output.gif]```

# SYNOPSIS

**agg** [_options_] _input.cast_ _output.gif_

# DESCRIPTION

**agg**（asciinema gif generator）把 asciinema 终端录制转换为动画 GIF 文件。它会渲染终端会话的颜色、光标和所有格式，生成适合放进文档或分享的高质量 GIF。

该工具用 Rust 编写，提供丰富的输出外观定制选项，包括主题、字体、尺寸和播放速度。

# PARAMETERS

**--font-size** _size_
> 字体大小，单位像素（默认：16）。

**--font-family** _name_
> 要使用的字体家族列表，逗号分隔。

**--font-dir** _dir_
> 额外扫描字体文件的目录。

**--line-height** _factor_
> 行高，以字号的倍数表示（默认：1.4）。

**--speed** _factor_
> 播放速度倍率（默认：1）。

**--theme** _name_
> 配色主题（asciinema、dracula、github-dark、github-light、gruvbox-dark、kanagawa、monokai、nord、solarized-dark、solarized-light）。默认：dracula。

**--cols** _n_
> 覆盖终端宽度（列数）（默认：沿用录制内容）。

**--rows** _n_
> 覆盖终端高度（行数）（默认：沿用录制内容）。

**--fps-cap** _n_
> 最大帧率，每秒帧数（默认：30）。

**--renderer** _type_
> 渲染后端：swash（默认）或 resvg。

**--idle-time-limit** _seconds_
> 把帧间空闲时间限制为指定秒数（默认：5）。

**--no-loop**
> 禁用循环；动画只播放一次。

**--last-frame-duration** _seconds_
> 最后一帧的停留时长（默认：3 秒）。

# CAVEATS

较大或较长的录制会生成体积可观的 GIF 文件。可考虑调整播放速度或 idle-time-limit 来缩小文件。字体渲染效果取决于系统可用的字体。

# HISTORY

**agg** 作为其他 asciinema 转 GIF 工具的 Rust 实现替代方案而创建，性能更好、渲染质量更高。它作为 asciinema 生态的一部分持续维护。

# INSTALL

```aur: yay -S agg```

```brew: brew install agg```

```nix: nix profile install nixpkgs#agg```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[asciinema](/man/asciinema)(1), [ffmpeg](/man/ffmpeg)(1)

# RESOURCES

```[Source code](https://github.com/asciinema/agg)```

```[Documentation](https://docs.asciinema.org/manual/agg/)```

<!-- verified: 2026-06-11 -->
