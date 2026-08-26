# TAGLINE

从命令行管理 Jira sprint

# TLDR

列出项目的 sprint

```jira sprint list -p [PROJECT]```

查看当前 sprint 的 issue

```jira sprint list --current -p [PROJECT]```

查看上一个 sprint 的 issue

```jira sprint list --prev -p [PROJECT]```

列出未来与活跃的 sprint

```jira sprint list --state future,active -p [PROJECT]```

将 issue 添加到 sprint

```jira sprint add [SPRINT_ID] [PROJ-123]```

列出当前 sprint 中分配给你的 issue

```jira sprint list --current -a$(jira me) -p [PROJECT]```

# SYNOPSIS

**jira sprint** _command_ [_options_]

# PARAMETERS

**list**
> 在交互式浏览器视图中列出 sprint 及其 issue。

**add** _SPRINT_ _ISSUE_
> 将 issue 添加到 sprint。

**--current**
> 显示当前活跃 sprint 中的 issue。

**--prev**
> 显示上一个 sprint 中的 issue。

**--next**
> 显示下一个计划 sprint 中的 issue。

**--state** _STATES_
> 按状态过滤 sprint（逗号分隔：active、closed、future）。

**-a** _ASSIGNEE_
> 按经办人过滤 issue。

**-p** _PROJECT_
> 项目键。

**--table**
> 以表格视图而非浏览器视图显示结果。

**--plain**
> 输出纯文本（便于脚本处理）。

**--no-headers**
> 省略列标题（配合 --plain 用于脚本）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jira sprint** 从命令行管理 Jira sprint。它可以列出 sprint、查看 sprint 中的 issue 以及向 sprint 中添加 issue。结果默认显示在交互式浏览器视图中，也可选择表格或纯文本输出模式。

该命令支持 issue 列表命令的所有过滤标志，可在 sprint 范围内按经办人、状态、优先级及其他 issue 字段进行过滤。

# CAVEATS

**jira-cli**（ankitpokhrel/jira-cli）的子命令。要求项目已配置 Scrum 看板。需要相应的 Jira 项目权限。

# HISTORY

jira sprint 是 **jira-cli** 的一部分，这是一款由 **Ankit Pokhrel** 开发的开源 Go 工具，可从终端进行敏捷 sprint 管理。

# SEE ALSO

[jira](/man/jira)(1), [jira-issue](/man/jira-issue)(1), [jira-sprints](/man/jira-sprints)(1), [jira-me](/man/jira-me)(1)
