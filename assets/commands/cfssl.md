# TAGLINE

PKI/TLS 证书颁发机构工具集

# TLDR

**初始化新的 CA**

```cfssl gencert -initca [ca-csr.json] | cfssljson -bare [ca]```

**生成由 CA 签署的证书**

```cfssl gencert -ca [ca.pem] -ca-key [ca-key.pem] [csr.json] | cfssljson -bare [cert]```

**签署 CSR**

```cfssl sign -ca [ca.pem] -ca-key [ca-key.pem] [request.csr]```

**生成自签名证书**

```cfssl selfsign [hostname] [csr.json] | cfssljson -bare [cert]```

**启动 API 服务器**

```cfssl serve -ca [ca.pem] -ca-key [ca-key.pem]```

**打包证书捆绑包**

```cfssl bundle -cert [cert.pem]```

**打印默认配置**

```cfssl print-defaults config```

# SYNOPSIS

**cfssl** _command_ [_options_] [_arguments_]

# DESCRIPTION

**cfssl** 是 CloudFlare 的 PKI/TLS 工具集，用于签署、验证和捆绑 TLS 证书。它既提供命令行工具，也提供用于运行完整证书颁发机构（CA）的 HTTP API 服务器。

该工具集处理完整的证书生命周期：生成根 CA 和中间 CA、签署证书请求、创建自签名证书以及构建用于部署的证书捆绑包。配置文件定义签名配置文件（signing profile），其中包含特定的有效期、密钥用途和认证要求。

配套工具 cfssljson 将 cfssl 的 JSON 输出提取为 PEM 文件。multirootca 组件允许运行一个持有多个签名密钥、用于不同用途的 CA 服务器。

# COMMANDS

**gencert**
> 生成新密钥和已签署的证书

**sign**
> 签署证书签名请求

**selfsign**
> 生成自签名证书

**bundle**
> 构建证书捆绑包

**genkey**
> 生成私钥和 CSR

**serve**
> 启动 HTTP API 服务器

**info**
> 获取远程签名服务器的信息

**print-defaults**
> 打印默认配置

**version**
> 打印版本号

# PARAMETERS

**-ca** _file_
> CA 证书文件（默认：ca.pem）

**-ca-key** _file_
> CA 私钥文件（默认：ca_key.pem）

**-config** _file_
> 配置文件路径

**-hostname** _names_
> SAN 所用的逗号分隔主机名列表

**-initca**
> 初始化新 CA

**-remote** _host_
> 远程 CFSSL 服务器地址

# API SERVER

默认地址：127.0.0.1:8888

```cfssl serve -address [0.0.0.0] -port [8888] -ca [ca.pem] -ca-key [ca-key.pem]```

# COMPANION TOOLS

**cfssljson**
> 从 JSON 输出写入证书/密钥

**multirootca**
> 多签名密钥的 CA 服务器

**mkbundle**
> 构建证书捆绑包

# CONFIGURATION

**ca-csr.json**
> 证书签名请求（CSR）的默认值（密钥算法、长度、名称、hosts）。

**config.json**
> 签名配置文件，定义 CA 的证书有效期、用途和认证密钥。

# CAVEATS

从源码构建需要 Go 1.20+。私钥应妥善保护。复杂的签名策略请使用配置文件。

# INSTALL

```apt: sudo apt install golang-cfssl```

```pacman: sudo pacman -S cfssl```

```brew: brew install cfssl```

```nix: nix profile install nixpkgs#cfssl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1), [certbot](/man/certbot)(1)

# RESOURCES

```[Source code](https://github.com/cloudflare/cfssl)```

<!-- verified: 2026-06-22 -->
