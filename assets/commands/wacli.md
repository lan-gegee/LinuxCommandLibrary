# TAGLINE

用于本地同步、搜索和收发消息的 WhatsApp 命令行工具

# TLDR

**扫描**主设备上的二维码**完成认证**

```wacli auth```

**搜索**已同步的消息历史中的关键词

```wacli messages search "[keyword]"```

**向联系人发送文本消息**

```wacli send text --to [phone_number] --message "[message]"```

**发送文件**并附上说明文字

```wacli send file --to [phone_number] --file [path/to/file] --caption "[caption]"```

**列出**所有聊天

```wacli chats list```

在后台**运行持续同步**循环

```wacli sync --follow```

向主设备**请求更早的消息**

```wacli history backfill --chat [chat_jid] --count [50]```

# SYNOPSIS

**wacli** \<command\> [options]

# PARAMETERS

**auth**
> 通过二维码交互式登录并执行初始数据同步

**sync**
> 非交互式同步循环；需要事先完成认证

**sync --follow**
> 持续不断地同步

**messages search** _query_
> 使用 FTS5 全文搜索已同步的消息

**messages list** [_--chat jid_] [_--limit n_]
> 列出消息，可按聊天过滤

**history backfill** **--chat** _jid_ [_--count n_] [_--requests n_]
> 从主设备获取更早的消息

**media download** **--chat** _jid_ **--id** _msg_id_
> 下载特定消息的媒体文件

**send text** **--to** _recipient_ **--message** _text_
> 向联系人或群组发送文本消息

**send file** **--to** _recipient_ **--file** _path_ [_--caption text_] [_--filename name_]
> 发送文件，可选附上说明文字并覆盖显示名称

**chats list**
> 列出所有聊天

**groups list**
> 列出所有群组

**groups rename** **--jid** _group_jid_ **--name** _new_name_
> 重命名群组

**doctor**
> 对本地存储运行诊断

**--store** _DIR_
> 覆盖默认存储目录（默认：~/.wacli）

**--json**
> 输出机器可读的 JSON 格式

# DESCRIPTION

**wacli** 是一个基于 **whatsmeow** 库构建的 WhatsApp 命令行界面。它提供尽力而为的消息历史本地同步、快速的离线全文搜索、消息发送以及联系人和群组管理，全部都可以在终端中完成。

认证时需用你的 WhatsApp 主设备扫描终端中显示的二维码。认证完成后，wacli 默认将会话数据、消息、联系人和媒体引用存储在本地 SQLite 数据库 **~/.wacli** 中。sync 命令持续捕获传入的消息，而 history backfill 则按需向主设备请求更早的消息。

搜索使用 SQLite FTS5 进行快速全文查询，并以 LIKE 作为回退，返回带上下文摘录的结果。所有输出默认为人类可读格式，同时提供 **--json** 选项以便脚本化和自动化。

# CAVEATS

wacli 是一个通过 whatsmeow 使用 WhatsApp Web 协议的**第三方工具**，与 WhatsApp **无任何关联**。WhatsApp 会主动封禁使用第三方客户端的账号，且封禁通常是永久性的，没有申诉渠道。历史回填是尽力而为的，且要求主设备在线。媒体下载取决于 WhatsApp 的内容保留策略。

# HISTORY

wacli 由 **Peter Steinberger**（steipete）创建，使用 **Go** 编写。该项目于 **2025 年**首次发布，专注于为 WhatsApp 提供原生的终端体验，实现官方 WhatsApp 客户端不具备的本地消息同步和离线搜索能力。

# INSTALL

```aur: yay -S wacli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[neomutt](/man/neomutt)(1)
