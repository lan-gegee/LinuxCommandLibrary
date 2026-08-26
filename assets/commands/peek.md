# TAGLINE

Linux 上简单的动画 GIF 录屏工具

# TLDR

**开始录制**

```peek```

**录制指定窗口**

```peek --window```

**录制为指定格式**

```peek --format [gif|mp4|webm]```

**录制到文件**

```peek -o [output.gif]```

# SYNOPSIS

**peek** [_options_]

# PARAMETERS

**-o**, **--output** _file_
> 输出文件路径。

**--format** _format_
> 输出格式（gif、mp4、webm、apng）。

**--window**
> 选择要录制的窗口。

**--fullscreen**
> 录制全屏。

**--delay** _seconds_
> 开始录制前的延迟时间。

# DESCRIPTION

**peek** 是一款适用于 Linux 的简单动画 GIF 录屏工具。它提供易于使用的界面来创建屏幕录制，对编写文档和提交错误报告特别有用。
# 启动 peek 图形界面
peek

# 录制为 MP4
peek --format mp4

# 延迟录制
peek --delay 3 -o demo.gif
```

# KEYBOARD SHORTCUTS

```
Ctrl+R - Start/stop recording
Ctrl+P - Pause/resume
Escape - Cancel
```

# CONFIGURATION

可通过图形界面设置的选项：
- 帧率
- 缩小比例
- 输出格式
- 录制区域

# CAVEATS

GIF 文件可能很大。对 Wayland 的支持因环境而异。某些格式需要 FFmpeg。

# HISTORY

peek 由 **Philipp Wolfer** 开发，是一款面向 Linux 桌面的简易 GIF 录屏工具。

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [byzanz-record](/man/byzanz-record)(1), [recordmydesktop](/man/recordmydesktop)(1)

# INSTALL

```apt: sudo apt install peek```

```pacman: sudo pacman -S peek```

```apk: sudo apk add peek```

```zypper: sudo zypper install peek```

```nix: nix profile install nixpkgs#peek```

<!-- packages: 2026-07-22 -->
