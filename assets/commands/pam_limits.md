# TAGLINE

为用户会话设置资源限制

# TLDR

**在 PAM 服务文件中启用资源限制**

```session required pam_limits.so```

**为所有用户设置打开文件描述符的硬限制**

```echo "* hard nofile 65535" >> /etc/security/limits.conf```

**为一个组设置软限制和硬限制的进程数上限**

```echo "@developers - nproc 4096" >> /etc/security/limits.conf```

**添加针对单个应用程序的限制覆盖文件**

```echo "nginx hard nofile 100000" > /etc/security/limits.d/nginx.conf```

# SYNOPSIS

**pam_limits.so** [_options_]

# PARAMETERS

**conf=**_FILE_
> 使用替代的资源限制配置文件，而不是 `/etc/security/limits.conf`。

**debug**
> 将调试信息打印到系统日志。

**change_uid**
> 在读取 limits 文件前切换到目标用户的 UID。当 limits 文件只有目标用户才能访问时有用。

**utmp_early**
> 在模块运行前读取 utmp 条目。用于规避那些在 PAM 完成之前就分配 utmp 条目的有缺陷的应用程序。

**noaudit**
> 不向审计子系统报告超出最大登录次数的情况。

**set_all**
> 从 PID 1 进程的限制中设置未指定的限制项。不推荐在 systemd 系统上使用，因为 PID 1 的限制与内核默认值不同。

配置从 `/etc/security/limits.conf` 以及 `/etc/security/limits.d/*.conf` 中的 drop-in 文件读取。

# DESCRIPTION

**pam_limits** 是一个 PAM session 模块，在登录时强制执行按用户和按组的资源限制。它从 `/etc/security/limits.conf` 和 `/etc/security/limits.d/` 目录中的 `*.conf` 文件读取限制定义，后者按字典序应用。

配置中的每条规则格式为：`domain type item value`。domain 可以是用户名、`@groupname`、`*`（所有用户）或 UID/GID 范围。type 可以是 `soft`（用户可调整的上限）、`hard`（内核强制执行的最大值）或 `-`（两者都设置）。常见的 item 包括 `nofile`（打开文件描述符数）、`nproc`（进程数）、`memlock`（锁定内存，KB）、`stack`（栈大小，KB）、`cpu`（CPU 时间，分钟）、`as`（地址空间，KB）、`maxlogins`（每用户并发登录数）和 `priority`（调度优先级）。

单个用户的条目优先于组条目。包括 root（uid=0）在内的所有用户都受这些限制约束。可将值设为 `unlimited`、`infinity` 或 `-1` 来移除某个限制（对 `priority`、`nice` 或 `nonewprivs` 无效）。

限制只对新登录会话生效；正在运行的进程不受影响。

# CAVEATS

仅为 session 模块——必须放在 PAM 服务文件的 `session` 栈中（例如 `/etc/pam.d/common-session`）。限制在登录时按会话生效；更改要求用户注销后重新登录。

root（uid=0）与其他用户一样受这些限制影响。

systemd 服务会忽略 `/etc/security/limits.conf`；请改用 unit 文件中的 `LimitNOFILE=` 等相关指令。

不得从多线程应用程序中调用此模块。

# SEE ALSO

[limits.conf](/man/limits.conf)(5), [pam](/man/pam)(8), [ulimit](/man/ulimit)(1), [sysctl](/man/sysctl)(8)
