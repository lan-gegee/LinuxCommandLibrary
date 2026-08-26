# TAGLINE

node

# TLDR

**运行负载测试**

```loadtest -c [10] -n [1000] [http://example.com/api]```

**限制每秒请求数运行**

```loadtest -c [10] --rps [100] [http://example.com/api]```

**带请求体的 POST 请求**

```loadtest -c [5] -P '[{"key":"value"}]' -T 'application/json' [http://example.com/api]```

# SYNOPSIS

**loadtest** [_options_] _url_

# PARAMETERS

**-c** _num_
> 并发客户端数量。

**-n** _num_
> 总请求数。

**--rps** _num_
> 每秒请求数上限。

**-t** _seconds_
> 最大运行时间。

**-P** _body_
> POST 请求体。

**-T** _type_
> Content-Type 头部。

**-H** _header_
> 自定义头部。

**-k**
> 保持连接（keep-alive）。

# DESCRIPTION

**loadtest** 是一款 Node.js 的 HTTP API 负载测试工具。它生成可配置的并发请求来测量服务器性能并找出瓶颈，报告延迟百分位数、吞吐量和错误率。

# SEE ALSO

[ab](/man/ab)(1), [wrk](/man/wrk)(1), [siege](/man/siege)(1)
