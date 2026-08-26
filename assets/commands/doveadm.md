# TAGLINE

Dovecot 邮件服务器管理工具

# TLDR

**显示邮箱状态**

```doveadm mailbox status -u [user@example.com] all '*'```

**列出用户邮箱**

```doveadm mailbox list -u [user@example.com]```

**搜索邮件**

```doveadm search -u [user@example.com] mailbox INBOX subject "[test]"```

**清除已删除的邮件**

```doveadm expunge -u [user@example.com] mailbox Trash all```

**强制用户重建索引**

```doveadm index -u [user@example.com] INBOX```

**显示用户配额**

```doveadm quota get -u [user@example.com]```

**同步邮箱**

```doveadm sync -u [user@example.com] [remote_host]```

# SYNOPSIS

**doveadm** [_options_] _command_ [_args_]

# DESCRIPTION

**doveadm** 是 Dovecot IMAP/POP3 服务器的管理工具。它提供管理邮箱、用户和服务器操作的命令，无需直接操作邮件存储。

该工具负责邮箱维护、邮件搜索与操作、配额管理和复制控制等任务。

# PARAMETERS

**-u** _user_
> 操作的目标用户。

**-A**
> 应用于所有用户。

**-D**
> 启用调试输出。

**-v**
> 详细输出。

**-f** _format_
> 输出格式（flow、pager、tab、table）。

**-o** _setting=value_
> 覆盖配置项。

# COMMANDS

**mailbox list/status/create/delete/rename**：邮箱管理
**search**：查找邮件
**fetch**：获取邮件数据
**expunge**：删除邮件
**index**：为邮箱重建索引
**quota**：配额操作
**sync**：Dsync 复制
**user**：用户信息

# CONFIGURATION

**/etc/dovecot/dovecot.conf**
> Dovecot 主配置文件，控制邮件存储、身份验证和协议。

# CAVEATS

需要正确的 Dovecot 配置。某些命令需要 root 或 dovecot 用户权限。对大型邮箱的操作可能较慢。用户必须存在于 Dovecot 的用户数据库中。

# HISTORY

**doveadm** 于 **2010 年**前后随 **Dovecot 2.0** 推出，取代了较早的管理脚本。**Dovecot** 本身由 **Timo Sirainen** 于 **2002 年**创建，是一个安全、高性能的 IMAP 服务器。Doveadm 将各种管理任务统一到单一一致的接口之下。

# INSTALL

```apt: sudo apt install dovecot-core```

```dnf: sudo dnf install dovecot```

```pacman: sudo pacman -S dovecot```

```apk: sudo apk add dovecot```

```zypper: sudo zypper install dovecot```

```brew: brew install dovecot```

```nix: nix profile install nixpkgs#dovecot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dovecot](/man/dovecot)(1), [postfix](/man/postfix)(1), [mutt](/man/mutt)(1)
