# TAGLINE

将屏幕录制为动画 GIF 或视频

# TLDR

将屏幕**录制**到文件（默认 10 秒）

```byzanz-record [path/to/file.gif]```

录制期间显示**详细**信息

```byzanz-record -v [path/to/file.gif]```

按**指定时长**录制

```byzanz-record -d 60 [path/to/file.gif]```

开始录制前**延迟**

```byzanz-record --delay 10 [path/to/file.gif]```

# SYNOPSIS

**byzanz-record** [_options_] _file_

# DESCRIPTION

**byzanz-record** 捕获屏幕录像并以多种格式保存，包括 GIF、WebM、OGV 和 FLV。它专为制作简短的屏幕演示和用于文档或演示的动画 GIF 而设计。

默认录制时长为 10 秒。该工具支持录制特定窗口或屏幕区域。

# PARAMETERS

**-d, --duration** _seconds_
> 录制时长（秒）

**--delay** _seconds_
> 开始录制前的延迟时间

**-v, --verbose**
> 在录制期间和结束后显示信息

**-x, -y** _pixels_
> 录制区域的 X 和 Y 坐标

**-w, --width** _pixels_
> 录制区域宽度

**-h, --height** _pixels_
> 录制区域高度

**-c, --cursor**
> 录制光标移动

**-a, --audio**
> 随视频一起录制音频（当输出格式支持时）。

**--exec** _command_
> 运行指定命令并录制直到其退出（覆盖时长设置）。

**--display** _DISPLAY_
> 指定要录制的 X display。

# OUTPUT FORMATS

- **.gif** - 动画 GIF
- **.webm** - WebM 视频
- **.ogv/.ogg** - Ogg Theora 视频
- **.flv** - Flash 视频
- **.byzanz** - 原生格式

# CAVEATS

长时间录制时 GIF 输出可能产生很大的文件。仅支持 X11，不支持 Wayland。录制高分辨率屏幕可能消耗大量资源。

# INSTALL

```apt: sudo apt install byzanz```

```nix: nix profile install nixpkgs#byzanz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[peek](/man/peek)(1), [ffmpeg](/man/ffmpeg)(1), [recordmydesktop](/man/recordmydesktop)(1)
