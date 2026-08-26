# TAGLINE

移除 Void Linux 上的旧内核

# TLDR

**列出**可移除的内核

```vkpurge list [version]```

移除**所有**未使用的内核

```vkpurge rm all```

移除**指定的**版本

```vkpurge rm [version]```

# SYNOPSIS

**vkpurge** _COMMAND_ [_VERSION_]

# COMMANDS

**list** [_VERSION_]
> 列出可移除的内核版本

**rm** _VERSION_|all
> 移除内核版本

# DESCRIPTION

**vkpurge** 用于列出或移除 Void Linux 上 xbps 软件包管理器留下的旧内核版本。版本参数支持 shell 通配符，便于灵活匹配。

该工具通过移除未使用的内核安装来帮助清理磁盘空间，同时保留当前正在运行的内核。

# CAVEATS

仅适用于 Void Linux。无法移除当前正在运行的内核。需要 root 权限。使用时须谨慎，避免误删仍需要的内核。

# SEE ALSO

[xbps-remove](/man/xbps-remove)(1), [xbps-install](/man/xbps-install)(1)
