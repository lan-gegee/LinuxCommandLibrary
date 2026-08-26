# TAGLINE

管理电子邮件的 CLI

# TLDR

**列出收件箱中的邮件信封**

```himalaya envelope list```

**阅读特定邮件**

```himalaya message read [id]```

**撰写并发送新邮件**

```himalaya message write```

**回复邮件**

```himalaya message reply [id]```

**转发邮件**

```himalaya message forward [id]```

**列出文件夹**

```himalaya folder list```

**下载附件**

```himalaya attachment download [id]```

**使用指定账户**

```himalaya -a [account_name] envelope list```

# SYNOPSIS

**himalaya** [_options_] _command_ _subcommand_ [_arguments_]

# DESCRIPTION

**himalaya** 是一个用于管理电子邮件的命令行界面。与 **mutt** 或 **aerc** 这类 TUI 邮件客户端不同，himalaya 是一个没有事件循环的纯 CLI——你以无状态的方式用 shell 命令操作邮件。这使它可以与管道和脚本组合，并自由地与其他 CLI 工具集成。

它支持多种后端，包括 **IMAP**、**SMTP**、**Maildir** 和 **Notmuch**，具备多账户支持、**PGP 加密**和 **OAuth 2.0** 身份验证等特性。Himalaya 的设计理念是将邮件逻辑提取为一个简单的 CLI API，可以直接从终端、脚本和 UI 中使用。

# PARAMETERS

**-a**, **--account** _name_
> 使用指定的电子邮件账户。

**envelope list**
> 列出当前文件夹中的邮件信封。

**envelope watch**
> 实时监视新信封的变化。

**message read** _id_
> 阅读特定的邮件。

**message write**
> 撰写新邮件。

**message reply** _id_
> 回复某封邮件。

**message forward** _id_
> 转发某封邮件。

**message delete** _id_
> 删除某封邮件。

**folder list**
> 列出邮件文件夹。

**folder create** _name_
> 创建新的邮件文件夹。

**attachment download** _id_
> 从邮件中下载附件。

# CONFIGURATION

配置保存在 **$XDG_CONFIG_HOME/himalaya/config.toml**（或 **~/.config/himalaya/config.toml**）中，其中定义了各个账户及其 IMAP、SMTP、Maildir 或 Notmuch 后端设置。运行 **himalaya account configure** 可启动交互式设置向导。

# CAVEATS

初始配置需要手动设置邮件账户。OAuth 2.0 的设置可能因提供商而需要额外步骤。PGP 加密需要安装并配置 GPG。

# HISTORY

**himalaya** 由 **Clément DOUIN** 创建，是 **Pimalaya** 项目的一部分，使用 **Rust** 编写。其设计遵循 Unix 哲学处理邮件：提供简单可组合的命令，而不是一个庞大的 TUI 应用。

# INSTALL

```pacman: sudo pacman -S himalaya```

```apk: sudo apk add himalaya```

```zypper: sudo zypper install himalaya```

```brew: brew install himalaya```

```nix: nix profile install nixpkgs#himalaya```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mutt](/man/mutt)(1), [aerc](/man/aerc)(1), [neomutt](/man/neomutt)(1), [mail](/man/mail)(1)
