# TAGLINE

Let's Encrypt 证书管理

# TLDR

通过 **webroot** 方式验证获取证书

```sudo certbot certonly --webroot -w [path/to/webroot] -d [subdomain.example.com]```

为 **nginx** 获取并安装证书

```sudo certbot --nginx -d [subdomain.example.com]```

为 **apache** 获取并安装证书

```sudo certbot --apache -d [subdomain.example.com]```

**续期**所有即将过期的证书

```sudo certbot renew```

进行**演练（dry run）**测试而不保存证书

```sudo certbot --webroot -w [path/to/webroot] -d [subdomain.example.com] --dry-run```

使用 standalone 模式**获取证书**（无需 Web 服务器）

```sudo certbot certonly --standalone -d [subdomain.example.com]```

**列出所有受管理的证书**

```sudo certbot certificates```

# SYNOPSIS

**certbot** [_options_] _command_

# DESCRIPTION

**certbot** 是 Let's Encrypt 官方客户端，用于自动获取和续期免费的 TLS/SSL 证书。它可以自动配置 Apache 和 Nginx 等 Web 服务器。

证书有效期为 90 天。应定期运行 renew 命令（通常通过 cron）以保持证书有效。

# SUBCOMMANDS

**certonly**
> 仅获取证书而不安装

**run**
> 获取并安装证书

**renew**
> 续期即将过期的证书

**revoke**
> 吊销证书

**delete**
> 删除证书

**certificates**
> 列出已安装的证书

# PARAMETERS

**-d, --domain** _domain_
> 证书的域名

**-w, --webroot-path** _path_
> 用于验证的 webroot 路径

**--nginx**
> 使用 nginx 插件

**--apache**
> 使用 apache 插件

**--dry-run**
> 测试而不保存

**--standalone**
> 使用内置 Web 服务器进行验证

**--test-cert**
> 使用 staging 服务器（不受信任的证书）

**--non-interactive**
> 无用户交互运行

**--agree-tos**
> 同意服务条款

**-m**, **--email** _email_
> 用于账户注册的邮箱

**--preferred-challenges** _type_
> 首选验证方式：http-01、dns-01 或 tls-alpn-01

**--deploy-hook** _command_
> 证书部署成功后运行的命令（如重载 Web 服务器）

# CONFIGURATION

**/etc/letsencrypt/renewal/**
> 每张证书的续期配置文件，控制自动续期行为。

**/etc/letsencrypt/cli.ini**
> 所有证书操作共用的全局 certbot 默认设置。

# CAVEATS

Webroot 验证要求 Web 服务器正在运行。Let's Encrypt 生产服务器有速率限制。续期后需重启 Web 服务器才能让新证书生效。

# HISTORY

**certbot** 由 Electronic Frontier Foundation (EFF) 开发，最初名为 Let's Encrypt client。Let's Encrypt 于 **2016 年**上线，提供免费、自动化的 TLS 证书。

# INSTALL

```dnf: sudo dnf install certbot```

```pacman: sudo pacman -S certbot```

```apk: sudo apk add certbot```

```brew: brew install certbot```

```nix: nix profile install nixpkgs#certbot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1), [nginx](/man/nginx)(8), [apache2](/man/apache2)(8)
