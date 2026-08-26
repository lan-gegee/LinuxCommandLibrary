# TAGLINE

列出所有可访问的 Jira 项目

# TLDR

列出所有项目

```jira projects```

以纯文本格式列出项目

```jira projects --plain```

不带标题行列出

```jira projects --no-headers```

列出最近查看的项目

```jira projects --recent```

# SYNOPSIS

**jira** **projects** [_options_]

# PARAMETERS

**--plain**
> 输出不带格式的文本。

**--no-headers**
> 省略列标题。

**--recent**
> 列出最近查看的项目。

**--paginate**
> 获取全部分页结果。

**--json**
> 生成 JSON 输出。

# DESCRIPTION

**jira projects** 列出所有可访问的 Jira 项目。它是 jira-cli 的一部分，显示项目键、名称和类型。它是 `jira project list` 的别名，并提供了便利的输出选项。

# SEE ALSO

[jira](/man/jira)(1), [jira-project](/man/jira-project)(1), [jira-issue](/man/jira-issue)(1)
