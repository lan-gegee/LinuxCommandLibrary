# TAGLINE

Zabbix 监控代理守护进程

# TLDR

**启动代理**

```zabbix_agentd```

**使用配置文件**

```zabbix_agentd -c [/etc/zabbix/zabbix_agentd.conf]```

**前台模式**

```zabbix_agentd -f```

**测试单个监控项键**

```zabbix_agentd -t [system.cpu.load]```

**打印所有支持的监控项及当前值**

```zabbix_agentd -p```

**校验配置文件**

```zabbix_agentd -T```

**运行时提高日志级别**

```zabbix_agentd -R log_level_increase```

# SYNOPSIS

**zabbix_agentd** [_-c config_] [_-f_] [_-t item_] [_options_]

# PARAMETERS

**-c**, **--config** _config-file_
> 使用替代的配置文件而非默认文件（/usr/local/etc/zabbix_agentd.conf）。

**-f**, **--foreground**
> 在前台运行代理，而不是作为守护进程。

**-p**, **--print**
> 打印所有已知监控项及其当前值，然后退出。

**-t**, **--test** _item-key_
> 测试单个监控项键并打印结果，然后退出。

**-R**, **--runtime-control** _runtime-option_
> 执行管理功能。选项：userparameter_reload、log_level_increase[=target]、log_level_decrease[=target]。

**-T**, **--test-config**
> 校验配置文件并退出。

**-h**, **--help**
> 显示帮助并退出。

**-V**, **--version**
> 输出版本信息并退出。

# DESCRIPTION

**zabbix_agentd** 是 Zabbix 监控代理守护进程，负责收集系统指标并发送到 Zabbix 服务器或代理。它使用内置的监控项键收集 CPU、内存、磁盘、网络等系统资源数据。

该代理支持两种工作模式：被动模式下服务器按需查询代理；主动模式下代理主动发起连接并按配置的间隔发送数据。可通过用户参数添加自定义监控，用户参数定义了代理执行以采集应用特定指标的命令。

**-t** 选项可测试单个监控项键以排障，**-p** 打印所有支持的监控项及其当前值。通过 **-R** 进行运行时控制，可在不重启守护进程的情况下更改日志级别和重新加载配置。

# CAVEATS

需要 Zabbix 服务器或代理来接收收集的数据。必须有配置文件，默认路径为 /usr/local/etc/zabbix_agentd.conf。部分监控项键需要 root 权限。OpenBSD、NetBSD 和 Windows 不支持运行时控制（-R）。

# HISTORY

**zabbix_agentd** 是企业级监控解决方案 **Zabbix** 的代理守护进程。

# INSTALL

```apt: sudo apt install zabbix-agent```

```dnf: sudo dnf install zabbix-agent```

```pacman: sudo pacman -S zabbix-agent```

```apk: sudo apk add zabbix-agent```

```zypper: sudo zypper install zabbix-agent```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zabbix_server](/man/zabbix_server)(1), [zabbix_proxy](/man/zabbix_proxy)(1), [zabbix_get](/man/zabbix_get)(1)
