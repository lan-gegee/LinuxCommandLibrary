# TAGLINE

管理 Postfix 邮件队列

# TLDR

**列出邮件队列**

```postqueue -p```

**清空邮件队列**

```postqueue -f```

**清空特定站点**

```postqueue -s [example.com]```

**安排立即投递特定邮件**

```postqueue -i [queue_id]```

**以 JSON 格式列出**

```postqueue -j```

# SYNOPSIS

**postqueue** [_options_]

# PARAMETERS

**-p**
> 打印队列内容。

**-f**
> 清空队列（重试投递）。

**-s** _site_
> 清空特定站点。

**-i** _queue_id_
> 安排立即投递具有指定队列 ID 的延迟邮件。

**-j**
> 以 JSON 格式输出队列列表。

**-v**
> 启用详细日志以便调试。多个 -v 选项会提高详细程度。

**-c** _dir_
> 使用指定的配置目录代替默认目录。

# DESCRIPTION

**postqueue** 管理 Postfix 邮件队列，让普通用户无需 root 权限即可安全地进行队列操作。它会显示队列中消息的 ID、大小、到达时间、发件人和收件人，并可触发投递重试。

flush 选项会强制对所有延迟邮件或特定目标站点立即尝试投递。JSON 输出模式使队列数据便于监控脚本解析。要执行删除或暂扣单条消息等高级队列管理操作，则需要使用有特权的 **postsuper** 命令。

# EXAMPLES

```bash
# View queue
postqueue -p

# Flush all queued mail
postqueue -f

# Retry specific domain
postqueue -s gmail.com

# JSON output for scripting
postqueue -j

# Retry delivery of a specific message
postqueue -i ABC123DEF

# Count queued messages
postqueue -p | tail -1
```

# QUEUE OUTPUT

```
-Queue ID-  --Size-- ----Arrival Time---- -Sender/Recipient-------
ABC123DEF     1234 Mon Jan 01 12:00:00  sender@example.com
                                         recipient@dest.com
```

# QUEUE LOCATIONS

```
/var/spool/postfix/incoming  - New mail
/var/spool/postfix/active    - Being delivered
/var/spool/postfix/deferred  - Temporary failures
/var/spool/postfix/hold      - Manually held
```

# CAVEATS

对于永久性失败，清空队列可能无济于事。高级队列管理请使用 postsuper。

# HISTORY

postqueue 是 **Wietse Venema** 的 **Postfix** 的组成部分，为无特权用户提供安全的队列管理。

# INSTALL

```apt: sudo apt install postfix```

```dnf: sudo dnf install postfix```

```pacman: sudo pacman -S postfix```

```apk: sudo apk add postfix```

```zypper: sudo zypper install postfix```

```nix: nix profile install nixpkgs#postfix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mailq](/man/mailq)(1), [postfix](/man/postfix)(1), [postconf](/man/postconf)(1), [postmap](/man/postmap)(1), [sendmail](/man/sendmail)(1)
