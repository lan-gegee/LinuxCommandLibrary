# TAGLINE

功能丰富的交互式 Jira 命令行工具

# TLDR

初始化配置

```jira init```

创建 issue

```jira issue create```

列出分配给你的 issue

```jira issue list -a$(jira me)```

查看某个 issue

```jira issue view [ISSUE-123]```

将 issue 移动到其他状态

```jira issue move [ISSUE-123] "[In Progress]"```

在浏览器中打开 issue

```jira open [ISSUE-123]```

列出 sprint

```jira sprint list```

添加评论

```jira issue comment add [ISSUE-123]```

# SYNOPSIS

**jira** _command_ [_options_] [_arguments_]

# DESCRIPTION

**jira-cli** 是一款面向 **Atlassian Jira** 的交互式命令行工具，让你无需离开终端即可管理 issue、sprint 和项目。它支持 issue 的创建、克隆、关联、状态流转、评论、sprint 管理，以及带 TUI 选择的交互式 issue 搜索。

该工具使用 Jira 的 REST API，同时支持 Jira Cloud 和 Jira Server。配置存储在本地，采用 API 令牌进行身份验证。

# PARAMETERS

**init**
> 配置 Jira 服务器和身份验证

**issue create**
> 以交互方式创建新 issue

**issue list**
> 使用过滤器列出 issue

**issue view** _KEY_
> 查看 issue 详情

**issue move** _KEY_ _STATUS_
> 流转 issue 状态

**issue comment add** _KEY_
> 添加评论

**sprint list**
> 列出 sprint

**open** _KEY_
> 在浏览器中打开 issue

**me**
> 打印当前用户

# CAVEATS

需要 Jira API 令牌进行身份验证。部分功能在较旧的 Jira Server 版本上可能不可用。大量使用时可能受到速率限制。

# HISTORY

**jira-cli** 由 **Ankit Pokhrel** 创建，用 **Go** 编写。它旨在填补 Atlassian Jira 命令行工具的空缺，提供快速、交互式的终端工作流。

# INSTALL

```zypper: sudo zypper install jira-cli```

```brew: brew install jira-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1)
