# TAGLINE

将字体文件转换为 C 源代码数组

# TLDR

**将字体转换为** C 数组

```font2c [font.ttf] [output.c]```

**指定字符范围**

```font2c --range [32-126] [font.ttf] [output.c]```

**设置像素大小**

```font2c --size [16] [font.ttf] [output.c]```

**生成头文件**

```font2c --header [font.ttf] [output.h]```

# SYNOPSIS

**font2c** [_options_] _font-file_ _output-file_

# PARAMETERS

_FONT-FILE_
> 输入的字体文件（.ttf、.otf）。

_OUTPUT-FILE_
> 输出的 C 源文件。

**--range** _CHARS_
> 要包含的字符范围。

**--size** _PIXELS_
> 字体大小（以像素为单位）。

**--header**
> 生成头文件。

**--format** _FORMAT_
> 输出格式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**font2c** 将字体文件转换为面向嵌入式系统的 C 源代码数组。它按指定尺寸渲染字符，并将位图数据输出为 C 数组。

借助该工具，无需字体渲染库即可在显示屏上使用自定义字体。字符范围可以限制，以减少受限设备上的内存占用。

font2c 生成的数据适用于微控制器、OLED 显示屏以及其他嵌入式图形应用。

# CAVEATS

输出大小取决于字体和字符数量。抗锯齿并非在所有目标平台上都可用。位图字体失去了可伸缩性。

# HISTORY

font2c 类工具以多种形式存在于嵌入式开发中，用于将矢量字体转换为位图数组，从而在资源受限设备上无需运行时字体渲染即可使用。

# SEE ALSO

[fontforge](/man/fontforge)(1)
