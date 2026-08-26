# TAGLINE

跨平台的环境变量命令行工具

# TLDR

**显示**所有环境变量

```envfetch```

**获取**某个特定变量

```envfetch [VARIABLE_NAME]```

**搜索**匹配模式的环境变量

```envfetch --search [pattern]```

以 JSON 格式**输出**

```envfetch --json```

# SYNOPSIS

**envfetch** [_options_] [_variable_]

# PARAMETERS

**--search** _PATTERN_
> 搜索匹配模式的环境变量

**--json**
> 以 JSON 格式输出

**--export**
> 以 shell export 命令的形式输出

**--no-color**
> 禁用彩色输出

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**envfetch** 是一个跨平台工具，用于显示和查询环境变量。它在不同操作系统和 shell 之间提供统一的接口，便于检查环境配置。

该工具支持搜索、过滤和多种输出格式，可用于调试环境问题和提取配置值。

# CAVEATS

跨平台兼容性可能存在细微差异。敏感变量默认会直接显示。庞大的环境变量集合可能需要过滤。

# HISTORY

**envfetch** 的开发目标是提供一个可移植的替代品，取代各平台专属的环境检查工具。

# INSTALL

```aur: yay -S envfetch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[env](/man/env)(1), [printenv](/man/printenv)(1), [set](/man/set)(1)
