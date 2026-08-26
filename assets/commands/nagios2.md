# TAGLINE

IT 基础设施监控系统

# TLDR

**使用配置文件启动 Nagios**

```nagios [/etc/nagios/nagios.cfg]```

**检查配置文件中的错误**

```nagios -v [/etc/nagios/nagios.cfg]```

**让 Nagios 以守护进程方式在后台运行**

```nagios -d [/etc/nagios/nagios.cfg]```

**显示调度信息**

```nagios -s [/etc/nagios/nagios.cfg]```

# SYNOPSIS

**nagios** [_options_] _config_file_

# PARAMETERS

**-v**
> 检查配置文件中的错误但不启动。

**-d**
> 以守护进程（后台进程）方式运行。

**-s**
> 显示调度信息。

**-p**
> 显示预计/待处理事件。

# DESCRIPTION

**nagios**（版本 2）是一个 IT 基础设施监控系统。它监视主机、服务和网络设备，为系统管理员提供告警和报告。Nagios 的检查由插件执行，其结果决定主机/服务的状态。Nagios 2 属于遗留版本；建议升级到 Nagios 4。

# CAVEATS

Nagios 2 已不再维护，缺少 Nagios 4 中的功能和安全更新。强烈建议迁移到 Nagios 4 或 Icinga 等替代方案。

# SEE ALSO

[nagios4](/man/nagios4)(1), [nagios](/man/nagios)(1)
