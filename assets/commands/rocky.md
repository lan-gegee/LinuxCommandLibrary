# TAGLINE

可编程的 HTTP 和 WebSocket 反向代理 CLI

# TLDR

将来自本地端口的全部流量**转发**到上游服务器

```rocky --port [8080] --forward [http://server:9000]```

**只转发选定的路由**而忽略其他所有请求

```rocky --port [8080] --forward [http://server] --route "[/api/*, /images/*]"```

向第二个后端**重放流量**（影子/镜像请求）

```rocky --port [8080] --forward [http://primary] --replay [http://shadow]```

在多个上游服务器之间进行**负载均衡**

```rocky --port [8080] --balance "[http://a:9000, http://b:9000]"```

**从 TOML 配置文件运行**

```rocky --config [path/to/rocky.toml]```

使用密钥和证书以 **HTTPS 提供服务**

```rocky --port [8443] --key [server.key] --cert [server.crt] --forward [http://backend]```

# SYNOPSIS

**rocky** [_options_]

# PARAMETERS

**-c** _file_, **--config** _file_
> 从 TOML 文件加载配置。

**-p** _port_, **--port** _port_
> 本地 HTTP 服务器的 TCP 端口。

**-f** _url_, **--forward** _url_
> 默认的上游 URL，流量将被转发到此处。

**-r** _url_, **--replay** _url_
> 额外的上游，接收每个请求的副本（重放/影子目标）。可重复使用。

**-t** _routes_, **--route** _routes_
> 要处理的逗号分隔路由模式列表。支持 glob 风格的通配符。

**-b** _urls_, **--balance** _urls_
> 逗号分隔的上游 URL 列表，用于在其间均衡流量。

**-k** _file_, **--key** _file_
> SSL/TLS 私钥路径。

**-e** _file_, **--cert** _file_
> SSL/TLS 证书路径。

**-s**, **--secure**
> 代理到 HTTPS 上游时启用严格的 SSL 证书校验。

**-m**, **--mute**
> 禁用 HTTP 流量日志。

**-d**, **--debug**
> 启用详细的调试输出。

**-v**, **--version**
> 打印版本并退出。

**-h**, **--help**
> 显示用法帮助。

# DESCRIPTION

**rocky** 是一个面向中间件的 HTTP 和 WebSocket 反向代理，构建于 Node.js 之上。**rocky-cli** 前端通过单个命令暴露其核心功能，因此无需编写 JavaScript 即可启动代理。它可以把请求转发到一个或多个后端、将流量重放到影子服务、在上游之间做负载均衡，并即时拦截或转换请求和响应。

路由用 glob 模式表示并与请求路径匹配，让你只代理特定端点而忽略其余部分。重放目标会收到每个被转发请求的副本，这适用于蓝绿部署、针对新后端的回归测试，或录制流量供日后分析。

配置既可以完全通过命令行传入，也可以通过 **--config** 从 TOML 文件加载，便于把可复现的代理配置随项目一起提交保存。

# CONFIGURATION

典型的 **rocky.toml** 文件如下：

```
port = 8080
forward = "http://127.0.0.1:9000"
replay = ["http://127.0.0.1:9001"]

[[routes]]
path = "/api/*"
forward = "http://api.internal:8080"

[[routes]]
path = "/static/*"
forward = "http://cdn.internal"
```

同时提供时，命令行标志会覆盖配置文件中的值。

# CAVEATS

上游 **rocky** 项目已**弃用**且不再活跃维护，因此新的生产部署不应依赖它。由于它运行在 Node.js 上，高负载下的性能低于 **nginx** 或 **HAProxy** 等原生代理。glob 路由匹配是贪婪的；请按从最具体到最宽泛的顺序排列模式，以避免意外的转发行为。

# HISTORY

**rocky** 由 **Tomás Aparicio**（h2non）创建，作为开源 Node.js HTTP 代理框架发布。配套的 **rocky-cli** 软件包随后发布，无需编写代码即可使用相同的功能。两个项目均已归档弃用，用户通常迁移到 **nginx**、**HAProxy** 或 **Envoy** 等专用代理。

# INSTALL

```aur: yay -S rocky```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nginx](/man/nginx)(8), [haproxy](/man/haproxy)(1), [caddy](/man/caddy)(1), [mitmproxy](/man/mitmproxy)(1), [socat](/man/socat)(1)
