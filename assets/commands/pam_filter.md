# TAGLINE

面向终端 I/O 的 PAM 过滤模块

# TLDR

对认证 I/O **运行过滤器**

```auth required pam_filter.so run1 /path/to/filter```

在会话打开时**运行过滤器**并输出调试信息

```session required pam_filter.so debug run1 /path/to/filter```

分配新的伪终端并**运行过滤器**

```session required pam_filter.so new_term run1 /path/to/filter```

# SYNOPSIS

**pam_filter.so** [debug] [new_term] [non_term] run1|run2 _filter_ [_..._]

# PARAMETERS

**debug**
> 将调试信息打印到 syslog。

**new_term**
> 将 PAM_TTY 设置为过滤后的伪终端。默认行为是将 PAM_TTY 设置为指示用户连接所用的终端。

**non_term**
> 不尝试设置 PAM_TTY 项。

**run1** _FILTER_
> 在第一阶段运行过滤器。auth 对应 pam_authenticate；session 对应 pam_open_session；password 对应 PAM_PRELIM_CHECK 阶段。

**run2** _FILTER_
> 在第二阶段运行过滤器。auth 对应 pam_setcred；session 对应 pam_close_session；password 对应 PAM_UPDATE_AUTHTOK 阶段。

# DESCRIPTION

**pam_filter** 是一个 PAM 模块，旨在充当一个平台，提供对所有在用户与应用程序之间传递的输入/输出的访问。它只适用于基于 tty 以及 stdin/stdout 的应用程序。

调用过滤器时，argv[0] 总是过滤程序本身，其后依次是连接类型和 PAM 服务类型。所有模块类型（auth、account、password、session）均受支持。

# CAVEATS

这是一个实验性模块。过滤器必须是可执行的二进制文件。只适用于基于 tty 和 stdin/stdout 的应用程序。标准 PAM 发行版没有附带任何已知的过滤器。

# SEE ALSO

[pam](/man/pam)(8), [pam_tty_audit](/man/pam_tty_audit)(8)
