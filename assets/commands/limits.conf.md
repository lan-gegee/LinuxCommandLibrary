# TAGLINE

为用户和组设置资源限制的 PAM 配置文件

# TLDR

**为用户设置最大打开文件数**

```[username] hard nofile [65535]```

**设置内存限制**

```[username] hard as [4194304]```

**为所有用户设置**

```* soft nproc [1024]```

**为组设置**

```@[groupname] hard maxlogins [10]```

# SYNOPSIS

**/etc/security/limits.conf**

# PARAMETERS

**hard**
> 硬限制（最大值）。

**soft**
> 软限制（默认值）。

**nofile**
> 最大打开文件数。

**nproc**
> 最大进程数。

**as**
> 地址空间限制。

**maxlogins**
> 最大登录数。

**memlock**
> 最大锁定内存。

**stack**
> 最大栈大小。

# DESCRIPTION

**limits.conf** 是一个 PAM 配置文件，用于为用户和组设置资源限制。当用户通过启用了 PAM 的服务登录时，这些限制会被强制执行。

格式为：domain type item value。domain 可以是用户名、@组名，或表示所有用户的 *。

# EXAMPLE CONFIG

```
# /etc/security/limits.conf
* soft nofile 4096
* hard nofile 65535
@developers soft nproc 2048
root hard nproc unlimited
```

# CAVEATS

需要 pam_limits 模块。更改将在下次登录时生效。systemd 服务可能需要在 unit 文件中设置 LimitNOFILE。可用 ulimit -a 检查。

# SEE ALSO

[ulimit](/man/ulimit)(1), [pam](/man/pam)(8), [pam_limits](/man/pam_limits)(8), [sysctl](/man/sysctl)(8)
