# TAGLINE

PHP Code Beautifier and Fixer

# TLDR

**修复文件中的编码规范违规**

```phpcbf [path/to/file.php]```

**修复目录中的所有文件**

```phpcbf [path/to/src/]```

**按指定编码标准修复**

```phpcbf --standard=[PSR12] [path/to/file.php]```

**只修复特定的 sniffs**

```phpcbf --sniffs=[Sniff.Name] [path/to/file.php]```

**以加后缀的方式写出修复后的文件**而不是覆盖

```phpcbf --suffix=[.fixed] [path/to/file.php]```

**只处理特定的文件扩展名**

```phpcbf --extensions=[php,inc] [path/to/src/]```

# SYNOPSIS

**phpcbf** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要修复的文件或目录。

**--standard=**_NAME_
> 要使用的编码标准（如 PSR1、PSR2、PSR12、Squiz、PEAR）。

**--sniffs=**_LIST_
> 要应用的特定 sniffs 的逗号分隔列表。

**--exclude=**_LIST_
> 要排除的 sniffs 的逗号分隔列表。

**--extensions=**_LIST_
> 要修复的文件扩展名的逗号分隔列表（默认：php,inc）。可包含 type: module/php,es/js 形式。

**--suffix=**_SUFFIX_
> 用此后缀写出修复后的文件，而不是覆盖原文件。

**--no-patch**
> 使用 PHP 而不是 diff/patch 命令进行文件替换。

**--diff**
> 生成更改的 diff 而不实际应用。

**-p**
> 修复过程中显示进度。

**--help**
> 显示帮助信息。

# DESCRIPTION

**phpcbf**（PHP Code Beautifier and Fixer）自动纠正 phpcs 检测出的编码规范违规。它是 **PHP_CodeSniffer** 软件包中配套的修复工具。

该工具默认就地修改文件，为定义了自动修复器的违规应用修复。并非所有 phpcs 违规都能自动修复；phpcbf 只会修复具有相应修复器实现的违规项。使用 **--suffix** 可写出修复后的副本而不覆盖原文件，或使用 **--diff** 生成补丁而不修改文件。

# CAVEATS

属于 PHP_CodeSniffer。并非所有编码规范违规都能自动修复。修复后务必复查更改，尤其是在代码库上首次使用时。

# HISTORY

PHPCBF 是 **PHP_CodeSniffer** 的一部分，最初由 **Greg Sherwood**（Squiz Labs）开发，现由 **PHPCSStandards** 维护。

# SEE ALSO

[phpcs](/man/phpcs)(1), [php-cs-fixer](/man/php-cs-fixer)(1)
