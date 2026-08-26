# TAGLINE

查看和配置 Zapier CLI 的分析数据收集

# TLDR

**显示当前分析状态**

```zapier analytics```

**启用完整分析收集**

```zapier analytics -m enabled```

**设置匿名分析模式**

```zapier analytics -m anonymous```

**禁用分析收集**

```zapier analytics -m disabled```

# SYNOPSIS

**zapier** **analytics** [_-m mode_]

# PARAMETERS

**-m**, **--mode** _MODE_
> 设置分析收集模式：enabled（默认，发送命令信息、操作系统类型和用户 ID）、anonymous（仅发送命令信息）或 disabled（不收集任何数据）。

# DESCRIPTION

**zapier analytics** 显示 Zapier CLI 的分析数据收集状态，并允许更改收集哪些数据。默认情况下分析处于启用状态，包含关于集成、CLI 命令、操作系统和 Zapier 用户 ID 的信息。

在匿名模式下，会省略操作系统类型和用户 ID，但命令信息仍会被发送。也可以运行 zapier analytics -m disabled 或将 DISABLE_ZAPIER_ANALYTICS 环境变量设为 1 来完全禁用分析。

要查看运行时具体收集了什么，可在任意命令前加 DEBUG=zapier:analytics。

# SEE ALSO

[zapier](/man/zapier)(1), [zapier-history](/man/zapier-history)(1), [zapier-push](/man/zapier-push)(1), [zapier-validate](/man/zapier-validate)(1)
