# TAGLINE

在网页浏览器中打开各种 Jira 视图

# TLDR

跳转到项目页面

```jira navigate --project [PROJECT_KEY]```

跳转到活跃 sprint 看板

```jira navigate --board```

跳转到 backlog 视图

```jira navigate --backlog```

# SYNOPSIS

**jira** **navigate** [_options_]

# PARAMETERS

**--project** _key_
> 跳转到给定项目键的项目概要页面。

**--board**
> 打开当前项目的活跃 sprint 看板。

**--backlog**
> 打开当前项目的 backlog 视图。

# DESCRIPTION

**jira navigate** 在默认网页浏览器中打开各种 Jira 视图。它是 **jira-cli**（由 Ankit Pokhrel 开发）的一部分，无需手动构造 URL 即可快速访问看板、backlog 和项目页面。项目默认取自 jira-cli 设置中配置的项目。

# SEE ALSO

[jira](/man/jira)(1), [jira-open](/man/jira-open)(1), [jira-sprint](/man/jira-sprint)(1)
