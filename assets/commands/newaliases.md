# TAGLINE

根据 /etc/aliases 重建别名数据库

# TLDR

**重建别名数据库**

```sudo newaliases```

**指定别名文件**

```sudo newaliases -oA[/etc/mail/aliases]```

# SYNOPSIS

**newaliases** [_options_]

# PARAMETERS

**-oA** _file_
> 指定别名文件。

**-v**
> 详细输出。

# DESCRIPTION

**newaliases** 从 /etc/aliases（或等效文件）重建别名数据库。邮件传输代理（MTA）使用该数据库来展开电子邮件别名。

编辑别名文件后必须运行此命令，更改才能生效。

# ALIASES FILE FORMAT

```
# /etc/aliases
postmaster: root
webmaster: admin@example.com
support: user1, user2, user3
noreply: /dev/null
archive: |/usr/bin/archive-mail
```

# WORKFLOW

```bash
# Edit aliases
sudo nano /etc/aliases

# Rebuild database
sudo newaliases

# Verify
sendmail -bv aliasname
```

# CAVEATS

取决于具体的 MTA（sendmail、postfix 等）。文件位置因系统而异。需要 root 权限。

# HISTORY

newaliases 自 sendmail 的早期就一直是 Unix 邮件系统的组成部分，sendmail 由加州大学伯克利分校于 **20 世纪 80 年代**开发。

# INSTALL

```apt: sudo apt install dma```

```dnf: sudo dnf install postfix```

```pacman: sudo pacman -S postfix```

```apk: sudo apk add postfix```

```zypper: sudo zypper install postfix```

```nix: nix profile install nixpkgs#dma```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sendmail](/man/sendmail)(8), [postfix](/man/postfix)(1)
