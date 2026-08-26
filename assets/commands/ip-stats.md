# TAGLINE

管理并显示网络接口统计信息

# TLDR

显示**所有**接口的统计信息

```ip stats```

显示**特定接口**的统计信息

```ip stats show dev [eth0]```

显示**链路层**统计信息

```ip stats show group link```

显示**硬件卸载**统计信息

```ip stats show group offload```

显示**特定接口**的卸载统计信息

```ip stats show dev [eth0] group offload```

显示特定的**卸载子组**

```ip stats show dev [eth0] group offload subgroup [l3_stats|cpu_hit|hw_stats_info]```

**启用** L3 硬件统计

```ip stats set dev [eth0] l3_stats on```

# SYNOPSIS

**ip stats** [_command_] [_options_]

# PARAMETERS

**show** [**dev** _DEVICE_]
> 显示统计信息

**set** **dev** _DEVICE_
> 配置统计信息收集

**group** _GROUP_
> 统计组：link、offload、afstats

**subgroup** _SUBGROUP_
> 组内的特定子组

**l3_stats** _on|off_
> 启用/禁用 L3 硬件统计

# DESCRIPTION

**ip stats** 管理并显示网络接口统计信息。它既可访问软件维护的计数器，也可在硬件支持时访问硬件卸载统计信息。

统计组包括链路层计数器、硬件卸载指标，以及 MPLS 等特定地址族的统计。硬件统计收集可能需要显式启用。

# CAVEATS

硬件卸载统计需要驱动和硬件支持。某些统计在所有接口上未必可用。启用统计收集可能影响性能。

# HISTORY

ip stats 被加入 iproute2，用于统一访问各种网络统计信息，包括较新内核版本中提供的硬件卸载指标。

# SEE ALSO

[ip](/man/ip)(8), [ip-link](/man/ip-link)(8), [ifstat](/man/ifstat)(1)
