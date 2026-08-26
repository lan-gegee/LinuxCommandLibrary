# TAGLINE

封装 ffmpeg 的键盘驱动终端 UI

# TLDR

在当前目录**启动**交互式 TUI

```nano-ffmpeg```

**打开指定目录的文件选择器**

```nano-ffmpeg -d [path/to/videos]```

**跳过选择器**，直接载入预置文件进行操作

```nano-ffmpeg -d [path/to/video.mp4]```

为本次会话**强制**使用指定的 UI 主题

```nano-ffmpeg -t [dark|light]```

**显示**版本

```nano-ffmpeg --version```

# SYNOPSIS

**nano-ffmpeg** [_-t theme_] [_-d path_] [_--version_] [_--help_]

# PARAMETERS

**-d** _path_, **--dir** _path_
> 若 _path_ 是目录，则以该目录为根打开文件选择器。若 _path_ 是文件，则跳过选择器并直接将其加载到操作菜单。

**-t** _theme_, **--theme** _theme_
> 覆盖当前会话的 UI 主题。可选 **dark** 或 **light**。

**--version**
> 输出版本后退出。

**-h**, **--help**
> 输出用法信息。

# DESCRIPTION

**nano-ffmpeg** 是一个终端用户界面，它将 **ffmpeg** 封装在一个键盘驱动的仪表盘之后。用户无需记忆各种标志，只需浏览文件、从菜单中选择操作、通过预设调整参数，并在 ffmpeg 后台编码时观看实时进度条。

该 TUI 提供十二种常用操作：格式转换、音频提取、调整尺寸、剪辑、压缩、拼接、字幕处理、GIF 制作、缩略图提取、加水印、音频调整，以及防抖、去隔行和旋转等视频滤镜。每个设置界面都会预览将要执行的确切 **ffmpeg** 命令，让用户在工作中学习底层标志。

硬件加速编码器会被自动检测：macOS 上的 **VideoToolbox**、配备 NVIDIA GPU 系统上的 **NVENC**，以及 Linux 上的 **VAAPI**。编码过程中的实时统计包括已用时间、剩余时间、速度、FPS、码率、已写入帧数和输出大小。

# CAVEATS

需要已安装 **ffmpeg** 和 **ffprobe** 并能在 **PATH** 中找到；nano-ffmpeg 只负责调度它们。要求终端至少有 80x24 个单元格。硬件编码器的可用性取决于平台、驱动程序和 ffmpeg 的构建选项。

# HISTORY

**nano-ffmpeg** 是由 **dgr8akki** 用 **Go** 编写的开源项目，通过 Homebrew、Scoop、**go install** 以及 GitHub 上的预构建二进制文件分发。其目标是降低 ffmpeg 的入门门槛：提供引导式、易于发现的工作流，同时不牺牲对底层命令的访问。

# INSTALL

```aur: yay -S nano-ffmpeg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [ffprobe](/man/ffprobe)(1)
