# TAGLINE

现代化的终端 Mastodon TUI 客户端

# TLDR

**启动 Mastodon 客户端**

```mastui```

**登录 Mastodon 实例**

```mastui login```

**选择主题**

```mastui theme```

# SYNOPSIS

**mastui** [_options_]

# PARAMETERS

**login**
> 向 Mastodon 实例进行身份验证。

**theme**
> 选择 UI 主题。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**mastui** 是一个用 Python 和 Textual 构建的快速、现代化 Mastodon TUI 客户端。它以多栏方式显示时间线（首页、通知、跨站联邦时间线），并带有持久缓存以保证流畅滚动。

功能包括终端内图片查看（ANSI/Sixel/TGP）、多套明暗主题、可按时间线配置的刷新间隔、带内容警告和语言选择的全屏发帖编辑器，以及投票的创建和管理。

# CAVEATS

需要 Mastodon 账户和 API 访问令牌。图片显示能力取决于终端模拟器的支持程度。

# HISTORY

**mastui** 由 **kimusan** 创建，使用 **Python** 和 Textual 框架编写。

# SEE ALSO

[toot](/man/toot)(1)
