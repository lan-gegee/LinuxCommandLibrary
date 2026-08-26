# TAGLINE

GTK+ 网络摄像头查看与捕获应用程序

# TLDR

**启动网络摄像头查看器**

```guvcview```

**指定视频设备**

```guvcview -d [/dev/video0]```

**请求分辨率和格式**

```guvcview -x [1920x1080] -f [MJPG]```

**选择 GUI 工具包**

```guvcview -g [gtk3]```

**直接录制视频到文件**

```guvcview -j [output.mkv]```

**拍摄单张照片保存到文件**

```guvcview -i [photo.jpg] -n [1]```

# SYNOPSIS

**guvcview** [_options_]

# PARAMETERS

**-d**, **--device** _DEVICE_
> 要使用的视频设备（默认为 /dev/video0）。

**-x**, **--resolution** _WxH_
> 请求采集分辨率（如 640x480）。

**-f**, **--format** _FOURCC_
> 请求视频格式/FourCC（如 MJPG、YUYV）。

**-F**, **--fps** _NUM[/DENOM]_
> 请求帧率。

**-g**, **--gui** _API_
> 选择 GUI 工具包：none、gtk3 或 qt6。

**-r**, **--render** _API_
> 选择渲染 API：none、sdl 或 sfml。

**-m**, **--render_window** _FLAGS_
> 设置渲染窗口标志（none、full、max 或 WIDTHxHEIGHT）。

**-a**, **--audio** _API_
> 选择音频 API：none、port 或 pulse。

**-k**, **--audio_device** _INDEX_
> 为所选音频 API 选择音频设备索引。

**-j**, **--video** _FILE_
> 录制视频的文件名。

**-u**, **--video_codec** _CODEC_
> 要使用的视频编解码器（如 raw、mjpg、h264、vp80）。

**-i**, **--image** _FILE_
> 拍摄照片的文件名。

**-n**, **--photo_total** _N_
> 要拍摄的照片总数。

**-t**, **--photo_timer** _SECONDS_
> 照片拍摄之间的时间间隔。

**-p**, **--profile** _FILE_
> 加载已保存的控制配置文件。

**-e**, **--exit_on_term**
> 视频或图像采集结束后退出应用。

**-z**, **--control_panel**
> 仅以控制面板模式启动。

**-w**, **--verbosity** _LEVEL_
> 设置详细程度（默认为 0）。

**-v**, **--version**
> 打印版本信息。

**-h**, **--help**
> 打印帮助信息。

# DESCRIPTION

**guvcview** 是一款面向 Linux 上 UVC（USB Video Class）兼容网络摄像头的视频采集和控制应用程序。它提供实时预览以及亮度、对比度、曝光和白平衡等摄像头设置控制，并可以录制视频和拍摄静态照片。

新版本基于 **GTK3** 或 **Qt6** 构建界面（可用 **-g** 选择），并支持多种渲染后端（SDL、SFML）和音频 API（PortAudio、PulseAudio），可录制带声音的视频。

# CAVEATS

需要 UVC 兼容摄像头和支持 V4L2 的内核驱动。部分控制和编解码器取决于硬件/驱动程序。命令行标志和默认值在各主要 guvcview 版本间有所变化；请始终对已安装版本运行 `guvcview --help` 查看。

# HISTORY

**guvcview** 由 **Paulo Assis** 于 **2008 年**创建，最初是一款使用 V4L2 API 的简单 GTK+ Linux 网络摄像头查看器。此后它增加了 Qt6 图形界面支持和多种渲染/音频后端，同时保持轻量级定位，适合快速预览和采集网络摄像头画面而无需完整的视频编辑套件。

# INSTALL

```apt: sudo apt install guvcview```

```dnf: sudo dnf install guvcview```

```pacman: sudo pacman -S guvcview```

```apk: sudo apk add guvcview```

```zypper: sudo zypper install guvcview```

```nix: nix profile install nixpkgs#guvcview```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cheese](/man/cheese)(1), [v4l2-ctl](/man/v4l2-ctl)(1), [ffmpeg](/man/ffmpeg)(1)

# RESOURCES

```[Homepage](https://guvcview.sourceforge.net/)```

```[Source code](https://sourceforge.net/projects/guvcview/)```

<!-- verified: 2026-07-17 -->
