# TAGLINE

在默认网页浏览器中打开 Jira 资源

# TLDR

在浏览器中打开 issue

```jira open [PROJ-123]```

打开项目看板

```jira open -p [PROJECT]```

打开当前 sprint

```jira open --sprint```

打开 backlog

```jira open --backlog -p [PROJECT]```

# SYNOPSIS

**jira open** [_options_] [_issue_]

# PARAMETERS

_ISSUE_
> 要打开的 issue 键。

**-p** _PROJECT_
> 要打开的项目。

**--sprint**
> 打开活跃 sprint。

**--backlog**
> 打开 backlog。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jira open** 在默认网页浏览器中打开 Jira 资源。它可以快速访问 issue、看板和 backlog。

该命令将 issue 键或项目标识转换为 Web URL。比在 Web 界面中层层导航更快。

# CAVEATS

jira-cli 的子命令。需要已配置的服务器。使用默认浏览器。

# HISTORY

jira open 是 **jira-cli** 中的一个便利命令，用于从终端快速访问 Jira Web 界面。

# SEE ALSO

[jira](/man/jira)(1), [jira-me](/man/jira-me)(1), [open](/man/open)(1)
