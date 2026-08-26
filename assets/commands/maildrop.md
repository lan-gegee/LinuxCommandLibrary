# TAGLINE

带过滤功能的邮件投递代理

# TLDR

**使用过滤器处理邮件**

```maildrop [filter.rc]```

**投递邮件**

```maildrop < [message.eml]```

**测试过滤器**

```maildrop -V [9] [filter.rc] < [message.eml]```

**使用指定的 maildir**

```maildrop -d [user] [filter.rc]```

**显示版本**

```maildrop -v```

# SYNOPSIS

**maildrop** [_options_] [_filterfile_]

# PARAMETERS

_FILTERFILE_
> 邮件过滤规则文件。

**-d** _USER_
> 以指定用户身份投递。

**-V** _LEVEL_
> 详细级别。

**-v**
> 显示版本。

**-f** _ADDRESS_
> 发件人地址。

**--help**
> 显示帮助信息。

# DESCRIPTION

**maildrop** 是一个带过滤功能的邮件投递代理。它使用规则对收到的邮件进行分类排序。

该工具可将邮件投递到 maildir 或 mbox。过滤规则支持条件和动作。

# CAVEATS

需要配置过滤规则。属于 courier-maildrop 项目。推荐使用 Maildir 格式。

# HISTORY

maildrop 是 **Courier Mail Server** 项目的一部分，提供灵活的邮件过滤和投递功能。

# INSTALL

```apt: sudo apt install maildrop```

```dnf: sudo dnf install maildrop```

```nix: nix profile install nixpkgs#maildrop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[procmail](/man/procmail)(1), [dovecot](/man/dovecot)(1), [postfix](/man/postfix)(1)
