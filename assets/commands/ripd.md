# TAGLINE

RIP 路由协议守护进程

# TLDR

**启动 RIP 守护进程**

```ripd -d```

**使用配置文件启动**

```ripd -d -f [/etc/frr/ripd.conf]```

**通过 VTY 连接到运行中的守护进程**

```vtysh -d ripd```

**将 VTY 绑定到 localhost 启动**

```ripd -d -A 127.0.0.1```

**打开交互式终端会话**

```ripd -t```

# SYNOPSIS

**ripd** [_options_]

# PARAMETERS

**-d**, **--daemon**
> 以守护进程方式运行，初始化完成后转入后台。

**-f**, **--config_file** _file_
> 配置文件（默认：/etc/frr/ripd.conf）。

**-t**, **--terminal**
> 在终端上打开交互式 VTY 会话。

**-A**, **--vty_addr** _addr_
> VTY 绑定地址。

**-P**, **--vty_port** _port_
> VTY 端口（默认：2602）。设为 0 表示禁用。

**-i**, **--pid_file** _file_
> PID 文件路径（默认：/var/run/frr/ripd.pid）。

**-z**, **--zclient_path** _path_
> 覆盖用于与 zebra 通信的 ZAPI 套接字路径。

**-u**, **--user** _user_
> 以指定用户身份运行。

**-g**, **--group** _group_
> 以指定组身份运行。

# DESCRIPTION

**ripd** 是 Quagga/FRRouting 中的 RIP（Routing Information Protocol，路由信息协议）守护进程。它实现了 RIPv1 和 RIPv2，适用于中小型网络的动态路由。

# EXAMPLES

```bash
# Start daemon
ripd -d -f /etc/frr/ripd.conf

# Connect via vtysh
vtysh
router rip
  network 192.168.1.0/24
  version 2
```

# CONFIGURATION

**/etc/frr/ripd.conf**（FRRouting）/ **/etc/quagga/ripd.conf**（Quagga）
> 主配置文件，定义 RIP 网络、版本、重分发规则和接口设置。

# CAVEATS

属于 FRRouting（或旧版 Quagga）的一部分。需要 zebra 守护进程处于运行状态。RIP 的最大跳数为 15，且收敛速度慢。更大的网络请使用 OSPF。

# HISTORY

ripd 是 **Quagga** 路由套件（从 GNU Zebra 分叉而来）的组成部分，后来也属于 Unix 路由守护进程套件 **FRRouting**。

# INSTALL

```apk: sudo apk add quagga```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zebra](/man/zebra)(8), [ospfd](/man/ospfd)(8), [vtysh](/man/vtysh)(1), [bgpd](/man/bgpd)(8)
