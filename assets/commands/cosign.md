# TAGLINE

容器镜像签名与验证工具

# TLDR

**签名容器镜像（无密钥模式）**

```cosign sign [registry/image@sha256:digest]```

**使用本地密钥签名**

```cosign sign --key [cosign.key] [registry/image@sha256:digest]```

**验证镜像签名（无密钥模式）**

```cosign verify --certificate-identity=[email] --certificate-oidc-issuer=[issuer] [image]```

**使用公钥验证**

```cosign verify --key [cosign.pub] [registry/image@sha256:digest]```

**生成密钥对**

```cosign generate-key-pair```

**带注解签名**

```cosign sign -a [key=value] [registry/image@sha256:digest]```

**将 SBOM 附加到镜像**

```cosign attach sbom --sbom [sbom.json] [registry/image@sha256:digest]```

# SYNOPSIS

**cosign** _command_ [_options_] [_arguments_]

# DESCRIPTION

**cosign** 是 Sigstore 出品的容器镜像与软件制品签名、验证工具。它支持基于 OIDC 身份的无密钥（keyless）签名，也支持传统的基于密钥的签名，为镜像的真实性和完整性提供密码学保证。

该工具与容器仓库集成，将签名和证明（attestation）作为 OCI 制品附加。无密钥签名利用绑定到 GitHub、Google 或 Microsoft 等身份提供方的短期证书，免去了管理长期签名密钥的负担。签名会记录在 Sigstore 的透明日志（Rekor）中，供公众验证和审计。

cosign 还能处理 SBOM（软件物料清单）、证明及其他元数据，实现全面的供应链安全。它支持多种密钥管理系统，包括云服务商的 KMS 服务和硬件安全模块。

# COMMANDS

**sign**
> 签名容器镜像

**verify**
> 验证镜像签名

**generate-key-pair**
> 生成签名密钥对

**attach**
> 将制品（SBOM、证明）附加到镜像

**download**
> 下载签名/制品

**triangulate**
> 定位镜像签名的存储位置

**copy**
> 在镜像之间复制签名

**clean**
> 从镜像移除签名

# PARAMETERS

**--key** _path|uri_
> 用于签名/验证的密钥

**--certificate** _path_
> 用于签名的证书

**--certificate-chain** _path_
> 证书链

**--certificate-identity** _identity_
> 证书中预期的身份

**--certificate-oidc-issuer** _issuer_
> 预期的 OIDC 签发方

**-a** _key=value_
> 为签名添加注解

# KEYLESS SIGNING

使用 OIDC 身份（GitHub、Google 等）配合短期密钥。签名会记录在透明日志中。

# KMS SUPPORT

通过 URI 格式支持 AWS KMS、GCP KMS、Azure Key Vault 和 HashiCorp Vault。

# CAVEATS

请始终按摘要（@sha256:...）而不是标签签名。一个镜像可以附加多个签名。无密钥模式的 OIDC 流程需要联网。

# INSTALL

```apt: sudo apt install cosign```

```pacman: sudo pacman -S cosign```

```apk: sudo apk add cosign```

```zypper: sudo zypper install cosign```

```brew: brew install cosign```

```nix: nix profile install nixpkgs#cosign```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [podman](/man/podman)(1)
