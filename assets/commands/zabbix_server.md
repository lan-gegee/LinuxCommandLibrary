# TAGLINE

Zabbix 中央监控服务器守护进程

# TLDR

**启动服务器**

```zabbix_server```

**使用配置文件**

```zabbix_server -c [/etc/zabbix/zabbix_server.conf]```

**前台模式**

```zabbix_server -f```

**运行时控制**

```zabbix_server -R [config_cache_reload]```

# SYNOPSIS

**zabbix_server** [_-c config_] [_-f_] [_-R command_] [_options_]

# PARAMETERS

**-c** _FILE_
> 配置文件。

**-f**
> 前台运行。

**-R** _CMD_
> 向正在运行的服务器发送运行时命令（例如 _config_cache_reload_、_housekeeper_execute_、_log_level_increase_、_log_level_decrease_、_diaginfo_、_snmp_cache_reload_、_ha_status_）。

**-T**, **--test-config**
> 校验配置文件并退出。

**-h**, **--help**
> 显示帮助并退出。

**-V**, **--version**
> 显示版本信息并退出。

# DESCRIPTION

**zabbix_server** 是 Zabbix 监控系统的核心守护进程。它接收来自代理和代理服务器（proxy）的监控数据，评估触发器条件，处理告警，并将历史数据存储到后端数据库。

服务器协调所有监控行为：调度检查、处理传入数据、检测阈值越限，并通过已配置的媒介类型（电子邮件、短信、脚本、webhook）发送通知。它需要数据库后端（MySQL、PostgreSQL 或 Oracle）来存储配置和采集到的指标。

Web 前端是连接同一数据库的独立组件，提供用于配置和可视化的图形界面。通过 **-R** 进行运行时控制，可在不重启服务的情况下重新加载配置缓存和调整日志级别。

# CAVEATS

需要已配置且在启动前可达的数据库后端（MySQL/MariaDB、PostgreSQL 或 TimescaleDB）。数据库架构必须已用 **zabbix_server** 的 SQL 文件导入。Web 前端是独立的组件。可用 **-R log_level_increase** 在运行时提高日志详细程度而无需重启。

# HISTORY

**zabbix_server** 是开源企业监控平台 **Zabbix** 的核心。

# INSTALL

```apt: sudo apt install zabbix-server-mysql```

```dnf: sudo dnf install zabbix-server-mysql```

```apk: sudo apk add zabbix-mysql```

```zypper: sudo zypper install zabbix-server-mysql```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zabbix_agentd](/man/zabbix_agentd)(1), [zabbix_proxy](/man/zabbix_proxy)(1)
