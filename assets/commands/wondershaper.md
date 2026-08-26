# TAGLINE

简单的网络带宽限制器

# TLDR

**限制带宽**

```wondershaper [eth0] [1024] [512]```

**清除限制**

```wondershaper clear [eth0]```

**显示当前限制**

```wondershaper [eth0]```

**使用长选项**

```wondershaper -a [eth0] -d [1024] -u [512]```

# SYNOPSIS

**wondershaper** [_-a interface_] [_-d down_] [_-u up_] | _interface_ _down_ _up_

# PARAMETERS

**-a** _IFACE_
> 接口名称。

**-d** _KBPS_
> 下载限速。

**-u** _KBPS_
> 上传限速。

**clear**
> 移除限制。

# DESCRIPTION

**wondershaper** 是一个简单的 shell 脚本，它使用 Linux 流量控制按网络接口限制带宽。它提供了一种简便的方式来设置以千比特每秒为单位的下载和上传速度限制，而无需直接理解复杂的 tc 命令语法。

该工具的工作原理是向指定的网络接口应用流量整形规则。可以通过简单的命令显示、设置或清除限制。它常用于在带宽受限条件下测试应用程序，或防止单台机器占满共享的网络连接。

# CAVEATS

需要 root 权限。是围绕 tc 的脚本封装。数值单位为 kbps。

# HISTORY

**wondershaper** 作为使用 Linux 流量控制来限制网络带宽的简单脚本而创建。

# INSTALL

```dnf: sudo dnf install wondershaper```

```zypper: sudo zypper install wondershaper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tc](/man/tc)(8), [iptables](/man/iptables)(8), [trickle](/man/trickle)(1)
