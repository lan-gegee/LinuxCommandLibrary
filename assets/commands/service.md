# TAGLINE

管理 SysV init 服务

# TLDR

列出所有服务的**名称和状态**

```service --status-all```

**启动/停止/重启/重载**某个服务

```service [service_name] [start|stop|restart|reload]```

执行**完整重启**（先 stop 后 start 运行脚本两次）

```service [service_name] --full-restart```

显示服务的**当前状态**

```service [service_name] status```

# SYNOPSIS

**service** _script_ _command_ [_options_]

**service** **--status-all**

# PARAMETERS

**--status-all**
> 列出所有服务的状态

_script_
> 服务名称（/etc/init.d/ 中的脚本）

**start**
> 启动服务

**stop**
> 停止服务

**restart**
> 先停止再启动服务

**reload**
> 重新加载服务配置

**status**
> 显示服务状态

**--full-restart**
> 执行完整的先停止后启动流程

# DESCRIPTION

**service** 是 /etc/init.d/ 中 init 脚本的包装器，为管理 SysV init 服务提供一致的接口。它会自动处理环境清理和路径规范化以执行 init 脚本。

在 systemd 系统上，service 通常会将命令转发给 systemctl 以保持向后兼容。它对于管理传统 init 脚本仍然有用，并为管理员提供了熟悉的接口。

# CAVEATS

在 systemd 系统上优先使用 **systemctl**。并非所有 init 脚本都实现全部命令（reload 可能不可用）。service 命令的大多数操作需要 root 权限。

# HISTORY

由 **Debian** 引入，随后被其他发行版采纳为 SysV init 脚本的标准接口。随着向 systemd 的过渡，service 成为了一个兼容包装器，在适当的情况下将命令转换为 systemctl 调用。

# INSTALL

```apt: sudo apt install runit-init```

```apk: sudo apk add openrc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [chkconfig](/man/chkconfig)(8), [update-rc.d](/man/update-rc.d)(8)
