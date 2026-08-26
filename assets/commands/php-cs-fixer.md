# TAGLINE

自动修复 PHP 编码规范问题

# TLDR

**修复当前目录**

```php-cs-fixer fix```

**修复指定文件**

```php-cs-fixer fix [file.php]```

**试运行**并显示将要进行的修改

```php-cs-fixer fix --dry-run```

**显示修改的 diff**

```php-cs-fixer fix --diff```

**使用指定的规则集**

```php-cs-fixer fix --rules=@PSR12```

**以详细输出修复**

```php-cs-fixer fix -v```

**列出需要修复的文件**

```php-cs-fixer list-files```

# SYNOPSIS

**php-cs-fixer** _command_ [_options_] [_path_]

# PARAMETERS

**fix** [_PATH_]
> 修复给定路径或当前目录中的编码规范问题。

**check** [_PATH_]
> `fix --dry-run` 的简写。只分析而不修改文件。

**--dry-run**
> 不修改文件，只显示将要进行的更改。

**--diff**
> 显示所应用更改的 diff。

**--rules** _RULES_
> 编码规范规则或规则集（如 @PSR12、@Symfony）。

**--config** _FILE_
> 配置文件的路径。

**--allow-risky** _yes|no_
> 允许可能改变代码行为的高风险规则。

**--using-cache** _yes|no_
> 启用或禁用缓存（默认：yes）。

**--cache-file** _FILE_
> 缓存文件路径（默认：.php-cs-fixer.cache）。

**--format** _FORMAT_
> 输出格式（txt、json、checkstyle、gitlab、junit、xml）。

**--stop-on-violation**
> 在第一个违规处停止执行。

**--path-mode** _override|intersection_
> 如何处理配置文件中的路径与命令行参数的关系（默认：override）。

# DESCRIPTION

**PHP CS Fixer** 自动修复 PHP 代码使其遵循编码规范。它支持 PSR-1、PSR-2、PSR-12、Symfony 以及自定义规则集。该工具解析 PHP 文件，应用配置的修复器，并以更正后的格式重写文件。

# CONFIGURATION

**.php-cs-fixer.php** 或 **.php-cs-fixer.dist.php**
> 定义规则、查找器和项目专属设置的 PHP 配置文件。默认在当前目录中查找。

# CAVEATS

高风险修复器可能改变代码行为，必须显式允许。相比命令行规则，通过 PHP 文件进行配置更加灵活。

# INSTALL

```dnf: sudo dnf install php-cs-fixer```

```zypper: sudo zypper install php-cs-fixer```

```brew: brew install php-cs-fixer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[phpcs](/man/phpcs)(1), [phpcbf](/man/phpcbf)(1), [php](/man/php)(1)
