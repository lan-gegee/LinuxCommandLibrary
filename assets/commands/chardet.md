# TAGLINE

检测文本文件的字符编码

# TLDR

**检测文件编码**

```chardet [file.txt]```

**检测多个文件的编码**

```chardet [file1.txt] [file2.txt] [file3.txt]```

**从 stdin 读取**

```cat [file.txt] | chardet```

**以详细模式检测**

```chardetect [file.txt]```

# SYNOPSIS

**chardet** [_file_...]

**chardetect** [_file_...]

# DESCRIPTION

**chardet**（或 chardetect）是一款检测文本文件字符编码的命令行工具。它基于 chardet 库，该库是 Mozilla 字符编码自动检测算法的移植版。

该工具分析文件中的字节模式，判断最可能的编码（UTF-8、ISO-8859-1、Windows-1252 等）并给出置信度评分。这在处理未知编码的文件或准备数据处理时非常有用。

chardet 属于 Python chardet 软件包，常用于必须在转换前确定编码的文本处理流水线。

# PARAMETERS

**file**
> 要分析的一个或多个文件。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# CAVEATS

检测是启发式的，并非 100% 准确，对短文本或模糊编码尤其如此。ASCII 是许多编码的子集，这增加了检测难度。置信度评分反映检测结果的可靠性。二进制文件可能产生错误或低置信度的结果。

# HISTORY

**chardet** 是 **Mozilla Firefox** 所用字符编码检测算法的 Python 实现。原始算法由 **Netscape/Mozilla** 开发，用于应对 Web 上字符编码的多样性。Python 移植版由 **Mark Pilgrim** 于 **2006 年**创建，目前由 **Dan Blanchard** 和社区维护。

# INSTALL

```brew: brew install chardet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[file](/man/file)(1), [iconv](/man/iconv)(1), [enca](/man/enca)(1)
