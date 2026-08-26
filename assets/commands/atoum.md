# TAGLINE

现代 PHP 单元测试框架

# TLDR

**运行**测试

```atoum -f [tests/units/MyTest.php]```

运行目录中的**所有测试**

```atoum -d [tests/units]```

以**代码覆盖率**模式运行

```atoum -d [tests/] -c```

生成 **HTML** 覆盖率报告

```atoum -d [tests/] --coverage-html [coverage/]```

以**调试**模式运行测试

```atoum -d [tests/] --debug```

# SYNOPSIS

**atoum** [_-f file_] [_-d directory_] [_-c_] [_options_]

# DESCRIPTION

**atoum** 是一款强调简洁清晰的现代 PHP 单元测试框架。它提供直观的 API，只需极少的样板代码即可编写测试，具备 mock、代码覆盖率和并行执行等特性。

该框架采用自然流畅的断言语法，并包含用于测试隔离和依赖注入的工具。

# PARAMETERS

**-f** _file_
> 运行指定的测试文件

**-d** _directory_
> 运行目录中的所有测试

**-c**, **--coverage**
> 生成代码覆盖率

**--coverage-html** _dir_
> HTML 覆盖率报告

**--coverage-xml** _file_
> XML 覆盖率报告

**--debug**
> 调试模式

**-l**, **--loop**
> 以持续模式运行测试

**-p** _n_, **--max-children-number** _n_
> 并行执行测试

**--fail-if-void-methods**
> 若测试方法为空则判定失败

# CONFIGURATION

**.atoum.php**
> 项目级配置文件，用于测试运行器、报告和覆盖率设置。

# CAVEATS

需要 PHP 5.6 及以上版本。普及程度不及 PHPUnit。部分 IDE 集成可能受限。文档主要以法语撰写。

# HISTORY

**atoum** 由 Frédéric Hardy 创建，于 **2011** 年首次发布，作为 PHPUnit 的现代化替代品，注重开发者体验和测试的可读性。

# SEE ALSO

[phpunit](/man/phpunit)(1), [phpspec](/man/phpspec)(1), [behat](/man/behat)(1)

# RESOURCES

```[Homepage](https://atoum.org/)```

```[Source code](https://github.com/atoum/atoum)```

```[Documentation](https://docs.atoum.org/)```

<!-- verified: 2026-06-17 -->
