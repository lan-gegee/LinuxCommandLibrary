# TAGLINE

支持流式推送的终端 Twitter 客户端

# TLDR

**启动 rainbowstream**

```rainbowstream```

**发布推文**

```t [message]```

**查看时间线**

```home```

**回复推文**

```rep [tweet_id] [message]```

**转发推文**

```rt [tweet_id]```

**点赞推文**

```fav [tweet_id]```

**搜索推文**

```s [query]```

**查看提及**

```mentions```

# SYNOPSIS

**rainbowstream** [_options_]

# INTERACTIVE COMMANDS

**t** _MESSAGE_
> 发布推文。

**home**
> 显示主时间线。

**mentions**
> 显示提及。

**me**
> 显示自己的推文。

**rep** _ID_ _MESSAGE_
> 回复推文。

**rt** _ID_
> 转发推文。

**fav** _ID_
> 点赞推文。

**s** _QUERY_
> 搜索推文。

**whois** _USER_
> 显示用户信息。

**fl** _USER_
> 关注用户。

**ufl** _USER_
> 取消关注用户。

# DESCRIPTION

**rainbowstream** 是一个基于终端的 Twitter 客户端，提供实时推文流，输出色彩丰富且带语法高亮。它连接 Twitter Streaming API，新推文到达时即显示，自动更新时间线而无需手动刷新。

交互式 Shell 提供一整套命令，可用于发布推文、回复、转发、点赞、关注用户和搜索。配色主题会对用户名、话题标签和 URL 进行高亮以提升可读性，内嵌图片预览还能将图片渲染为 ASCII 艺术直接显示在终端中。该客户端在一个命令行会话中支持所有主要的 Twitter 交互。

# CONFIGURATION

**~/.rainbow_oauth**
> OAuth 凭据文件，存储用于身份验证的 Twitter API 访问令牌。

**~/.rainbow_config.json**
> 用户配置文件，控制配色主题、显示设置、图片预览和通知偏好。

# CAVEATS

需要 Twitter API 访问权限。API 变更可能导致功能失效。存在速率限制。

# HISTORY

**Rainbowstream** 为在终端访问 Twitter 而生。它以彩色、易读的输出将社交媒体带入命令行。

# INSTALL

```nix: nix profile install nixpkgs#rainbowstream```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[twurl](/man/twurl)(1)
