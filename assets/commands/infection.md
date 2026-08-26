# TAGLINE

PHP 变异测试框架

# TLDR

**运行变异测试**

```infection```

**以指定线程数运行**

```infection --threads=[4]```

**只针对特定文件**

```infection --filter=[src/Service/]```

**设置最低得分**

```infection --min-msi=[70]```

**显示变异详情**

```infection --show-mutations```

**输出到文件**

```infection --log-verbosity=all --logger-text=[infection.log]```

# SYNOPSIS

**infection** [_options_]

# PARAMETERS

**--threads** _N_
> 并行执行的线程数。

**--filter** _PATH_
> 过滤要进行变异的源文件。

**--min-msi** _N_
> 最低变异分值指标（MSI）。

**--min-covered-msi** _N_
> 已覆盖代码的最低 MSI。

**--show-mutations**
> 显示变异详情。

**--mutators** _LIST_
> 要使用的特定变异算子。

**--help**
> 显示帮助信息。

# DESCRIPTION

**infection** 是一个 PHP 变异测试框架。它通过修改代码来检验你的测试套件的有效性。

该工具会创建突变体（被修改的代码）并对其运行测试。存活下来的突变体表明测试覆盖不足。

# CAVEATS

仅支持 PHP，需要 PHPUnit 或 Codeception。在大型代码库上资源消耗较大。

# HISTORY

infection 是受 Stryker 等其他语言同类工具启发而创建的 **PHP** 变异测试工具。

# SEE ALSO

[phpunit](/man/phpunit)(1), [phpspec](/man/phpspec)(1), [pest](/man/pest)(1)
