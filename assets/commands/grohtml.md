# TAGLINE

Groff 的 HTML 输出驱动

# TLDR

**将 groff 转换为 HTML**

```groff -Thtml [file.roff] > output.html```

**直接使用 grohtml**

```grohtml [file] > output.html```

**生成带图像的输出**

```groff -Thtml -P-i [file.roff] > output.html```

# SYNOPSIS

**grohtml** [_options_] [_file_]

# PARAMETERS

_FILE_
> groff 中间输出。

**-b**
> 创建背景色。

**-i**
> 生成内联图像。

**-s** _SIZE_
> 字体基础大小。

**-F** _DIR_
> 字体目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grohtml** 是一个生成 HTML 的 groff 输出驱动。它将 groff 文档转换为可在网页上查看的格式，对于无法直接映射为 HTML 的元素可以选择生成图像。

该驱动负责处理文本格式并创建相应的 HTML 标签。复杂的格式元素可以渲染为内联图像以保证精确呈现。

# CAVEATS

属于 groff 软件包。复杂格式可能无法完美呈现。生成图像需要额外的工具。

# HISTORY

grohtml 作为 **GNU groff** 的一部分开发，用于实现 groff 文档的 Web 发布。

# SEE ALSO

[groff](/man/groff)(1), [grops](/man/grops)(1)
