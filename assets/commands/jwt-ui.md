# TAGLINE

解码和编码 JSON Web Token 的终端界面工具

# TLDR

**以交互方式解码 JWT**

```jwt-ui [token]```

**从 stdin 解码**

```echo "[token]" | jwt-ui```

**使用密钥解码**

```jwt-ui -S [secret] [token]```

**从文件读取密钥解码**

```jwt-ui -S @[path/to/key.pem] [token]```

# SYNOPSIS

**jwt-ui** [**-S** _secret_] [_token_]

# DESCRIPTION

**jwt-ui** 是一个用于解码和编码 JSON Web Token 的终端界面工具，灵感来自 **jwt.io** 和 **jwt-cli**。它提供交互式界面，显示 JWT 的头部、载荷以及签名验证状态。

支持的算法包括 **HMAC**（HS256/384/512）、**RSA**（RS256/384/512、PS256/384/512）、**ECDSA**（ES256/384）和 **EdDSA**。密钥可以是纯文本、文件路径（加 **@** 前缀）或 base64 编码字符串（加 **b64:** 前缀）。

# CAVEATS

仅支持标准 JWT 格式。不支持加密 JWT（JWE）。在命令行参数中传递密钥可能将其暴露到 shell 历史记录中。

# HISTORY

**jwt-ui** 由 **jwt-rs** 组织开发，使用 **Rust** 编写。它的目标是把 jwt.io 等网页版 JWT 工具的便利性带到终端中。

# INSTALL

```pacman: sudo pacman -S jwt-ui```

```brew: brew install jwt-ui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1)
