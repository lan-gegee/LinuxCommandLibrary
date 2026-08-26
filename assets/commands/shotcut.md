# TAGLINE

免费跨平台视频编辑器

# TLDR

**打开 Shotcut**

```shotcut```

**打开项目**

```shotcut [project.mlt]```

**打开视频文件**

```shotcut [video.mp4]```

**GPU 处理**

```shotcut --gpu```

**全屏显示**

```shotcut --fullscreen```

# SYNOPSIS

**shotcut** [_--gpu_] [_--fullscreen_] [_options_] [_file_]

# PARAMETERS

**--gpu**
> 使用 GPU 处理。

**--fullscreen**
> 让 Shotcut 窗口铺满屏幕。

**--noupgrade**
> 隐藏升级提示和菜单项。

**--glaxnimate**
> 运行 Glaxnimate 而不是 Shotcut。

**--clear-recent**
> 退出时清除最近使用的文件记录。

**--appdata** _DIR_
> 指定应用配置和数据的目录。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**Shotcut** 是一款免费开源的跨平台视频编辑器，提供基于时间轴的非线性编辑工作流。它通过 FFmpeg 后端原生支持大量音视频格式，文件无需导入或转码即可直接放到时间轴上。

编辑器内置了丰富的视频和音频滤镜，可用于特效、调色、转场和合成。在支持的硬件上，可通过 OpenGL 实现 GPU 加速，加快预览和渲染速度。项目以 MLT XML 格式保存，并可导出为多种输出格式和编解码器。

# CAVEATS

GPU 处理效果因硬件而异，并非所有系统都可用。高分辨率或多轨道项目的资源消耗较大。不支持命令行渲染；批量/脚本化导出请使用 **melt**。

# HISTORY

**Shotcut** 由 **Dan Dennedy** 基于 MLT 框架开发，旨在提供一款免费开源的视频编辑器。

# INSTALL

```apt: sudo apt install shotcut```

```dnf: sudo dnf install shotcut```

```pacman: sudo pacman -S shotcut```

```apk: sudo apk add shotcut```

```zypper: sudo zypper install shotcut```

```nix: nix profile install nixpkgs#shotcut```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kdenlive](/man/kdenlive)(1), [ffmpeg](/man/ffmpeg)(1), [melt](/man/melt)(1)
