# TAGLINE

在命令行中编辑和删除 Telegram 消息

# TLDR

**删除聊天中所有匹配文本的消息**

```tgutil -n [session] -u [chat_id] -m deleteall --text "[text]"```

**编辑特定消息**

```tgutil -n [session] -u [me] -m edit --text "[old text]" --newtext "[new text]"```

**编辑所有匹配的消息**

```tgutil -n [session] -u [chat_id] -m editall --text "[old text]" --newtext "[new text]"```

**删除"收藏夹"（Saved Messages）中单条匹配的消息**

```tgutil -n [session] -u [me] -m delete --text "[text]"```

# SYNOPSIS

**tgutil** **-n** _session_ **-u** _chat_ **-m** _mode_ **--text** _text_ [**--newtext** _text_]

# PARAMETERS

**-n**, **--name** _SESSION_
> 会话名称（已认证的 Telegram 账户）。

**-u**, **--username** _CHAT_
> 目标聊天 ID 或用户名。使用 `me` 表示收藏夹（Saved Messages）。

**-m**, **--mode** _MODE_
> 操作模式：`edit`、`editall`、`delete`、`deleteall`。

**--text** _TEXT_
> 要在消息中搜索的文本。

**--newtext** _TEXT_
> 替换文本（`edit` 和 `editall` 模式必需）。

# DESCRIPTION

**tgutil** 是一款用于编辑和删除 Telegram 聊天消息的 CLI 工具。它是 **telegram-cloud** Python 软件包的一部分，该软件包提供了一整套从命令行操作 Telegram 的工具。

该工具有四种模式：`edit` 修改第一条匹配的消息，`editall` 修改所有匹配的消息，`delete` 删除第一条匹配的消息，`deleteall` 删除所有包含指定文本的匹配消息。

通过 pip 安装：`pip install telegram-cloud`。

# CAVEATS

需要先通过 **tglogin** 使用来自 https://my.telegram.org 的 Telegram API id 和 hash 进行认证。是 **telegram-cloud** 软件包的一部分。只能编辑或删除你自己发的消息。

# SEE ALSO

[tgsend](/man/tgsend)(1), [tgcloud](/man/tgcloud)(1), [tginfo](/man/tginfo)(1)
