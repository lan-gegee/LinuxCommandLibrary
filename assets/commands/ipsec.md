# TAGLINE

strongSwan/Libreswan IPsec VPN 实现的控制接口

# TLDR

**启动 IPsec 服务**

```sudo ipsec start```

**停止 IPsec 服务**

```sudo ipsec stop```

**检查状态**

```sudo ipsec status```

**显示所有连接**

```sudo ipsec statusall```

**重新加载配置**

```sudo ipsec reload```

**启动特定连接**

```sudo ipsec up [connection]```

**停止特定连接**

```sudo ipsec down [connection]```

**显示版本信息**

```ipsec --version```

从 ipsec.secrets **重新加载密钥**

```sudo ipsec rereadsecrets```

# SYNOPSIS

**ipsec** _command_ [_options_]

# PARAMETERS

**start**
> 启动 IPsec 守护进程。

**stop**
> 停止 IPsec 守护进程。

**restart**
> 重启守护进程。

**status**
> 显示活跃的连接。

**statusall**
> 显示详细状态。

**reload**
> 重新加载配置。

**up** _connection_
> 建立连接。

**down** _connection_
> 断开连接。

**update**
> 应用配置更改而无需完全重启。

**route** _connection_
> 为连接安装内核 IPsec 策略。

**unroute** _connection_
> 移除连接的内核 IPsec 策略。

**rereadsecrets**
> 从 ipsec.secrets 重新加载密钥。

**listalgs**
> 列出支持的加密算法。

**listcerts**
> 列出证书。

**listcacerts**
> 列出 CA 证书。

**listall**
> 列出全部信息。

**rereadall**
> 执行所有 reread 操作。

**--version**
> 显示版本信息。

# DESCRIPTION

**ipsec** 是 strongSwan/Libreswan IPsec VPN 实现的控制接口。它管理用于加密网络隧道的 IKE（Internet Key Exchange）连接。

IPsec 为 VPN 提供网络层加密，支持站点到站点隧道和远程访问。配置通常位于 /etc/ipsec.conf 和 /etc/ipsec.secrets 中。

# CONFIGURATION

```
# /etc/ipsec.conf
conn myvpn
    left=%defaultroute
    leftid=@myserver
    right=remote.example.com
    rightid=@remote
    auto=start
```

# CAVEATS

需要内核支持 IPsec。证书管理可能较为复杂。IKE（UDP 500、4500）需要相应的防火墙规则。可用 ipsec statusall 进行调试。

# HISTORY

IPsec 由 IETF 在 1990 年代标准化。strongSwan（2005 年从 FreeS/WAN 分叉而来）和 Libreswan 是 Linux 上主要的两个实现，提供 ipsec 命令接口。

# INSTALL

```apt: sudo apt install libreswan```

```dnf: sudo dnf install libreswan```

```pacman: sudo pacman -S strongswan```

```apk: sudo apk add strongswan```

```zypper: sudo zypper install strongswan```

```brew: brew install strongswan```

```nix: nix profile install nixpkgs#libreswan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip](/man/ip)(8), [openvpn](/man/openvpn)(8), [wg](/man/wg)(8)
