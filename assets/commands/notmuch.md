# TAGLINE

邮件索引与搜索工具

# TLDR

**初始设置**

```notmuch setup```

**为新邮件建立索引**

```notmuch new```

**搜索邮件**

```notmuch search [from:sender@example.com]```

**显示邮件**

```notmuch show [thread:id]```

**为邮件添加标签**

```notmuch tag +[important] [search-terms]```

**统计邮件数量**

```notmuch count [tag:inbox]```

**回复邮件**

```notmuch reply [thread:id]```

# SYNOPSIS

**notmuch** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> notmuch 子命令。

**setup**
> 初始配置。

**new**
> 为新邮件建立索引。

**search** _QUERY_
> 搜索邮件。

**show** _ID_
> 显示邮件。

**tag** _TAGS_ _QUERY_
> 修改标签。

**--help**
> 显示帮助信息。

# DESCRIPTION

**notmuch** 是一个邮件索引与搜索工具，提供快速的全文搜索。

该工具为 Maildir 邮件建立索引，可与多种邮件客户端配合使用。

# CAVEATS

仅支持 Maildir 格式。使用 Xapian 后端。有可用的前端客户端。

# HISTORY

notmuch 由 **Carl Worth** 创建，受 Gmail 搜索的启发，用于实现快速邮件搜索。

# INSTALL

```apt: sudo apt install notmuch```

```dnf: sudo dnf install notmuch```

```pacman: sudo pacman -S notmuch```

```apk: sudo apk add notmuch```

```zypper: sudo zypper install notmuch```

```brew: brew install notmuch```

```nix: nix profile install nixpkgs#notmuch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mu](/man/mu)(1), [mairix](/man/mairix)(1), [mutt](/man/mutt)(1)
