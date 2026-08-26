# TAGLINE

将桌面屏幕录制为视频文件

# TLDR

**录制全屏**

```recordmydesktop -o [output.ogv]```

**录制指定窗口**

```recordmydesktop --windowid $(xdotool selectwindow) -o [output.ogv]```

**录制区域**

```recordmydesktop -x [100] -y [100] --width [800] --height [600] -o [output.ogv]```

**录制时不录声音**

```recordmydesktop --no-sound -o [output.ogv]```

# SYNOPSIS

**recordmydesktop** [_options_]

# PARAMETERS

**-o** _file_
> 输出文件。

**--windowid** _id_
> 录制指定窗口。

**-x**, **-y**
> 起始位置。

**--width**, **--height**
> 录制尺寸。

**--no-sound**
> 禁用音频。

**--fps** _n_
> 每秒帧数。

**--delay** _n_
> 开始前的延迟。

**--on-the-fly-encoding**
> 边录制边编码。

# DESCRIPTION

**recordmydesktop** 是一款面向 Linux X11 会话的轻量级屏幕录制工具，可将桌面视频和音频捕获为 Ogg Theora/Vorbis 格式。它可以录制全屏、按 ID 选择的特定窗口，或由位置和尺寸定义的矩形区域。

音频从默认的 ALSA 或 OSS 输入设备捕获，可用 **--no-sound** 禁用。用 Ctrl+C 停止录制后，该工具会将捕获的帧编码到最终输出文件中。**--on-the-fly-encoding** 选项在录制过程中进行编码，可减少后期处理时间，但 CPU 占用更高。

# EXAMPLES

```bash
# Record full screen
recordmydesktop -o screencast.ogv

# Record window (click to select)
recordmydesktop --windowid $(xdotool selectwindow)

# Record region
recordmydesktop -x 0 -y 0 --width 1280 --height 720 -o region.ogv

# High quality
recordmydesktop --v_quality 63 --s_quality 10 -o hq.ogv

# No cursor
recordmydesktop --no-cursor -o nocursor.ogv
```

# CONTROLS

```
Ctrl+C       - Stop recording
Ctrl+Alt+P   - Pause (if enabled)
```

# CAVEATS

仅支持 X11（不支持 Wayland）。输出为 Ogg 格式。如需其他格式请用 ffmpeg 转换。

# HISTORY

recordmydesktop 由 **John Googalidis** 创建，是一款简单高效的 Linux 屏幕录制工具。

# INSTALL

```apt: sudo apt install recordmydesktop```

```pacman: sudo pacman -S recordmydesktop```

```apk: sudo apk add recordmydesktop```

```zypper: sudo zypper install recordmydesktop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [peek](/man/peek)(1), [obs](/man/obs)(1)
