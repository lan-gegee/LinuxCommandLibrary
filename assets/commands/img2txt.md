# TAGLINE

将图像转换为彩色文本画

# TLDR

以指定的输出**宽度**（列数）转换图像

```img2txt -W [10] [path/to/image]```

以指定的输出**高度**（行数）转换图像

```img2txt -H [5] [path/to/image]```

设置输出**字体宽度**

```img2txt -x [12] [path/to/image]```

设置输出**字体高度**

```img2txt -y [14] [path/to/image]```

将图像转换为 **HTML** 格式

```img2txt -f html [path/to/image] > [output.html]```

# SYNOPSIS

**img2txt** [_options_] _image_

# PARAMETERS

**-W**, **--width** _COLS_
> 以列数设置输出宽度

**-H**, **--height** _LINES_
> 以行数设置输出高度

**-x**, **--font-width** _PIXELS_
> 设置用于计算宽高比的假定字体宽度（默认 6）

**-y**, **--font-height** _PIXELS_
> 设置用于计算宽高比的假定字体高度（默认 10）

**-b**, **--brightness** _VALUE_
> 调整亮度（默认 1.0）

**-c**, **--contrast** _VALUE_
> 调整对比度（默认 1.0）

**-g**, **--gamma** _VALUE_
> 调整伽马值（默认 1.0）

**-d**, **--dither** _ALGORITHM_
> 抖动算法（none、ordered2、ordered4、ordered8、random、fstein）

**-f**, **--format** _FORMAT_
> 输出格式：ansi、utf8、html、html3、irc、bbfr、ps、svg、tga、caca（默认 ansi）。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**img2txt** 使用字符图案和终端颜色将图像转换为彩色文本画。它是 **libcaca** 库的一部分，支持 PNG、JPEG、GIF、BMP 等常见图像格式。默认输出宽度为 60 列，高度按保持宽高比计算。

该工具可以生成多种格式的输出，包括 ANSI 终端转义码、HTML、IRC 颜色码以及纯文本。生成的 ASCII 艺术可以在终端中显示，也可以嵌入文档中。

# CAVEATS

输出质量取决于终端能力和字体特性。宽字符或非等宽字体会使输出变形。颜色支持因终端模拟器而异。

# HISTORY

img2txt 是 libcaca 的一部分，这是一个由 Sam Hocevar 创建的面向文本终端的图形库。该库于 **2003 年**首次发布，已被多个项目使用，包括 VLC 媒体播放器的 ASCII 视频渲染。

# INSTALL

```apt: sudo apt install caca-utils```

```dnf: sudo dnf install caca-utils```

```apk: sudo apk add libcaca-apps```

```zypper: sudo zypper install caca-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cacaview](/man/cacaview)(1), [jp2a](/man/jp2a)(1)
