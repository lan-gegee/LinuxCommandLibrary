# TAGLINE

来自 FRRouting 的 OSPF 路由守护进程

# TLDR

**启动 OSPF 守护进程**

```ospfd -d```

**使用配置文件启动**

```ospfd -f [/etc/frr/ospfd.conf]```

**带调试启动**

```ospfd -d -A [127.0.0.1]```

**在前台运行**

```ospfd -A [127.0.0.1]```

# SYNOPSIS

**ospfd** [_options_]

# PARAMETERS

**-d**
> 以守护进程方式运行。

**-f** _file_
> 配置文件。

**-A** _address_
> VTY 绑定地址。

**-P** _port_
> VTY 端口。

**-u** _user_
> 以指定用户运行。

**-g** _group_
> 以指定组运行。

# DESCRIPTION

**ospfd** 是 FRRouting（或 Quagga）的 OSPF（Open Shortest Path First，开放式最短路径优先）路由守护进程。它实现用于 IPv4 路由的 OSPF 第 2 版，为网络提供动态路由能力。

OSPF 是企业网络中常用的链路状态路由协议。

# CONFIGURATION

```
! /etc/frr/ospfd.conf
router ospf
  ospf router-id 1.1.1.1
  network 192.168.1.0/24 area 0
  network 10.0.0.0/8 area 1
```

# VTY COMMANDS

```
show ip ospf neighbor
show ip ospf route
show ip ospf database
```

# CAVEATS

属于 FRRouting 套件。需要 zebra 守护进程。建议通过 vtysh 进行配置。

# HISTORY

ospfd 最初是 GNU Zebra 的组成部分，之后属于 Quagga，如今作为 **FRRouting**——领先的开源路由套件——的一部分进行维护。

# INSTALL

```apk: sudo apk add quagga```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zebra](/man/zebra)(8), [vtysh](/man/vtysh)(1), [bgpd](/man/bgpd)(8), [ripd](/man/ripd)(8)
