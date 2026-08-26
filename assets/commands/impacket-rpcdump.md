# TAGLINE

枚举目标系统上的 RPC 端点

# TLDR

**导出 RPC 端点**

```impacket-rpcdump [target]```

**使用身份验证导出**

```impacket-rpcdump [domain]/[user]:[password]@[target]```

**指定端口**

```impacket-rpcdump -port [135] [target]```

# SYNOPSIS

**impacket-rpcdump** [_options_] _target_

# PARAMETERS

**-port** _PORT_
> RPC 端点端口（默认 _135_）。

**-target-ip** _IP_
> 覆盖连接所用的 IP（当目标以主机名给出时很有用）。

**-hashes** _LMHASH:NTHASH_
> 通过哈希传递（Pass-the-Hash）进行身份验证，而不是提供密码。

**-no-pass**
> 不询问密码（单独使用 **-hashes** 或 **-k** 时）。

**-k**
> 使用 Kerberos 身份验证。凭据从 **ccache** 读取（由 **kinit** 设置）。

**-aesKey** _HEX_
> 用于 Kerberos 身份验证的 AES 密钥。

**-dc-ip** _IP_
> Kerberos 所用域控制器的 IP。

**-debug**
> 打印详细的协议级输出。

# DESCRIPTION

**impacket-rpcdump** 查询微软 RPC 端点映射器（默认端口 135），并打印每个已注册的端点、其 UUID 以及它支持的绑定方式（命名管道、TCP/UDP 端口）。它是微软经典工具 **rpcdump.exe** 的 Python/Impacket 版本，常用于经授权的渗透测试中枚举暴露的 Active Directory 服务。

提供凭据（明文密码、NTLM 哈希或 Kerberos 票据）时，列表中可能会出现需要身份验证的额外服务；未经身份验证的导出通常只返回可匿名访问的少量端点。

# CAVEATS

**仅限用于经授权的测试**。在现代 Windows 版本上，某些服务会限制匿名端点枚举（例如 **RestrictRemoteSAM**），因此输出为空并不代表没有服务在运行。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[impacket-rpcmap](/man/impacket-rpcmap)(1), [rpcclient](/man/rpcclient)(1)
