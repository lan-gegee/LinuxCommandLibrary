# TAGLINE

管理按域设置的 SELinux permissive 模式

# TLDR

**列出**所有处于 permissive 模式的进程类型

```sudo semanage permissive -l```

为某个域**设置** permissive 模式

```sudo semanage permissive -a [httpd_t]```

为某个域**取消** permissive 模式

```sudo semanage permissive -d [httpd_t]```

# SYNOPSIS

**semanage permissive** [**-l**|**-a**|**-d**] [_domain_]

# PARAMETERS

**-l, --list**
> 列出所有处于 permissive 模式的域

**-a, --add**
> 将一个域加入 permissive 模式

**-d, --delete**
> 将一个域移出 permissive 模式

# DESCRIPTION

**semanage permissive** 管理 SELinux 中按域设置的 permissive 模式。当某个域被设为 permissive 时，SELinux 会记录该域进程的策略违规行为，但不强制执行。

这比全局 permissive 模式（**setenforce 0**）提供更细粒度的控制，可以让特定服务不受约束，而系统其余部分仍保持 enforcing 模式。

# CAVEATS

permissive 域实际上是不受约束的，只应用于故障排查。在生产系统中，应配置正确的 SELinux 策略规则，而不是让域一直处于 permissive 模式。需要 root 权限。

# SEE ALSO

[semanage](/man/semanage)(8), [setenforce](/man/setenforce)(8), [getenforce](/man/getenforce)(8), [audit2allow](/man/audit2allow)(1)
