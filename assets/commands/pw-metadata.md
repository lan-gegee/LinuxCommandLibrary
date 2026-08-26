# TAGLINE

监控和管理 PipeWire 元数据

# TLDR

显示**默认**名称下的元数据

```pw-metadata```

显示 settings 中 **ID 为 0** 的元数据

```pw-metadata -n settings 0```

列出所有**可用的元数据**对象

```pw-metadata -l```

持续运行并**记录元数据的变更**

```pw-metadata -m```

**删除**所有元数据

```pw-metadata -d```

在 settings 中将 log.level **设置为** 1

```pw-metadata -n settings 0 log.level 1```

# SYNOPSIS

**pw-metadata** [_options_] [_id_] [_key_] [_value_] [_type_]

# PARAMETERS

**-n**, **--name** _name_
> 要操作的元数据名称（默认："default"）

**-l**, **--list**
> 列出所有可用的元数据对象

**-m**, **--monitor**
> 持续监控元数据变化

**-d**, **--delete**
> 删除元数据条目

**-r**, **--remote** _NAME_
> 要连接的远程实例名称（默认：默认 PipeWire 实例）。

**--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**pw-metadata** 监控、设置和删除 PipeWire 对象上的元数据。元数据提供与 PipeWire 图对象关联的键值对，用于配置和运行时状态管理。

该工具可以操作不同的元数据命名空间，包括用于一般元数据的 "default" 和用于 PipeWire 配置值（如日志级别）的 "settings"。

# CAVEATS

修改 "settings" 命名空间中的元数据会立即影响 PipeWire 的行为。删除元数据时须谨慎，因为这可能将配置重置为默认值。

# HISTORY

**PipeWire**（Linux 上的现代多媒体框架）的一部分。提供对 PipeWire 元数据系统的运行时检查和修改。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [pw-mon](/man/pw-mon)(1), [pw-cli](/man/pw-cli)(1)
