# TAGLINE

从命令行管理 Jira issue

# TLDR

列出 issue

```jira issue list```

创建新 issue

```jira issue create```

查看 issue 详情

```jira issue view [ISSUE-123]```

将 issue 移动到某状态

```jira issue move [ISSUE-123] "[Done]"```

分配 issue

```jira issue assign [ISSUE-123] [username]```

# SYNOPSIS

**jira** **issue** _subcommand_ [_options_]

# PARAMETERS

**list**
> 列出符合过滤条件的 issue。

**create**
> 以交互方式创建新 issue。

**view** _key_
> 查看 issue 详情。

**move** _key_ _status_
> 将 issue 流转到新状态。

**assign** _key_ _user_
> 将 issue 分配给用户。

**comment** _key_
> 为 issue 添加评论。

# DESCRIPTION

**jira issue** 从命令行管理 Jira issue。它是 jira-cli 的一部分，无需使用 Web 界面即可创建、查看、更新和流转 issue。支持过滤、JQL 查询和批量操作。

# SEE ALSO

[jira](/man/jira)(1), [jira-browse](/man/jira-browse)(1), [jira-sprint](/man/jira-sprint)(1)
