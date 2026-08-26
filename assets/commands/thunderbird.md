# TAGLINE

Mozilla 邮件与日历客户端

# TLDR

**启动 Thunderbird**

```thunderbird```

**撰写新邮件**

```thunderbird -compose "[to='email@example.com',subject='Hello']"```

**打开配置文件管理器**

```thunderbird -ProfileManager```

**使用指定配置文件**

```thunderbird -P [profile-name]```

**安全模式**

```thunderbird -safe-mode```

**检查新邮件**

```thunderbird -mail```

**打开通讯录**

```thunderbird -addressbook```

# SYNOPSIS

**thunderbird** [_-compose opts_] [_-P profile_] [_options_]

# PARAMETERS

**-compose** _OPTS_
> 撰写新邮件。选项包括 to、cc、bcc、subject、body、attachment，以逗号分隔的 key=value 键值对形式传入。

**-P** _NAME_
> 以指定的配置文件启动。

**-ProfileManager**
> 打开配置文件管理器，用于创建或选择配置文件。

**-safe-mode**
> 以安全模式启动，禁用所有扩展，用于故障排查。

**-mail**
> 打开邮件客户端并检查新消息。

**-addressbook**
> 打开通讯录。

**-no-remote**
> 不接受或不发送远程命令；启动一个新实例。

**-search**
> 打开全局搜索标签页。

# DESCRIPTION

**thunderbird** 是 Mozilla 的免费开源电子邮件客户端，支持多邮箱账户、日历集成、通讯录、RSS 订阅阅读以及内置 OpenPGP 加密的安全通信。

该应用支持 IMAP、POP3 和 SMTP 协议，可通过附加组件扩展更多功能。它使用配置文件（profile）存储设置和数据，可通过 **-ProfileManager** 标志管理，还可以用 **-safe-mode** 启动以排查扩展相关的问题。

# CAVEATS

桌面应用程序。基于配置文件（profile）存储。账户较多或邮箱较大时内存占用可能偏高。

# HISTORY

**Thunderbird** 最初由 **Mozilla Foundation** 开发，作为 Firefox 的姊妹项目。自 2020 年起由子公司 **MZLA Technologies** 维护。在 115 版（2023 年）大幅刷新界面后更名为 **Thunderbird Supernova**。

# INSTALL

```apt: sudo apt install thunderbird```

```dnf: sudo dnf install thunderbird```

```pacman: sudo pacman -S thunderbird```

```apk: sudo apk add thunderbird```

```nix: nix profile install nixpkgs#thunderbird```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mutt](/man/mutt)(1), [evolution](/man/evolution)(1), [firefox](/man/firefox)(1), [neomutt](/man/neomutt)(1)
