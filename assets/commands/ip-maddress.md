# TAGLINE

管理链路层组播地址

# TLDR

**列出**所有组播地址

```ip maddress```

列出**特定设备**的组播地址

```ip maddress show dev [eth0]```

静态**加入**一个组播组

```sudo ip maddress add [33:33:00:00:00:02] dev [eth0]```

**离开**一个组播组

```sudo ip maddress delete [33:33:00:00:00:02] dev [eth0]```

显示**帮助**

```ip maddress help```

# SYNOPSIS

**ip maddress** [_command_] [_options_]

# PARAMETERS

**show** [**dev** _DEVICE_]
> 显示组播地址（可选指定具体设备）

**add** _ADDRESS_ **dev** _DEVICE_
> 在指定设备上加入一个组播组

**delete** _ADDRESS_ **dev** _DEVICE_
> 在指定设备上离开一个组播组

**help**
> 显示帮助信息

# DESCRIPTION

**ip maddress** 用于管理链路层组播地址。它显示设备订阅了哪些组播组，并允许手动添加或移除静态组播成员关系。

组播地址实现一对多通信：单个数据包可以被加入了该组播组的多个主机接收。这常用于服务发现、流媒体传输和集群通信。

# CAVEATS

添加和删除组播地址需要 root 权限。更改在重启后不会保留。应用层的组播（IGMP）则另行处理。

# HISTORY

ip maddress 命令是 iproute2 的一部分，后者是旧 net-tools 软件包的现代替代品。iproute2 由 Alexey Kuznetsov 自 **1999** 年起开发，旨在为 Linux 网络功能提供统一的管理接口。

# SEE ALSO

[ip](/man/ip)(8), [ip-link](/man/ip-link)(8), [ip-address](/man/ip-address)(8)
