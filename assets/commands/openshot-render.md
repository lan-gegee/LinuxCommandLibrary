# TAGLINE

从命令行渲染 OpenShot 项目

# TLDR

将 OpenShot 项目**渲染**为视频文件

```openshot-render [project.osp] [output.mp4]```

使用导出配置**渲染**（例如 HD 1080p 30fps）

```openshot-render -p "[HD 1080p 30 fps]" [project.osp] [output.mp4]```

**渲染特定帧范围**

```openshot-render -s [1] -e [300] [project.osp] [output.mp4]```

**使用自定义视频编解码器渲染**

```openshot-render -v [libx264] -b [8000000] [project.osp] [output.mp4]```

# SYNOPSIS

**openshot-render** [_options_] _project_ _output_

# PARAMETERS

_PROJECT_
> 现有 OpenShot 项目文件（.osp）的路径。

_OUTPUT_
> 输出视频文件的路径。容器格式由文件扩展名决定。

**-p** _PROFILE_
> 导出配置名称（必须与已安装的 OpenShot 配置相匹配）。

**-s** _START_
> 导出中包含的第一帧。

**-e** _END_
> 导出中包含的最后一帧。

**-v** _CODEC_
> 传递给 FFmpeg 的视频编解码器（如 libx264、libvpx）。

**-a** _CODEC_
> 音频编解码器。

**-b** _BITRATE_
> 视频比特率（单位：比特/秒）。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**openshot-render** 是 OpenShot 的 libopenshot 渲染引擎的命令行前端。它无需启动 GUI 即可将 OpenShot 项目文件（.osp）无头导出为视频文件，非常适合自动化批量渲染、渲染农场和 CI 流水线。

该工具读取项目的时间线，应用特效和转场，并在底层使用 FFmpeg 编码最终的视频。配置名称和编解码器必须与 OpenShot 安装中可用的名称一致。

# CAVEATS

.osp 项目文件引用的是媒体的绝对路径；缺少源文件会导致渲染失败。GPU 加速编码器取决于链接到 libopenshot 的 FFmpeg 构建。配置名称区分大小写。

# HISTORY

**openshot-render** 由 OpenShot 项目提供，用于命令行导出和批处理。它与 OpenShot Qt GUI 使用相同的渲染引擎。

# INSTALL

```dnf: sudo dnf install openshot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openshot](/man/openshot)(1), [ffmpeg](/man/ffmpeg)(1), [melt](/man/melt)(1)
