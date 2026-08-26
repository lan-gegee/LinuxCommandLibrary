# TAGLINE

生成 RSA 私钥

# TLDR

**生成 2048 位 RSA 密钥**

```openssl genrsa -out [private.key] 2048```

**生成 4096 位密钥**

```openssl genrsa -out [private.key] 4096```

**使用 AES-256 生成加密密钥**

```openssl genrsa -aes256 -out [private.key] 4096```

**使用特定公共指数生成密钥**

```openssl genrsa -F4 -out [private.key] 2048```

**生成密钥到 stdout**

```openssl genrsa 2048```

# SYNOPSIS

**openssl** **genrsa** [_options_] [_bits_]

# PARAMETERS

**-out** _file_
> 私钥的输出文件。省略时写入 stdout。

**-aes256**, **-aes192**, **-aes128**, **-des3**, **-des**
> 用指定的密码算法加密输出的密钥。会提示输入口令。

**-passout** _arg_
> 加密密码的来源（例如 **pass:password**、**file:pathname**、**env:var**、**fd:number**、**stdin**）。

**-F4**
> 使用 65537 (0x10001) 作为公共指数（默认）。

**-3**
> 使用 3 作为公共指数。

**-traditional**
> 以传统的 PKCS#1 格式而非 PKCS#8 写出密钥。

**-verbose**
> 在密钥生成过程中打印更多细节。

_bits_
> 密钥长度，单位为比特（默认 2048）。最小为 512，但建议使用 2048 或更高。

# DESCRIPTION

**openssl genrsa** 用于生成 RSA 私钥。可以选择用口令加密密钥。常见的密钥长度为 2048 和 4096 位。默认输出 PEM 格式（OpenSSL 3.x 中为 PKCS#8，旧版本中为 PKCS#1）。

该命令被视为遗留的便捷封装。在 OpenSSL 3.x 中更推荐使用更通用的 **openssl genpkey -algorithm RSA**，后者支持更多选项。

# CAVEATS

低于 2048 位的密钥长度被认为不安全。某些应用程序需要传统的 PKCS#1 格式；需要时请使用 **-traditional**。在 OpenSSL 3.x 中，默认输出格式从 PKCS#1 变更为 PKCS#8，这可能会影响较旧的工具。

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

[openssl](/man/openssl)(1), [openssl-rsa](/man/openssl-rsa)(1), [openssl-genpkey](/man/openssl-genpkey)(1)
