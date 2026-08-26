# TAGLINE

SELinux 持久化策略管理工具

# TLDR

**设置**或取消 SELinux 布尔值

```sudo semanage boolean -m --on|--off [haproxy_connect_any]```

**添加**用户自定义的文件上下文标签规则

```sudo semanage fcontext -a -t [samba_share_t] '/mnt/share(/.*)?'```

**添加**用户自定义的端口标签规则

```sudo semanage port -a -t [ssh_port_t] -p [tcp] [22000]```

为受限域**设置**或取消 permissive 模式

```sudo semanage permissive --add|--delete [httpd_t]```

将本地自定义项**导出**到文件

```sudo semanage export -f [path/to/file]```

从文件**导入**自定义项

```sudo semanage import -f [path/to/file]```

# SYNOPSIS

**semanage** {_subcommand_} [_options_]

# PARAMETERS

**boolean**
> 管理 SELinux 布尔值。

**fcontext**
> 管理文件上下文标签规则。

**port**
> 管理端口类型定义。

**interface**
> 管理网络接口类型定义。

**node**
> 管理网络节点类型定义。

**login**
> 管理 Linux 用户与 SELinux 受限用户之间的映射。

**user**
> 管理 SELinux 用户定义及其授权角色。

**module**
> 管理 SELinux 策略模块。

**permissive**
> 管理受限域的 permissive 模式。

**dontaudit**
> 切换策略中的 dontaudit 规则。

**export**
> 导出本地自定义项。

**import**
> 导入本地自定义项。

**-a**, **--add**
> 添加新记录。

**-m**, **--modify**
> 修改现有记录。

**-d**, **--delete**
> 删除记录。

**-l**, **--list**
> 列出记录。

**-n**, **--noheading**
> 列出时不显示标题行。

**-C**, **--locallist**
> 仅列出自定义项（不含基础策略记录）。

**-f**, **--fcontext** _file_
> 配合 export/import 使用，从此文件读取或写入此文件。

# DESCRIPTION

**semanage** 是 SELinux 策略管理工具，用于配置持久化的安全策略设置。与 **setsebool** 或 **chcon** 不同，使用 semanage 所做的更改在重启后依然保留。

该工具管理布尔值、文件上下文、端口、网络接口和用户映射。它无需修改策略源码即可对 SELinux 策略进行细粒度控制。

# CONFIGURATION

**/etc/selinux/*/policy/**
> SELinux 策略存储目录，包含活动的策略模块和本地自定义项。

**/var/lib/selinux/**
> 策略模块数据库，存储已安装和本地修改的策略组件。

# CAVEATS

需要 root 权限。文件上下文的更改需要运行 **restorecon** 才能应用。导入自定义项可能移除已有的本地修改。仅在启用 SELinux 的系统上可用。

# SEE ALSO

[semanage-boolean](/man/semanage-boolean)(8), [semanage-fcontext](/man/semanage-fcontext)(8), [semanage-port](/man/semanage-port)(8), [restorecon](/man/restorecon)(8), [getsebool](/man/getsebool)(8), [setsebool](/man/setsebool)(8), [chcon](/man/chcon)(1)
