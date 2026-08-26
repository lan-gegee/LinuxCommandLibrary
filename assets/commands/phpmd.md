# TAGLINE

PHP Mess Detector（PHP 代码问题检测器）

# TLDR

**检查代码问题**

```phpmd [src/] text [cleancode,codesize]```

**生成 HTML 报告**

```phpmd [src/] html [rulesets] --reportfile [report.html]```

**使用规则集文件**

```phpmd [src/] text [phpmd.xml]```

**排除目录**

```phpmd [src/] text [rulesets] --exclude [vendor]```

# SYNOPSIS

**phpmd** _source_ _format_ _rulesets_ [_options_]

# PARAMETERS

_SOURCE_
> 源文件或目录。

_FORMAT_
> 输出格式（text、xml、html）。

_RULESETS_
> 要应用的规则。

**--reportfile** _FILE_
> 输出文件。

**--exclude** _PATTERN_
> 排除模式。

**--help**
> 显示帮助。

# DESCRIPTION

**phpmd** 即 PHP Mess Detector。用于查找代码中的潜在问题。

该工具检测代码异味、复杂度和设计问题。

# CAVEATS

规则可配置。可能产生误报。

# HISTORY

PHPMD 的创建目的是**检测 PHP 代码问题**和可维护性问题。

# INSTALL

```brew: brew install phpmd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[phpcs](/man/phpcs)(1), [phan](/man/phan)(1), [phpstan](/man/phpstan)(1)
