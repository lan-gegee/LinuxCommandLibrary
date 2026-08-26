# TAGLINE

Kerberos 票据授予票据请求工具

# TLDR

使用密码**获取 TGT**

```getTGT.py [domain]/[username]:[password] -dc-ip [dc_ip]```

使用 NTLM 哈希**获取 TGT**

```getTGT.py [domain]/[username] -hashes :[nthash] -dc-ip [dc_ip]```

使用 AES 密钥**获取 TGT**

```getTGT.py [domain]/[username] -aesKey [aes_key] -dc-ip [dc_ip]```

不内联传入密码，改为**交互式提示输入密码**

```getTGT.py [domain]/[username] -dc-ip [dc_ip]```

# SYNOPSIS

**getTGT.py** _domain_/_user_[:_password_] [_options_]

# PARAMETERS

_DOMAIN/USER_[:_PASSWORD_]
> 目标身份。密码为可选；省略时会提示输入。

**-dc-ip** _IP_
> 域控制器的 IP 地址。省略时默认为域名 FQDN。

**-hashes** _LMHASH:NTHASH_
> 用于认证的 NTLM 哈希。LM 部分可以留空（`:NTHASH`）。

**-aesKey** _KEY_
> 用于 Kerberos 认证的 AES 密钥（128 或 256 位）。

**-k**
> 使用 ccache 文件（KRB5CCNAME）中的 Kerberos 凭据，失败时回退到所提供的凭据。

**-no-pass**
> 不提示输入密码，与 -k 配合使用很有用。

**-debug**
> 开启 DEBUG 输出。

**-ts**
> 为每条日志行添加时间戳。

# DESCRIPTION

**getTGT.py** 是一个 Impacket 示例脚本，给定密码、NTLM 哈希或 AES 密钥时，向 Active Directory 域控制器请求 Kerberos 票据授予票据（TGT）。官方描述如下："Given a password, hash or aesKey, it will request a TGT and save it as ccache."

生成的票据会写入以主体名命名的 ccache 文件（例如 `username.ccache`）。将 **KRB5CCNAME** 环境变量指向该文件后，其他 Impacket 工具或原生工具即可复用该票据进行 pass-the-ticket 认证。

该脚本没有专门的输出标志：ccache 文件名自动由用户名派生。

# CAVEATS

**仅限授权测试。**需要有效凭据并与域控制器时钟同步，因为较大的时间偏差会导致 Kerberos 失败。票据的有效期有限。

# HISTORY

getTGT.py 是 **Impacket** 的一部分。Impacket 是用于 Active Directory 安全测试的 Python 网络协议工具集，最初由 Core Security 开发，现由 Fortra 维护。

# SEE ALSO

[getuserspns.py](/man/getuserspns.py)(1), [kerberos](/man/kerberos)(7), [kinit](/man/kinit)(1)
