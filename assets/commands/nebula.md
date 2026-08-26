# TAGLINE

跨网络连接主机的可扩展 overlay 组网工具

# TLDR

**生成 CA 证书**

```nebula-cert ca -name "[My Organization]"```

**签署主机证书**

```nebula-cert sign -name "[server1]" -ip "[10.0.0.1/24]"```

**带组签署**

```nebula-cert sign -name "[web1]" -ip "[10.0.0.2/24]" -groups "[servers,web]"```

**启动 Nebula**

```nebula -config [/etc/nebula/config.yaml]```

**打印证书详情**

```nebula-cert print -path [host.crt]```

**验证证书**

```nebula-cert verify -ca [ca.crt] -crt [host.crt]```

**生成示例配置**

```nebula -print-default```

# SYNOPSIS

**nebula** [_options_]

**nebula-cert** _command_ [_options_]

# NEBULA OPTIONS

**-config** _path_
> 配置文件路径。

**-test**
> 测试配置后退出。

**-print-default**
> 打印默认配置。

**-version**
> 显示版本信息。

# NEBULA-CERT COMMANDS

**ca**
> 生成 CA 证书和密钥。

**sign**
> 签署主机证书。

**print**
> 打印证书详情。

**verify**
> 对照 CA 验证证书。

# CA OPTIONS

**-name** _name_
> CA 名称。

**-duration** _duration_
> 有效期。默认：1 年。

**-out-crt** _path_
> CA 证书输出路径。

**-out-key** _path_
> CA 密钥输出路径。

# SIGN OPTIONS

**-name** _name_
> 主机名。

**-ip** _cidr_
> 带子网的 Nebula IP 地址。

**-groups** _list_
> 以逗号分隔的组名列表。

**-ca-crt** _path_
> CA 证书路径。

**-ca-key** _path_
> CA 密钥路径。

**-out-crt** _path_
> 主机证书输出路径。

**-out-key** _path_
> 主机密钥输出路径。

**-duration** _duration_
> 证书有效期。

# DESCRIPTION

**nebula** 是一款可扩展的 overlay 组网工具，用于跨网络连接主机。它使用基于证书的身份验证和对等（peer-to-peer）连接。

每个 Nebula 网络都有一个为各主机证书签名的 CA。证书定义主机的 Nebula IP 地址及其所属组，用于访问控制。

**Lighthouse** 是帮助其他节点相互发现的已知节点。至少需要一台拥有公网 IP 的 lighthouse。节点一旦互相发现，即可直接点对点通信。

配置文件（YAML）定义 CA、主机证书/密钥、lighthouse、防火墙规则和网络设置。防火墙规则使用证书中的组进行访问控制。

Nebula 通过 UDP 打洞穿透 NAT。NAT 后面的节点可以直接通信，无需经由中心服务器转发。

# CAVEATS

lighthouse 上的 UDP 端口（默认 4242）必须可达。证书校验依赖时钟同步。吊销证书需要重新分发。某些 NAT 类型可能无法打洞。

# HISTORY

Nebula 由 **Slack** 开发，并于 **2019 年 11 月**开源。它最初是为了安全地连接 Slack 的全球基础设施而构建的。该项目以简洁和高可扩展性为目标，采用现代密码学和组网原理。需要在跨云服务商与本地基础设施之间构建软件定义网络的组织都在使用 Nebula。

# INSTALL

```apt: sudo apt install nebula```

```dnf: sudo dnf install nebula```

```pacman: sudo pacman -S nebula```

```apk: sudo apk add nebula```

```zypper: sudo zypper install nebula```

```brew: brew install nebula```

```nix: nix profile install nixpkgs#nebula```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[headscale](/man/headscale)(1), [tailscale](/man/tailscale)(1), [zerotier-one](/man/zerotier-one)(1)
