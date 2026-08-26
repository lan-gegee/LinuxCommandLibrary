# TAGLINE

通过发送 HTTP 请求测量 Web 服务器的延迟和吞吐量

# TLDR

**Ping 一个 URL**

```httping [https://example.com]```

**指定次数 Ping**

```httping -c [5] [https://example.com]```

**使用 GET 代替 HEAD**

```httping -G [https://example.com]```

**使用 SSL/HTTPS**

```httping -l [https://example.com]```

**显示分阶段的延迟计时**

```httping -S [https://example.com]```

**使用持久连接**

```httping -Q [https://example.com]```

**设置超时时间**

```httping -t [5] [https://example.com]```

# SYNOPSIS

**httping** [_options_] _url_

# PARAMETERS

**-c** _count_
> Ping 次数。

**-G**
> 使用 GET 请求代替 HEAD。

**-l**
> 使用 SSL 连接（用于 https）。

**-S**
> 将延迟细分为连接、发送、接收等阶段。

**-Q**
> 使用持久连接（Keep-Alive）。

**-t** _seconds_
> 每个请求的超时时间。

**-i** _seconds_
> 请求之间的间隔。

**-q**
> 安静模式，只显示摘要。

**-x** _host:port_
> 通过指定的代理服务器进行探测。

**-m**
> 输出机器可读格式，便于在脚本中使用。

**-b**
> 以 KB/s 显示传输速度（与 **-G** 配合使用）。

**-v**
> 详细模式，额外显示标准差和时间戳。

# DESCRIPTION

**httping** 通过发送 HTTP 请求并对响应计时来测量 Web 服务器的延迟和吞吐量。与 ICMP ping 不同，它测量的是实际的 HTTP 往返时间，其中包含网络延迟和服务器处理时间。使用 **-S** 可以查看各连接阶段的耗时分解。

# INSTALL

```apt: sudo apt install httping```

```dnf: sudo dnf install httping```

```pacman: sudo pacman -S httping```

```brew: brew install httping```

```nix: nix profile install nixpkgs#httping```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ping](/man/ping)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/folkertvanheusden/HTTPing)```

```[Homepage](https://www.vanheusden.com/httping/)```

<!-- verified: 2026-07-19 -->
