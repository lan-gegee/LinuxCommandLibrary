# TAGLINE

云原生 HTTP 反向代理

# TLDR

以默认配置**启动 Traefik**

```traefik```

**使用指定配置文件启动**

```traefik --configFile=[traefik.yml]```

**启用 Docker provider**

```traefik --providers.docker```

**以指定端点启用 Docker**

```traefik --providers.docker.endpoint=unix:///var/run/docker.sock```

为 HTTP 流量**设置入口点**

```traefik --entrypoints.web.address=:80```

**启用 API 仪表板**

```traefik --api.dashboard=true```

**检查健康状态**

```traefik healthcheck```

**显示帮助**

```traefik --help```

# SYNOPSIS

**traefik** [_command_] [_options_]

# PARAMETERS

**--configFile** _file_
> 从指定文件加载配置（traefik.yml、traefik.toml）。

**--providers.docker**
> 启用 Docker provider 以自动发现服务。

**--providers.docker.endpoint** _endpoint_
> Docker 守护进程端点（如 unix:///var/run/docker.sock）。

**--providers.file.filename** _file_
> 使用配置文件启用文件 provider。

**--entrypoints.**_name_**.address** _address_
> 定义入口点地址（如 :80、:443）。

**--api.dashboard**
> 启用 Web 仪表板。

**--api.insecure**
> 允许不安全地访问 API（用于开发）。

**--log.level** _level_
> 日志级别：DEBUG、INFO、WARN、ERROR。

**--accesslog**
> 启用访问日志。

**--certificatesresolvers.**_name_**.acme.email** _email_
> 用于 Let's Encrypt 证书的邮箱。

**healthcheck**
> 通过 /ping 端点检查 Traefik 健康状况。

**version**
> 显示版本信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Traefik** 是一款为微服务设计的现代 HTTP 反向代理和负载均衡器。它通过 Docker、Kubernetes 和 Consul 等 provider 自动发现服务，并动态配置路由规则。

主要特性包括基于 Let's Encrypt 的自动 HTTPS、负载均衡、熔断器、速率限制和指标收集。配置可通过文件（YAML、TOML）、环境变量或命令行选项提供。

Web 仪表板可实时查看路由器、服务和中间件。Traefik 与容器编排器和服务网格原生集成。

# CAVEATS

未经身份验证的 API 仪表板不应公开暴露。使用 Docker provider 时，Traefik 需要访问 Docker 套接字，这会带来安全隐患。使用 ACME 申请证书时受 Let's Encrypt 的速率限制约束。

# HISTORY

Traefik 由 **Emile Vauge** 创建，于 **2015 年**由 **Traefik Labs**（前身为 Containous）首次发布。它专为云原生时代和微服务架构设计。**2019 年**发布的 Traefik 2.0 引入了由路由器、服务和中间件构成的新路由架构。它已成为容器环境中最流行的反向代理之一。

# INSTALL

```pacman: sudo pacman -S traefik```

```apk: sudo apk add traefik```

```zypper: sudo zypper install traefik```

```brew: brew install traefik```

```nix: nix profile install nixpkgs#traefik```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nginx](/man/nginx)(1), [caddy](/man/caddy)(1), [haproxy](/man/haproxy)(1), [docker](/man/docker)(1)
