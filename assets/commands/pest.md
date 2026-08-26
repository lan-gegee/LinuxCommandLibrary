# TAGLINE

优雅的 PHP 测试框架

# TLDR

**运行所有测试**

```pest```

**运行特定测试**

```pest --filter [test_name]```

**带覆盖率运行**

```pest --coverage```

**并行运行**

```pest --parallel```

**首次失败即停止**

```pest --bail```

**监视文件变化**

```pest --watch```

**显示测试列表**

```pest --list-tests```

**运行特定文件**

```pest [tests/Feature/ExampleTest.php]```

# SYNOPSIS

**pest** [_--filter pattern_] [_--parallel_] [_--coverage_] [_options_] [_files_]

# PARAMETERS

**--filter** _PATTERN_
> 按名称过滤测试。

**--parallel**
> 并行运行。

**--coverage**
> 生成覆盖率报告。

**--bail**
> 首次失败即停止。

**--watch**
> 监视模式。

**--list-tests**
> 列出可用的测试。

**--min** _PERCENT_
> 最低覆盖率。

**--group** _NAME_
> 运行指定的测试组。

**--exclude-group** _NAME_
> 排除指定的测试组。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**pest** 是一个优雅的 PHP 测试框架。它在 PHPUnit 的基础上提供简洁而富有表现力的语法。

测试使用类似 JavaScript 测试框架的 describe/it 语法。期望（expectation）可以流畅地链式书写，得到易读的断言。

并行执行可以加速大型测试套件。进程会分布到各个可用核心上。

覆盖率报告显示代码覆盖百分比。支持 HTML 等多种格式。

监视模式会在文件变化时重新运行测试。失败的测试会优先重跑，以便更快获得反馈。

# CAVEATS

需要 PHP 8.1 或更高版本。构建于 PHPUnit 之上。某些 PHPUnit 特性的使用方式有所不同。

# HISTORY

**Pest** 由 **Nuno Maduro** 于 **2020 年**创建。它为 PHP 测试带来了现代、富有表现力的语法，同时保持与 PHPUnit 的完全兼容。

# INSTALL

```nix: nix profile install nixpkgs#pest```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[phpunit](/man/phpunit)(1), [php](/man/php)(1), [composer](/man/composer)(1)
