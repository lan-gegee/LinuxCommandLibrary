# TAGLINE

视频编辑器

# TLDR

**启动 OpenShot**

```openshot-qt```

**打开项目文件**

```openshot-qt [project.osp]```

**用媒体文件打开**并加入项目

```openshot-qt [video.mp4]```

**启用调试日志**运行

```openshot-qt --debug```

# SYNOPSIS

**openshot-qt** [_options_] [_file_...]

# PARAMETERS

_FILE_
> 启动时要打开的一个或多个项目（.osp）或媒体文件。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本。

**--debug**
> 启用输出到 stdout 的详细调试日志。

**--lang** _CODE_
> 强制指定界面语言（例如 `en_US`、`de_DE`）。

**--list-languages**
> 列出可用的界面语言。

# DESCRIPTION

**openshot-qt** 用于启动 OpenShot Video Editor，这是一款免费、跨平台的非线性视频编辑器，构建于 Qt 和 libopenshot 渲染库之上。

该应用支持多轨时间线编辑、转场、动画标题、关键帧动画，并通过 FFmpeg 支持大量音频/视频编解码器。项目文件使用 **.osp** 扩展名，其中存储 JSON 序列化的片段和时间线元数据。

# CAVEATS

GUI 应用程序。需要显示器。复杂项目对资源要求较高。

# HISTORY

OpenShot 作为面向 Linux、macOS 和 Windows 的**免费开源视频编辑器**而创建。

# INSTALL

```dnf: sudo dnf install openshot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kdenlive](/man/kdenlive)(1), [shotcut](/man/shotcut)(1), [ffmpeg](/man/ffmpeg)(1)
