# TAGLINE

当前稳定的 IT 基础设施监控系统

# TLDR

**验证配置**

```nagios4 -v [/etc/nagios4/nagios.cfg]```

**启动 Nagios**

```nagios4 [/etc/nagios4/nagios.cfg]```

**以守护进程方式运行**

```nagios4 -d [/etc/nagios4/nagios.cfg]```

**显示版本**

```nagios4 -V```

# SYNOPSIS

**nagios4** [_options_] _config_file_

# PARAMETERS

**-v**
> 验证配置。

**-d**
> 以守护进程方式运行。

**-s**
> 显示调度信息。

**-p**
> 显示待处理事件。

**-V**
> 显示版本。

**-W**
> 预缓存对象。

# DESCRIPTION

**nagios4**（版本 4）是当前稳定的 IT 基础设施监控系统。监视主机、服务、网络设备和应用程序。提供告警、报告和 Web 界面。

# INSTALL

```apt: sudo apt install nagios4-core```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[icinga2](/man/icinga2)(1), [prometheus](/man/prometheus)(1)
