# TAGLINE

快速统计代码行数

# TLDR

**统计当前目录的代码行数**

```loc```

**统计指定目录的代码行数**

```loc [path/to/directory]```

**显示逐文件统计信息**

```loc --files```

**排除匹配正则表达式的文件**

```loc --exclude [test]```

**只统计匹配正则表达式的文件**

```loc --include [\.rs$]```

**按指定列排序输出**

```loc --sort [code]```

**包含被 .gitignore 忽略的文件**

```loc -u```

**同时包含隐藏文件和目录**

```loc -uu```

# SYNOPSIS

**loc** [_options_] [_paths_]

# PARAMETERS

_PATHS_
> 要分析的目录或文件。默认为当前目录。

**--files**
> 显示每个被解析文件的单独统计。

**--sort** _COLUMN_
> 按指定列排序结果（如 code、comment、lines、blank）。默认按 code 降序排列。

**--include** _REGEX_
> 只统计匹配指定正则表达式的文件。

**--exclude** _REGEX_
> 排除匹配指定正则表达式的文件。

**-u**
> 无限制模式。忽略 .gitignore 和 .ignore 文件。使用两次（-uu）还会包含隐藏文件和目录。

# DESCRIPTION

**loc** 快速统计代码行数。它能识别编程语言并区分代码、注释和空行。默认情况下，它遵循 .gitignore 和 .ignore 文件，并跳过隐藏文件和目录。

该工具采用 Rust 编写以保证速度，处理大型代码库时明显快于 cloc 等同类工具。

# CAVEATS

由于语言检测启发式规则和注释解析规则的差异，结果可能与其他行数统计工具不同。该项目已不再积极维护。

# INSTALL

```brew: brew install loc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cloc](/man/cloc)(1), [tokei](/man/tokei)(1), [sloccount](/man/sloccount)(1)
