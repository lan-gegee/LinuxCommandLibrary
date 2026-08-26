# TAGLINE

HTTP 负载测试工具

# TLDR

**发送 200 个请求**

```hey -n [200] [https://example.com]```

**设置并发数**

```hey -n [1000] -c [50] [https://example.com]```

**设置持续时间**

```hey -z [30s] [https://example.com]```

**带请求体进行 POST**

```hey -m POST -d "[{\"key\":\"value\"}]" [https://example.com/api]```

**从文件读取请求体进行 POST**

```hey -m POST -D [data.json] -T "[application/json]" [https://example.com/api]```

**添加请求头**

```hey -H "[Authorization: Bearer token]" [https://example.com]```

# SYNOPSIS

**hey** [_options_] _url_

# PARAMETERS

**-n** _requests_
> 要运行的请求总数。默认为 200。

**-c** _concurrency_
> 并发工作线程数。默认为 50。

**-z** _duration_
> 发送请求的持续时间（例如 10s、3m）。会覆盖 -n。

**-m** _method_
> HTTP 方法（GET、POST、PUT、DELETE、HEAD、OPTIONS）。默认为 GET。

**-d** _body_
> 请求体。

**-D** _file_
> 从文件读取请求体。

**-T** _content-type_
> Content-Type 请求头。默认为 "text/html"。

**-H** _header_
> 自定义 HTTP 请求头。可重复使用以添加多个请求头。

**-t** _timeout_
> 每个请求的超时时间（秒）。默认为 20。设为 0 表示无限等待。

**-A** _accept_
> HTTP Accept 请求头。

**-a** _auth_
> 基本认证，格式为 username:password。

**-x** _proxy_
> HTTP 代理地址，格式为 host:port。

**-q** _rate_
> 每个工作线程的 QPS 速率限制。默认不限制。

**-o** _format_
> 输出格式：csv。

**-h2**
> 启用 HTTP/2。

**-host** _header_
> HTTP Host 请求头。

**-disable-compression**
> 禁用压缩。

**-disable-keepalive**
> 禁用 keep-alive，阻止 TCP 连接复用。

**-disable-redirects**
> 禁用跟随 HTTP 重定向。

**-cpus** _n_
> 要使用的 CPU 核心数。

# DESCRIPTION

**hey** 是一个 HTTP 负载测试工具。它向 URL 发送并发请求，并提供延迟分布、吞吐量和状态码分布等统计信息。

hey 用 Go 编写，设计简单而快速。适合对 Web 服务进行快速性能测试和基准测试。

# OUTPUT

显示内容：
- 总耗时和请求数
- 每秒请求数
- 延迟分布（10%、50%、90%、99%）
- 状态码分布
- 错误摘要

# CAVEATS

可能使目标服务器过载，请负责任地使用。可能被速率限制器拦截。不适合分布式负载测试。受单机性能限制。

# HISTORY

hey 由 Google 的 **Jaana B. Dogan**（rakyll）创建，是工具 "boom" 的后继者。它用 Go 编写，设计上追求简洁易用。

# INSTALL

```apt: sudo apt install hey```

```apk: sudo apk add hey```

```zypper: sudo zypper install hey```

```brew: brew install hey```

```nix: nix profile install nixpkgs#hey```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ab](/man/ab)(1), [wrk](/man/wrk)(1), [siege](/man/siege)(1), [k6](/man/k6)(1)
