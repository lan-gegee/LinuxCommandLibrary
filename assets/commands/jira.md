# TAGLINE

Atlassian Jira 的命令行客户端

# TLDR

初始化配置

```jira init```

列出最近的 issue

```jira issue list```

用 JQL 过滤 issue

```jira issue list --jql "[project = PROJ AND status = Open]"```

以交互方式创建 issue

```jira issue create```

查看某个 issue

```jira issue view [PROJ-123]```

将 issue 移动到某状态

```jira issue move [PROJ-123] "[In Progress]"```

将 issue 分配给用户

```jira issue assign [PROJ-123] [username]```

添加评论

```jira issue comment add [PROJ-123] "[comment body]"```

在浏览器中打开 issue

```jira open [PROJ-123]```

# SYNOPSIS

**jira** _command_ [_subcommand_] [_options_]

# COMMANDS

**init**
> 初始化配置文件，填入服务器 URL、登录信息和默认项目。

**issue**
> Issue 管理：创建、查看、列表、编辑、分配、移动、评论、关联、关注等。

**project**
> 列出和检查项目。

**sprint**
> 管理 sprint（Jira Cloud / Software）。

**epic**
> 管理 epic 及其子 issue。

**board**
> 列出项目中的看板。

**me**
> 显示当前已认证的用户。

**open**
> 在默认网页浏览器中打开 issue。

**completion**
> 生成 Shell 补全脚本。

# PARAMETERS

**-p**, **--project** _key_
> 为当前调用覆盖默认的项目键。

**--config** _file_
> 指定默认配置文件之外的配置文件路径。

**--debug**
> 启用详细的调试日志。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jira**（jira-cli）是一款开源的 Atlassian Jira Cloud 和 Data Center 命令行客户端。它为常见的工作流操作（创建、流转、评论）提供交互式 TUI 流程，并支持适合管道传入 Shell 脚本的基于 JQL 的列表查询。

身份验证通过存储在 **~/.config/.jira/.config.yml** 中的 API 令牌完成。该工具支持多个 Jira 实例、自定义字段以及用于创建 issue 的模板。

# CONFIGURATION

**~/.config/.jira/.config.yml**
> 存储服务器 URL、默认项目、用户/邮箱和 API 令牌。

**JIRA_API_TOKEN**
> 覆盖已存储 API 令牌的环境变量。

# CAVEATS

需要 Jira 账户和 API 令牌（Atlassian Cloud），或个人访问令牌（Data Center）。这是由 **ankitpokhrel** 开发的第三方 **jira-cli** 工具，并非 Atlassian 官方产品。部分功能（如 sprint 操作）需要 Jira Software，而不仅是 Jira Core/Work Management。

# HISTORY

**jira-cli** 由 **Ankit Pokhrel** 创建，旨在从终端提供快速、可脚本化的 Jira 接口。该项目使用 Go 编写。

# SEE ALSO

[gh](/man/gh)(1), [glab](/man/glab)(1), [git](/man/git)(1)
