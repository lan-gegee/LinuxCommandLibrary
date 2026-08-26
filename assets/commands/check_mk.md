# TAGLINE

IT 基础设施监控工具

# TLDR

**手动检查一台主机**

```cmk -nv [hostname]```

**发现主机上的服务**

```cmk -I [hostname]```

**发现所有主机上的服务**

```cmk -I```

**更新配置并重新加载**

```cmk -O```

**查看主机的 agent 输出**

```cmk -d [hostname]```

**列出所有主机**

```cmk --list-hosts```

**激活更改**

```cmk -R```

# SYNOPSIS

**cmk** [_options_] [_hostname_]

# PARAMETERS

**-I**, **--discover**
> 发现主机上的新服务。

**-II**
> 移除已消失的服务并发现新服务。

**-n**
> 模拟检查而不提交结果（dry run）。

**-v**
> 详细输出。常组合为 **-nv** 用于测试。

**-d**
> 转储主机的 agent 输出。

**-O**, **--reload**
> 重新加载配置而不重启。

**-R**, **--restart**
> 重启监控核心。

**--list-hosts**
> 列出所有已配置的主机。

**--list-checks**
> 列出所有可用的检查插件。

**--paths**
> 显示 Checkmk 目录路径。

**-P**, **--package** _action_
> 管理扩展包（install、remove、list）。

**--snmpwalk** _HOSTNAME_
> 对主机执行 SNMP walk 以进行诊断。

**--debug**
> 启用调试输出。

# DESCRIPTION

**Checkmk**（前身为 Check_MK）是基于 Nagios 监控核心概念构建的综合性 IT 监控解决方案。**cmk** 命令是管理主机、服务和配置的核心 CLI 工具。

系统使用安装在受监控主机上的 agent 来收集指标和状态信息。**cmk** 命令处理这些数据、发现可用服务、执行检查并管理配置。

发现操作（**cmk -I**）扫描主机上可监控的服务。配置更改需要通过 **cmk -O** 或 **cmk -R** 激活才能生效。该工具支持分布式监控、用于部署的 agent 打包（agent bakery），以及丰富的插件架构。

# CONFIGURATION

**/omd/sites/&lt;site&gt;/etc/check_mk/main.mk**
> 主配置文件，包含主机定义、检查参数和规则。

**/omd/sites/&lt;site&gt;/etc/check_mk/conf.d/**
> 存放附加配置文件的目录，通常由 Web 界面管理。

# CAVEATS

对配置的更改必须激活后才会生效。商业版（CEE、CME）包含 Raw 版中没有的附加功能。大规模的服务发现可能非常消耗资源。基于 agent 的监控要求在目标主机上部署 agent。

# HISTORY

Check_MK 由 **Mathias Kettner** 于 **2008** 年创建，最初是 Nagios 的扩展，旨在简化配置并提升性能。它从一个插件发展为完整的监控解决方案。**2019** 年，项目更名为 **Checkmk**，并成立了 tribe29 GmbH（现为 Checkmk GmbH）。Raw 版保持开源，商业版则增加了企业级功能。

# SEE ALSO

[nagios](/man/nagios)(8), [icinga2](/man/icinga2)(8), [prometheus](/man/prometheus)(1)
