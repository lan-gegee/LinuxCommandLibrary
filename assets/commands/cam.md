# TAGLINE

通过 libcamera 与摄像头交互

# TLDR

**列出**可用摄像头

```cam -l```

列出摄像头的**控制项**

```cam -c [camera_index] --list-controls```

将帧**捕获**到文件

```cam -c [camera_index] --capture=[frames] --file```

在**窗口**中显示摄像头画面

```cam -c [camera_index] --capture --sdl```

# SYNOPSIS

**cam** [_options_]

# DESCRIPTION

**cam** 是一个通过 libcamera 框架与摄像头交互的命令行工具。它可以列出摄像头、显示其控制项、捕获帧，并在窗口中显示实时视频。

libcamera 为 Linux 提供了现代的摄像头栈，用更灵活的架构取代了仅依赖 V4L2 的旧方案。

# PARAMETERS

**-l, --list**
> 列出可用摄像头

**-c, --camera** _index_
> 按索引选择摄像头

**--list-controls**
> 显示摄像头控制项

**--capture** [_frames_]
> 捕获指定数量的帧（0 表示不限制）

**--file**
> 将捕获的帧写入文件

**--sdl**
> 在 SDL 窗口中显示视频

**--list-properties**
> 显示摄像头属性

**--stream** _config_
> 配置流参数（如 width、height、pixelformat、role）

**--monitor**
> 监视摄像头的热插拔和移除事件

# CAVEATS

需要 libcamera 支持，并非所有摄像头都可用。某些摄像头使用直接的 V4L2 访问效果更好。

# INSTALL

```apt: sudo apt install libcamera-tools```

```dnf: sudo dnf install libcamera-tools```

```pacman: sudo pacman -S libcamera-tools```

```apk: sudo apk add libcamera-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[v4l2-ctl](/man/v4l2-ctl)(1), [rpicam-still](/man/rpicam-still)(1), [rpicam-vid](/man/rpicam-vid)(1)
