# TAGLINE

打印文件的媒体类型

# TLDR

**判断文件**的媒体类型

```gst-typefind-1.0 [path/to/file]```

**检测多个文件**的媒体类型

```gst-typefind-1.0 [path/to/file1] [path/to/file2]```

类型检测时**使用自定义插件路径**

```gst-typefind-1.0 --gst-plugin-path=[path/to/plugins] [path/to/file]```

# SYNOPSIS

**gst-typefind-1.0** [_options_] _files_

# PARAMETERS

**--gst-plugin-path=**_PATH_
> 向 GStreamer 插件搜索路径添加以冒号分隔的目录。

**--gst-plugin-spew**
> 启用加载 GStreamer 插件时的错误打印。

**--gst-debug-level=**_LEVEL_
> 设置调试输出阈值（0-9，默认为 0）。

**--gst-info-mask=**_FLAGS_
> 设置 GStreamer info 标志。

**--gst-debug-mask=**_FLAGS_
> 设置 GStreamer 调试标志。

**--gst-mask=**_FLAGS_
> 同时设置 GStreamer 的 info 和调试标志。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gst-typefind-1.0** 是来自 GStreamer 多媒体框架的命令行工具，用于识别文件的媒体类型（MIME 类型）。它使用 GStreamer 的 typefind 子系统，通过已安装的插件检查文件头和内容模式，从而确定文件包含何种媒体。

该工具采用基于概率的检测机制，插件会为其媒体类型匹配结果报告置信度。它专为 GStreamer 能处理的多媒体文件设计，并非通用的文件类型检测器。

# CAVEATS

检测准确性完全取决于已安装的 GStreamer 插件。如果缺少特定媒体格式对应的插件，文件可能无法被正确识别或完全无法识别。此工具不能取代通用的 **file** 命令，因为它只识别已安装的 GStreamer 插件生态所支持的媒体类型。

# HISTORY

**gst-typefind-1.0** 是 **GStreamer** 多媒体框架的一部分，该框架最初为 GNOME 项目而创建。**1.0** 后缀随 **2012 年 9 月**的 GStreamer 1.0 发布引入，以便与较旧的 0.10 系列并行安装。typefind 子系统是 GStreamer 架构的核心部分，使整个框架具备自动媒体格式检测能力。

# INSTALL

```apt: sudo apt install gstreamer1.0-tools```

```apk: sudo apk add gstreamer-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gst-inspect-1.0](/man/gst-inspect-1.0)(1), [gst-launch-1.0](/man/gst-launch-1.0)(1), [file](/man/file)(1)
