# TAGLINE

从 Active Directory 域请求 Kerberos 票据授予票据（TGT）

# TLDR

为拥有密码的域用户**请求 TGT**

```impacket-gettgt '[domain]/[user]:[password]'```

**请求 TGT** 并保存到指定文件

```impacket-gettgt -dc-ip [192.168.1.100] '[domain]/[user]:[password]'```

**使用 NTLM 哈希请求 TGT**

```impacket-gettgt -hashes ':[nthash]' '[domain]/[user]'```

**使用 AES 密钥请求 TGT**

```impacket-gettgt -aesKey '[aes256key]' '[domain]/[user]'```

# SYNOPSIS

**impacket-gettgt** [_-h_] [_-hashes LMHASH:NTHASH_] [_-no-pass_] [_-k_] [_-aesKey KEY_] [_-dc-ip IP_] [_-service SPN_] _target_

# PARAMETERS

**-hashes** _LMHASH:NTHASH_
> 使用 NTLM 哈希而非密码进行身份验证。

**-no-pass**
> 不询问密码（与 **-k** 搭配时有用）。

**-k**
> 使用 Kerberos 身份验证；从 ccache 文件（KRB5CCNAME）获取凭据。

**-aesKey** _KEY_
> 用于 Kerberos 身份验证的 AES 密钥（128 或 256 位）。

**-dc-ip** _IP_
> 域控制器（KDC）的 IP 地址。省略时使用身份中的域部分。

**-service** _SPN_
> 通过 AS-REQ 直接为给定 SPN 请求服务票据。

**-principalType** _TYPE_
> 主体名称类型（默认 NT_PRINCIPAL）。

**-debug**
> 启用调试输出。

# DESCRIPTION

**impacket-gettgt** 从 Active Directory 域控制器请求 Kerberos 票据授予票据（TGT）。TGT 会保存到 ccache 文件中，可供后续与其他工具进行 Kerberos 身份验证时使用。

当你持有有效凭据（密码、哈希或 AES 密钥）并需要向支持 Kerberos 的服务进行身份验证时，该工具可用于获取 Kerberos 票据。生成的 ccache 文件可通过 KRB5CCNAME 环境变量导出。

# CAVEATS

需要某种形式的有效域凭据（密码、NTLM 哈希或 AES 密钥）。域控制器必须可达，且 Kerberos 端口（88/tcp）必须可访问。客户端与 KDC 之间的时间同步对 Kerberos 正常工作至关重要。

# HISTORY

属于 SecureAuth 的 **Impacket** 库，用 Python 实现了用于渗透测试的 Kerberos 协议。TGT 获取是基于 Kerberos 的攻击和身份验证工作流中的基础操作。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[impacket-getst](/man/impacket-getst)(1), [kinit](/man/kinit)(1), [impacket-secretsdump](/man/impacket-secretsdump)(1)
