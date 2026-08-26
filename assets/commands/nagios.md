# TAGLINE

跟踪主机、服务和网络的基础设施监控系统

# TLDR

**验证配置**

```nagios -v [/etc/nagios/nagios.cfg]```

**启动 Nagios 守护进程**

```nagios -d [/etc/nagios/nagios.cfg]```

**在前台运行**

```nagios [/etc/nagios/nagios.cfg]```

**显示版本**

```nagios --version```

**测试调度**

```nagios -s [/etc/nagios/nagios.cfg]```

# SYNOPSIS

**nagios** [_-v_] [_-d_] [_-s_] [_config_file_]

# PARAMETERS

**-v**
> 验证配置文件。

**-d**
> 以守护进程方式运行。

**-s**
> 显示调度信息。

**-p** _FILE_
> 指定预缓存对象文件。

**-u** _FILE_
> 指定预缓存宏文件。

**-x** _FILE_
> 将对象转储到文件。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**nagios** 是一个基础设施监控系统，用于跟踪主机、服务和网络设备。它在问题发生和解决时向管理员发出告警。

配置定义主机、服务和检查命令。插件执行检查并返回状态码：OK、WARNING、CRITICAL 或 UNKNOWN。通知功能通过电子邮件、短信或自定义方式提醒联系人。

Web 界面显示当前状态、趋势和报告。它展示哪些服务正常运行、哪些已宕机，以及对已知问题的确认。

主动检查按计划运行。被动检查从外部来源接收结果。两者都整合到同一个状态视图中。

升级机制根据问题持续时间将告警路由给不同的人。依赖关系可防止父系统故障时的通知风暴。

检查产生的性能数据可以输入 PNP4Nagios 或 Grafana 等图表工具，用于历史趋势分析。

# CAVEATS

大型环境的配置可能很复杂。Web 界面需要单独的 Web 服务器。可用插件众多但质量参差不齐。可以考虑 Icinga 或 Naemon 等后继项目。

# HISTORY

**Nagios** 由 **Ethan Galstad** 于 **1999 年**创建，最初名为 NetSaint，**2002 年**更名为 Nagios。它成为开源监控系统的标准，衍生出多个分支（Icinga、Naemon），并启发了现代替代方案。

# INSTALL

```dnf: sudo dnf install nagios```

```apk: sudo apk add nagios```

```zypper: sudo zypper install nagios```

```brew: brew install nagios```

```nix: nix profile install nixpkgs#nagios```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[icinga2](/man/icinga2)(1), [naemon](/man/naemon)(8), [check_mk](/man/check_mk)(1), [prometheus](/man/prometheus)(1)
