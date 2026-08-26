# TAGLINE

面向 Maildir 和 MH 邮箱的快速邮件索引与搜索工具

# TLDR

**为邮件文件夹建立索引**

```mairix```

**按主题搜索**

```mairix s:[search term]```

**按发件人搜索**

```mairix f:[sender@example.com]```

**按日期范围搜索**

```mairix d:[1w-]```

**组合搜索**

```mairix s:[report] f:[boss] d:[1m-]```

**搜索正文内容**

```mairix b:[keyword]```

# SYNOPSIS

**mairix** [_options_] [_search-terms_...]

# PARAMETERS

**-f** _config_
> 配置文件路径。

**-p**
> 清空结果文件夹。

**-F**
> 强制完整重建索引。

**-v**
> 详细输出。

**-Q**
> 快速模式（找到 100 个匹配即停止）。

**-t**
> 包含会话线程。

# DESCRIPTION

**mairix** 是一个面向 Maildir 和 MH 邮箱的快速邮件索引与搜索工具。它会创建索引数据库以实现快速搜索，并将匹配的邮件链接到结果文件夹。

搜索词使用前缀：s:（主题）、f:（发件人）、t:（收件人）、b:（正文）、d:（日期）。

# CONFIGURATION

```
# ~/.mairixrc
base=/home/user/mail
maildir=Maildir
mfolder=search
database=/home/user/.mairix_db
```

# DATE SYNTAX

```
d:1w-      # Last week
d:-2m      # Older than 2 months
d:1y-6m    # Between 1 year and 6 months ago
```

# CAVEATS

收到新邮件后必须更新索引。搜索结果是符号链接。仅支持 Maildir 和 MH 格式。数据库损坏时需要完整重建索引。

# HISTORY

mairix 由 **Richard Curnow** 创建，作为基于 grep 的邮件搜索的快速替代方案。

# INSTALL

```apt: sudo apt install mairix```

```dnf: sudo dnf install mairix```

```pacman: sudo pacman -S mairix```

```zypper: sudo zypper install mairix```

```brew: brew install mairix```

```nix: nix profile install nixpkgs#mairix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[notmuch](/man/notmuch)(1), [mu](/man/mu)(1), [mutt](/man/mutt)(1), [maildir](/man/maildir)(5)
