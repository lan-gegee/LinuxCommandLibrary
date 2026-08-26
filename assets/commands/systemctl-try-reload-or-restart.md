# TAGLINE

仅对运行中的单元重载或重启

# TLDR

**重载或重启**单元（若在运行）

```systemctl try-reload-or-restart [unit]```

重载或重启**多个**单元

```systemctl try-reload-or-restart [unit1 unit2 ...]```

按**模式匹配**重载或重启

```systemctl try-reload-or-restart '[pattern]'```

# SYNOPSIS

**systemctl try-reload-or-restart** _PATTERN_...

# DESCRIPTION

**systemctl try-reload-or-restart** 尝试为运行中的单元重载配置（若其支持重载），否则重启它们。与 `reload-or-restart` 不同，此命令只影响当前处于活动状态的单元。

如果单元未在运行，则不采取任何操作。这适用于在不启动已停止服务的情况下应用配置更改。

# CAVEATS

对未激活的单元不做任何事。只有单元定义了 ExecReload 时重载才会生效。如果不支持重载，该单元会被重启。

# ALIASES

此命令有若干别名：`condreload`、`force-reload`、`reload-or-try-restart`。

# HISTORY

**try-reload-or-restart** 子命令提供将配置更改应用到服务的最安全方式，避免意外的服务启动。

# SEE ALSO

[systemctl-reload-or-restart](/man/systemctl-reload-or-restart)(1), [systemctl-reload](/man/systemctl-reload)(1), [systemctl-restart](/man/systemctl-restart)(1)
