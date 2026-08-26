# TAGLINE

通用密钥处理工具

# TLDR

**查看私钥详细信息**

```openssl pkey -in [private.key] -text -noout```

**提取公钥**

```openssl pkey -in [private.key] -pubout -out [public.key]```

**转换为 DER 格式**

```openssl pkey -in [private.key] -outform DER -out [private.der]```

**加密私钥**

```openssl pkey -in [private.key] -aes256 -out [encrypted.key]```

**移除加密**

```openssl pkey -in [encrypted.key] -out [decrypted.key]```

**检查密钥有效性**

```openssl pkey -in [private.key] -check```

# SYNOPSIS

**openssl pkey** [_options_] [-in _file_] [-out _file_]

# PARAMETERS

**-in** _file_
> 输入文件。

**-out** _file_
> 输出文件。

**-inform** _format_
> 输入格式（PEM、DER）。

**-outform** _format_
> 输出格式。

**-pubout**
> 输出公钥。

**-text**
> 打印文本形式。

**-noout**
> 不输出密钥。

**-check**
> 检查密钥。

**-aes256**
> 加密输出。

# DESCRIPTION

**openssl pkey** 是一个通用密钥处理工具。它可以在不同格式之间转换、提取公钥、加密/解密私钥，以及显示密钥信息。

支持 RSA、EC、ED25519 和其他密钥类型。

# KEY FORMATS

```
PEM - Base64 encoded (-----BEGIN...)
DER - Binary format
```

# CAVEATS

使用 -nodes 或不加加密会输出未受保护的密钥。务必保护好私钥。

# HISTORY

pkey 命令在 OpenSSL 中为不同算法提供统一的密钥处理能力。

# INSTALL

```apt: sudo apt install openssl```

```dnf: sudo dnf install openssl```

```pacman: sudo pacman -S openssl```

```apk: sudo apk add openssl```

```zypper: sudo zypper install openssl```

```brew: brew install openssl```

```nix: nix profile install nixpkgs#openssl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl-genpkey](/man/openssl-genpkey)(1), [openssl-rsa](/man/openssl-rsa)(1)
