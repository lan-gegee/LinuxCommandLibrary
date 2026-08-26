# TAGLINE

快速的多语言构建系统

# TLDR

**构建目标**

```buck build //[path/to:target]```

**运行二进制目标**

```buck run //[path/to:target]```

**运行测试**

```buck test //[path/to:target]```

**查询目标依赖**

```buck query "deps(//[path/to:target])"```

**列出包中的所有目标**

```buck targets //[path/to/package]:```

**以指定配置构建**

```buck build //[target] --config [section.option=value]```

**清理构建产物**

```buck clean```

**显示构建输出路径**

```buck build //[target] --show-output```

# SYNOPSIS

**buck** _command_ [_options_] [_targets_]

**buck2** _command_ [_options_] [_targets_]

# DESCRIPTION

**Buck** 是由 Facebook（Meta）开发的快速多语言构建系统。它利用依赖图判断哪些目标需要重新构建，从而支持增量构建。Buck2 是重写后的后继版本，性能更佳。

构建规则定义在 BUCK 文件（Buck2 中为 BUILD 文件）中，使用类 Python 的语法。目标通过 //path/to/package:name 约定引用。Buck 会缓存构建产物，并可在多台机器间分发构建。

借助可扩展的规则系统，Buck 支持 C++、Java、Python、Go、Rust 等多种语言。它面向依赖图复杂的大型 monorepo 代码库而设计。

# PARAMETERS

**build** _targets_
> 构建指定的目标。

**run** _target_
> 构建并运行二进制目标。

**test** _targets_
> 构建并运行测试。

**clean**
> 删除构建产物。

**targets** _pattern_
> 列出匹配模式的目标。

**query** _expression_
> 查询目标图。

**audit** _subcommand_
> 审计构建配置。

**install** _target_
> 构建并安装（移动应用）。

**--config** _key=value_
> 覆盖配置值。

**--show-output**
> 显示输出文件路径。

**--no-cache**
> 忽略缓存结果。

**-j** _jobs_
> 并行任务数量。

**-v** _verbosity_
> 详细程度（0-10）。

**--show-full-output**
> 显示包含哈希的完整输出路径。

**--help**
> 显示帮助信息。

# CONFIGURATION

**.buckconfig**
> Buck1 的项目级配置，指定构建设置、工具路径和仓库选项。

**.buckroot**
> 标记 Buck 项目根目录的标记文件。

**BUCK** / **BUILD**
> 各目录下的构建文件，定义目标和规则（Buck1 用 BUCK，Buck2 用 BUILD）。

# CAVEATS

需要 Java 运行时（Buck1）或独立二进制文件（Buck2）。构建文件必须符合特定格式。庞大的依赖图可能导致初始分析缓慢。远程执行需要额外的基础设施。Buck2 与 Buck1 不完全向后兼容。

# HISTORY

**Buck** 由 **Facebook** 自 **2013 年**前后开始开发，用于应对公司庞大代码库的构建需求。它已开源，并被 Uber、Airbnb 等公司采用。**Buck2** 于 **2022 年**公布，是用 Rust 完全重写的版本，性能显著提升。Buck2 于 **2023 年 4 月**开源，现已成为推荐版本。

# INSTALL

```aur: yay -S buck```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bazel](/man/bazel)(1), [make](/man/make)(1), [ninja](/man/ninja)(1), [gradle](/man/gradle)(1)
