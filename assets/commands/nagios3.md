# TAGLINE

IT 基础设施监控系统

# TLDR

**验证配置**

```nagios3 -v [/etc/nagios3/nagios.cfg]```

**启动 Nagios**

```nagios3 [/etc/nagios3/nagios.cfg]```

**以守护进程方式运行**

```nagios3 -d [/etc/nagios3/nagios.cfg]```

# SYNOPSIS

**nagios3** [_options_] _config_file_

# PARAMETERS

**-v**
> 验证配置。

**-d**
> 以守护进程方式运行。

**-s**
> 显示调度信息。

**--help**
> 显示帮助。

# DESCRIPTION

**nagios3** 是 Nagios IT 基础设施监控系统的版本 3 守护进程。它监视主机和服务、调度主动检查、处理被动结果，并在状态发生变化时触发通知。配置分布在 **nagios.cfg**（主设置）、**resource.cfg**（宏和机密信息）以及定义主机、服务、联系人和命令的对象文件中。

重启守护进程前可使用 **-v** 验证配置，使用 **-d** 将其作为守护进程启动（通常由 service 单元管理），使用 **-s** 显示调度和负载分布信息。Nagios 3 是遗留版本；新部署应使用 Nagios 4 或 Nagios Core 的现代软件包。

# CAVEATS

不再积极开发；安全和缺陷修复有限。配置语法与 Nagios Core 4 不同。CGI Web 界面依赖 httpd 认证，默认不通过 HTTPS 暴露。

# SEE ALSO

[nagios4](/man/nagios4)(1), [check_mk](/man/check_mk)(1), [naemon](/man/naemon)(1)
