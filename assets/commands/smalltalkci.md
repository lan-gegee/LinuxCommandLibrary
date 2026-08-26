# TAGLINE

Smalltalk 项目的持续集成工具

# TLDR

**运行测试**

```smalltalkci```

**使用配置运行**

```smalltalkci [.smalltalk.ston]```

**指定 Smalltalk**

```smalltalkci -s [Squeak64-5.3]```

**无头模式**

```smalltalkci --headless```

**调试模式**

```smalltalkci -d```

# SYNOPSIS

**smalltalkci** [_-s smalltalk_] [_-d_] [_options_] [_config_]

# PARAMETERS

**-s** _SMALLTALK_
> 要使用的 Smalltalk image 版本（如 Squeak64-5.3、Pharo-10.0）。

**-d**
> 调试模式，排错时提供更多输出。

**--headless**
> 无图形显示地运行 Smalltalk VM（CI 环境的默认值）。

**--image** _FILE_
> 使用指定的 Smalltalk image 文件。

**--baseline** _NAME_
> 定义要加载或测试的 Metacello baseline。

**--dir** _PATH_
> 设置项目的工作目录。默认为当前目录。

**--cache-dir** _PATH_
> 缓存 Smalltalk image 和 VM 的目录。

**--github-token** _TOKEN_
> 用于访问私有仓库或提高 API 速率限制的 GitHub token。

**--no-tracking**
> 退出匿名的构建指标收集。

**--help**
> 显示帮助。

# DESCRIPTION

**smalltalkci** 为 Smalltalk 项目提供跨多种方言的持续集成测试，包括 Squeak、Pharo、GemStone/S 和 Moose。它自动完成下载合适的 Smalltalk 虚拟机、加载项目代码、运行测试和报告结果的全过程。

配置在 **.smalltalk.ston** 文件中以 STON（Smalltalk Object Notation）格式定义，指定要使用的 Smalltalk 平台、要加载的包以及要运行的测试类。该工具可与 GitHub Actions、Travis CI 及其他 CI/CD 平台集成。

测试默认以无头模式运行，不需要图形显示。调试模式为排查失败的构建提供额外输出，对于有特定环境需求的项目，还可以指定自定义的 Smalltalk image。

# CAVEATS

仅适用于 Smalltalk。必须通过 .smalltalk.ston 配置。首次运行时 VM 下载可能较慢，之后会使用缓存。

# SEE ALSO

[pharo](/man/pharo)(1), [squeak](/man/squeak)(1)
