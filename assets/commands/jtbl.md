# TAGLINE

将 JSON 转换为 ASCII 表格以便在终端显示

# TLDR

**将 JSON 显示为表格**

```cat [data.json] | jtbl```

**截断过长的值**

```cat [data.json] | jtbl -t```

**不显示表头**

```cat [data.json] | jtbl -n```

**Markdown 表格**

```cat [data.json] | jtbl -m```

**在指定列数处换行**长文本

```cat [data.json] | jtbl -w [80]```

**旋转输出**（每页一行记录，列变行）

```cat [data.json] | jtbl -r```

# SYNOPSIS

**jtbl** [_options_]

# PARAMETERS

**-t**, **--truncate**
> 截断过长的单元格内容以适应终端宽度。

**-n**, **--no-headers**
> 不打印列标题。

**-m**, **--markdown**
> 输出为 Markdown 表格。

**-c**, **--csv**
> 输出为 CSV。

**-H**, **--html**
> 输出为 HTML 表格。

**-r**, **--rotate**
> 旋转输出，让列变成行（对宽表格很有用）。

**-w** _COLS_, **--wrap**=_COLS_
> 在指定的列数处为过长单元格内容换行。

**-q**, **--quiet**
> 抑制警告消息。

**-v**, **--version**
> 显示版本号。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jtbl** 将 JSON 转换为 ASCII 表格以便在终端显示。它把 JSON 数组格式化为易读的表格形式。

该工具与 jc 搭配使用效果极佳，可用于展示命令输出。它还支持输出 Markdown 表格用于文档编写。

# CAVEATS

要求输入为对象数组。基于 Python 实现。可与 jc 的输出配合使用。

# HISTORY

jtbl 由 **Kelly Brazil** 开发，作为 jc 的配套工具，用于将 JSON 数据展示为格式化的表格。

# INSTALL

```brew: brew install jtbl```

```nix: nix profile install nixpkgs#jtbl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jc](/man/jc)(1), [jq](/man/jq)(1), [column](/man/column)(1)
