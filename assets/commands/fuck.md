# TAGLINE

命令纠错建议工具

# TLDR

**修正上一条命令**

```fuck```

运行前先确认

```fuck --yeah```

**使用指定的修正方案**

```fuck --yes [number]```

**显示可用的修复**

```fuck --help```

# SYNOPSIS

**fuck** [_options_]

# PARAMETERS

**--yeah**, **--yes**
> 立即确认修正。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.config/thefuck/settings.py**
> 配置规则、排除的命令、优先级和别名。

# DESCRIPTION

**fuck** 是 The Fuck 应用中用于修正上一条控制台命令的命令。它会分析上一条失败的命令并提出修正建议。

当你输错命令或忘记 sudo 时，运行 fuck 会给出修正后的命令。它从你的 shell 历史中学习，支持许多常见的错误模式。

fuck 通过别名或按键绑定与 shell 集成，便于快速调用。

# CAVEATS

需要设置别名。可能无法捕获所有错误。某些修正未必合适。请谨慎使用。

# HISTORY

fuck 是 Vladimir Iakovlev 创建的 **The Fuck** 项目的一部分。该应用通过基于 Python 的规则匹配，提供一种有趣而实用的方式来纠正命令行错误。

# INSTALL

```aur: yay -S fuck```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1)
