# TAGLINE

按聊天和 ID 显示特定的 WhatsApp 消息

# TLDR

**查看某条消息**，指定聊天 JID 和消息 ID，以 JSON 格式输出

```wacli messages show --chat 491234567890@s.whatsapp.net --id ABC123 --json```

**使用自定义存储目录查看**

```wacli messages show --chat 491234567890@s.whatsapp.net --id ABC123 --json --store /path/to/store```

# SYNOPSIS

**wacli** **messages** **show** **--chat** _jid_ **--id** _msg_id_ [--json] [--store _dir_]

# DESCRIPTION

**wacli messages show** 根据聊天 JID 和消息 ID，从本地存储中获取并打印单条消息的完整记录。

当你已经拿到一个 ID（例如来自之前的搜索或列表）时，可用于查看详情、媒体引用或编写脚本。被删除但保留为本地墓碑记录的消息，即使已从列表/搜索中隐藏，仍可通过直接 `show` 查看。

默认存储路径在 Linux 上为 `~/.local/state/wacli`，其他平台为 `~/.wacli`。

# PARAMETERS

**--chat** _jid_
> 包含该消息的聊天 JID。

**--id** _msg_id_
> 该聊天内的消息标识符。

**--json**
> 以 JSON 格式输出（推荐用于后续处理）。

**--store** _dir_
> 使用备用存储位置（Linux 上默认为 `~/.local/state/wacli`，其他平台为 `~/.wacli`）。

# SEE ALSO

[wacli](/man/wacli)(1), [wacli-messages-list](/man/wacli-messages-list)(1), [wacli-messages-search](/man/wacli-messages-search)(1), [wacli-messages-context](/man/wacli-messages-context)(1)

# RESOURCES

```[Source code](https://github.com/openclaw/wacli)```

```[Documentation](https://wacli.sh/messages.html)```

<!-- verified: 2026-07-11 -->
