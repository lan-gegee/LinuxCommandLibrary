# TAGLINE

以太坊网络引导节点

# TLDR

**生成节点密钥**

```bootnode -genkey [node.key]```

使用现有密钥**运行引导节点**

```bootnode -nodekey [node.key]```

在**指定地址**和端口上运行

```bootnode -nodekey [node.key] -addr [192.168.1.1:30301]```

**将节点 URL 写入**文件

```bootnode -nodekey [node.key] -writeaddress```

以详细日志**运行**

```bootnode -nodekey [node.key] -verbosity [4]```

# SYNOPSIS

**bootnode** [_options_]

# DESCRIPTION

**bootnode** 运行以太坊发现协议的引导节点。引导节点帮助新节点发现并连接以太网网络中的对等节点，而自身不必成为全节点。

该工具是 go-ethereum（geth）项目的一部分，实现了节点发现协议 v4 和 v5，支撑点对点网络的组建。

# PARAMETERS

**-genkey** _file_
> 生成新的节点密钥并保存到文件。

**-nodekey** _file_
> 节点私钥文件的路径。

**-addr** _ip:port_
> 监听地址（默认：:30301）。

**-writeaddress**
> 将节点的公钥/URL 输出到 stdout。

**-verbosity** _level_
> 日志详细程度（0=静默，5=最详细）。

**-nat** _method_
> NAT 端口映射机制（none、upnp、pmp、extip:IP）。

**-netrestrict** _CIDR_
> 将网络通信限制在给定的 CIDR 范围内。

**-v5**
> 启用 Discovery v5 协议。

# CAVEATS

引导节点应有稳定且可公开访问的 IP 地址。节点密钥标识着该节点，必须妥善保管。引导节点不参与区块链共识，也不存储链数据。

# HISTORY

bootnode 由以太坊基金会作为 **go-ethereum** 项目的一部分开发。它实现了类 Kademlia 的发现协议，使以太坊的点对点网络无需中心化协调即可运转。

# SEE ALSO

[geth](/man/geth)(1)
