# TAGLINE

将覆盖率数据上传到 Coveralls

# TLDR

**将覆盖率上传到 Coveralls**

```php-coveralls```

**指定覆盖率文件**

```php-coveralls -v --coverage_clover=[coverage.xml]```

**试运行**

```php-coveralls --dry-run```

**使用配置文件**

```php-coveralls -c [.coveralls.yml]```

# SYNOPSIS

**php-coveralls** [_options_]

# PARAMETERS

**--coverage_clover** _FILE_
> clover.xml 覆盖率文件的路径。

**--coverage-php** _FILE_
> PHP 代码覆盖率报告文件的路径。

**-c**, **--config** _FILE_
> 配置文件的路径。

**-o**, **--json_path** _FILE_
> 待上传 JSON 输出的路径（默认：build/logs/coveralls-upload.json）。

**-r**, **--root_dir** _DIR_
> 项目根目录。

**--dry-run**
> 测试而不实际上传。

**-v**
> 详细输出。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**php-coveralls** 将覆盖率数据上传到 Coveralls，用于报告 PHP 代码覆盖率。

该工具可与 CI 系统集成，持续跟踪测试覆盖率的变化。

# CAVEATS

需要 Coveralls 账号。需要相应的 CI 环境变量。

# HISTORY

php-coveralls 为向 Coveralls 报告 **PHP 代码覆盖率**而创建。

# SEE ALSO

[phpunit](/man/phpunit)(1), [codecov](/man/codecov)(1)
