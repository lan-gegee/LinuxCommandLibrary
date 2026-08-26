# TAGLINE

从 UVC 网络摄像头捕获静态图像

# TLDR

从网络摄像头**捕获单张图像**

```uvccapture```

**捕获到指定文件**

```uvccapture -o [image.jpg]```

**以指定分辨率捕获**

```uvccapture -x [1280] -y [720]```

**从指定设备捕获**

```uvccapture -d [/dev/video1]```

**设置 JPEG 质量**

```uvccapture -q [90]```

每隔 N 秒**连续拍摄**

```uvccapture -t [5] -o [image.jpg]```

每次捕获后**运行命令**

```uvccapture -t [10] -c "[scp image.jpg user@host:]"```

**调整亮度和对比度**

```uvccapture -B [128] -C [64]```

# SYNOPSIS

**uvccapture** [_options_]

# PARAMETERS

**-o** _FILE_
> 输出文件名（默认：snap.jpg）

**-d** _DEVICE_
> 视频设备（默认：/dev/video0）

**-x** _WIDTH_
> 图像宽度（必须是设备支持的值）

**-y** _HEIGHT_
> 图像高度（必须是设备支持的值）

**-q** _QUALITY_
> JPEG 质量 0-100（默认：95）

**-t** _SECONDS_
> 连续捕获间隔（0 表示单次拍摄）

**-c** _COMMAND_
> 每次捕获后要运行的命令

**-w**
> 等待命令执行完毕后再进行下一次捕获

**-s** _FRAMES_
> 首次捕获后要跳过的帧数

**-r**
> 使用 read() 而不是 mmap 进行捕获

**-m**
> 切换到 YUYV 捕获模式

**-v**
> 详细输出

**-B** _VALUE_
> 设置亮度

**-C** _VALUE_
> 设置对比度

**-S** _VALUE_
> 设置饱和度

**-G** _VALUE_
> 设置增益

# DESCRIPTION

**uvccapture** 从兼容 USB Video Class（UVC）的网络摄像头捕获静态图像。它输出 JPEG 图像，专为脚本编写、延时摄影以及无图形界面的自动化图像采集而设计。

该工具使用 Video4Linux2（V4L2）访问摄像头。分辨率必须为设备所支持；可使用 **v4l2-ctl --list-formats-ext** 查看可用选项。高分辨率（>960x720）会自动启用 YUYV 捕获模式。

要进行连续捕获，可将 **-t** 与以秒为单位的时间间隔配合使用。**-c** 选项会在每次捕获后运行一条命令，可用于上传图像或触发其他操作。JPEG 之外的图像处理可以借助 ImageMagick 等工具完成。

# CAVEATS

用户必须对视频设备拥有读写权限。分辨率必须为网络摄像头原生支持。仅支持 JPEG 输出；其他格式请使用 ImageMagick。某些摄像头可能需要预热帧（**-s**）才能获得正确的曝光。依赖 libjpeg 库。

# HISTORY

uvccapture 是为在 Linux 系统上从 UVC 网络摄像头捕获图像而开发的。UVC（USB Video Class）是 USB 视频设备的一项标准，可在各操作系统间提供免驱动兼容性。该工具被设计为完整网络摄像头应用的轻量替代品，专注于命令行脚本和自动化场景。

# INSTALL

```apt: sudo apt install uvccapture```

```nix: nix profile install nixpkgs#uvccapture```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fswebcam](/man/fswebcam)(1), [v4l2-ctl](/man/v4l2-ctl)(1), [ffmpeg](/man/ffmpeg)(1), [streamer](/man/streamer)(1)
