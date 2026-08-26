# TAGLINE

管理 SysV init 脚本的运行级别链接

# TLDR

以默认运行级别**安装**服务

```update-rc.d [mysql] defaults```

**启用**服务

```update-rc.d [mysql] enable```

**禁用**服务

```update-rc.d [mysql] disable```

**强制移除**服务

```update-rc.d -f [mysql] remove```

# SYNOPSIS

**update-rc.d** [**-f**] _name_ _action_

# PARAMETERS

**defaults**
> 以默认的启动/停止运行级别添加服务

**enable**
> 允许服务开机自启

**disable**
> 禁止服务开机自启

**remove**
> 移除该服务的全部符号链接

**-f, --force**
> 即使 init 脚本仍然存在也强制移除

**-n**
> 试运行，仅显示将要执行的操作

# DESCRIPTION

**update-rc.d** 用于安装和删除 System-V 风格的 init 脚本链接。它管理 **/etc/rc?.d/** 目录中的符号链接，这些链接决定了各个运行级别下会启动哪些服务。

使用此命令前，init 脚本必须已经放置在 **/etc/init.d/** 中。该工具主要用于仍采用传统 SysV init 的 Debian 系系统。

# CAVEATS

需要 root 权限。在使用 systemd 的系统上，此命令可能只是兼容性封装。安装前 init 脚本必须存在于 **/etc/init.d/** 中。现代基于 systemd 的系统请改用 **systemctl**。

# SEE ALSO

[systemctl](/man/systemctl)(1), [service](/man/service)(8), [chkconfig](/man/chkconfig)(8)
