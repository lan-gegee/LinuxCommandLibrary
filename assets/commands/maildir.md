# TAGLINE

一种邮件存储格式，每封电子邮件以独立文件存储在

# TLDR

**创建 Maildir 结构**

```mkdir -p [~/Maildir]/{cur,new,tmp}```

**列出新邮件**

```ls [~/Maildir/new/]```

**将邮件移为已读**

```mv [~/Maildir/new/message] [~/Maildir/cur/]```

**检查 Maildir 权限**

```ls -la [~/Maildir/]```

# SYNOPSIS

**Maildir/** - 基于目录的电子邮件存储格式

# DESCRIPTION

**Maildir** 是一种邮件存储格式，每封电子邮件都以独立文件存储在目录结构中。它由三个子目录组成：cur（已读）、new（未读）和 tmp（正在投递）。

Maildir 避免了 mbox 格式的文件锁定问题，并允许多个程序并发访问。

# DIRECTORY STRUCTURE

```
Maildir/
├── cur/     # Read messages
├── new/     # Unread messages
├── tmp/     # Temporary (delivery)
└── .Folder/ # Subfolders (ISTRSTRSTRSTRSTRSTRSTRSTRSTRSTRSTR
    ├── cur/
    ├── new/
    └── tmp/
```

# FILE NAMING

```
# Format: time.pid.hostname:2,flags
1234567890.12345.hostname:2,S

Flags: S=Seen, R=Replied, F=Flagged, T=Trashed, D=Draft
```

# CAVEATS

比 mbox 产生更多文件。文件系统必须支持大量小文件。某些工具要求特定的命名方式。子文件夹以点号作为前缀。

# HISTORY

Maildir 由 **Daniel J. Bernstein** 于 **1995 年**为其 **qmail** MTA 开发，作为传统 mbox 格式的可靠替代方案。

# SEE ALSO

[mutt](/man/mutt)(1), [dovecot](/man/dovecot)(1), [offlineimap](/man/offlineimap)(1)
