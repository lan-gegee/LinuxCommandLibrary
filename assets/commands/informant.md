# TAGLINE

Arch Linux 新闻阅读器和 pacman 钩子

# TLDR

**检查**是否有未读新闻

```informant check```

**交互式阅读**所有未读新闻

```sudo informant read```

**将所有新闻标记为已读**但不打印

```sudo informant read --all```

**列出**最新的新闻标题

```informant list```

**只列出未读的**新闻条目

```informant list --unread```

**以倒序列出新闻**（最新在前）

```informant list --reverse```

# SYNOPSIS

**informant** [_options_] _command_

# PARAMETERS

**check**
> 检查是否有未读新闻（退出码等于未读条数）。当只有一条未读时打印并将其标记为已读。

**read**
> 循环遍历未读条目，逐条打印并提示是否继续。可通过索引或标题匹配指定某个条目。

**read --all**
> 将所有条目标记为已读而不打印。

**list**
> 列出最近的新闻标题（含已读与未读）。

**--unread**
> 只显示未读条目（配合 `list`）。

**--reverse**
> 最新条目优先显示（配合 `list`）。

**-n**, **--count** _NUM_
> 要显示的条目数量。

**-h**, **--help**
> 显示帮助消息。

# DESCRIPTION

**informant** 是一个用于阅读 archlinux.org 网站上 Arch Linux 新闻的工具。它帮助用户及时了解重要的软件包更新、需要手动干预的事项以及系统变更。

该工具可与 pacman 钩子集成：存在未读新闻时阻止更新，确保用户在执行系统更新前先查看重要公告。

# CAVEATS

仅适用于 Arch Linux。获取新闻需要网络访问。某些操作需要 root 权限，以便在系统级缓存中将新闻标记为已读。

# HISTORY

informant 的诞生是为了解决 Arch Linux 的一个常见问题：用户在不阅读重要新闻公告的情况下更新系统，而这些公告可能要求手动干预。它可以在用户确认新闻之前阻止 pacman 更新。

# INSTALL

```aur: yay -S informant```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [yay](/man/yay)(8), [paru](/man/paru)(8)
