# TAGLINE

对 PHP 代码执行静态分析，无需运行代码即可发现 bug

# TLDR

**分析源码目录**

```phpstan analyse [src/]```

**以指定级别分析**

```phpstan analyse --level [5] [src/]```

**使用配置文件分析**

```phpstan analyse -c [phpstan.neon]```

**以最高级别分析**

```phpstan analyse --level max [src/]```

**生成基线文件**

```phpstan analyse --generate-baseline```

**清除缓存**

```phpstan clear-result-cache```

**显示版本**

```phpstan --version```

# SYNOPSIS

**phpstan** [_analyse_] [_--level n_] [_-c config_] [_options_] [_paths_]

# PARAMETERS

**analyse**, **analyze**
> 运行分析。

**--level**, **-l** _N_
> 规则级别（0-9 或 max）。

**-c** _FILE_
> 配置文件。

**--configuration** _FILE_
> 配置文件（长格式）。

**--memory-limit** _SIZE_
> 内存限制。

**--debug**
> 调试模式。

**--generate-baseline**
> 生成错误基线文件。

**-b** _FILE_
> 基线文件。

**--error-format** _FMT_
> 输出格式（table、json、raw 等）。

**--no-progress**
> 禁用进度条。

**clear-result-cache**
> 清除分析缓存。

# DESCRIPTION

**phpstan** 对 PHP 代码执行静态分析，无需运行代码即可发现 bug。它能捕获类型错误、未定义的方法调用以及不正确的函数调用。

分析级别从 0（基础）到 9（最严格）。级别越高，检查的条件越多，但在遗留代码中可能产生更多误报。建议从低级别开始，逐步提高。

配置文件（phpstan.neon）定义要分析的路径、排除项和自定义规则。它们让团队成员和 CI 流水线之间的分析保持一致。

基线文件会忽略已存在的错误，从而支持渐进式采用。新代码必须通过分析，而遗留问题可以随时间逐步修复。

该工具通过插件与 IDE 集成，在输入时实时显示错误。CI 集成可在合并前捕获回归问题。

PHPStan 支持 PHPDoc 注解为旧代码提供类型提示。现代 PHP 类型声明在可行时更受推荐。

# CAVEATS

高级别对遗留代码可能不切实际。某些动态 PHP 模式无法分析。框架需要相应扩展支持。内存占用随代码库规模增长。

# HISTORY

**PHPStan** 由 **Ondřej Mirtes** 于 **2016 年**创建，旨在将静态类型的优势带给 PHP。它已成为最流行的 PHP 静态分析工具之一，与 Psalm 和 Phan 相互竞争。

# INSTALL

```brew: brew install phpstan```

```nix: nix profile install nixpkgs#phpstan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[psalm](/man/psalm)(1), [php](/man/php)(1), [composer](/man/composer)(1), [phpcs](/man/phpcs)(1)
