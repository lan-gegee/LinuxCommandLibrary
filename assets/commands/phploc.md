# TAGLINE

测量 PHP 项目的大小与复杂度

# TLDR

**测量项目大小**

```phploc [src/]```

**以 CSV 格式输出**

```phploc --log-csv [stats.csv] [src/]```

**排除某个目录**

```phploc --exclude [vendor] [.]```

**统计测试代码**

```phploc --count-tests [src/]```

**分析特定文件后缀**

```phploc --suffix [php] --suffix [inc] [src/]```

**排除多个目录**

```phploc --exclude [vendor] --exclude [tests] [src/]```

# SYNOPSIS

**phploc** [_options_] _directories_...

# PARAMETERS

_DIRECTORIES_
> 要分析的一个或多个目录。

**--log-csv** _FILE_
> 将结果以 CSV 格式写入文件。

**--log-xml** _FILE_
> 将结果以 XML 格式写入文件。

**--exclude** _DIR_
> 从分析中排除指定目录。可多次指定。

**--suffix** _SUFFIX_
> 要包含的文件后缀（默认：php）。可多次指定。

**--count-tests**
> 在输出中包含与测试相关的指标。

**--names** _NAMES_
> 要包含的文件名列表，以逗号分隔。

**--names-exclude** _NAMES_
> 要排除的文件名列表，以逗号分隔。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**phploc** 用于测量 PHP 项目的大小与复杂度。它报告的指标包括代码行数（LOC）、注释行数、非注释行数，以及类、方法、函数、接口、trait、命名空间、常量的数量和圈复杂度。

该工具递归扫描目录中的 PHP 文件，并生成结构化指标的汇总报告。它是由 Sebastian Bergmann 创建的 PHP QA 工具链的一部分。

# CAVEATS

phploc 已被作者**归档**，不再积极维护。默认情况下它会递归分析目录。除非通过 `--suffix` 更改，否则只扫描 `.php` 后缀的文件。

# HISTORY

PHPLOC 由 **Sebastian Bergmann**（同样以 PHPUnit 闻名）创建，是 PHP 质量保证工具集的一部分。

# INSTALL

```aur: yay -S phploc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cloc](/man/cloc)(1), [phpmd](/man/phpmd)(1), [phpcs](/man/phpcs)(1), [sloccount](/man/sloccount)(1)
