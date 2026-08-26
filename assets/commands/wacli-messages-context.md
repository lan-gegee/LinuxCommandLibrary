# TAGLINE

显示某条 WhatsApp 消息周围的消息（上下文）

# TLDR

**查看某条消息的周围上下文**

```wacli messages context --chat 491234567890@s.whatsapp.net --id ABC123 --json```

**控制前后各取多少条消息**

```wacli messages context --chat 491234567890@s.whatsapp.net --id ABC123 --before 3 --after 3 --json```

**使用其他存储路径**

```wacli messages context --chat 491234567890@s.whatsapp.net --id ABC123 --json --store ~/.wacli-work```

# SYNOPSIS

**wacli** **messages** **context** **--chat** _jid_ **--id** _msg_id_ [--before _n_] [--after _n_] [--json] [--store _dir_]

# DESCRIPTION

**wacli messages context** 返回目标消息以及同一聊天中紧邻其前后的若干条消息。这有助于理解某条特定消息前后的对话脉络。

默认存储路径在 Linux 上为 `~/.local/state/wacli`，其他平台为 `~/.wacli`。

# PARAMETERS

**--chat** _jid_
> 包含该消息的聊天 JID。

**--id** _msg_id_
> 中心消息的 ID。

**--before** _n_
> 要包含的前置消息数量。

**--after** _n_
> 要包含的后继消息数量。

**--json**
> 以 JSON 格式输出。

**--store** _dir_
> 备用存储路径（Linux 上默认为 `~/.local/state/wacli`，其他平台为 `~/.wacli`）。

# SEE ALSO

[wacli](/man/wacli)(1), [wacli-messages-show](/man/wacli-messages-show)(1), [wacli-messages-list](/man/wacli-messages-list)(1), [wacli-messages-search](/man/wacli-messages-search)(1)

# RESOURCES

```[Source code](https://github.com/openclaw/wacli)```

```[Documentation](https://wacli.sh/messages.html)```

<!-- verified: 2026-07-11 -->
