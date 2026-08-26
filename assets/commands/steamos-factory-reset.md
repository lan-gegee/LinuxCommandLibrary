# TAGLINE

将 SteamOS 恢复为出厂设置

# TLDR

开始**恢复出厂设置**

```steamos-factory-reset```

显示**帮助**

```steamos-factory-reset --help```

# SYNOPSIS

**steamos-factory-reset** [_OPTIONS_]

# DESCRIPTION

**steamos-factory-reset** 将 SteamOS 恢复为出厂设置，擦除用户数据和配置，同时保留操作系统。该命令在继续之前需要用户确认。

通常用于出售设备前的准备、排查顽固问题，或将系统恢复到干净状态。

# CAVEATS

此操作具有破坏性且无法撤销。所有用户数据、已安装的游戏和配置都将被擦除。运行前请备份重要数据。需要确认提示。

# HISTORY

**steamos-factory-reset** 是 **Valve** 开发的 **SteamOS** 工具的一部分。对于作为消费设备的 Steam Deck 而言，恢复出厂设置功能必不可少。

# SEE ALSO

[steamos-factory-reset-config](/man/steamos-factory-reset-config)(1), [steamos-update](/man/steamos-update)(1)
