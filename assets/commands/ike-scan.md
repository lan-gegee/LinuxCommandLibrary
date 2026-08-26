# TAGLINE

发现并识别 IPsec VPN 服务器指纹

# TLDR

**扫描 IKE 主机**

```sudo ike-scan [192.168.1.0/24]```

**积极模式**

```sudo ike-scan -A [target]```

**指定变换集**

```sudo ike-scan --trans=[5,2,1,2] [target]```

**显示厂商 ID**

```sudo ike-scan -M [target]```

**源端口**

```sudo ike-scan -s [500] [target]```

# SYNOPSIS

**ike-scan** [_options_] _targets_

# PARAMETERS

_TARGETS_
> IP 地址或地址范围。

**-A**, **--aggressive**
> 积极模式。

**-M**, **--multiline**
> 多行输出。

**--trans** _SET_
> 变换（transform）集合。

**-s** _PORT_
> 源端口。

**-d** _PORT_
> 目的端口。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ike-scan** 发现并识别 IPsec VPN 服务器的指纹。它发送 IKE 数据包并分析响应，以识别 VPN 实现。

该工具通过 IKE 协议扫描进行安全评估。它能识别厂商、版本和支持的变换集。

# CAVEATS

安全测试工具。需要获得授权。使用 UDP 端口 500。

# HISTORY

ike-scan 由 **Roy Hills** 开发，用于 IPsec VPN 的发现和指纹识别。

# INSTALL

```apt: sudo apt install ike-scan```

```brew: brew install ike-scan```

```nix: nix profile install nixpkgs#ike-scan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [ipsec](/man/ipsec)(8)
