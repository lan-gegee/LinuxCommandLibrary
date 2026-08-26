# TAGLINE

仅在运行时重启单元

# TLDR

若在运行则**重启**单元

```systemctl try-restart [unit]```

若在运行则重启**多个**单元

```systemctl try-restart [unit1 unit2 ...]```

若在运行则按**模式匹配**重启

```systemctl try-restart '[pattern]'```

# SYNOPSIS

**systemctl try-restart** _PATTERN_...

# DESCRIPTION

**systemctl try-restart** 只在一个或多个单元当前正在运行时才重启它们。如果单元未处于活动状态，则不采取任何操作。

这适用于在配置更改后重启服务，同时避免误启动那些被有意停止的服务。

# CAVEATS

对未激活的单元不做任何事。与 `restart` 不同，它不会启动已停止的服务。对于未运行的单元，命令会成功返回但不执行操作。

# ALIASES

此命令也被称为 `condrestart`。

# HISTORY

**try-restart** 子命令提供尊重服务当前状态的安全重启操作，避免意外的服务启动。

# SEE ALSO

[systemctl-restart](/man/systemctl-restart)(1), [systemctl-try-reload-or-restart](/man/systemctl-try-reload-or-restart)(1), [systemctl](/man/systemctl)(1)
