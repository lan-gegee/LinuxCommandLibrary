# TAGLINE

基于 shell 的 ACME SSL/TLS 证书客户端

# TLDR

以 webroot 模式**签发**证书

```acme.sh --issue -d [example.com] -w [/var/www/html]```

以 DNS 模式签发**泛域名证书**

```acme.sh --issue -d [example.com] -d [*.example.com] --dns [dns_cf]```

**安装**证书

```acme.sh --install-cert -d [example.com] --key-file [/path/to/key.pem] --fullchain-file [/path/to/cert.pem] --reloadcmd "[systemctl reload nginx]"```

**续期**所有证书

```acme.sh --renew-all```

**列出**所有已签发的证书

```acme.sh --list```

# SYNOPSIS

**acme.sh** _--issue_|_--install-cert_|_--renew_ [_-d domain_] [_options_]

# DESCRIPTION

**acme.sh** 是一个纯 Unix shell 编写的 ACME 客户端，用于从 Let's Encrypt 及其他符合 ACME 规范的证书颁发机构获取免费的 SSL/TLS 证书。它支持多种验证方式，包括 webroot、standalone、DNS 以及 Apache/Nginx 插件。

该工具通过 cron 任务自动处理证书续期，并支持经由 DNS 验证的泛域名证书。除 POSIX 兼容 shell 和 curl、wget 等常见工具外，它不需要任何依赖。

# PARAMETERS

**--issue**
> 签发新证书

**--install-cert**
> 将已签发的证书安装到指定位置

**--renew**
> 续期特定证书

**--renew-all**
> 续期所有已签发的证书

**--list**
> 列出所有已签发的证书

**-d** _domain_
> 域名（可重复使用以指定多个域名/SAN）

**-w** _path_
> 用于 HTTP 验证的 webroot 路径

**--dns** _provider_
> 使用指定提供商进行 DNS 验证（dns_cf、dns_aws 等）

**--standalone**
> 使用 standalone 模式（会启动临时 Web 服务器）

**--nginx**
> 使用 Nginx 模式进行验证

**--apache**
> 使用 Apache 模式进行验证

**--key-file** _path_
> 私钥的安装路径

**--fullchain-file** _path_
> 完整证书链的安装路径

**--reloadcmd** _cmd_
> 安装完成后重新加载服务的命令

**--force**
> 无论是否到期都强制续期

**--revoke** **-d** _domain_
> 吊销证书

**--remove** **-d** _domain_
> 将证书从续期列表中移除

**--server** _url_
> 指定 ACME 服务器（默认：Let's Encrypt）。可用 letsencrypt、zerossl、buypass 或自定义 URL。

**--upgrade**
> 将 acme.sh 升级到最新版本

# CONFIGURATION

**~/.acme.sh/account.conf**
> 主配置文件，保存默认设置、CA 服务器、邮箱以及 DNS API 凭据。

**~/.acme.sh/[domain]/[domain].conf**
> 每个域名的配置，保存签发参数、验证方式和续期设置。

**~/.acme.sh/[domain]/[domain].cer**
> 该域名的已签发证书文件。

**~/.acme.sh/[domain]/[domain].key**
> 该域名的私钥文件。

# CAVEATS

DNS 验证需要你的 DNS 提供商的 API 凭据。webroot 模式要求 Web 服务器正在运行且可访问。standalone 模式要求 80/443 端口空闲。自动续期依赖 cron；请确保 cron 正在运行。

# HISTORY

**acme.sh** 由 Neil Pang（Neilpang）创建，于 **2015** 年首次发布，距 Let's Encrypt 宣布其服务后不久。它的设计目标是成为 Certbot 的轻量、无依赖替代品，后来成为 shell 环境中最流行的 ACME 客户端之一。

# INSTALL

```pacman: sudo pacman -S acme.sh```

```apk: sudo apk add acme.sh```

```brew: brew install acme.sh```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[certbot](/man/certbot)(1), [openssl](/man/openssl)(1), [nginx](/man/nginx)(8), [apache2](/man/apache2)(8)
