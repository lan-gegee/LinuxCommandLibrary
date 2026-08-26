# TAGLINE

Maildir 邮件索引与搜索工具

# TLDR

**初始化数据库**

```mu init --maildir=[~/Maildir]```

**索引邮件消息**

```mu index```

**搜索消息**

```mu find [from:john subject:report]```

**查看一条消息**

```mu view [path/to/message]```

**以特定输出格式搜索**

```mu find --format=links [query]```

**按日期范围搜索**

```mu find date:2024-01-01..2024-12-31```

**从消息中提取附件**

```mu extract [path/to/message]```

**从已索引的消息中搜索联系人**

```mu cfind [john]```

# SYNOPSIS

**mu** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> 要执行的操作。

**init**
> 初始化 mu 数据库。

**index**
> （重新）索引 Maildir 中的邮件消息。

**find** _QUERY_
> 在数据库中搜索消息。

**view** _FILE_
> 显示消息内容。

**extract** _FILE_
> 从消息中提取附件及其他 MIME 部分。

**cfind** [_QUERY_]
> 从已索引的消息中搜索联系人。

**add** _FILE_
> 将特定消息添加到数据库。

**remove** _FILE_
> 从数据库中移除特定消息。

**mkdir** _DIR_
> 创建新的 Maildir。

**info**
> 显示 mu 数据库的相关信息。

**--maildir** _PATH_
> Mail 目录的位置（默认：~/Maildir）。

**--format** _FORMAT_
> 输出格式（plain、links、xml、sexp、json）。

**--sortfield** _FIELD_
> 按字段排序（date、from、to、subject、size）。

**--reverse**
> 反转排序顺序。

**-d**, **--debug**
> 生成额外的调试信息。

**-q**, **--quiet**
> 抑制提示信息和进度输出。

**--nocolor**
> 禁用 ANSI 彩色输出。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**mu** 是面向 Maildir 格式邮箱的邮件索引与搜索工具。它借助 Xapian 搜索引擎对消息建立索引，实现快速全文搜索。查询支持 `from:`、`to:`、`subject:`、`date:`、`flag:`、`mime:` 等字段以及布尔运算符（`and`、`or`、`not`）。

该工具是 Emacs 邮件客户端 **mu4e** 的后端，但作为独立命令行工具也完全可用。

# CAVEATS

仅支持 Maildir 格式。需要 Xapian 库。Maildir 发生更改后必须重新建立索引（运行 `mu index`）。查询语法在主要版本之间有变化（1.0 前与 1.0 后）。

# HISTORY

**mu** 由 **Dirk-Jan C. Binnema** 创建，是一款快速邮件搜索工具，也是 **mu4e** Emacs 邮件客户端的后端。它的设计定位是 notmuch 的轻量级替代品，注重简洁和速度。

# INSTALL

```apt: sudo apt install maildir-utils```

```dnf: sudo dnf install maildir-utils```

```apk: sudo apk add mu```

```zypper: sudo zypper install maildir-utils```

```brew: brew install mu```

```nix: nix profile install nixpkgs#mu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[notmuch](/man/notmuch)(1), [mairix](/man/mairix)(1), [mutt](/man/mutt)(1), [neomutt](/man/neomutt)(1)
