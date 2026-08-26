# TAGLINE

查找 PHP 项目中的重复代码

# TLDR

**查找重复代码**

```phpcpd [src/]```

**设置最小行数**

```phpcpd --min-lines [10] [src/]```

**设置最小标记数**

```phpcpd --min-tokens [50] [src/]```

**排除目录**

```phpcpd --exclude [vendor] [src/]```

**输出到文件**

```phpcpd --log-pmd [report.xml] [src/]```

**检查多个目录**

```phpcpd [src/] [lib/]```

**模糊匹配**

```phpcpd --fuzzy [src/]```

# SYNOPSIS

**phpcpd** [_--min-lines n_] [_--min-tokens n_] [_--exclude dir_] [_options_] _directories_

# PARAMETERS

**--min-lines** _N_
> 判定为重复的最小行数。

**--min-tokens** _N_
> 判定为重复的最小标记数。

**--exclude** _DIR_
> 排除目录。

**--log-pmd** _FILE_
> 输出 PMD-CPD XML 格式。

**--fuzzy**
> 模糊匹配。

**--suffix** _EXT_
> 要检查的文件后缀。

**-v**, **--verbose**
> 详细输出。

**--help**
> 显示帮助。

# DESCRIPTION

**phpcpd**（PHP Copy/Paste Detector）查找 PHP 项目中的重复代码。它识别出应当重构的代码。

基于标记的分析能发现相似的代码块。重命名变量也无法掩盖重复。

阈值控制检测灵敏度。更高的最小值只会发现更大、更显著的重复。

模糊匹配可以发现近似重复。存在细微差异的代码也会被检出。

报告显示文件位置和重复内容。与 CI 工具集成可实现自动化检查。

# CAVEATS

相似但有意不同的代码可能被误报。超大型代码库运行较慢。**注意：** phpcpd 已被作者归档，不再积极维护。新项目请考虑其他静态分析工具。

# HISTORY

**phpcpd** 由 **Sebastian Bergmann** 创建，是 PHP QA 工具集的一部分。它通过检测复制粘贴的代码块帮助维护代码质量。

# INSTALL

```dnf: sudo dnf install phpcpd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[phpcs](/man/phpcs)(1), [phpcbf](/man/phpcbf)(1), [phpmd](/man/phpmd)(1), [phpstan](/man/phpstan)(1)
