# TAGLINE

并行运行多个 HTTP 请求的 HTTP 基准测试工具

# TLDR

以**每秒 20 个请求**进行测试，持续 60 秒

```http_load -rate 20 -seconds 60 urls.txt```

以 **5 个并发**连接进行测试，持续 60 秒

```http_load -parallel 5 -seconds 60 urls.txt```

以每秒 20 个的速度执行 **1000 个请求**

```http_load -rate 20 -fetches 1000 urls.txt```

使用 5 个并发连接执行 **1000 个请求**

```http_load -parallel 5 -fetches 1000 urls.txt```

直接测试单个 **URL**

```echo "http://example.com/" | http_load -parallel 5 -seconds 30 /dev/stdin```

# SYNOPSIS

**http_load** [_options_] _url_file_

# DESCRIPTION

**http_load** 是一款 HTTP 基准测试工具，通过并行运行多个 HTTP 请求来测试 Web 服务器的吞吐量和响应时间。它从文件中读取 URL，并按指定参数生成负载。

# PARAMETERS

**-rate N**
> 每秒生成 N 个请求

**-parallel N**
> 同时保持 N 个活动连接

**-fetches N**
> 要执行的请求总数

**-seconds N**
> 测试持续时间（秒）

**-timeout N**
> 每个请求的超时时间（秒）

**-sip**
> 源 IP 地址（文件中每行一个）

**-cipher CIPHER**
> 要使用的 SSL 密码套件

**-proxy HOST:PORT**
> 使用 HTTP 代理

**-jitter**
> 让 -rate 的速率随机波动约 10%，以避免过于规律、不真实的流量模式

**-throttle**
> 将数据消耗限制在 33.6Kbps，以模拟调制解调器速度的客户端

**-checksum**
> 对照每个 URL 首次抓取时计算出的校验和，验证之后抓取到的文件

**-verbose**
> 测试运行期间向标准错误打印进度报告

# CAVEATS

必须指定 -rate 或 -parallel 其中之一，不能同时指定。必须指定 -fetches 或 -seconds 之一来设定测试时长。URL 文件应每行包含一个 URL；每次抓取都会从文件中随机选取 URL。

# HISTORY

**http_load** 由 **Jef Poskanzer** 编写并通过 **ACME Labs** 分发，是一款简单的单进程 HTTP 负载测试工具，用于测量 Web 服务器的吞吐量。

# INSTALL

```brew: brew install http_load```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ab](/man/ab)(1), [wrk](/man/wrk)(1), [siege](/man/siege)(1), [hey](/man/hey)(1)

# RESOURCES

```[Source code](https://www.acme.com/software/http_load/)```

<!-- verified: 2026-07-19 -->
