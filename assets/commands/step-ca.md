# TAGLINE

私有证书颁发机构服务器

# TLDR

**初始化新的 CA**

```step ca init```

**启动 CA 服务器**

```step-ca [$(step path)/config/ca.json]```

**请求证书**

```step ca certificate [hostname] [host.crt] [host.key]```

**续订证书**

```step ca renew [host.crt] [host.key]```

**吊销证书**

```step ca revoke [host.crt]```

**添加 provisioner**

```step ca provisioner add [name] --type [OIDC] --client-id [id] --configuration-endpoint [url]```

**获取 CA 健康状态**

```step ca health```

**获取根证书**

```step ca root```

# SYNOPSIS

**step-ca** [_config_] [_options_]

**step ca** _command_ [_options_]

# STEP-CA OPTIONS

**--password-file** _path_
> CA 密钥的密码文件。

**--issuer-password-file** _path_
> 签发者密钥的密码文件。

**--resolver** _address_
> DNS 解析器地址。

**--pidfile** _path_
> PID 文件路径。

# STEP CA COMMANDS

**init**
> 初始化新的 PKI 和 CA 配置。

**certificate** _name_ _crt_ _key_
> 请求新证书。

**renew** _crt_ _key_
> 续订证书。

**revoke** [_serial_|_crt_]
> 吊销证书。

**sign** _csr_ _crt_
> 签署证书签名请求。

**provisioner** add|remove|update|list
> 管理 provisioner。

**root**
> 下载根证书。

**health**
> 检查 CA 健康状态。

**token** _subject_
> 生成身份验证令牌。

**bootstrap**
> 配置客户端以信任 CA。

# CERTIFICATE OPTIONS

**--san** _name_
> 使用者可选名称（可重复）。

**--not-after** _time_
> 过期时间或有效期时长。

**--provisioner** _name_
> 要使用的 provisioner。

**--kty** _type_
> 密钥类型：EC、RSA、OKP。

**--size** _bits_
> 密钥长度。

**--force**
> 覆盖已存在的文件。

# DESCRIPTION

**step-ca** 是一个私有证书颁发机构（CA）服务器。结合 **step ca** 客户端命令，它提供自动化的证书生命周期管理。

**step ca init** 会创建包含根 CA 和中间 CA 的 PKI 结构。生成的配置定义了 provisioner、证书模板和策略。

Provisioner 用于对证书请求进行身份验证。类型包括 ACME、OIDC、JWK、X5C 和 SSHPOP。每种 provisioner 都有特定的身份验证要求和证书约束。

**step ca certificate** 使用配置好的 provisioner 请求证书。ACME provisioner 可实现类似 Let's Encrypt 的自动化。证书中包含指定的 SAN。

使用 **step ca renew** 续订可以延长证书的有效期。配合 **step-renewer** 守护进程可实现自动续订。吊销操作可在证书过期前使其失效。

step-ca 支持 ACME 协议，可与 certbot 及其他 ACME 客户端集成，实现自动化的证书签发。

# CONFIGURATION

**$(step path)/config/ca.json**
> CA 服务器主配置，定义地址、数据库、TLS 设置和授权参数。

**$(step path)/config/defaults.json**
> 默认客户端设置，包括 CA URL 和指纹。

**$(step path)/certs/**
> 存放根 CA 与中间 CA 证书的目录。

**$(step path)/secrets/**
> 存放 CA 私钥（根与中间）的目录。

# CAVEATS

根密钥的安全至关重要——一旦泄露即可签发任意证书。ACME 需要正确配置 DNS 或 HTTP 质询。证书模板需要对 X.509 有所了解。生产环境部署需要妥善的备份和 HSM 方案。

# HISTORY

step-ca 由 **Smallstep** 创建，于 **2018 年**作为其开源 PKI 工具包的一部分发布。它旨在为内部基础设施带来现代化的证书管理。该项目通过自动化证书签发支持零信任安全。Smallstep 在此开源基础上提供商业产品。

# INSTALL

```pacman: sudo pacman -S step-ca```

```apk: sudo apk add step-certificates```

```nix: nix profile install nixpkgs#step-ca```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1), [certbot](/man/certbot)(1), [cfssl](/man/cfssl)(1), [vault](/man/vault)(1)
