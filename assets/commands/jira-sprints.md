# TAGLINE

列出 Jira 项目的 sprint

# TLDR

列出所有 sprint

```jira sprints -p [PROJECT]```

列出活跃的 sprint

```jira sprints --state active -p [PROJECT]```

列出已关闭的 sprint

```jira sprints --state closed -p [PROJECT]```

限制数量列出

```jira sprints -l [10] -p [PROJECT]```

# SYNOPSIS

**jira sprints** [_options_]

# PARAMETERS

**-p** _PROJECT_
> 项目键。

**--state** _STATE_
> Sprint 状态（active、closed、future）。

**-l** _LIMIT_
> 最大结果数。

**--plain**
> 纯文本输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jira sprints** 列出 Jira 项目的 sprint。它显示 sprint 名称、状态和日期。

该命令提供 sprint 历史与规划的总览。它可按状态过滤，聚焦相关的 sprint。

# CAVEATS

jira-cli 的子命令。要求已配置 Scrum 看板。需要项目权限。

# HISTORY

jira sprints 是 **jira-cli** 的一部分，为敏捷项目管理提供 sprint 列举功能。

# SEE ALSO

[jira](/man/jira)(1), [jira-sprint](/man/jira-sprint)(1), [jira-me](/man/jira-me)(1)
