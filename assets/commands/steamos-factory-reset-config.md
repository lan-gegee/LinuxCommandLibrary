# TAGLINE

生成 SteamOS 恢复出厂设置配置

# TLDR

生成恢复出厂设置的**配置**

```steamos-factory-reset-config```

# SYNOPSIS

**steamos-factory-reset-config**

# DESCRIPTION

**steamos-factory-reset-config** 生成 `steamos-factory-reset` 所需的配置文件。此命令通常由恢复出厂设置流程内部调用，不适合手动运行。

生成的配置定义了在恢复出厂设置过程中要保留哪些数据、要擦除哪些数据。

# CAVEATS

这是内部命令，不供手动使用。直接运行此命令可能产生意外后果。属于恢复出厂设置基础设施的一部分。

# HISTORY

**steamos-factory-reset-config** 是 **Valve** 为 Steam Deck 系统恢复操作开发的 **SteamOS** 工具的一部分。

# SEE ALSO

[steamos-factory-reset](/man/steamos-factory-reset)(1)
