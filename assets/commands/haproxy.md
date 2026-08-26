# TAGLINE

高性能 TCP/HTTP 负载均衡器与代理

# TLDR

**启动 HAProxy**

```haproxy -f [/etc/haproxy/haproxy.cfg]```

**检查配置**

```haproxy -c -f [/etc/haproxy/haproxy.cfg]```

**重载配置**（待新进程就绪后再软停止旧进程）

```haproxy -f [config.cfg] -sf $(pidof haproxy)```

**以守护进程模式启动**

```haproxy -D -f [config.cfg]```

**以 master-worker 模式启动**（对 systemd 友好，官方 unit 文件即采用此模式）

```haproxy -Ws -f [/etc/haproxy/haproxy.cfg] -p [/run/haproxy.pid]```

**显示版本**

```haproxy -v```

# SYNOPSIS

**haproxy** [_options_] **-f** _config_

# PARAMETERS

**-f** _file_
> 配置文件。

**-c**
> 检查配置并退出。

**-D**
> 守护进程模式。

**-sf** _pids_
> 软停止旧进程。

**-st** _pids_
> 硬停止旧进程。

**-p** _pidfile_
> PID 文件路径。

**-n** _maxconn_
> 最大连接数。

**-N** _maxconn_
> 每个代理的默认 maxconn。

**-d**
> 调试模式；禁用守护进程模式并保持在前台运行。

**-V**
> 详细模式（抵消 -q）。

**-q**
> 安静模式；抑制信息性消息。

**-v**
> 显示版本号和构建日期。

**-W**
> master-worker 模式：主进程监督一个或多个工作进程，并可在不断开连接的情况下重载配置。

**-Ws**
> 带 systemd `sd_notify` 支持的 master-worker 模式；官方 systemd unit 即采用此模式。

**-x** _socket_
> 从旧进程获取监听套接字（内部用于无缝重载）。

**-C** _dir_
> 在加载配置文件之前先切换到该目录。

# DESCRIPTION

**HAProxy**（High Availability Proxy）是一款高性能的 TCP/HTTP 负载均衡器和反向代理，可将传入流量分发到多组后端服务器。它的配置围绕 frontend（在绑定的地址和端口上接受客户端连接）和 backend（定义处理请求的服务器集合以及负载均衡算法——轮询、最少连接、源地址哈希等）组织。主动健康检查持续探测后端服务器，并自动把不健康的节点移出轮换。

除了基本的负载均衡之外，HAProxy 还提供 SSL/TLS 终止、HTTP 头操作、基于 ACL 的内容路由、连接速率限制、用于会话保持的 stick table，以及实时统计仪表板。它采用事件驱动的多线程工作进程模型，能以低延迟和极低的资源消耗处理数十万并发连接，因而成为高流量生产环境的标准选择。

现代部署通常以 master-worker 模式（**-W**/**-Ws**）运行：主进程监督一个或多个工作进程，能够在不断开既有连接的情况下重载配置或更换二进制文件。

# CONFIG EXAMPLE

```
frontend http_front
    bind *:80
    default_backend http_back

backend http_back
    balance roundrobin
    server web1 192.168.1.1:80 check
    server web2 192.168.1.2:80 check
```

# CAVEATS

配置更改需要重载才能生效。复杂的 ACL 需要仔细测试。统计功能需要单独配置。SSL 设置需要管理证书。

# HISTORY

HAProxy 由 **Willy Tarreau** 于 **2000 年**创建，现已成为部署最广泛的负载均衡器之一。GitHub、Reddit 和 Stack Overflow 等高流量网站都由它支撑。

# INSTALL

```apt: sudo apt install haproxy```

```dnf: sudo dnf install haproxy```

```pacman: sudo pacman -S haproxy```

```apk: sudo apk add haproxy```

```zypper: sudo zypper install haproxy```

```brew: brew install haproxy```

```nix: nix profile install nixpkgs#haproxy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nginx](/man/nginx)(1), [envoy](/man/envoy)(1), [traefik](/man/traefik)(1)

# RESOURCES

```[Source code](https://github.com/haproxy/haproxy)```

```[Homepage](https://www.haproxy.org/)```

```[Documentation](https://docs.haproxy.org/)```

<!-- verified: 2026-07-17 -->
