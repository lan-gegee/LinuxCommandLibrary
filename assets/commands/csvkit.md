# TAGLINE

命令行 CSV 处理工具集

# TLDR

以可读的表格形式显示 CSV 文件

```csvlook [data.csv]```

获取 CSV 文件的统计信息

```csvstat [data.csv]```

选择指定列

```csvcut -c [col1,col2] [data.csv]```

按某列排序

```csvsort -c [column] [data.csv]```

用 SQL 查询 CSV

```csvsql --query "[SELECT * FROM data WHERE id > 100]" [data.csv]```

按模式过滤行

```csvgrep -c [column] -m "[value]" [data.csv]```

将 Excel 文件转换为 CSV

```in2csv [data.xlsx] > [data.csv]```

垂直堆叠多个 CSV 文件

```csvstack [file1.csv] [file2.csv]```

# SYNOPSIS

_tool_ [_options_] [_file_]

# INCLUDED TOOLS

**in2csv**
> 将各种格式（Excel、JSON、定宽）转换为 CSV。

**sql2csv**
> 在数据库上执行 SQL 查询并将结果输出为 CSV。

**csvlook**
> 以人类可读的表格形式显示 CSV。

**csvstat**
> 为 CSV 列生成统计信息。

**csvcut**
> 选择和重排列。

**csvgrep**
> 按列值过滤行。

**csvsort**
> 按列排序行。

**csvjoin**
> 基于公共列连接两个 CSV 文件。

**csvstack**
> 垂直拼接 CSV 文件。

**csvsql**
> 生成 SQL 语句或对数据库执行查询。

**csvjson**
> 将 CSV 转换为 JSON。

**csvpy**
> 将 CSV 加载到 Python shell 中进行交互式探索。

**csvclean**
> 校验并修复 CSV 格式问题。

**csvformat**
> 将 CSV 转换为其他分隔格式。

# DESCRIPTION

**csvkit** 是一套全面的命令行 CSV 处理工具。它遵循 Unix 哲学，无需数据库即可对表格数据执行类数据库操作。

这些工具正确处理 CSV 的引号与转义，避免了直接用 awk、sed 或 cut 处理 CSV 数据的种种陷阱。它们支持多种输入编码和分隔符，足以应对现实世界的数据处理任务。

csvkit 特别适合数据新闻、快速数据探索、ETL 流程，以及作为数据管道的一环。所有工具都可以从 stdin 读取并向 stdout 写出，便于串联使用。

# CAVEATS

某些操作会把整个文件载入内存。类型推断偶尔会误判数据。对于超大文件，性能可能不如专用工具。需要安装 Python。

# HISTORY

csvkit 由 Christopher Groskopf 创建，首次发布于 **2011** 年。它专为数据记者和分析师设计，提供强大的 CSV 命令行处理工具，已成为数据科学领域的标准工具集。

# INSTALL

```pacman: sudo pacman -S csvkit```

```brew: brew install csvkit```

```nix: nix profile install nixpkgs#csvkit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[miller](/man/miller)(1), [xsv](/man/xsv)(1), [jq](/man/jq)(1), [awk](/man/awk)(1), [cut](/man/cut)(1)
