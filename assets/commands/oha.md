# TAGLINE

用 Rust 编写的 HTTP 压力测试工具，灵感来自 hey 和 rakyll/hey

# TLDR

**向 URL 发送 100 个请求**

```oha -n [100] [https://example.com]```

**运行 30 秒的压力测试**

```oha -z [30s] [https://example.com]```

**使用 50 个并发连接测试**

```oha -c [50] -n [1000] [https://example.com]```

**发送带 JSON 主体的 POST 请求**

```oha -m POST -d '[{"key":"value"}]' -T application/json [https://example.com/api]```

**使用自定义请求头**

```oha -H "Authorization: Bearer [token]" [https://example.com]```

**设置每秒查询数限制**

```oha -q [100] -z [30s] [https://example.com]```

**禁用 TLS 验证**

```oha --insecure [https://example.com]```

**以 JSON 格式输出结果**

```oha -n [100] --json [https://example.com]```

# SYNOPSIS

**oha** [_options_] _url_

# PARAMETERS

**-n** _num_
> 要发送的请求数量。默认：200。

**-c** _num_
> 并发连接数。默认：50。

**-z** _duration_
> 测试时长（如 10s、1m）。

**-q** _rate_
> 每秒查询数速率限制。

**-m**, **--method** _method_
> HTTP 方法：GET、POST、PUT、DELETE 等。

**-d**, **--data** _body_
> 请求主体数据。

**-D**, **--data-file** _file_
> 从文件读取请求主体。

**-T**, **--content-type** _type_
> Content-Type 请求头的值。

**-H** _header_
> 自定义请求头（可重复）。

**-A**, **--accept** _type_
> Accept 请求头的值。

**-t**, **--timeout** _secs_
> 请求超时时间（秒）。

**--latency-correction**
> 启用协调遗漏（coordinated omission）修正。

**--no-tui**
> 禁用实时终端界面。

**--json**
> 以 JSON 格式输出结果。

**--insecure**
> 跳过 TLS 证书验证。

**--http2**
> 使用 HTTP/2。

**--host** _host_
> 覆盖 Host 请求头。

**-p**, **--redirect** _num_
> 最大重定向跟随次数。

# DESCRIPTION

**oha** 是一个用 Rust 编写的 HTTP 压力测试工具，灵感来自 hey 和 rakyll/hey。它在压测过程中提供实时 TUI 可视化以及详细的延迟统计。

默认情况下，oha 会显示一个终端界面，展示请求进度、延迟分布和错误率。脚本化执行请用 **--no-tui**，需要机器可读的输出请用 **--json**。

该工具测量响应时间的分布，包括百分位数（p50、p90、p99）、吞吐量和错误率。启用 **--latency-correction** 后会应用协调遗漏修正，从而在负载下获得准确的延迟数据。

配合 **-q** 进行限速，可以在不压垮目标的情况下进行受控压测；再结合 **-z** 设定测试时长，即可模拟真实的流量场景。

oha 支持 HTTP/1.1 和 HTTP/2、用于认证的自定义请求头，以及多种请求主体格式，便于进行 API 测试。

# CAVEATS

过高的并发设置可能耗尽文件描述符或网络资源。请谨慎使用 --insecure。限速精度取决于系统性能。解读结果时应考虑网络状况的影响。

# HISTORY

oha 由 **Haruki Shimada**（hatoo）创建，于 **2020** 年前后首次发布。名字在日语中意为"早上好"。它使用 Rust 编写并基于 tokio 实现异步 I/O，提供带实时可视化的现代压测能力。作为 ab、wrk 等老牌工具之外快速易用的替代品，该项目广受欢迎。

# INSTALL

```pacman: sudo pacman -S oha```

```brew: brew install oha```

```nix: nix profile install nixpkgs#oha```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hey](/man/hey)(1), [wrk](/man/wrk)(1), [ab](/man/ab)(1), [curl](/man/curl)(1), [siege](/man/siege)(1)
