# TAGLINE

HTTP 服务器基准测试工具

# TLDR

以 10 个并发连接对 URL 发起 100 个请求进行**基准测试**

```ab -n 100 -c 10 [http://example.com/]```

向 URL **POST** 数据

```ab -n 100 -c 10 -p [data.json] -T application/json [http://example.com/api]```

使用 **keep-alive** 连接

```ab -n 100 -c 10 -k [http://example.com/]```

设置**自定义请求头**

```ab -n 100 -c 10 -H "Authorization: Bearer [token]" [http://example.com/]```

# SYNOPSIS

**ab** [_-n requests_] [_-c concurrency_] [_-t timelimit_] [_options_] _URL_

# DESCRIPTION

**ab**（Apache Benchmark）是一个用于 HTTP 服务器基准测试的命令行工具。它通过向指定的 URL 发送多个请求来产生负载，并测量服务器的响应时间、吞吐量和其他性能指标。

该工具报告的统计信息包括每秒请求数、每请求耗时、传输速率以及按百分位细分的连接时间。它同时支持 HTTP 和 HTTPS，可自定义请求头、发送 POST 数据、携带 Cookie 以及使用 HTTP 认证。

# PARAMETERS

**-n** _requests_
> 本轮测试要执行的请求总数

**-c** _concurrency_
> 同时执行的请求数（并发连接数）

**-t** _timelimit_
> 基准测试的最长秒数（隐含 -n 50000）

**-k**
> 启用 HTTP KeepAlive 特性（持久连接）

**-p** _file_
> 包含要 POST 数据的文件

**-T** _content-type_
> POST/PUT 数据的 Content-type 请求头

**-H** _header_
> 为请求追加额外请求头（可重复使用）

**-A** _auth_
> HTTP Basic 认证凭据（user:password）

**-C** _cookie_
> 添加 Cookie 请求头（name=value）

**-s** _timeout_
> 套接字超时前的最长等待秒数（默认 30）

**-v** _verbosity_
> 详细程度（2=警告，3=响应码，4 及以上=响应头）

**-u** _file_
> 包含要 PUT 数据的文件（需同时设置 -T）

**-X** _proxy[:port]_
> 通过代理服务器发送请求

**-e** _csv-file_
> 输出包含响应时间百分位（1%-100%）的 CSV 文件

**-g** _gnuplot-file_
> 将测量值写成 gnuplot/TSV 文件

**-i**
> 使用 HEAD 请求代替 GET

**-l**
> 接受可变长度的文档（针对动态页面）

**-r**
> 套接字接收出错时不退出

**-q**
> 抑制 stderr 上的进度信息（针对超过 150 个请求的情况）

# CAVEATS

**ab** 制造的是合成负载，未必反映真实流量模式。它不解析 HTML 也不执行 JavaScript，因此只测试原始的 HTTP 性能。如果服务器实现了限速或缓存，结果可能产生误导。如需更真实的负载测试，可以考虑 **wrk**、**siege** 或 **k6** 等工具。

# HISTORY

**ab** 是 Apache HTTP Server 项目于上世纪 **90 年代末**创建的组件。它的设计初衷是开发过程中测试 Apache 配置的简单基准测试工具。该工具多年来几乎没有变化，如今随全球的 Apache HTTPD 安装一起分发。

# INSTALL

```apt: sudo apt install apache2-utils```

```apk: sudo apk add apache2-utils```

```zypper: sudo zypper install apache2-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [wrk](/man/wrk)(1), [siege](/man/siege)(1)
