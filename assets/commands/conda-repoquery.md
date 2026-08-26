# TAGLINE

高级软件包查询工具

# TLDR

**搜索软件包**

```conda repoquery search [package_name]```

**显示软件包的依赖**

```conda repoquery depends [package_name]```

**显示哪些软件包依赖它**

```conda repoquery whoneeds [package_name]```

# SYNOPSIS

**conda** **repoquery** _subcommand_ [_options_] [_query_]

# SUBCOMMANDS

**search**
> 搜索软件包。

**depends**
> 显示软件包依赖。

**whoneeds**
> 显示反向依赖。

# CONFIGURATION

**~/.condarc**
> 用户级 conda 配置，涵盖频道、软件包设置和求解器选项。

**/opt/conda/.condarc**
> 系统级 conda 配置。

# DESCRIPTION

**conda repoquery** 借助 libmamba 提供高级软件包查询能力。它可以搜索仓库并分析依赖关系。

# CAVEATS

需要 libmamba 求解器。较旧的 conda 版本中可能不可用。

# SEE ALSO

[conda](/man/conda)(1), [conda-search](/man/conda-search)(1)

# RESOURCES

```[Source code](https://github.com/conda/conda)```

```[Homepage](https://docs.conda.io)```

```[Documentation](https://docs.conda.io/projects/conda/en/stable/commands/index.html)```

<!-- verified: 2026-06-23 -->
