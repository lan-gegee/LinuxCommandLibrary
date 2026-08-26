# TAGLINE

TUI Twitch 聊天客户端

# TLDR

**启动** Twitch 聊天 TUI 客户端

```chatuino```

**管理**已关联的 Twitch 账号

```chatuino account```

**查看**当前缓存大小

```chatuino cache```

**清除**缓存的表达

```chatuino cache clear --emotes```

# SYNOPSIS

**chatuino** [_flags_] [_command_]

# PARAMETERS

**account**
> 打开账号管理器，用于添加、移除或切换 Twitch 账号。

**cache**
> 查询当前缓存大小。使用 **cache clear --emotes**、**--database** 或 **--badges** 清除特定缓存。

**--help**
> 显示帮助信息。

# DESCRIPTION

**chatuino** 是一个用 Go 编写的跨平台 Twitch 聊天终端用户界面客户端。它允许用户在终端中管理多个 Twitch 账号，并同时参与多个聊天室。它支持在 Kitty 和 Ghostty 终端中以图形方式渲染表情，集成了第三方表情服务（7TV、BTTV、FFZ），并包含管理员工具、基于 SQLite 的本地聊天日志、使用 Go template 语法的自定义命令，以及完整的主题和按键绑定自定义。

主要功能包括表情和用户名的 Tab 补全、按用户的聊天历史查看、提及通知与实时提醒、本地消息搜索，以及带快速 timeout 快捷键的管理员工具。

# CONFIGURATION

配置存储在 **~/.config/chatuino/settings.yaml**。按键绑定位于 **~/.config/chatuino/keymap.yaml**。在应用内按 **?** 可查看按键绑定。

值得注意的选项包括 **vertical_tab_list**、**smooth_scroll**、**graphic_emotes**（需要 Kitty/Ghostty）、**graphic_badges**、**time_format**、**store_chat_logs**（SQLite）、**check_links**、**block_settings**（用户/词语）和 **custom_commands**。设置 **NO_COLOR=1** 可禁用彩色渲染。

# CAVEATS

图形表情渲染仅在 Kitty 和 Ghostty 终端中可用。身份验证需要通过 chatuino.net 授权页面并粘贴令牌完成。**logs_channel_include** 和 **logs_channel_exclude** 设置互斥。

# HISTORY

**chatuino** 由 **julez-dev** 开发，于 2023 年 12 月首次发布。其灵感来自 **Chatterino**（流行的 GUI Twitch 聊天客户端）和 **twitch-tui**（基于 Rust 的终端客户端）。名称由 "chat" 与 Chatterino 的 "-uino" 后缀组合而成。最新版本为 v1.1.0（2026 年 2 月），使用 Go 编写，采用 MIT 许可证。

# SEE ALSO

[weechat](/man/weechat)(1), [irssi](/man/irssi)(1)
