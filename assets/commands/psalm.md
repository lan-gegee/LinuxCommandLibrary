# TAGLINE

PHP 类型安全的静态分析工具

# TLDR

**分析项目**

```psalm```

**以指定级别分析**

```psalm --level=[5]```

**分析特定文件**

```psalm [src/File.php]```

**初始化配置**

```psalm --init```

**生成基线**

```psalm --set-baseline=[baseline.xml]```

**显示 info 级别问题**

```psalm --show-info=true```

**输出为 JSON**

```psalm --output-format=json```

**只分析已更改的文件**（基于 git diff）

```psalm --diff```

**运行安全污点分析**

```psalm --taint-analysis```

**自动修复问题**

```psalm --alter --issues=[MissingReturnType]```

# SYNOPSIS

**psalm** [_--level n_] [_--set-baseline file_] [_--config file_] [_options_] [_paths_]

# PARAMETERS

**--level** _N_
> 错误级别（1-9，1 最严格）。

**--config**, **-c** _FILE_
> 配置文件。

**--init**
> 初始化 psalm.xml。

**--set-baseline** _FILE_
> 生成基线文件。

**--use-baseline** _FILE_
> 使用基线文件。

**--ignore-baseline**
> 忽略基线。

**--show-info**
> 显示 info 级别的问题。

**--output-format** _FMT_
> 输出格式（console、json、xml 等）。

**--alter**
> 修改文件以修复问题。

**--issues** _LIST_
> 配合 --alter 修复的问题类型。

**--threads** _N_
> 并行分析的线程数。

**--memory-limit** _SIZE_
> 内存限制。

**--diff**
> 只分析自上次运行以来发生变化的文件。

**--taint-analysis**
> 启用污点分析以检测数据流中的安全漏洞。

**--clear-cache**
> 清除缓存。

**--stats**
> 显示类型覆盖率统计。

# DESCRIPTION

**psalm** 是一款 PHP 静态分析工具，用于发现缺陷并强制实施类型安全。它理解 PHP 类型声明和 PHPDoc 注解。

错误级别从 1（最严格）到 9（最宽松）。级别越高允许越多潜在问题，适合遗留代码库。

psalm.xml 中的配置定义分析范围、排除的文件和问题的严重程度。针对项目的设置支持渐进式采用。

基线记录需要忽略的既有问题。新代码必须通过分析，而遗留问题可以逐步处理。

alter 模式可自动修复某些问题，例如添加返回类型或参数类型。这加快了向更严格类型化的迁移。

Psalm 通过 PHPDoc 语法理解复杂的 PHP 模式，包括泛型、联合类型和模板类型。

# CONFIGURATION

**psalm.xml**（或 **psalm.xml.dist**）
> 项目配置文件，定义错误级别、分析范围、排除目录、插件加载以及问题严重性覆盖。使用 **--init** 创建。

**baseline.xml**
> 基线文件，记录需要忽略的既有问题，允许对新代码执行严格分析，同时将遗留问题的修复延后。使用 **--set-baseline** 生成。

# CAVEATS

严格级别对遗留代码可能不切实际。某些 PHP 模式难以分析。内存占用随项目规模增长。

# HISTORY

**Psalm** 由 **Vimeo** 的 **Matthew Brown** 于 **2016 年**前后创建。它为 PHP 带来了高级静态分析，在 PHP 原生支持泛型之前就已提供相关功能。

# INSTALL

```pacman: sudo pacman -S psalm```

```brew: brew install psalm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[phpstan](/man/phpstan)(1), [php](/man/php)(1), [composer](/man/composer)(1), [phpcs](/man/phpcs)(1)
