# TAGLINE

高 QPS 的 DNS 基准测试工具

# TLDR

用 A 查询对域名**进行 DNS 服务器基准测试**

```dnspyre --server [8.8.8.8] [example.com]```

以高并发**运行基准测试**，持续 60 秒

```dnspyre --server [8.8.8.8] --duration 60s --concurrency [100] [example.com]```

以固定查询次数**运行基准测试**

```dnspyre --server [8.8.8.8] --number [1000] [example.com]```

**测试特定的查询类型**

```dnspyre --server [8.8.8.8] --type A --type AAAA [example.com]```

**从文件加载查询**

```dnspyre --server [8.8.8.8] @[path/to/queries.txt]```

基于 DNS over HTTPS **运行基准测试**

```dnspyre --server https://dns.google/dns-query --doh-method post [example.com]```

# SYNOPSIS

**dnspyre** [_options_] _queries_...

# PARAMETERS

**-s**, **--server** _ADDR_
> 要测试的 DNS 服务器地址。

**-n**, **--number** _N_
> 查询重复次数（与 --duration 互斥）。

**-d**, **--duration** _DURATION_
> 测试时长（默认：1m，与 --number 互斥）。

**-c**, **--concurrency** _N_
> 并发连接数（默认：1）。

**-t**, **--type** _TYPE_
> DNS 查询类型：A、AAAA、CNAME、MX、TXT、HTTPS 等。可多次指定。

**--tcp**
> 使用 TCP 而非 UDP。

**--dot**
> 使用 DNS over TLS（DoT）。

**--doh-method** _METHOD_
> 以 GET 或 POST 方法使用 DNS over HTTPS。

**--doh-protocol** _PROTO_
> DoH 的 HTTP 协议版本（1.1、2、3）。

**--doq**
> 使用 DNS over QUIC（DoQ）。

**--recurse**
> 设置 recursion desired 标志（默认：开启）。

**--probability** _FLOAT_
> 每个查询的发送概率（0.0-1.0）。

**--progress**
> 显示进度条（默认：开启）。

**-o**, **--output** _FORMAT_
> 输出格式：text、json、csv。

**-v**, **--verbose**
> 启用详细输出。

# DESCRIPTION

**dnspyre** 是一款高性能 DNS 基准测试工具，专为在重负载下压测 DNS 服务器而设计。它可以模拟每秒数千个并发查询，并提供响应时间、错误率和吞吐量的详细统计。它最初是 dnstrace 的分支，后来经过了大量重写和增强。

查询可以直接指定域名、用 **@file-path** 从本地文件加载，或从 HTTP URL 获取。一次运行中可以组合多个查询来源。该工具支持 UDP、TCP、DNS over TLS（DoT）、DNS over HTTPS（DoH）和 DNS over QUIC（DoQ）。

# OUTPUT METRICS

- 每秒查询数（QPS）
- 延迟百分位（p50、p90、p99、p999）
- 错误率及错误类型
- 连接统计
- 响应时间直方图

# CAVEATS

高 QPS 测试可能压垮目标服务器。--duration 与 --number 选项互斥。网络状况和中间解析器的 DNS 缓存可能使结果失真。

# HISTORY

**dnspyre** 由 **Tantalor93** 开发，是 dnstrace 的现代化分支，增加了对现代 DNS 协议（DoT、DoH、DoQ）的支持并改进了并发控制。

# INSTALL

```brew: brew install dnspyre```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [nslookup](/man/nslookup)(1), [q](/man/q)(1)
