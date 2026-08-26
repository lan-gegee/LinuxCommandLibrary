# TAGLINE

专为表格和 PostgreSQL 输出设计的 Unix 分页器

# TLDR

**作为 psql 的分页器**

```export PAGER=pspg```

**查看 CSV 文件**

```pspg --csv < [file.csv]```

**查看 TSV 文件**

```pspg --tsv < [file.tsv]```

**直接打开文件**

```pspg -f [file.txt]```

**设置配色样式**

```pspg -s [5] < [file.csv]```

**滚动时冻结前 N 列**

```pspg --csv -c [2] < [file.csv]```

**内容不足一屏时退出**

```pspg -F < [file.txt]```

**与 psql 配合使用流式模式**

```psql -c "SELECT * FROM table" | pspg --stream```

# SYNOPSIS

**pspg** [_options_] [**-f** _file_]

# PARAMETERS

**-f**, **--file** _FILE_
> 打开指定文件。

**-F**, **--quit-if-one-screen**
> 内容不足一屏时退出。

**--csv**
> 按 CSV 格式读取输入。

**--csv-separator** _CHAR_
> 指定 CSV 字段分隔符。

**--csv-header** _on|off_
> 控制 CSV 输入是否使用标题行。

**--tsv**
> 按 TSV 格式读取输入。

**--stream**
> 以流式模式连续读取输入。

**--querystream**
> 从管道或文件读取查询流。

**-c**, **--freezecols** _N_
> 冻结前 N 列（0-9）。

**-s**, **--style** _N_
> 设置配色样式（0-22）。

**-b**, **--blackwhite**
> 使用黑白配色。

**-a**, **--ascii**
> 强制使用 ASCII 字符绘制边框。

**-i**, **--ignore-case**
> 搜索模式不含大写字母时忽略大小写。

**-I**, **--IGNORE-CASE**
> 所有搜索均忽略大小写。

**-g**, **--hlite-search**
> 不高亮搜索结果。

**-G**, **--HILITE-SEARCH**
> 不高亮匹配的行。

**--line-numbers**
> 显示行号列。

**--no-mouse**
> 禁用自定义鼠标处理。

**--no-bars**
> 隐藏顶部和底部状态条。

**--no-cursor**
> 隐藏行光标。

**--no-scrollbar**
> 隐藏滚动条。

**--no-sound**
> 滚动到边界时禁止蜂鸣。

**--vertical-cursor**
> 显示纵向列光标。

**--bold-labels**
> 行标签和列标签加粗显示。

**--force-uniborder**
> 用 Unicode 边框替换 ASCII 边框。

**--only-for-tables**
> 内容不是表格时改用标准分页器。

**--on-sigint-exit**
> 收到 Ctrl+C 或 Escape 时退出。

**-X**, **--reprint-on-exit**
> 退出后在终端中保留内容。

**--ni**
> 非交互模式（仅限 CSV 和查询）。

**-q**, **--query** _QUERY_
> 执行指定查询。

**-w**, **--watch** _N_
> 每 N 秒重复执行查询或读取文件。

**-d**, **--dbname** _NAME_
> 为直接查询指定数据库名称。

**-h**, **--host** _HOST_
> 数据库服务器主机。

**-p**, **--port** _PORT_
> 数据库服务器端口。

**-U**, **--username** _USER_
> 数据库用户名。

**-V**, **--version**
> 显示版本信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**pspg** 是一款功能丰富的 Unix 分页器，专为处理表格而设计。它最初为 PostgreSQL 的 psql 而创建，同时也支持 MySQL，并可作为通用的 CSV/TSV 查看器。它支持冻结列标题、搜索、按行/列/块选择、导出到剪贴板以及鼠标操作。

主要特性包括：用 **-c** 冻结列、用 **-s** 选择多种配色样式、纵横双向滚动，以及用 **-q** 直接查询数据库。在流式模式（**--stream**）下，它可以显示持续更新的输出，例如 psql 的 **\watch** 结果。

# HISTORY

**pspg** 由 **Pavel Stehule**（okbob）创建，使用 **C** 编写。

# INSTALL

```apt: sudo apt install pspg```

```dnf: sudo dnf install pspg```

```apk: sudo apk add pspg```

```zypper: sudo zypper install pspg```

```brew: brew install pspg```

```nix: nix profile install nixpkgs#pspg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[less](/man/less)(1), [psql](/man/psql)(1), [mysql](/man/mysql)(1), [ov](/man/ov)(1)
