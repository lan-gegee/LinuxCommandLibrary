# TAGLINE

PHP CodeSniffer

# TLDR

**检查文件**

```phpcs [file.php]```

**检查目录**

```phpcs [src/]```

**使用特定标准**

```phpcs --standard=PSR12 [file.php]```

**只显示摘要**

```phpcs --report=summary [src/]```

**生成报告**

```phpcs --report-file=[report.txt] [src/]```

# SYNOPSIS

**phpcs** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 文件或目录。

**--standard** _NAME_
> 编码标准。

**--report** _TYPE_
> 报告格式。

**--report-file** _FILE_
> 将报告保存到文件。

**-n**
> 忽略警告。

**--help**
> 显示帮助。

# DESCRIPTION

**phpcs** 是 PHP CodeSniffer，用于检测编码规范违规。

该工具检查代码风格。支持 PSR、PEAR 和自定义标准。

# CAVEATS

通过 phpcs.xml 进行配置。可定义自定义标准。

# HISTORY

PHP_CodeSniffer 为**强制执行 PHP 编码标准**而创建。

# SEE ALSO

[phpcbf](/man/phpcbf)(1), [php-cs-fixer](/man/php-cs-fixer)(1), [phpmd](/man/phpmd)(1)
