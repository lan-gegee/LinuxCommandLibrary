# TAGLINE

将 IMAP 邮箱与本地 Maildir 文件夹同步

# TLDR

**同步所有通道**

```mbsync -a```

**同步指定通道**

```mbsync [channel]```

**同步指定组**

```mbsync [group]```

**详细模式同步**

```mbsync -V [channel]```

**试运行**

```mbsync -n [channel]```

**创建缺失的邮箱**

```mbsync -C [channel]```

# SYNOPSIS

**mbsync** [_options_] _channel_|_group_...

# PARAMETERS

**-a**, **--all**
> 同步所有通道。

**-l**, **--list**
> 列出远程邮箱。

**-C**, **--create**
> 创建缺失的邮箱。

**-n**, **--dry-run**
> 显示将要执行的操作。

**-V**, **--verbose**
> 详细输出。

**-D**, **--debug**
> 调试输出。

**-c** _file_
> 配置文件。

# DESCRIPTION

**mbsync**（isync 的一部分）将 IMAP 邮箱与本地 Maildir 文件夹同步。它提供双向同步，并能细粒度控制同步内容，支持按邮箱进行状态跟踪以实现可靠的可恢复传输。

mbsync 通常与 mu、notmuch 或其他本地邮件工具配合使用，实现离线邮件访问。

# CONFIGURATION

```
# ~/.mbsyncrc
IMAPAccount gmail
Host imap.gmail.com
User user@gmail.com
PassCmd "gpg -q --decrypt ~/.gmail-pass.gpg"
SSLType IMAPS

IMAPStore gmail-remote
Account gmail

MaildirStore gmail-local
Path ~/mail/gmail/
Inbox ~/mail/gmail/Inbox

Channel gmail
Far :gmail-remote:
Near :gmail-local:
Patterns *
Create Both
```

# CAVEATS

需要配置文件。在一侧删除会传播到另一侧。受 IMAP 配额限制。初始同步可能较慢。

# HISTORY

mbsync 由 **Oswald Buddenhagen** 开发，是 isync 的一部分，后者是一个自由的 IMAP4 同步实现，提供可靠的双向同步。

# INSTALL

```apt: sudo apt install isync```

```dnf: sudo dnf install isync```

```pacman: sudo pacman -S isync```

```apk: sudo apk add isync```

```zypper: sudo zypper install isync```

```brew: brew install isync```

```nix: nix profile install nixpkgs#isync```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[offlineimap](/man/offlineimap)(1), [mu](/man/mu)(1), [notmuch](/man/notmuch)(1), [mutt](/man/mutt)(1)
