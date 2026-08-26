# TAGLINE

将图片转换为 ASCII 艺术

# TLDR

从**文件**读取图片并以 ASCII 打印

```asciiart [path/to/image.jpg]```

从 **URL** 读取图片并以 ASCII 打印

```asciiart [www.example.com/image.jpg]```

选择输出**宽度**

```asciiart -w [50] [path/to/image.jpg]```

为 ASCII 输出**着色**

```asciiart -c [path/to/image.jpg]```

选择输出**格式**

```asciiart -f [text|html] [path/to/image.jpg]```

**反转**字符映射

```asciiart -i [path/to/image.jpg]```

# SYNOPSIS

**asciiart** [_options_] _image_

# DESCRIPTION

**asciiart** 将图片转换为 ASCII 艺术，用文本字符渲染图像。它分析图像中每个区域的亮度，并将其映射为合适的 ASCII 字符。

该工具支持从本地文件或 URL 读取图片，并可输出纯文本或 HTML。彩色输出使用 ANSI 转义码在终端中显示。

# PARAMETERS

**-w, --width** _n_
> 以字符数设置输出宽度（默认：100）

**-c, --color**
> 使用 ANSI 码启用彩色输出

**-f, --format** _type_
> 输出格式：**text**（默认）或 **html**

**-i, --invert-chars**
> 反转字符映射（明暗互换）

**-v, --version**
> 显示版本号

**-h, --help**
> 显示帮助信息

# CAVEATS

输出质量取决于终端字体和字符宽度。等宽字体效果最佳。HTML 输出可在浏览器中查看，颜色支持更好。非常宽的图片在终端中可能会折行。

# HISTORY

**asciiart** 是 Stephen Schor（nodanaonlyzuul）编写的 Ruby gem。它已打包进 Debian 和 Ubuntu，也可通过 **gem install asciiart** 安装。

# SEE ALSO

[jp2a](/man/jp2a)(1), [img2txt](/man/img2txt)(1), [figlet](/man/figlet)(1)

# RESOURCES

```[Source code](https://github.com/nodanaonlyzuul/asciiart)```

```[Documentation](https://github.com/nodanaonlyzuul/asciiart/blob/main/README.md)```

<!-- verified: 2026-06-16 -->
