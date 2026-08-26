# TAGLINE

新一代 Zabbix 监控代理

# TLDR

**在前台启动代理**

```zabbix_agent2 -f```

**使用配置文件启动**

```zabbix_agent2 -c [/etc/zabbix/zabbix_agent2.conf]```

**测试指定的监控项键**

```zabbix_agent2 -t [system.cpu.load]```

**打印所有支持的监控项**

```zabbix_agent2 -p```

**校验配置文件**

```zabbix_agent2 -T```

**运行时更改日志级别**

```zabbix_agent2 -R [log_level_increase]```

**运行时重新加载用户参数**

```zabbix_agent2 -R userparameter_reload```

# SYNOPSIS

**zabbix_agent2** [_options_]

# PARAMETERS

**-c**, **--config** _file_
> 使用替代的配置文件而非默认配置。

**-f**
> 在前台运行。

**-p**, **--print**
> 打印已知的监控项并退出。

**-t** _item-key_
> 测试单个监控项键并退出。

**-T**, **--test-config**
> 校验配置文件并退出。

**-R**, **--runtime-control** _option_
> 执行管理功能。选项：log_level_increase、log_level_decrease、userparameter_reload、metrics、version、help。

**-h**, **--help**
> 显示帮助并退出。

**-V**, **--version**
> 显示版本信息并退出。

# DESCRIPTION

**zabbix_agent2** 是以 Go 编写的新一代 Zabbix 监控代理。它收集系统指标并发送到 Zabbix 服务器，支持插件和并发检查。

# INSTALL

```apt: sudo apt install zabbix-agent2```

```pacman: sudo pacman -S zabbix-agent2```

```apk: sudo apk add zabbix-agent2```

```zypper: sudo zypper install zabbix-agent2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zabbix_agentd](/man/zabbix_agentd)(1), [zabbix_get](/man/zabbix_get)(1), [zabbix_proxy](/man/zabbix_proxy)(1), [zabbix_server](/man/zabbix_server)(1)
