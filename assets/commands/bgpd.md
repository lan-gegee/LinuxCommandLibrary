# TAGLINE

边界网关协议路由守护进程

# TLDR

**以默认配置启动 bgpd**

```bgpd```

**以指定的配置文件启动**

```bgpd -f [/etc/bgpd.conf]```

**以前台方式运行**并输出调试信息

```bgpd -d```

**仅检查配置语法**而不启动

```bgpd -n```

**以详细日志启动**

```bgpd -v```

# SYNOPSIS

**bgpd** [**-dnv**] [**-D** _macro=value_] [**-f** _file_]

# DESCRIPTION

**bgpd** 是 OpenBGPD 项目的边界网关协议守护进程。它管理与对等路由器的 BGP 会话，并维护路由信息库（RIB），用于在自治系统之间交换路由信息。

BGP 是让互联网得以运作的协议，它实现不同网络（自治系统）之间的路由。bgpd 实现 BGP-4，支持路由过滤、community、本地优先级、MED 和 AS 路径操作等特性。

该守护进程从 /etc/bgpd.conf 读取配置，其中定义了邻居、过滤器和路由策略。初始化完成后它会以非特权用户身份运行，并与 bgpctl 通信以进行运行时管理。

# PARAMETERS

**-d**
> 以前台方式运行，不进行守护进程化。

**-D** _macro=value_
> 定义一个供配置使用的宏。

**-f** _file_
> 使用指定的配置文件。

**-n**
> 仅检查配置语法。

**-v**
> 输出详细日志。

**-V**
> 显示版本信息。

# CAVEATS

在公共互联网上运行 BGP 守护进程需要与上游提供商协调并拥有有效的 AS 号分配。配置错误可能导致影响网络连通性的路由问题。bgpd 启动需要 root 权限，但初始化后会放弃特权。配置更改通常需要重启或重载信号才能生效。

# HISTORY

**OpenBGPD** 由 Henning Brauer 和 Claudio Jeker 自 **2003 年**起为 **OpenBSD** 开发，是 OpenBSD 网络协议栈的一部分。在其他路由守护进程暴露漏洞和复杂性问题之后，它被创建为一个安全、干净的 BGP 实现。面向 Linux 和 FreeBSD 的可移植版本自 **2016 年**起持续维护。ISP 和网络运营商看重其简洁性与安全性而使用 OpenBGPD。

# INSTALL

```apt: sudo apt install openbgpd```

```dnf: sudo dnf install openbgpd```

```apk: sudo apk add quagga```

```nix: nix profile install nixpkgs#openbgpd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bgpctl](/man/bgpctl)(8), [ospfd](/man/ospfd)(8), [bird](/man/bird)(8)
