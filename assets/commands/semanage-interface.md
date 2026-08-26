# TAGLINE

管理 SELinux 网络接口类型

# TLDR

**列出**所有接口类型定义

```sudo semanage interface -l```

**添加**网络接口类型定义

```sudo semanage interface -a -t type_name interface_name```

**删除**接口类型定义

```sudo semanage interface -d interface_name```

**修改**接口类型定义

```sudo semanage interface -m -t type_name interface_name```

仅列出**自定义的**定义

```sudo semanage interface -l -C```

# SYNOPSIS

**semanage interface** [_options_]

# PARAMETERS

**-l**, **--list**
> 列出接口类型定义

**-a**, **--add**
> 添加新定义

**-d**, **--delete**
> 删除定义

**-m**, **--modify**
> 修改现有定义

**-t**, **--type** _type_
> 接口的 SELinux 类型

**-C**, **--locallist**
> 仅显示本地自定义项

**-D**, **--deleteall**
> 移除所有本地自定义项

**-E**, **--extract**
> 提取可自定义的命令以便在事务中使用

**-n**, **--noheading**
> 列出时不打印标题

**-N**, **--noreload**
> 提交后不重新加载策略

**-r**, **--range** _RANGE_
> MLS/MCS 安全范围（仅限 MLS/MCS 系统）

# DESCRIPTION

**semanage interface** 管理 SELinux 网络接口类型定义。它为网络接口分配 SELinux 类型，用于基于网络的访问控制。

通过接口标签，SELinux 策略可以基于接口类型控制网络流量。

# CAVEATS

更改需要重新加载策略才能生效。错误的接口类型设置可能影响网络连接。

# HISTORY

属于 **policycoreutils**，提供 SELinux 策略管理工具。

# SEE ALSO

[semanage](/man/semanage)(8), [semanage-port](/man/semanage-port)(8), [semanage-fcontext](/man/semanage-fcontext)(8), [semanage-boolean](/man/semanage-boolean)(8)
