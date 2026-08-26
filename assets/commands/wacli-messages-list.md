# TAGLINE

列出某个 WhatsApp 聊天中的消息

# TLDR

**列出特定聊天的消息**，以 JSON 格式输出

```wacli messages list --chat 491234567890@s.whatsapp.net --json```

**列出某日期之后收到的消息**

```wacli messages list --chat 491234567890@s.whatsapp.net --after 2026-01-01 --json```

**限制结果数量**并按从旧到新排列

```wacli messages list --chat 491234567890@s.whatsapp.net --limit 20 --asc --json```

**只列出你发送的消息**

```wacli messages list --from-me --limit 20 --json```

**列出某个日期范围内的消息**

```wacli messages list --chat 491234567890@s.whatsapp.net --after 2026-01-01 --before 2026-01-31 --json```

# SYNOPSIS

**wacli** **messages** **list** [--chat _jid_] [--sender _jid_] [--from-me|--from-them] [--asc] [--limit _n_] [--after _date_] [--before _date_] [--forwarded] [--starred] [--json] [--store _dir_]

# DESCRIPTION

**wacli messages list** 从本地 SQLite 存储中检索消息，可按单个聊天（JID）、发送者、方向、标志和/或时间范围进行过滤。默认输出为人类可读格式；如需供机器处理，请使用 `--json`。

WhatsApp 状态广播单独存储，不会由 `messages list` 返回。

本地存储由 `wacli sync`（或 `sync --follow`）填充。默认存储路径在 Linux 上为 `~/.local/state/wacli`，其他平台为 `~/.wacli`（Linux 上已有的 `~/.wacli` 仍可继续使用）。

# PARAMETERS

**--chat** _jid_
> 仅限此聊天 JID 中的消息（例如 `491234567890@s.whatsapp.net` 或群组 JID）。

**--sender** _jid_
> 仅限此发送者 JID 发出的消息。

**--from-me**, **--from-them**
> 只显示你发送的消息，或只显示他人发来的消息。

**--asc**
> 按升序排序（从旧到新）。默认顺序为从新到旧。

**--after** _date_
> 只显示此时间及之后的消息（RFC3339 或 `YYYY-MM-DD` 格式）。

**--before** _date_
> 只显示此时间之前的消息（RFC3339 或 `YYYY-MM-DD` 格式）。

**--limit** _n_
> 返回消息的最大数量。

**--forwarded**
> 只显示被转发的消息。

**--starred**
> 只显示加星标的消息。

**--json**
> 输出 JSON 而非人类可读的表格。

**--store** _dir_
> 覆盖存储目录（不能与 `--account` 同时使用）。

# SEE ALSO

[wacli](/man/wacli)(1), [wacli-messages-search](/man/wacli-messages-search)(1), [wacli-messages-show](/man/wacli-messages-show)(1), [wacli-messages-context](/man/wacli-messages-context)(1)

# RESOURCES

```[Source code](https://github.com/openclaw/wacli)```

```[Documentation](https://wacli.sh/messages.html)```

<!-- verified: 2026-07-11 -->
