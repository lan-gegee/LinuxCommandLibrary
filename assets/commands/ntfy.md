# TAGLINE

简单的发布-订阅推送通知服务

# TLDR

**向主题发布消息**

```ntfy publish [topic] "[message]"```

**带标题和优先级发布**

```ntfy publish --title "[title]" --priority [high] [topic] "[message]"```

**带 emoji 标签发布**

```ntfy publish --tags "[warning,skull]" [topic] "[message]"```

**订阅主题**

```ntfy subscribe [topic]```

**订阅并在收到消息时执行命令**

```ntfy subscribe [topic] "[command]"```

**运行 ntfy 服务器**

```ntfy serve```

# SYNOPSIS

**ntfy** _command_ [_options_]

# PARAMETERS

**publish** _TOPIC_ [_MESSAGE_]
> 向主题发送通知。别名：send、trigger、pub。

**subscribe** _TOPIC_ [_COMMAND_]
> 订阅主题通知。可选在消息到达时运行命令。

**serve**
> 运行 ntfy 服务器（自托管）。

**--priority** _LEVEL_
> 设置优先级：min、low、default、high、max（或 1-5）。

**--title** _TITLE_
> 设置通知标题。

**--tags** _TAGS_
> 添加 emoji 标签（逗号分隔）。

**--attach** _URL_
> 通过 URL 附带文件。

**--server** _URL_
> 指定 ntfy 服务器 URL（默认：ntfy.sh）。

**--user** _USER_
> 用于身份验证的用户名。

**--since** _TIME_
> 接收自某时间或某消息 ID 以来的消息（配合 subscribe 使用）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ntfy** 是一个简单的基于 HTTP 的发布-订阅通知服务。它允许通过主题向手机和桌面发送推送通知。同一个二进制文件既可作为客户端（发布/订阅），也可作为服务器。

消息可以通过 CLI、curl 或任何 HTTP 客户端发布。订阅者可以在移动应用、网页界面或命令行上接收实时推送通知。

# CAVEATS

需要 ntfy.sh 或自托管服务器。除非配置了访问控制，主题默认是公开的。ntfy.sh 免费版有速率限制。

# CONFIGURATION

**~/.config/ntfy/client.yml**
> 客户端配置，包括用于自托管服务器的 default-host。

# HISTORY

ntfy 由 **Philipp C. Heckel** 创建，是一个简单的基于 HTTP 的发布-订阅通知服务。

# INSTALL

```apt: sudo apt install ntfy```

```apk: sudo apk add ntfy```

```brew: brew install ntfy```

```nix: nix profile install nixpkgs#ntfy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [notify-send](/man/notify-send)(1)
