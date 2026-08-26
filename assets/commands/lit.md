# TAGLINE

LLVM 集成测试器

# TLDR

**运行测试**

```lit [tests/]```

**运行特定测试**

```lit [test.py]```

**详细输出**

```lit -v [tests/]```

**显示全部输出**

```lit -a [tests/]```

**并行执行**

```lit -j [4] [tests/]```

**过滤测试**

```lit --filter [pattern] [tests/]```

# SYNOPSIS

**lit** [_options_] _tests_

# PARAMETERS

_TESTS_
> 测试文件或目录。

**-v**
> 详细输出。

**-a**
> 显示全部输出。

**-j** _N_
> 并行作业数。

**--filter** _PATTERN_
> 只运行匹配的测试。

**--no-progress-bar**
> 禁用进度条。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lit**（LLVM Integrated Tester）是一个便携式测试执行框架，专为运行编译器和工具的测试套件而设计。它在目录树中发现测试文件，按照可配置的测试格式执行它们，并报告结果，同时支持多线程并行执行。测试通常是一些内嵌 RUN 行的小脚本：RUN 行指定要执行的命令，CHECK 行定义预期的输出模式。

该框架支持多种测试格式，包括 ShTest（由 lit 自身解释的 shell 脚本风格测试）、GoogleTest 二进制文件，以及通过 Python 配置文件定义的自定义格式。每个测试目录包含一个 `lit.cfg` 或 `lit.cfg.py` 文件，用于指定测试格式、可用的替换规则和环境配置。虽然 lit 是为 LLVM 自己的测试基础设施构建的，但它是一个通用工具，可用于测试任何命令行程序。

# CAVEATS

主要面向 LLVM 项目。需要测试配置。基于 Python。

# HISTORY

lit 作为 **LLVM** 项目的一部分开发，旨在为编译器测试提供灵活、快速的测试框架。

# INSTALL

```apk: sudo apk add llvm-test-utils```

```brew: brew install lit```

```nix: nix profile install nixpkgs#lit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pytest](/man/pytest)(1), [make](/man/make)(1)
