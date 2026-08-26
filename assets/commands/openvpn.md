# TAGLINE

使用 SSL/TLS 进行密钥交换的开源 VPN 方案

# TLDR

**使用配置文件连接**

```sudo openvpn --config [client.ovpn]```

**使用认证文件连接**

```sudo openvpn --config [client.ovpn] --auth-user-pass [credentials.txt]```

**以守护进程方式启动**

```sudo openvpn --config [client.ovpn] --daemon```

**生成静态密钥**

```openvpn --genkey secret [static.key]```

**不连接而测试配置**

```openvpn --config [client.ovpn] --verb 3 --pull```

**显示版本和编译选项**

```openvpn --version```

# SYNOPSIS

**openvpn** [_--config file_] [_--remote host_] [_--dev tun_|_tap_] [_--ca file_] [_--cert file_] [_--key file_] [_options_]

# PARAMETERS

**--config** _file_
> 从文件读取配置。

**--remote** _host_ [_port_]
> 远程 VPN 服务器地址。

**--port** _num_
> 本地和远程端口号。

**--dev** _type_
> TUN/TAP 设备类型（tun、tap）。

**--proto** _proto_
> 协议：udp、tcp-client、tcp-server。

**--ca** _file_
> CA 证书文件。

**--cert** _file_
> 本地证书文件。

**--key** _file_
> 本地私钥文件。

**--auth-user-pass** [_file_]
> 用户名/密码认证。

**--tls-auth** _file_ [_direction_]
> 在控制通道上进行 HMAC 认证。

**--cipher** _alg_
> 加密密码算法。

**--auth** _alg_
> HMAC 摘要算法。

**--compress** [_alg_]
> 压缩算法。

**--daemon** [_name_]
> 初始化后转入后台运行（守护进程化）。

**--log** _file_
> 记录日志到文件。

**--verb** _level_
> 日志详细级别（0-11）。

**--ping** _n_
> 每隔 n 秒 ping 一次远程端。

**--ping-restart** _n_
> 若 n 秒内无 ping 响应则重启。

**--script-security** _level_
> 脚本执行策略。

# DESCRIPTION

**OpenVPN** 是一种使用 SSL/TLS 进行密钥交换的开源 VPN 方案。它可以创建安全的点对点或站点到站点连接，运行于 UDP 或 TCP 之上。

存在两种模式：路由模式（TUN）和桥接模式（TAP）。TUN 模式创建点对点 IP 隧道，适合大多数 VPN 需求。TAP 模式桥接以太网帧，非 IP 协议需要使用该模式。

配置通常使用包含全部连接参数的 .ovpn 文件。这些文件可以内嵌证书或引用外部文件。商业 VPN 提供商会分发预配置好的 .ovpn 文件。

安全特性包括：基于证书的认证、完美前向保密、HMAC 包认证，以及可选的用户名/密码验证。TLS-auth 额外增加一层 HMAC 以防范 DoS 攻击。

客户端与服务器模式使用同一个二进制程序。服务器配置包括路由、客户端管理和多客户端处理。脚本可以在连接事件上执行，以实现动态路由和防火墙规则。

# CAVEATS

创建 TUN/TAP 设备需要 root/管理员权限。防火墙必须允许 VPN 流量。证书管理会增加复杂度。性能取决于所选密码算法和硬件。MTU 问题可能导致连接故障。部分网络会封锁 OpenVPN 的流量特征。

# HISTORY

**OpenVPN** 由 **James Yonan** 创建，于 **2001 年**首次发布。它被设计为 IPsec 的开源替代方案，控制通道采用标准 TLS。该项目已成为部署最广泛的 VPN 方案之一，被商业提供商和企业广泛使用。OpenVPN 3 引入了新的 C++ 核心库。

# INSTALL

```apt: sudo apt install openvpn```

```dnf: sudo dnf install openvpn```

```pacman: sudo pacman -S openvpn```

```apk: sudo apk add openvpn```

```zypper: sudo zypper install openvpn```

```brew: brew install openvpn```

```nix: nix profile install nixpkgs#openvpn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ipsec](/man/ipsec)(8), [stunnel](/man/stunnel)(8), [ssh](/man/ssh)(1)
