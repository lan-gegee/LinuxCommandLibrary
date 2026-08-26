# TAGLINE

跨平台的表格数据美化打印工具

# TLDR

**美化打印 CSV 文件**

```tidy-viewer [path/to/file.csv]```

**美化打印从 stdin 管道输入的数据**

```cat [path/to/file.csv] | tidy-viewer```

**使用自定义分隔符**

```tidy-viewer -s "|" [path/to/file.psv]```

通过分隔符处理**制表符分隔的输入**

```tidy-viewer -s $'\t' [path/to/file.tsv]```

**以指定调色板显示**

```tidy-viewer -c [3] [path/to/file.csv]```

**打印全部行并着色，再分页查看输出**

```tidy-viewer -af [path/to/file.csv] | less -RS```

# SYNOPSIS

**tidy-viewer** [_options_] [_file_]

# PARAMETERS

**-s**, **--delimiter** _DELIM_
> 字段分隔符。默认：逗号。TSV 用制表符。

**-c**, **--color** _N_
> 调色板：1（nord）、2（one_dark）、3（gruvbox）、4（dracula）、5（solarized light）。

**-n**, **--number-of-rows-to-output** _ROWS_
> 要显示的行数。默认：25。

**-t**, **--title** _TITLE_
> 可选的表格标题。

**-a**, **--color-always**
> 即使不是 TTY 也强制彩色输出。

**-f**, **--force-all-rows**
> 打印所有行，而不采用默认的预览行数限制。

**-e**, **--extend-width-and-length**
> 让输出超出终端宽度/长度，以便配合 **less** 分页。

**-g**, **--sigfig** _N_
> 数字的有效数字位数（默认 3，最大 7）。

**-C**, **--config-details**
> 显示当前生效的配置。

**-h**, **--help**
> 显示帮助和示例配置。

# DESCRIPTION

**tidy-viewer** 是一款跨平台 CLI 工具，用于在终端中美化打印表格数据。它可以从路径或 stdin 读取 CSV、TSV、PSV、Parquet、Arrow IPC 和 Feather 文件，然后渲染出列对齐的表格，带有配色样式、有效数字格式化以及对缺失值的 NA 高亮。

该工具先打印行列维度信息，将过长的字符串截断以保持对齐，并跳过超出终端宽度的列（多余的列会在页脚中列出）。大文件会自动流式处理以节省内存。输出针对可读性优化，而非逐字还原原始内容。

通常被别名为 **tv**；实际安装的二进制文件名是 **tidy-viewer**。

# CONFIGURATION

配置保存在一个 TOML 点文件中。位置因操作系统而异：

> Linux：**$XDG_CONFIG_HOME/tv.toml** 或 **~/.config/tv.toml**
> macOS：**~/Library/Application Support/tv.toml**
> Windows：**%AppData%\tv.toml**

每个键都必须存在，否则整个文件会被忽略。运行 **tidy-viewer --help** 可查看完整的示例模板。使用 **tidy-viewer --config-details** 可检查当前生效的设置。

# CAVEATS

多个互不相关的工具共用短名称 **tv**。本条目描述的是 Rust 版 **tidy-viewer** 二进制程序。不完整的配置文件会被静默忽略。

# INSTALL

```brew: brew install tidy-viewer```

```nix: nix profile install nixpkgs#tidy-viewer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tv](/man/tv)(1), [column](/man/column)(1), [csvlook](/man/csvlook)(1), [miller](/man/miller)(1)

# RESOURCES

```[Source code](https://github.com/alexhallam/tv)```

```[Documentation](https://docs.rs/tidy-viewer-core)```

<!-- verified: 2026-07-11 -->
