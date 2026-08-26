# TAGLINE

带实时 TUI 图表的 HTTP 负载测试工具

# TLDR

对某个 URL **运行基本负载测试**

```ali [http://host.xz]```

**设置自定义请求速率和持续时间**

```ali --rate=[500] --duration=[5m] [http://host.xz]```

携带 body 文件**发送 POST 请求**

```ali --method=POST --body-file=[path/to/payload.json] [http://host.xz]```

为请求**添加自定义头部**

```ali -H "Authorization: Bearer [token]" [http://host.xz]```

将结果**导出**到目录以便后续分析

```ali --export-to [path/to/results/] [http://host.xz]```

禁用 TLS 验证进行**负载测试**

```ali --insecure [https://host.xz]```

以**最大速度运行**，不限速率

```ali --rate=0 --duration=[30s] [http://host.xz]```

# SYNOPSIS

**ali** [_options_] _target_

# PARAMETERS

**-r**, **--rate** _n_
> 每秒请求数；0 表示最大速度（默认：50）

**-d**, **--duration** _duration_
> 攻击持续时间；0s 表示无限（默认：10s）

**-w**, **--workers** _n_
> 初始 worker 数量（默认：10）

**-m**, **--method** _method_
> HTTP 方法（默认：GET）

**-t**, **--timeout** _duration_
> 请求超时时间（默认：30s）

**-b**, **--body** _string_
> 以字符串形式给出的请求体

**-B**, **--body-file** _file_
> 请求体文件的路径

**-H**, **--header** _header_
> 自定义头部（可重复）

**-c**, **--connections** _n_
> 每个主机的最大空闲连接数（默认：10000）

**--export-to** _dir_
> 导出结果的目录

**--insecure**
> 跳过 TLS 证书验证

**--no-http2**
> 禁用 HTTP/2

**-K**, **--no-keepalive**
> 禁用 keep-alive 连接

**--resolvers** _addrs_
> 自定义 DNS 解析器地址

# DESCRIPTION

**ali** 是一款基于终端的 HTTP 负载测试工具，它生成 HTTP 负载并将结果以图表形式实时绘制在终端中。它结合了 vegeta 等工具的负载生成能力与实时终端图表，展示延迟、分位数（p50、p90、p95、p99）、吞吐量以及输入/输出字节数。交互式 TUI 支持用鼠标缩放图表，便于详细分析。

ali 用 Go 编写，默认支持 HTTP/2、自定义 TLS 证书、可配置的并发度，以及用于下游分析的结果导出。

# CAVEATS

终端 UI 需要支持标准转义序列的终端。极高的请求速率可能受系统资源和网络容量限制。将持续时间设为 0 会让攻击无限持续，直到手动停止。

# HISTORY

**ali** 由 **Ryo Nakao**（nakabonne）创建，他是一位来自日本东京的 Go 开发者。该工具的灵感来自 **vegeta**（HTTP 负载测试）和 **jplot**（终端绘图），将二者融合为一个实时工具。它以 MIT 许可证开源。

# INSTALL

```pacman: sudo pacman -S ali```

```apk: sudo apk add ali```

```brew: brew install ali```

```nix: nix profile install nixpkgs#ali```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ab](/man/ab)(1), [wrk](/man/wrk)(1), [curl](/man/curl)(1), [hey](/man/hey)(1), [siege](/man/siege)(1), [vegeta](/man/vegeta)(1), [k6](/man/k6)(1)
