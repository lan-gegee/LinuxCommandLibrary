# TAGLINE

管理 SysVinit 服务的运行级别

# TLDR

**列出**服务及其运行级别

```chkconfig --list```

显示**特定服务的**运行级别

```chkconfig --list [ntpd]```

开机**启用**服务

```chkconfig [sshd] on```

为**指定运行级别**启用服务

```chkconfig --level [2345] [sshd] on```

开机**禁用**服务

```chkconfig [ntpd] off```

为**指定运行级别**禁用服务

```chkconfig --level [3] [ntpd] off```

# SYNOPSIS

**chkconfig** [_options_] [_name_] [_on|off|reset_]

# DESCRIPTION

**chkconfig** 在使用 SysVinit 的基于 Red Hat 的 Linux 系统上管理服务的运行级别。它更新 /etc/rc.d/ 目录中的符号链接，这些链接控制每个运行级别下哪些服务会启动。

该工具主要用于 CentOS 6 和更早的 RHEL 系统。使用 systemd 的现代系统应改用 systemctl。

# PARAMETERS

**--list** [_name_]
> 列出所有服务或特定服务的运行级别

**--level** _levels_
> 指定要影响的运行级别（例如 2345）

**--add** _name_
> 添加新服务以纳入管理

**--del** _name_
> 将服务移出管理

# CONFIGURATION

**/etc/rc.d/init.d/**
> 存放 chkconfig 所管理的 SysVinit 服务脚本的目录。每个脚本包含一个 chkconfig 头部，指明默认运行级别。

# CAVEATS

这是面向 SysVinit 系统的旧式工具。在基于 systemd 的系统上（CentOS 7+、RHEL 7+），请改用 systemctl。运行级别 0-6 有各自的含义：0=停机、1=单用户、2-5=多用户、6=重启。

# HISTORY

**chkconfig** 由 Red Hat 开发，用于管理 SysVinit 服务。随着 systemd 的普及，其功能已基本被 systemctl 取代，但出于兼容性考虑仍然可用。

# INSTALL

```dnf: sudo dnf install chkconfig```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [service](/man/service)(8), [update-rc.d](/man/update-rc.d)(8)

# RESOURCES

```[Source code](https://github.com/fedora-sysv/chkconfig)```

<!-- verified: 2026-06-22 -->
