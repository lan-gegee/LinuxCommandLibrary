# TAGLINE

用于检查、重放和修改流量的本地代理

# TLDR

**将 oproxy 作为**本地 HTTP、HTTPS 和 SOCKS5 代理**运行**

```oproxy```

**让请求经过**代理

```curl -x http://127.0.0.1:8080 [http://example.com]```

**在 Docker 中运行 oproxy**，暴露代理与 UI 端口

```docker run --rm -p 127.0.0.1:8080:8080 -p 127.0.0.1:1080:1080 ghcr.io/sauravrao637/oproxy:latest```

# SYNOPSIS

**oproxy** [_options_]

# DESCRIPTION

**oproxy** 是一款本地 HTTP、HTTPS 和 SOCKS5 代理，用于检查、重放和修改来自浏览器、命令行工具和应用程序的网络流量。安装其本地证书颁发机构（CA）后，它可以对 HTTPS 执行中间人拦截，解码包括头部、正文、状态和耗时在内的请求与响应，并能识别 JWT、GraphQL、gRPC 和 WebSocket 载荷。

除了观测之外，oproxy 还能实时改写流量：规则集支持 map-remote 和 map-local 重定向、限流、断点、模拟响应以及 DNS 覆盖，因此可用于调试、测试错误处理，以及针对尚未就绪的 API 进行开发。它会在本地提供一个 Web UI，展示捕获的流量和规则配置。

# CAVEATS

拦截 HTTPS 需要信任 oproxy 本地生成的证书颁发机构；请只在你能控制的机器上安装，用完后将其移除。该代理面向本地开发和测试，不适合作为生产网关。

# SEE ALSO

[mitmproxy](/man/mitmproxy)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/sauravrao637/oproxy)```

<!-- verified: 2026-06-10 -->
