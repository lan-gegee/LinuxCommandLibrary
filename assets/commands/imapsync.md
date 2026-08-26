# TAGLINE

在服务器之间同步 IMAP 邮箱

# TLDR

**同步邮箱**

```imapsync --host1 [src] --user1 [user] --password1 [pass] --host2 [dst] --user2 [user] --password2 [pass]```

**试运行**

```imapsync --dry --host1 [src] --user1 [user] ...```

**排除文件夹**

```imapsync --exclude "Trash|Spam" --host1 [src] ...```

**SSL 连接**

```imapsync --ssl1 --ssl2 --host1 [src] ...```

**同步后删除源邮件**

```imapsync --delete1 --host1 [src] ...```

# SYNOPSIS

**imapsync** [_options_]

# PARAMETERS

**--host1** _HOST_
> 源 IMAP 服务器。

**--user1** _USER_
> 源用户名。

**--password1** _PASS_
> 源密码。

**--host2** _HOST_
> 目标服务器。

**--user2** _USER_
> 目标用户名。

**--dry**
> 试运行模式。

**--ssl1**, **--ssl2**
> 使用 SSL。

**--help**
> 显示帮助信息。

# DESCRIPTION

**imapsync** 在服务器之间同步 IMAP 邮箱。它将邮件、文件夹和标志从源复制到目标。

该工具可用于邮件迁移和备份。它支持增量同步、过滤以及多种身份验证方式。

# CAVEATS

邮箱较大时速度可能较慢。内存占用随数据量增长。另有商业版本可用。

# HISTORY

imapsync 由 **Gilles Lamiral** 创建，用于 IMAP 邮箱的迁移与同步。

# INSTALL

```dnf: sudo dnf install imapsync```

```pacman: sudo pacman -S imapsync```

```brew: brew install imapsync```

```nix: nix profile install nixpkgs#imapsync```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[offlineimap](/man/offlineimap)(1), [mbsync](/man/mbsync)(1), [fetchmail](/man/fetchmail)(1)
