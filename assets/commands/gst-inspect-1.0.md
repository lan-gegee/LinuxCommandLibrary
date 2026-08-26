# TAGLINE

GStreamer 插件和元素检查器

# TLDR

**列出所有可用的插件和元素**

```gst-inspect-1.0```

**检查特定元素**

```gst-inspect-1.0 [filesrc]```

**按名称检查插件**

```gst-inspect-1.0 [coreelements]```

**打印所有元素的详情**

```gst-inspect-1.0 -a```

**打印某插件机器可解析的特性信息**

```gst-inspect-1.0 --print-plugin-auto-install-info [playback]```

**显示 GStreamer 版本**

```gst-inspect-1.0 --version```

**按名称或描述搜索元素**

```gst-inspect-1.0 | grep [audio]```

# SYNOPSIS

**gst-inspect-1.0** [_options_] [_element_|_plugin_]

# PARAMETERS

**-a**, **--print-all**
> 打印所有可用元素的信息。

**--print-plugin-auto-install-info**
> 打印指定插件或元素所提供特性的机器可解析列表。对软件包管理器和自动安装程序很有用。

**-b**, **--print-blacklist**
> 打印被列入黑名单（加载失败）的插件列表。

**--plugin**
> 列出插件的特性。参数被视为插件名而非元素。

**--types** _types_
> 与 `--print-all` 一起使用时按类型过滤元素（例如 Audio/Sink）。

**--exists** _element_
> 检查指定元素是否存在。存在则返回退出码 0，否则返回 1。

**--atleast-version** _version_
> 与 `--exists` 一起使用时，还检查元素版本是否不低于指定版本。

**--uri-handlers**
> 打印所有可用的 URI 处理器。

**--gst-plugin-path=**_PATH_
> 向插件搜索路径添加目录（以冒号分隔）。

**--version**
> 显示 GStreamer 版本信息。

**--help**
> 打印帮助并退出。

# DESCRIPTION

**gst-inspect-1.0** 查询 GStreamer 插件和元素的信息。它显示元素详情，包括 pad 信息、能力、带类型和默认值的属性以及可用的信号。

不带参数时，它列出所有可用插件及其元素的摘要。给定元素或插件名称时，它会显示该组件的详细信息，包括元素的工厂详情、pad、属性和信号。

这是 GStreamer 流水线开发的重要工具，让开发者能够在用 **gst-launch-1.0** 构建流水线之前发现可用元素、了解其能力并检查属性类型。

# INSTALL

```apt: sudo apt install gstreamer1.0-tools```

```apk: sudo apk add gstreamer-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gst-launch-1.0](/man/gst-launch-1.0)(1), [gst-discoverer-1.0](/man/gst-discoverer-1.0)(1), [gst-play-1.0](/man/gst-play-1.0)(1), [gst-typefind-1.0](/man/gst-typefind-1.0)(1)
