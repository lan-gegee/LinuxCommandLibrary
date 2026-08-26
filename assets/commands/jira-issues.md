# TAGLINE

从命令行列出 Jira issue

# TLDR

列出所有 issue

```jira issues```

使用 JQL 查询列出 issue

```jira issues --jql "[project = PROJ AND status = Open]"```

列出分配给我的 issue

```jira issues --assignee me```

以 JSON 格式列出 issue

```jira issues --plain --no-headers```

# SYNOPSIS

**jira** **issues** [_options_]

# PARAMETERS

**--jql** _query_
> 使用 JQL 查询过滤 issue。

**--assignee** _user_
> 按经办人过滤。

**--status** _status_
> 按状态过滤。

**--project** _key_
> 按项目过滤。

**--plain**
> 输出不带格式的文本。

**--no-headers**
> 省略列标题。

# DESCRIPTION

**jira issues** 从命令行列出 Jira issue。它是 jira-cli 的一部分，支持通过 JQL 过滤查找特定 issue。它是 `jira issue list` 的别名，并针对常见查询提供了便利的默认值。

# SEE ALSO

[jira](/man/jira)(1), [jira-issue](/man/jira-issue)(1)
