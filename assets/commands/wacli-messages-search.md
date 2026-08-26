# TAGLINE

使用全文搜索查找 WhatsApp 消息历史

# TLDR

**搜索所有消息**中的关键词

```wacli messages search "meeting notes" --json```

**在特定聊天内搜索**

```wacli messages search "project" --chat 491234567890@s.whatsapp.net --json```

**搜索某位发送者的消息**

```wacli messages search "report" --from 491234567890@s.whatsapp.net --json```

**按消息类型搜索**（图片、视频等）

```wacli messages search "" --type image --json```

**搜索带媒体附件的文档**

```wacli messages search "invoice" --has-media --type document --json```

**限制数量并按日期过滤**

```wacli messages search "budget" --chat 491234567890@s.whatsapp.net --after 2026-01-01 --limit 5 --json```

# SYNOPSIS

**wacli** **messages** **search** _query_ [--chat _jid_] [--from _jid_] [--has-media] [--type _type_] [--forwarded] [--starred] [--limit _n_] [--after _date_] [--before _date_] [--json] [--store _dir_]

# DESCRIPTION

**wacli messages search** 对本地已同步的消息正文执行全文搜索。如果二进制文件以 `-tags sqlite_fts5` 构建，则使用 SQLite FTS5，否则回退到 `LIKE`。可选过滤器涵盖聊天、发送者、日期范围、媒体、类型以及加星标/转发标志。

存储同步完成后，搜索即可完全离线进行。状态广播不包含在内。

默认存储路径在 Linux 上为 `~/.local/state/wacli`，其他平台为 `~/.wacli`。

# PARAMETERS

_query_
> 搜索词。支持简单的词条；短语需根据 shell 要求加引号。

**--chat** _jid_
> 将搜索范围限定在一个聊天内。

**--from** _jid_
> 仅限此发送者发出的消息。

**--has-media**
> 只显示包含媒体的消息。

**--type** _type_
> 按内容类型过滤：`text`、`image`、`video`、`audio` 或 `document`。

**--forwarded**
> 只显示被转发的消息。

**--starred**
> 只显示加星标的消息。

**--after**, **--before** _date_
> 日期过滤（RFC3339 或 `YYYY-MM-DD` 格式）。

**--limit** _n_
> 结果的最大数量。

**--json**
> 以 JSON 格式输出。

**--store** _dir_
> 覆盖存储目录（不能与 `--account` 同时使用）。

# CAVEATS

搜索只覆盖已同步到本地存储的消息。历史记录尽力而为；较旧的消息请使用 `wacli history backfill` 获取。

# SEE ALSO

[wacli](/man/wacli)(1), [wacli-messages-list](/man/wacli-messages-list)(1), [wacli-messages-show](/man/wacli-messages-show)(1), [wacli-messages-context](/man/wacli-messages-context)(1)

# RESOURCES

```[Source code](https://github.com/openclaw/wacli)```

```[Documentation](https://wacli.sh/messages.html)```

<!-- verified: 2026-07-11 -->
