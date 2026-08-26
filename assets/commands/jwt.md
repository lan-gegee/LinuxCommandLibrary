# TAGLINE

编码和解码 JSON Web Token

# TLDR

**解码 JWT**

```jwt decode [token]```

**编码 JWT**

```jwt encode --secret [secret] --payload '[{"sub":"user"}]'```

**不验证签名解码**

```jwt decode --no-verify [token]```

**显示头部**

```jwt decode --header [token]```

**以指定算法编码**

```jwt encode --alg [HS256] --secret [key] --payload '[{}]'```

# SYNOPSIS

**jwt** _command_ [_options_]

# PARAMETERS

**decode** _TOKEN_
> 解码 JWT 令牌。

**encode**
> 创建 JWT 令牌。

**--secret** _SECRET_
> 签名密钥。

**--payload** _JSON_
> 令牌载荷。

**--alg** _ALG_
> 签名算法。

**--no-verify**
> 跳过签名验证。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jwt** 用于编码和解码 JSON Web Token。它可以为身份认证系统创建和验证 JWT。

该工具支持多种签名算法，并可显示令牌内容以便调试。

# CAVEATS

存在多种实现。涉及安全敏感操作。请仔细核对所用算法。

# HISTORY

各类 jwt CLI 工具为 **JSON Web Token** 的编码和解码提供了命令行入口，便于测试和调试。

# INSTALL

```apt: sudo apt install jwt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1), [jq](/man/jq)(1)
