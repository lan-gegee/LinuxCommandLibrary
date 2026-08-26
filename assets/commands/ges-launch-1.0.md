# TAGLINE

创建并渲染 GStreamer 多媒体时间线

# TLDR

在时间线上**播放媒体文件**

```ges-launch-1.0 +clip [path/to/file.mp4]```

将时间线**渲染到输出文件**

```ges-launch-1.0 +clip [path/to/input.mp4] -o file:///[path/to/output.webm]```

**添加指定时长的片段**（以纳秒为单位）

```ges-launch-1.0 +clip [path/to/file.mp4] duration=[5000000000]```

对片段**应用视频特效**

```ges-launch-1.0 +clip [path/to/file.mp4] +effect videobalance saturation=[0.0]```

**加载现有项目**文件

```ges-launch-1.0 -l [path/to/project.xges]```

向时间线**添加标题片段**

```ges-launch-1.0 +title text="[Hello World]" duration=[3000000000]```

# SYNOPSIS

**ges-launch-1.0** [_options_] [_commands_]

# PARAMETERS

**-h**, **--help**
> 显示帮助选项。

**--help-all**
> 显示所有可用的帮助选项。

**--help-gst**
> 显示 GStreamer 特定的选项。

**-l**, **--load** _URI_
> 从 .xges 文件加载现有项目。

**-s**, **--save** _URI_
> 渲染前将当前时间线保存到项目文件。

**-p**, **--sample-path** _PATH_
> 在指定目录中查找缺失的资源。

**-o**, **--outputuri** _URI_
> 将时间线渲染到给定的文件 URI 而非播放。

**-f**, **--format** _PROFILE_
> 从命令行指定编码配置。

**-e**, **--encoding-profile** _PRESET_
> 使用编码配置预设。

**-t**, **--track-types** _TYPES_
> 定义要创建的轨道类型（音频、视频或两者）。

**-v**, **--videosink** _SINK_
> 设置播放用的视频输出 sink。

**-a**, **--audiosink** _SINK_
> 设置播放用的音频输出 sink。

**-m**, **--mute**
> 播放期间静音音频和视频。

**--disable-mixing**
> 禁用图层混合与合成。

**--list-transitions**
> 列出所有有效的转场类型后退出。

**-r**, **--repeat** _N_
> 将时间线重复播放 _N_ 次。

# TIMELINE COMMANDS

**+clip** _URI_ [_inpoint=ns_] [_duration=ns_] [_start=ns_] [_layer=n_]
> 向时间线添加媒体片段。时间以纳秒为单位。

**+effect** _BIN-DESCRIPTION_
> 对前一个片段应用 GStreamer bin 特效（使用 gst-launch 语法）。

**+title** [_text=STRING_] [_duration=ns_]
> 向时间线插入标题文本片段。

**set-** _PROPERTY_ _VALUE_
> 按名称设置时间线对象（片段、特效）的属性。

# DESCRIPTION

**ges-launch-1.0** 是 **GStreamer Editing Services**（GES）库的命令行工具。它从片段、特效和标题构建多媒体时间线，然后实时播放或将其渲染为指定格式的文件。时间线可以通过命令行参数构建，也可以从现有的 **.xges** 项目文件加载。

该工具利用完整的 GStreamer 管道框架，这意味着 GStreamer 支持的任何格式或编解码器都可用于输入和输出。它常用于快速视频编辑任务、自动化渲染流水线以及测试 GES 功能。

# CAVEATS

时长和时间值以**纳秒**为单位，可能不太直观（1 秒 = 1000000000）。渲染格式取决于可用的 GStreamer 插件和编码配置；缺少插件会导致静默失败或晦涩的错误。复杂的时间线更适合用 .xges 项目文件格式或 **Pitivi** 等 GUI 编辑器管理，而不是冗长的命令行调用。

# HISTORY

GES 作为 **GStreamer** 项目的一部分开发，旨在 GStreamer 媒体框架之上提供高层编辑 API。**ges-launch-1.0** 工具与 GES 库一同推出，用于在命令行构建和渲染时间线。它与 **Pitivi** 视频编辑器紧密相关，后者使用 GES 作为其后端引擎。该工具遵循 GStreamer 1.x 版本方案。

# INSTALL

```apt: sudo apt install ges1.0-tools```

```dnf: sudo dnf install gst-editing-services```

```pacman: sudo pacman -S gst-editing-services```

```apk: sudo apk add gst-editing-services```

```brew: brew install gst-editing-services```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gst-launch-1.0](/man/gst-launch-1.0)(1), [gst-inspect-1.0](/man/gst-inspect-1.0)(1), [ffmpeg](/man/ffmpeg)(1)
