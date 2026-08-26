# TAGLINE

用于与 Atlassian Jira 交互的 TUI

# TLDR

启动 jiratui

```jiratui```

# SYNOPSIS

**jiratui** [_options_]

# DESCRIPTION

**jiratui** 是一个文本用户界面（TUI），可直接在终端中与 **Atlassian Jira** 交互。它基于 **Textual** 和 **Rich** 框架构建，支持 Jira Cloud Platform REST API v3。该界面提供支持 **JQL**（Jira Query Language）的搜索功能、任务管理、评论管理和 issue 关联。

主要功能包括查看和编辑 issue、管理评论、关联与取消关联相关任务，以及使用复杂 JQL 查询执行高级搜索。

# CONFIGURATION

配置存储在 **$HOME/.config/jiratui/config.yaml**，也可通过 **JIRA_TUI_CONFIG_FILE** 环境变量指定。设置项包括 Jira 服务器 URL、身份验证凭据和默认项目。

# CAVEATS

需要 Jira Cloud 账户和 API 令牌。对 Jira Server/Data Center 的支持可能有限。部分高级 Jira 功能可能在 TUI 中不可用。

# HISTORY

**jiratui** 由 **whyisdifficult** 创建，用 **Python** 基于 Textual 框架编写。它旨在为喜欢在终端工作的开发者提供键盘驱动的 Jira 使用体验。

# INSTALL

```brew: brew install jiratui```

```nix: nix profile install nixpkgs#jiratui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jira-cli](/man/jira-cli)(1)
