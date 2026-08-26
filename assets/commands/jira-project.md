# TAGLINE

从命令行管理 Jira 项目

# TLDR

列出所有项目

```jira project list```

查看项目详情

```jira project view [PROJECT_KEY]```

以纯表格格式列出项目

```jira project list --plain```

# SYNOPSIS

**jira** **project** _subcommand_ [_options_]

# PARAMETERS

**list**
> 列出所有可访问的项目。

**view** _key_
> 按键查看项目详情（如 PROJ）。

**--plain**
> 以无边框的纯表格格式显示输出。

# DESCRIPTION

**jira project** 从命令行管理 Jira 项目。它是 **jira-cli**（由 ankitpokhrel 开发）的一部分，可以列出和查看项目信息，包括项目键、名称、负责人和项目类型。

# SEE ALSO

[jira](/man/jira)(1), [jira-issue](/man/jira-issue)(1), [jira-sprint](/man/jira-sprint)(1)
