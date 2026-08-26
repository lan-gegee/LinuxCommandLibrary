# TAGLINE

处理 RSA 密钥

# TLDR

**查看 RSA 密钥详情**

```openssl rsa -in [private.key] -text -noout```

**提取公钥**

```openssl rsa -in [private.key] -pubout -out [public.key]```

**移除口令**

```openssl rsa -in [encrypted.key] -out [decrypted.key]```

**添加口令**

```openssl rsa -in [private.key] -aes256 -out [encrypted.key]```

**将 PEM 转换为 DER**

```openssl rsa -in [private.key] -outform DER -out [private.der]```

**检查密钥有效性**

```openssl rsa -in [private.key] -check```

# SYNOPSIS

**openssl rsa** [_options_] [-in _file_] [-out _file_]

# PARAMETERS

**-in** _file_
> 输入文件。

**-out** _file_
> 输出文件。

**-pubout**
> 输出公钥。

**-pubin**
> 输入为公钥。

**-text**
> 打印密钥各组成部分。

**-noout**
> 不输出密钥。

**-check**
> 检查一致性。

**-aes256**, **-aes128**
> 对输出加密。

**-inform**, **-outform**
> 输入/输出格式。

# DESCRIPTION

**openssl rsa** 用于处理 RSA 密钥。它可以转换格式、提取公钥、添加/移除加密，以及验证密钥完整性。

对于一般密钥操作，建议改用 openssl pkey。

# KEY COMPONENTS

```
n - Modulus
e - Public exponent
d - Private exponent
p, q - Prime factors
```

# CAVEATS

仅限 RSA；其他算法请使用 pkey。务必保护好私钥。新应用可考虑使用 Ed25519。

# HISTORY

自该库创建以来，RSA 密钥处理一直是 OpenSSL 的核心功能，不过现在更推荐使用 genpkey/pkey。

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

[openssl-pkey](/man/openssl-pkey)(1), [openssl-genpkey](/man/openssl-genpkey)(1), [openssl-genrsa](/man/openssl-genrsa)(1)
