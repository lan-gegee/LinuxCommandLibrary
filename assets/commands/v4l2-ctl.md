# TAGLINE

控制和查询 Video4Linux2 设备

# TLDR

**列出**所有视频设备

```v4l2-ctl --list-devices```

列出支持的**格式**和分辨率

```v4l2-ctl --list-formats-ext```

列出**指定设备**的格式

```v4l2-ctl -d /dev/video0 --list-formats-ext```

显示设备的**全部细节**

```v4l2-ctl -d /dev/video0 --all```

**列出控件**及其取值

```v4l2-ctl -d /dev/video0 --list-ctrls```

**设置控件**值

```v4l2-ctl -d /dev/video0 --set-ctrl brightness=128```

**捕获**一张 JPEG 照片

```v4l2-ctl -d /dev/video0 --set-fmt-video=width=1920,height=1080,pixelformat=MJPG --stream-mmap --stream-to=photo.jpg --stream-count=1```

捕获**视频流**

```v4l2-ctl -d /dev/video0 --stream-mmap --stream-to=video.raw --stream-count=100```

# SYNOPSIS

**v4l2-ctl** [**-h**] [**-d** _dev_] [_options_]

# DESCRIPTION

**v4l2-ctl** 用于控制 video4linux 设备，包括输入和输出的视频、VBI、广播（radio）及软件广播（swradio）设备。它提供了对几乎全部 V4L2 API 功能的访问，可用于查询和配置视频设备。

# PARAMETERS

**-d, --device DEV**
> 指定目标视频设备（默认：/dev/video0）

**-D, --info**
> 显示驱动能力

**--all**
> 显示全面的设备信息

**--list-devices**
> 列出所有视频设备

**--list-formats-ext**
> 列出支持的格式及帧尺寸

**-l, --list-ctrls**
> 列出所有可用控件

**-C, --get-ctrl**
> 获取控件值

**-c, --set-ctrl**
> 设置控件值

**--set-fmt-video**
> 设置视频捕获格式（宽度、高度、像素格式）

**--stream-mmap**
> 使用内存映射 I/O 进行捕获

**--stream-dmabuf**
> 使用 DMA 缓冲区进行捕获

**--stream-to FILE**
> 将捕获的流写入文件

**--stream-count N**
> 捕获 N 帧

**-e, --out-device DEV**
> 指定用于流式输出的设备

**-v, --verbose**
> 启用详细输出

**--help-all**
> 显示完整的选项文档

# CAVEATS

未指定时默认设备为 /dev/video0。格式设置必须与设备能力匹配。原始视频输出需要使用 ffmpeg 等工具转换后才能播放。

# HISTORY

**v4l2-ctl** 属于 **v4l-utils** 软件包，为 Linux 系统上基于 Video4Linux2 API 的设备提供用户空间实用工具。

# INSTALL

```apt: sudo apt install v4l-utils```

```dnf: sudo dnf install v4l-utils```

```pacman: sudo pacman -S v4l-utils```

```apk: sudo apk add v4l-utils```

```zypper: sudo zypper install v4l-utils```

```nix: nix profile install nixpkgs#v4l-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[v4l2-compliance](/man/v4l2-compliance)(1), [ffmpeg](/man/ffmpeg)(1), [cheese](/man/cheese)(1)
