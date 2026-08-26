# TAGLINE

支持自动 HTTPS 的 Web 服务器

# TLDR

**启动** Web 服务器

```caddy run```

**提供**当前目录的文件服务

```caddy file-server```

**反向**代理

```caddy reverse-proxy --from [example.com] --to [localhost:8080]```

**校验** Caddyfile

```caddy validate```

**重载**配置

```caddy reload```

# SYNOPSIS

**caddy** _command_ [_options_]

# DESCRIPTION

**caddy** 是一款支持自动 HTTPS 的现代 Web 服务器。它通过 Let's Encrypt 自动获取并续期 TLS 证书，支持 HTTP/2 和 HTTP/3，并使用简单的配置格式。

该服务器在设计上注重易用性，同时保持高性能和安全性。

# PARAMETERS

**run**
> 启动 Caddy 服务器

**start**
> 在后台启动 Caddy

**stop**
> 停止 Caddy 服务器

**reload**
> 重载配置

**validate**
> 校验 Caddyfile

**file-server**
> 快速文件服务器模式

**reverse-proxy**
> 快速反向代理模式

**--config** _file_
> 配置文件（默认：Caddyfile）

**--adapter** _name_
> 配置适配器（caddyfile、json）

# CADDYFILE

简单配置：
```
example.com {
    root * /var/www/html
    file_server
}
```

反向代理：
```
example.com {
    reverse_proxy localhost:8080
}
```

# FEATURES

- 自动 HTTPS（Let's Encrypt）
- 支持 HTTP/2 和 HTTP/3
- 反向代理
- 负载均衡
- 文件服务器
- 模板引擎
- 通过 API 动态配置
- 插件系统

# QUICK COMMANDS

```bash
# Serve current directory
caddy file-server

# Serve on specific port
caddy file-server --listen :8080

# Reverse proxy
caddy reverse-proxy --from :80 --to :8080

# Start with Caddyfile
caddy run

# Validate config
caddy validate --config Caddyfile
```

# CONFIGURATION

**Caddyfile**
> 当前目录下的默认配置文件，定义站点、路由和服务器行为

# CAVEATS

自动 HTTPS 需要能访问 80/443 端口。受 Let's Encrypt 速率限制约束。证书存储需要磁盘空间。内存占用高于 nginx。插件生态比同类产品小。2.x 版本与 v1 配置不兼容。

# HISTORY

**Caddy** 由 Matt Holt 于 **2015** 年创建，是一款以易用性和自动 HTTPS 为优先的 Web 服务器，2.0 版本于 **2019** 年重写。

# INSTALL

```apt: sudo apt install caddy```

```dnf: sudo dnf install caddy```

```pacman: sudo pacman -S caddy```

```apk: sudo apk add caddy```

```zypper: sudo zypper install caddy```

```brew: brew install caddy```

```nix: nix profile install nixpkgs#caddy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nginx](/man/nginx)(8), [apache2](/man/apache2)(8), [traefik](/man/traefik)(1)

# RESOURCES

```[Source code](https://github.com/caddyserver/caddy)```

```[Homepage](https://caddyserver.com/)```

```[Documentation](https://caddyserver.com/docs/)```

<!-- verified: 2026-06-22 -->
