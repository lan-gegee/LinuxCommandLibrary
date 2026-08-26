# TAGLINE

PHP 静态分析器

# TLDR

**分析 PHP 项目**

```phan```

**分析指定目录**

```phan --directory [src/]```

**生成基线**

```phan --save-baseline [.phan/baseline.php]```

**使用基线**

```phan --load-baseline [.phan/baseline.php]```

**设置输出格式**

```phan --output-mode [json]```

# SYNOPSIS

**phan** [_options_]

# PARAMETERS

**--directory** _DIR_
> 要分析的目录。

**--config-file** _FILE_
> 配置文件。

**--save-baseline** _FILE_
> 保存基线。

**--load-baseline** _FILE_
> 加载基线。

**--output-mode** _FORMAT_
> 输出格式。

**--help**
> 显示帮助。

# DESCRIPTION

**phan** 是一款 PHP 静态分析器，通过类型检查发现缺陷。

该工具执行深度分析，支持 PHP 7/8 特性。

# CAVEATS

需要带 AST 扩展的 PHP。建议进行配置。

# HISTORY

Phan 为**高级 PHP 静态分析**而创建，支持类型推断。

# INSTALL

```aur: yay -S phan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[phpstan](/man/phpstan)(1), [psalm](/man/psalm)(1), [php](/man/php)(1)
