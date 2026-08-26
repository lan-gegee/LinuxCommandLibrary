# TAGLINE

将文本格式化为对齐的列

# TLDR

按**指定宽度**格式化输出

```printf "header1 header2\nbar foo\n" | column -c 30```

**自动对齐**表格格式的列

```printf "header1 header2\nbar foo\n" | column -t```

在表格模式下指定列**分隔符**

```printf "header1,header2\nbar,foo\n" | column -t -s ,```

**先填满行再换列**

```printf "header1\nbar\nfoobar\n" | column -c 30 -x```

# SYNOPSIS

**column** [_options_] [_file_...]

# DESCRIPTION

**column** 将来自标准输入或文件的文本格式化为多列。默认情况下，以空白字符为分隔符，先填满一行再填下一行。

表格模式（-t）特别适合将结构化数据对齐成易读的表格。

# PARAMETERS

**-c, --output-width** _width_
> 输出宽度（字符数）

**-t, --table**
> 创建列对齐的表格

**-s, --separator** _chars_
> 表格模式的列分隔符（默认：空白字符）

**-x, --fillrows**
> 先填满行再填充列

**-o, --output-separator** _string_
> 表格输出的列分隔符

# CAVEATS

属于 util-linux 的一部分。表格模式要求分隔符使用一致。过长的行可能导致格式错乱。

# INSTALL

```apt: sudo apt install bsdextrautils```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[colrm](/man/colrm)(1), [cut](/man/cut)(1), [paste](/man/paste)(1)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

```[Documentation](https://man7.org/linux/man-pages/man1/column.1.html)```

<!-- verified: 2026-06-22 -->
