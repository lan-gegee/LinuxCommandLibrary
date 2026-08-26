# TAGLINE

Quagga 路由管理守护进程

# TLDR

**启动 zebra 守护进程**

```sudo zebra -d```

**使用指定的配置文件启动**

```sudo zebra -d -f [/etc/quagga/zebra.conf]```

**在前台运行**

```sudo zebra -A [127.0.0.1]```

**在指定端口上启动 VTY**

```sudo zebra -d -P [2601]```

**连接 zebra shell**

```telnet localhost 2601```

# SYNOPSIS

**zebra** [_options_]

# PARAMETERS

**-d**, **--daemon**
> 作为守护进程在后台运行。

**-f**, **--config_file** _file_
> 使用指定的配置文件。

**-P**, **--vty_port** _port_
> VTY（telnet）端口号。

**-A**, **--vty_addr** _address_
> VTY 绑定地址。

**-u**, **--user** _user_
> 以指定用户身份运行。

**-g**, **--group** _group_
> 以指定组身份运行。

**-v**, **--version**
> 显示版本。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**zebra** 是 Quagga（前身为 GNU Zebra）的核心路由管理守护进程。它管理内核路由表，并提供 Zserv API，供 ospfd、bgpd、ripd 等协议守护进程传递路由更新。

Zebra 对内核的路由接口做了抽象，使协议守护进程可以跨各种 Unix 变体移植。它接收来自协议守护进程的路由，并将其安装到内核 FIB（转发信息库）中。

配置使用类 Cisco 的 CLI，可通过 telnet 或 vtysh 统一 shell 访问。通过该界面可以查看路由并配置静态路由。

# CONFIGURATION

配置文件：/etc/quagga/zebra.conf

定义接口、静态路由和访问控制。各协议守护进程有单独的配置文件。

# CAVEATS

Quagga 在很大程度上已被 FRRouting（FRR）取代。应修改默认的 VTY 密码。需要 root 权限或 CAP_NET_ADMIN 能力。

# HISTORY

**zebra** 源自 Kunihiro Ishiguro 发起的 GNU Zebra 项目，该项目于 2005 年停止开发。Quagga 从其分叉出来并持续维护，直到 2017 年 FRRouting 又从 Quagga 分叉，以实现更快、更开放的开发。zebra 守护进程的名字在这两个项目中都得以延续。

# INSTALL

```apk: sudo apk add quagga```

```brew: brew install zebra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ospfd](/man/ospfd)(8), [bgpd](/man/bgpd)(8), [ripd](/man/ripd)(8), [vtysh](/man/vtysh)(1)
