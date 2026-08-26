# TAGLINE

用于 IP 地址分配的 ISC DHCP 服务器守护进程

# TLDR

**启动 DHCP 服务器**

```sudo dhcpd```

**在指定接口上启动**

```sudo dhcpd [eth0]```

**以前台方式启动**（调试）

```sudo dhcpd -f -d```

**测试配置文件**

```sudo dhcpd -t```

**使用其他配置文件**

```sudo dhcpd -cf [/path/to/dhcpd.conf]```

**使用其他租约文件**

```sudo dhcpd -lf [/path/to/dhcpd.leases]```

# SYNOPSIS

**dhcpd** [_options_] [_interfaces_]

# PARAMETERS

**-f**
> 以前台方式运行。

**-d**
> 将日志输出到 stderr（隐含 -f）。

**-t**
> 测试配置后退出。

**-T**
> 测试租约文件后退出。

**-cf** _file_
> 使用其他配置文件。

**-lf** _file_
> 使用其他租约数据库。

**-pf** _file_
> 使用其他 PID 文件。

**-4** / **-6**
> 强制 IPv4 或 IPv6 模式。

**-p** _port_
> 监听其他 UDP 端口（默认 67）。

**-s** _address_
> 将应答发送到指定地址而不是广播。

**-q**
> 安静启动（不显示版权信息）。

**-user** _user_
> 在特权操作完成后 setuid 为指定用户。

**-group** _group_
> 在特权操作完成后 setgid 为指定组。

**-chroot** _dir_
> chroot 到指定目录。

**-tf** _tracefile_
> 记录启动状态和事务以便调试。

**--no-pid**
> 不写 PID 文件。

**--version**
> 显示版本并退出。

# CONFIGURATION

**/etc/dhcp/dhcpd.conf**:
```
subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.100 192.168.1.200;
  option routers 192.168.1.1;
  option domain-name-servers 8.8.8.8, 8.8.4.4;
  default-lease-time 600;
  max-lease-time 7200;
}

host server1 {
  hardware ethernet 00:11:22:33:44:55;
  fixed-address 192.168.1.10;
}
```

# DESCRIPTION

**dhcpd** 是 Internet Systems Consortium (ISC) 的 DHCP 服务器守护进程。它使用动态主机配置协议为本地网络上的客户端分配 IP 地址和网络配置。

服务器维护一个租约数据库，跟踪哪些地址分配给了哪些客户端。配置中定义地址池、租约时长以及网关、DNS 服务器、域名等选项。

静态分配可以为已知的 MAC 地址保留特定地址。该服务器还能提供 PXE 启动选项、面向特定厂商的自定义选项，以及用于高可用性的故障转移配置。

# CAVEATS

需要 root 权限并必须绑定 67 端口。租约文件必须可写。同一网络上的多台 DHCP 服务器若未配置故障转移会产生冲突。IPv6 支持（dhcpd -6）使用不同的配置语法。

# HISTORY

ISC DHCP 由 Internet Systems Consortium 的 **Ted Lemon** 开发，首次发布于 **1997 年**。它曾是 Unix 系统上的参考 DHCP 实现。ISC 于 **2022 年**宣布 ISC DHCP 生命周期终止，建议迁移到下一代 ISC DHCP 服务器 **Kea**。

# INSTALL

```apt: sudo apt install isc-dhcp-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dhclient](/man/dhclient)(8)
