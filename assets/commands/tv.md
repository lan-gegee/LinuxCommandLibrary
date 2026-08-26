# TAGLINE

终端表格数据查看器

# TLDR

**查看 CSV 文件**

```tv [data.csv]```

**查看 TSV 文件**

```tv -t [data.tsv]```

**使用自定义分隔符查看**

```tv -d ";" [data.txt]```

**只显示前 N 行**

```tv -n [10] [data.csv]```

**不显示表头行**

```tv --no-header [data.csv]```

**使用指定的配色方案**

```tv -c [1] [data.csv]```

**从其他命令管道传入数据**

```cat [data.csv] | tv```

# SYNOPSIS

**tv** [_-t_] [_-d delim_] [_--no-header_] [_options_] _file_

# PARAMETERS

**-t**
> 制表符分隔。

**-d** _DELIM_
> 自定义分隔符。

**--no-header**
> 无表头行。

**-n** _NUM_
> 要输出的行数。默认：25。

**-c** _N_
> 配色方案：1 (nord)、2 (one_dark)、3 (gruvbox)、4 (dracula)、5 (uncolor)。

**-u** _WIDTH_
> 列宽上限（最大值）。默认：20。

**-l** _WIDTH_
> 列宽下限（最小值）。必须为 2 或更大。默认：2。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**tv**（tidy-viewer）是一个终端表格数据查看器，可将 CSV、TSV 及其他分隔符文件显示为格式化、列对齐的表格。它从文件或标准输入读取数据，并以正确的对齐方式渲染数据，便于在终端中阅读。

对于非标准格式可以指定自定义分隔符，**--no-header** 选项用于处理没有表头行的文件。该工具支持将输出限制为指定行数（默认 25 行），以便预览大型数据集。缺失值（NA、NULL、空值）会被检测并高亮显示。

输出针对终端显示进行了优化，可配置列宽，内置 5 种配色方案。可以使用 dotfile（**~/.tv.toml**）进行持久化配置。

# CAVEATS

多个工具共用 "tv" 这个名称。此处指的是基于 Rust 的 tidy-viewer/tv 工具。大文件可能会被截断以适应终端尺寸。

# HISTORY

**tv**（tidy-viewer）是一个基于 Rust 的命令行工具，用于在终端中渲染表格数据。

# INSTALL

```apt: sudo apt install treeviewx```

```nix: nix profile install nixpkgs#tv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[column](/man/column)(1), [csvlook](/man/csvlook)(1), [miller](/man/miller)(1)
