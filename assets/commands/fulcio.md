# TAGLINE

面向无密钥代码签名的证书颁发机构

# TLDR

使用配置文件**启动 Fulcio 服务器**

```fulcio serve --config-path [config.yaml]```

使用基于文件的 CA **启动服务器**

```fulcio serve --ca fileca --fileca-cert [ca.pem] --fileca-key [ca-key.pem]```

在特定主机和端口上**启动服务器**

```fulcio serve --host [0.0.0.0] --port [8080]```

# SYNOPSIS

**fulcio** _command_ [_options_]

# PARAMETERS

**serve**
> 启动 Fulcio 服务器。

**--ca** _type_
> 证书颁发机构类型：googleca、fileca、kmsca、tinkca、pkcs11ca、ephemeralca。

**--config-path** _file_
> Fulcio 配置 YAML 的路径（默认：/etc/fulcio-config/config.yaml）。

**--host** _addr_
> HTTP 服务器监听地址（默认：0.0.0.0）。

**--port** _num_
> HTTP 服务器端口（默认：8080）。

**--grpc-port** _num_
> gRPC 服务器端口（默认：8081）。

**--fileca-cert** _file_
> CA 证书路径（仅 fileca）。

**--fileca-key** _file_
> CA 加密私钥路径（仅 fileca）。

**--ct-log-url** _url_
> 证书透明度日志 URL。

**version**
> 显示版本。

# CONFIGURATION

**/etc/fulcio-config/config.yaml**
> 服务器配置，包括 OIDC provider 设置、证书策略和 CA 参数。

# DESCRIPTION

**Fulcio** 是一个用于代码签名的证书颁发机构，属于 Sigstore 项目。它签发与 OIDC 身份（GitHub、Google、Microsoft）绑定的短期证书，实现无密钥（keyless）代码签名。

Fulcio 让开发者无需管理长期签名密钥。证书会记录到透明度日志（Rekor）中以供验证。

# WORKFLOW

```
1. Developer authenticates via OIDC
2. Fulcio issues short-lived certificate
3. Developer signs artifact
4. Signature logged in Rekor
5. Verifier checks Rekor and certificate chain
```

# CAVEATS

需要集成 OIDC provider。证书按设计是短期的。生产环境需要妥善管理 CA。它是更大的 Sigstore 生态的一部分。

# HISTORY

Fulcio 是 **Sigstore** 的一部分。Sigstore 由 **Google**、**Red Hat** 和 **Purdue University** 于 **2021** 年发起，旨在让代码签名变得触手可及。Fulcio 以一位罗马执政官命名，提供无密钥签名基础设施中的 CA 组件。

# INSTALL

```pacman: sudo pacman -S fulcio```

```nix: nix profile install nixpkgs#fulcio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cosign](/man/cosign)(1), [rekor-cli](/man/rekor-cli)(1)
