# TAGLINE

快速的 CSV 处理工具

# TLDR

从 CSV 中**提取指定列**

```csvtool col [1,3,5] [data.csv]```

按范围**提取行**

```csvtool head [10] [data.csv]```

**转置 CSV**（行列互换）

```csvtool transpose [data.csv]```

拼接多个文件的**列**

```csvtool paste [file1.csv] [file2.csv]```

替换某列中的**值**

```csvtool replace [column] [old] [new] [data.csv]```

自定义分隔符的输入

```csvtool -t "[;]" col [1,2] [data.csv]```

# SYNOPSIS

**csvtool** [_options_] _command_ [_arguments_] _file_

# PARAMETERS

**col** _COLUMNS_
> 提取指定的列（从 1 开始编号，逗号分隔）。

**head** _N_
> 输出前 N 行。

**drop** _N_
> 丢弃前 N 行。

**transpose**
> 行列转置。

**paste**
> 将文件并排粘贴。

**replace** _COL_ _OLD_ _NEW_
> 替换某列中的值。

**join** _COL_
> 按某一列连接文件。

**call** _COMMAND_
> 对每一行运行命令。

**-t** _CHAR_
> 输入分隔符（默认：逗号）。

**-u** _CHAR_
> 输出分隔符。

**-o** _FILE_
> 输出文件。

# DESCRIPTION

**csvtool** 是一个用 OCaml 编写的快速 CSV 处理工具。它提供了多种操作，用于在命令行对 CSV 数据进行转换、过滤和分析。

该工具专为速度而设计，能高效处理大文件。它支持列提取、行过滤、转置、文件连接等常见操作。**call** 子命令可对每一行运行外部命令。

csvtool 在可能的情况下采用流式处理，因此许多操作都能处理超出可用内存的大文件。它能正确处理 CSV 的引号与转义。

# CAVEATS

列号从 1 开始计数，而不是 0。某些操作需要将整个文件载入内存。引号规则可能与其他 CSV 工具不同。错误信息可能晦涩难懂。

# HISTORY

csvtool 随 **ocaml-csv** 库一同发布，该库是一个 OCaml 的 CSV 解析器，最初由 Richard Jones 编写，现由 Christophe Troestler 维护。这个命令行工具将该库的解析能力开放出来，方便在 Shell 中快速完成 CSV 转换。

# INSTALL

```apt: sudo apt install csvtool```

```nix: nix profile install nixpkgs#csvtool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[csvkit](/man/csvkit)(1), [cut](/man/cut)(1), [awk](/man/awk)(1), [miller](/man/miller)(1)

# RESOURCES

```[Source code](https://github.com/Chris00/ocaml-csv)```

<!-- verified: 2026-06-26 -->
