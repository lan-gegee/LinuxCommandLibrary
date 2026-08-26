# TAGLINE

用于操作字体文件的 Python 工具集

# TLDR

显示 **fonttools** 的顶层帮助和子命令

```fonttools --help```

将 TTF 子集化为 **Basic Latin** Unicode 范围

```fonttools subset [path/to/font.ttf] --unicodes=U+0000-007F```

# SYNOPSIS

**fonttools** [_subcommand_] [_options_] [_file_]

# PARAMETERS

**subset**
> 将字体文件子集化，只包含特定字形或 Unicode 范围

**ttx**
> 在字体二进制与 XML 格式之间转换

**merge**
> 将多个字体文件合并为一个

**help**
> 显示 fonttools 或某个子命令的帮助

**--unicodes=**_RANGE_
> 指定要包含的 Unicode 范围（如 U+0000-007F）

**--output-file=**_FILE_
> 指定输出文件路径

**--help**
> 显示帮助信息

# DESCRIPTION

**fonttools** 是一个用于操作字体文件的 Python 库与命令行工具集。它提供转换、子集化、合并和检查 TrueType（TTF）、OpenType（OTF）及其他字体格式的工具。

最常见的用例包括：为 Web 优化而将字体子集化（只包含所需字形以减小文件体积）、在二进制与 XML 表示之间转换以便检查或编辑，以及合并字族。

需要 Python 3.10 或更高版本。可通过 pip 安装：**pip install fonttools**。

# CAVEATS

部分功能需要可选依赖，例如 WOFF2 压缩所需的 **brotli**，或优化 WOFF 压缩所需的 **zopfli**。复杂的字体操作可能需要对字体表结构有深入理解。

# HISTORY

fonttools 起源于 1990 年代末，由 Just van Rossum 创建。它是最早一批用 Python 以编程方式操作字体的工具之一。该项目已大幅演进，目前由开源社区在 GitHub 上维护，已成为字体开发生态中的基础工具。

# INSTALL

```dnf: sudo dnf install fonttools```

```apk: sudo apk add py3-fonttools```

```brew: brew install fonttools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fc-cache](/man/fc-cache)(1), [fc-list](/man/fc-list)(1)
