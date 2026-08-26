# TAGLINE

分布式 Zabbix 监控数据代理

# TLDR

**启动代理守护进程**

```sudo systemctl start zabbix-proxy```

**在前台运行**

```zabbix_proxy -f```

**使用替代的配置文件**

```zabbix_proxy -c [/etc/zabbix/zabbix_proxy.conf]```

**显示运行时诊断信息**

```zabbix_proxy -R diaginfo```

**重新加载配置缓存**

```zabbix_proxy -R config_cache_reload```

**显示版本**

```zabbix_proxy -V```

# SYNOPSIS

**zabbix_proxy** [_options_]

# PARAMETERS

**-c**, **--config** _file_
> 使用替代的配置文件。

**-f**, **--foreground**
> 在前台运行。

**-R**, **--runtime-control** _option_
> 运行时控制命令。

**-h**, **--help**
> 显示帮助。

**-V**, **--version**
> 显示版本。

# RUNTIME CONTROL

**config_cache_reload**: 重新加载配置缓存。

**housekeeper_execute**: 启动清理进程（housekeeper）。

**log_level_increase**: 提高日志级别。

**log_level_decrease**: 降低日志级别。

**diaginfo**: 将诊断信息写入日志。

# DESCRIPTION

**zabbix_proxy** 是一个守护进程，负责收集监控数据并转发给 Zabbix 服务器。它用于对远程位置进行分布式监控，并减轻中央服务器的负载。

代理从各代理端收集数据，先存储在本地数据库中，再传输给服务器。这种架构可以在临时网络中断时继续工作，并为远程站点集中数据收集。

代理可以以主动模式（主动连接服务器）或被动模式（接受服务器的连接）运行。每个代理需要自己的数据库（SQLite、MySQL 或 PostgreSQL）。

# CAVEATS

需要独立于服务器的数据库，不能与服务器共用数据库。配置更改可能需要重新加载缓存。在 Zabbix 7.0+ 中建议使用内存缓冲区以提升性能。

# HISTORY

**zabbix_proxy** 是为支持分布式监控架构而加入 Zabbix 的。它让组织无需与服务器直接连通即可监控远程站点，并通过压缩和批量传输数据减少 WAN 带宽占用。

# INSTALL

```apt: sudo apt install zabbix-proxy-mysql```

```dnf: sudo dnf install zabbix-proxy-mysql```

```apk: sudo apk add zabbix-mysql```

```zypper: sudo zypper install zabbix-proxy-mysql```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zabbix_server](/man/zabbix_server)(8), [zabbix_agentd](/man/zabbix_agentd)(8), [zabbix_get](/man/zabbix_get)(1)
