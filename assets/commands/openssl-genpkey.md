# TAGLINE

为各种算法生成私钥

# TLDR

**生成 RSA 私钥**

```openssl genpkey -algorithm RSA -out [private.key] -pkeyopt rsa_keygen_bits:[4096]```

**生成 EC 私钥**

```openssl genpkey -algorithm EC -out [private.key] -pkeyopt ec_paramgen_curve:[P-256]```

**生成 Ed25519 密钥**

```openssl genpkey -algorithm ED25519 -out [private.key]```

**生成加密的私钥**

```openssl genpkey -algorithm RSA -out [private.key] -aes256```

**使用自定义参数生成**

```openssl genpkey -algorithm RSA -out [key.pem] -pkeyopt rsa_keygen_bits:2048 -pkeyopt rsa_keygen_pubexp:65537```

# SYNOPSIS

**openssl genpkey** [_options_]

# PARAMETERS

**-algorithm** _alg_
> 密钥算法。

**-out** _file_
> 输出文件。

**-outform** _format_
> 输出格式（PEM、DER）。

**-aes256**, **-aes128**
> 加密输出。

**-pkeyopt** _opt:val_
> 算法选项。

**-pass** _arg_
> 输出口令（passphrase）。

# DESCRIPTION

**openssl genpkey** 为各种算法生成私钥。它是 genrsa、ecparam 等算法特定命令的现代替代品。

支持 RSA、EC、ED25519、ED448、X25519、X448 等。

# ALGORITHM OPTIONS

```
RSA: rsa_keygen_bits, rsa_keygen_pubexp
EC:  ec_paramgen_curve (P-256, P-384, secp256k1)
```

# CAVEATS

请保护好生成的私钥。存储时使用强加密。新应用推荐使用 ED25519。

# HISTORY

genpkey 作为统一的密钥生成命令被引入，取代了 OpenSSL 中较旧的算法特定命令。

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

[openssl-pkey](/man/openssl-pkey)(1), [openssl-req](/man/openssl-req)(1), [openssl-rsa](/man/openssl-rsa)(1)
