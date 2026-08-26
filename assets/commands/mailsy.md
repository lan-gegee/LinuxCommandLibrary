# TAGLINE

创建临时的一次性电子邮件

# TLDR

**生成临时邮箱**

```mailsy generate```

**检查收件箱**

```mailsy check```

**列出邮件**

```mailsy list```

**阅读邮件**

```mailsy read [message_id]```

**删除邮箱**

```mailsy delete```

**获取当前地址**

```mailsy me```

# SYNOPSIS

**mailsy** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的操作。

**generate**
> 创建新的临时邮箱。

**check**
> 检查新邮件。

**list**
> 列出所有邮件。

**read** _ID_
> 阅读指定邮件。

**delete**
> 删除邮箱地址。

**me**
> 显示当前地址。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mailsy** 用于创建临时的一次性电子邮件。它生成随机地址用于接收邮件。

该工具适用于注册和测试场景。地址会在一段时间后自动删除。

# CAVEATS

依赖外部服务。邮件会过期。不适用于生产环境。

# HISTORY

mailsy 提供了对**临时邮箱**服务的命令行访问，用于一次性地址。

# INSTALL

```brew: brew install mailsy```

```nix: nix profile install nixpkgs#mailsy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmpmail](/man/tmpmail)(1), [mail](/man/mail)(1)
