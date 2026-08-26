# TAGLINE

列出分配给当前用户的 issue

# TLDR

列出我的 issue

```jira me```

我在某项目中的 issue

```jira me -p [PROJECT]```

我未完成的 issue

```jira me --status [Open]```

限制数量的我的 issue

```jira me -l [20]```

原始输出的我的 issue

```jira me --plain```

# SYNOPSIS

**jira me** [_options_]

# PARAMETERS

**-p** _PROJECT_
> 按项目过滤。

**--status** _STATUS_
> 按状态过滤。

**-l** _LIMIT_
> 最大结果数。

**--plain**
> 纯文本输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jira me** 列出分配给当前用户的 issue。它可以快速查看个人工作量。

该命令默认过滤以显示未完成的 issue。额外的过滤器可按项目或状态进一步缩小结果范围。

# CAVEATS

jira-cli 的子命令。需要身份验证。可在配置中设置别名。

# HISTORY

jira me 是 **jira-cli** 中的一个便利命令，用于快速查看分配给已认证用户的 issue。

# SEE ALSO

[jira](/man/jira)(1), [jira-sprint](/man/jira-sprint)(1), [jira-open](/man/jira-open)(1)
