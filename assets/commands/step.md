# TAGLINE

证书与密钥管理 CLI

# TLDR

**创建 CA**

```step ca init```

**生成证书**

```step ca certificate [hostname] [cert.pem] [key.pem]```

**检查证书**

```step certificate inspect [cert.pem]```

**创建 CSR**

```step certificate create --csr [hostname] [csr.pem] [key.pem]```

**验证证书**

```step certificate verify [cert.pem] --roots [ca.pem]```

**获取 CA 指纹**

```step certificate fingerprint [ca.pem]```

**引导配置 CA 客户端**

```step ca bootstrap --ca-url [https://ca:9000] --fingerprint [fingerprint]```

# SYNOPSIS

**step** _command_ [_subcommand_] [_options_]

# PARAMETERS

**ca**
> 证书颁发机构相关命令。

**certificate**
> 证书操作。

**crypto**
> 加密操作。

**ssh**
> SSH 证书命令。

**oauth**
> OAuth 和 OIDC 授权操作。

**path**
> 打印已配置的 step 路径（默认为 ~/.step）。

**context**
> 管理证书颁发机构上下文。

**completion**
> 打印 Shell 补全脚本（bash、zsh、fish）。

**--ca-url** _URL_
> CA 服务器 URL。

**--fingerprint** _FP_
> CA 指纹。

# DESCRIPTION

**step** 是一个用于处理证书、密钥和加密操作的综合性命令行工具包。它既可作为独立的实用程序来检查和创建证书，也可作为 step-ca 私有证书颁发机构服务器的客户端接口。

该工具提供覆盖证书完整生命周期的子命令：创建证书签名请求、从 CA 请求签名证书、查看证书详情、验证证书链以及管理 SSH 证书。它支持 ECDSA、EdDSA 和 RSA 密钥等现代加密标准，并可通过 ACME 协议实现自动化证书签发。

与 step-ca 服务器配合使用时，step 支持自动化的 PKI 工作流，包括引导客户端信任、请求短期证书，以及管理面向 OIDC、JWK 和 ACME 等不同身份验证方式的 provisioner。它还支持 SSH 证书管理，作为传统长期 SSH 密钥的替代方案。

# CONFIGURATION

**~/.step/**
> 默认的 step 路径，包含 CA 配置、证书和密钥。

**~/.step/config/defaults.json**
> 默认设置，包括 CA URL、指纹和 provisioner。

**STEPPATH**
> 用于覆盖默认 step 配置目录的环境变量。

# CAVEATS

CA 的搭建需要规划。证书的有效期很重要。密钥安全必不可少。

# HISTORY

**step** 与 **step-ca** 由 **Smallstep** 为现代 PKI 而创建。它们简化了开发者和 DevOps 的证书管理。

# INSTALL

```apt: sudo apt install step```

```dnf: sudo dnf install step```

```pacman: sudo pacman -S step```

```apk: sudo apk add step```

```zypper: sudo zypper install step```

```brew: brew install step```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[step-ca](/man/step-ca)(1), [openssl](/man/openssl)(1), [cfssl](/man/cfssl)(1), [certbot](/man/certbot)(1)
