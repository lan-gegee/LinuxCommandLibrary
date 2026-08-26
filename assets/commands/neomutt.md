# TAGLINE

基于 Mutt 的终端邮件客户端

# TLDR

**启动 NeoMutt**

```neomutt```

**打开指定的邮箱**

```neomutt -f [/path/to/mailbox]```

**发送邮件**

```echo "[body]" | neomutt -s "[subject]" [recipient@example.com]```

**带附件发送**（必须是地址前的最后一个选项）

```neomutt -s "[subject]" -a [file.pdf] -- [recipient@example.com]```

**使用其他配置文件**

```neomutt -F [~/.neomuttrc]```

**打开第一个有新邮件的邮箱**，若没有则退出

```neomutt -Z```

**以只读模式打开邮箱**

```neomutt -R -f [/path/to/mailbox]```

# SYNOPSIS

**neomutt** [_options_] [_address_ ...]

# PARAMETERS

**-a** _FILE_
> 为邮件附加一个或多个文件。必须放在 **--** 和收件人地址之前，作为最后一个选项。

**-b** _ADDRESS_
> 指定密送（BCC）收件人。

**-c** _ADDRESS_
> 指定抄送（CC）收件人。

**-d** _LEVEL_
> 以指定级别（1-5）记录调试输出；推荐级别 2。

**-e** _COMMAND_
> 在读取配置文件后执行一条配置命令。

**-f** _MAILBOX_
> 打开指定的邮箱。

**-F** _FILE_
> 使用指定文件代替默认配置文件。

**-H** _DRAFT_
> 使用包含邮件头和正文的草稿文件来撰写邮件。

**-i** _FILE_
> 指定要嵌入邮件正文的文件。

**-l** _FILE_
> 将调试输出写入此文件而非默认位置。

**-m** _TYPE_
> 设置默认邮箱格式（mbox、MMDF、MH 或 Maildir）。

**-n**
> 不读取系统级配置文件。

**-p**
> 继续处理之前暂缓发送的邮件。

**-Q** _VARIABLE_
> 查询配置变量并打印其值，然后退出。

**-R**
> 以只读模式打开邮箱。

**-s** _SUBJECT_
> 指定邮件主题。

**-v**
> 打印版本和编译时定义，然后退出。

**-y**
> 启动时列出所有已定义的邮箱。

**-Z**
> 打开第一个有新邮件的邮箱；若没有则以退出码 1 退出。

**-z**
> 仅当指定的或第一个邮箱中有邮件时才打开，否则退出。

# DESCRIPTION

**neomutt** 是一个小而强大的终端邮件客户端，支持彩色终端、MIME、OpenPGP/GnuPG、S/MIME 以及按线索排序消息。它是 Mutt 的社区驱动分支，整合了长期积累的补丁并加入新特性。

支持的协议包括 IMAP、POP3、SMTP、NNTP 以及本地邮箱格式（mbox、Maildir、MH、MMDF）。NeoMutt 通过 `~/.neomuttrc` 高度可配置，默认使用类似 Vim 的按键绑定。

# CAVEATS

初次配置需要在 `~/.neomuttrc` 中设置账户、文件夹和按键绑定。发信必须配置 SMTP 服务器或本地 MTA。**-a** 标志必须出现在 **--** 和收件人地址之前，作为最后一个选项。

# HISTORY

**NeoMutt** 于 2016 年由 Richard Russon 从 **Mutt** 分支而来，目的是整合社区补丁，并不受 Mutt 开发节奏限制地添加新功能。

# INSTALL

```apt: sudo apt install neomutt```

```dnf: sudo dnf install neomutt```

```pacman: sudo pacman -S neomutt```

```apk: sudo apk add neomutt```

```zypper: sudo zypper install neomutt```

```brew: brew install neomutt```

```nix: nix profile install nixpkgs#neomutt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mutt](/man/mutt)(1), [alpine](/man/alpine)(1), [mailx](/man/mailx)(1), [mail](/man/mail)(1), [mbsync](/man/mbsync)(1)
