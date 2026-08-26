# TAGLINE

基于文本的电子邮件客户端

# TLDR

**启动 Mutt**

```mutt```

**从命令行发送邮件**

```echo "[body]" | mutt -s "[subject]" [recipient@example.com]```

**发送带附件的邮件**

```mutt -s "[subject]" -a [file.pdf] -- [recipient@example.com]```

**打开特定邮箱**

```mutt -f [/path/to/mailbox]```

**发送带抄送的邮件**

```mutt -s "[subject]" -c [cc@example.com] [to@example.com]```

**使用备用配置文件**

```mutt -F [~/.muttrc.alt]```

# SYNOPSIS

**mutt** [_options_] [_address_]

# PARAMETERS

_ADDRESS_
> 邮件收件人地址。

**-s** _SUBJECT_
> 邮件主题。

**-a** _FILE_
> 附加文件。

**-c** _ADDRESS_
> 抄送地址。

**-f** _MAILBOX_
> 打开邮箱。

**-F** _FILE_
> 配置文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mutt** 是一款基于文本的电子邮件客户端。它高度可配置，并采用类似 Vim 的按键绑定。

该工具支持 IMAP、POP3 和本地邮件。具备会话线程、PGP 和 MIME 功能。

# CAVEATS

需要进行配置。按键绑定有一定学习曲线。纯文本界面。

# HISTORY

Mutt 由 **Michael Elstrøm** 于 1995 年创建，是 EstrøM 的分支，后来成为广受欢迎的终端邮件客户端。

# INSTALL

```apt: sudo apt install mutt```

```dnf: sudo dnf install mutt```

```pacman: sudo pacman -S mutt```

```apk: sudo apk add mutt```

```zypper: sudo zypper install mutt```

```brew: brew install mutt```

```nix: nix profile install nixpkgs#mutt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[neomutt](/man/neomutt)(1), [alpine](/man/alpine)(1), [mailx](/man/mailx)(1)
