# TAGLINE

Apple 开发的可编程配置语言

# TLDR

**求值 Pkl 文件**

```pkl eval [config.pkl]```

**以 JSON 输出**

```pkl eval -f json [config.pkl]```

**以 YAML 输出**

```pkl eval -f yaml [config.pkl]```

**检查语法**

```pkl check [config.pkl]```

**启动 REPL**

```pkl repl```

# SYNOPSIS

**pkl** [_command_] [_options_] [_file_]

# PARAMETERS

**eval** _FILE_
> 对配置进行求值。

**check** _FILE_
> 校验语法。

**repl**
> 启动交互模式。

**-f** _FORMAT_
> 输出格式。

**--help**
> 显示帮助。

# DESCRIPTION

**pkl** 是 Apple 开发的可编程配置语言。它对 .pkl 文件求值并生成多种格式的输出，包括 JSON、YAML、XML 和属性列表，将静态配置的可读性与编程语言的强大能力结合在一起。

Pkl 通过类和模块提供类型安全、校验和代码复用，在求值阶段而非部署阶段就捕获配置错误。REPL 模式支持交互式探索和测试配置表达式。

# CAVEATS

Pkl 文件可以从网络导入模块，这可能带来安全问题。该语言需要基于 JVM 的运行时或原生二进制文件来执行求值。

# HISTORY

Pkl 由 **Apple** 创建，并于 **2024 年 2 月**开源，是一种类型安全的可编程配置语言。

# INSTALL

```brew: brew install pkl```

```nix: nix profile install nixpkgs#pkl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jsonnet](/man/jsonnet)(1), [dhall](/man/dhall)(1)
