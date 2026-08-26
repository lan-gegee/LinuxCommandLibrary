# TAGLINE

PHP 的 BDD 测试框架

# TLDR

**运行测试**

```kahlan```

**运行指定的 spec**

```kahlan --spec=[spec/MySpec.php]```

**按模式过滤**

```kahlan --pattern="[*Spec.php]"```

**生成覆盖率**

```kahlan --coverage=[4]```

**以指定报告器输出**

```kahlan --reporter=[dot|bar|verbose]```

**使用配置文件运行**

```kahlan --config=[kahlan-config.php]```

# SYNOPSIS

**kahlan** [_options_]

# PARAMETERS

**--spec** _PATH_
> 指定的 spec 文件/目录。

**--pattern** _GLOB_
> 文件匹配模式。

**--coverage** _LEVEL_
> 覆盖率级别（1-4）。

**--reporter** _NAME_
> 输出报告器。

**--config** _FILE_
> 配置文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Kahlan** 是 PHP 的 BDD 测试框架。它使用类似 Jasmine/RSpec 的 describe-it 语法。

该工具支持 mock、stub 和代码覆盖率。它专注于行为驱动开发。

# CAVEATS

基于 PHP。语法与 PHPUnit 不同。需要 Composer。

# HISTORY

Kahlan 作为一个 PHP 测试框架而创建，具有类似 JavaScript 的 BDD 语法和强大的 mock 能力。

# SEE ALSO

[phpunit](/man/phpunit)(1), [phpspec](/man/phpspec)(1), [pest](/man/pest)(1)
