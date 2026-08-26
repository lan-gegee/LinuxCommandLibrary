# TAGLINE

扫描目标上正在监听的 DCE/RPC 接口

# TLDR

在目标上**枚举 RPC 端点**

```impacket-rpcmap '[domain]/[user]:[password]@[192.168.1.100]'```

以空凭据**枚举 RPC 端点**

```impacket-rpcmap -no-pass '[192.168.1.100]'```

**使用 NTLM 哈希**代替密码**枚举**

```impacket-rpcmap -hashes ':[nthash]' '[domain]/[user]@[192.168.1.100]'```

在特定端口上**扫描 RPC 端点**

```impacket-rpcmap -port [135] '[domain]/[user]:[password]@[192.168.1.100]'```

对发现的接口**暴力枚举操作号**

```impacket-rpcmap -brute-opnums '[domain]/[user]:[password]@[192.168.1.100]'```

**使用特定的 RPC 传输**（ncacn_ip_tcp）

```impacket-rpcmap 'ncacn_ip_tcp:[192.168.1.100]'```

# SYNOPSIS

**impacket-rpcmap** [_-h_] [_-port PORT_] [_-hashes LMHASH:NTHASH_] [_-no-pass_] [_-k_] [_-aesKey KEY_] _target_

# PARAMETERS

**-port** _PORT_
> 要查询的目标端口（默认：135）

**-hashes** _LMHASH:NTHASH_
> 使用 NTLM 哈希而非密码进行身份验证

**-no-pass**
> 不询问密码

**-k**
> 使用 ccache 文件中的 Kerberos 身份验证

**-aesKey** _KEY_
> 用于 Kerberos 身份验证的 AES 密钥

**-brute-opnums**
> 对每个发现的接口暴力枚举操作号

**-brute-uuids**
> 暴力枚举 UUID 以发现隐藏的接口

**-auth-level** _LEVEL_
> 身份验证级别（1-6，默认：6/PKT_PRIVACY）

# DESCRIPTION

**impacket-rpcmap** 扫描目标系统上正在监听的 DCE/RPC 接口。它可以查询 RPC 端点映射器（通常在端口 135），也可以使用各种 RPC 传输（ncacn_ip_tcp、ncacn_np、ncacn_http）直接探测特定端口。

该工具连接到端点映射器（通常在端口 135），并检索已注册 RPC 接口的列表，包括它们的 UUID、版本和绑定信息。

# CAVEATS

端点映射器可能根据身份验证级别限制返回的信息。某些 RPC 服务可能未向端点映射器注册。防火墙规则可能阻止对 RPC 端口的访问。

# HISTORY

属于 SecureAuth 的 **Impacket** 库。RPC 枚举是 Windows 环境中的基础侦察技术，可以揭示可用的攻击面。

# SEE ALSO

[rpcclient](/man/rpcclient)(1), [impacket-getnpusers](/man/impacket-getnpusers)(1), [impacket-getadusers](/man/impacket-getadusers)(1), [nmap](/man/nmap)(1)
