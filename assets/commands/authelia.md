# TAGLINE

支持多因素认证与授权的服务器

# TLDR

**校验配置文件**

```authelia validate-config --config [config.yml]```

**生成密码哈希**

```authelia crypto hash generate argon2```

**生成随机密钥**

```authelia crypto rand --length [64]```

**生成 RSA 密钥对**

```authelia crypto pair rsa generate```

**生成 TOTP 密钥**

```authelia crypto totp generate --issuer [MyApp]```

以交互方式**哈希密码**

```authelia crypto hash generate argon2 --password```

**显示版本**

```authelia --version```

**运行服务器**

```authelia --config [/etc/authelia/config.yml]```

# SYNOPSIS

**authelia** [_global-options_] _command_ [_options_]

# COMMANDS

**crypto** hash|pair|rand|certificate|totp
> 用于生成密钥和哈希的加密工具集。

**validate-config**
> 校验配置文件的语法和取值。

**storage** migrate|schema-info|user|encryption
> 数据库存储管理与迁移。

**access-control** check-policy
> 针对请求测试访问控制规则。

**build-info**
> 显示构建信息。

# CRYPTO SUBCOMMANDS

**crypto hash generate** argon2|pbkdf2|sha2crypt|bcrypt
> 使用指定算法生成密码哈希。

**crypto pair** rsa|ecdsa|ed25519
> 生成加密密钥对。

**crypto rand**
> 生成随机字节或字符串。

**crypto certificate** rsa|ecdsa|ed25519
> 生成自签名证书。

**crypto totp generate**
> 生成 TOTP 密钥和二维码。

# PARAMETERS

**--config**, **-c** _path_
> 配置文件的路径。

**--password**
> 以交互方式读取密码。

**--length** _n_
> 随机生成的长度。

**--issuer** _name_
> TOTP 签发者名称。

**--algorithm** _algo_
> 哈希或加密算法。

**--help**, **-h**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**authelia** 是 Authelia 的命令行界面。Authelia 是一个开源的身份认证与授权服务器，可为反向代理后面的应用提供多因素认证和单点登录。

**crypto** 系列命令用于生成 Authelia 部署所需的密钥、密码哈希、证书和 TOTP 配置。使用 **crypto hash generate argon2** 可为用户数据库创建密码哈希。

通过 **validate-config** 进行的配置校验会在部署前检查 YAML 语法和设置取值，从而捕获常见的配置错误。

**storage** 系列命令管理用户数据库，包括跨版本的迁移和加密密钥轮换。Authelia 存储用户凭据、TOTP 密钥和会话数据。

Authelia 可与 Nginx、Traefik、HAProxy 等反向代理集成，通过认证门户和访问策略保护 Web 应用。

# CONFIGURATION

**/etc/authelia/configuration.yml**
> 主配置文件，定义认证后端、会话设置、访问控制规则和存储选项。

**/etc/authelia/users_database.yml**
> 使用文件认证后端时的基于文件的用户数据库，包含用户名、密码哈希和组成员关系。

# CAVEATS

Authelia 作为服务运行在反向代理之后，CLI 主要用于配置和实用操作。认证流程依赖正确的反向代理配置。用户数据库与会话存储必须先行配置。在高可用部署中，某些功能需要 Redis 作为会话存储。

# HISTORY

Authelia 由 **Clement Michaud** 于 **2016 年** 创建，最初只是一个简单的认证门户。项目逐步发展出多种第二因素认证方式（TOTP、WebAuthn、Duo）和高级访问控制。第 4 版带来重大架构改进，并在自托管认证领域得到广泛采用。项目强调安全性和隐私，并以容器优先的设计追求易部署性。

# INSTALL

```aur: yay -S authelia```

```nix: nix profile install nixpkgs#authelia```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[keycloak](/man/keycloak)(1), [nginx](/man/nginx)(1), [traefik](/man/traefik)(1)
