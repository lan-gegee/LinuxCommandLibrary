# TAGLINE

向系统日志添加条目

# TLDR

记录一条**消息**

```logger [message]```

从 **stdin** 记录

```echo [message] | logger```

记录到**远程服务器**

```echo [message] | logger -n [hostname] -P [port]```

使用**自定义标签**记录

```echo [message] | logger -t [tag]```

带**优先级**记录

```echo [message] | logger -p user.warning```

# SYNOPSIS

**logger** [_options_] [_message_]

# DESCRIPTION

**logger** 向系统日志（syslog）添加条目。适用于在 shell 脚本中写日志，或向系统日志添加自定义消息以进行调试和监控。

# PARAMETERS

**-n, --server HOST**
> 发送到远程 syslog 服务器

**-P, --port PORT**
> 远程服务器端口（默认：514）

**-t, --tag TAG**
> 用标签标记消息（默认：用户名）

**-p, --priority PRIORITY**
> 日志优先级（facility.level，默认：user.notice）

**-s, --stderr**
> 同时输出到 stderr

**-f, --file FILE**
> 记录文件的内容

**-i**
> 包含进程 ID

# PRIORITY LEVELS

Facilities: auth, cron, daemon, kern, local0-7, mail, news, syslog, user, uucp
Levels: emerg, alert, crit, err, warning, notice, info, debug

# INSTALL

```apt: sudo apt install bsdutils```

```apk: sudo apk add logger```

```nix: nix profile install nixpkgs#logger```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[journalctl](/man/journalctl)(1)
