# TAGLINE

现代 HTTP 压测工具

# TLDR

以默认设置**对 URL 压测**

```wrk [http://localhost:8080/]```

指定线程数、连接数和时长进行**压测**

```wrk -t [12] -c [400] -d [30s] [http://localhost:8080/]```

**显示详细的延迟统计**

```wrk -t [4] -c [100] -d [10s] --latency [http://localhost:8080/]```

**添加自定义请求头**

```wrk -H "Authorization: Bearer [token]" [http://localhost:8080/]```

**使用 Lua 脚本**自定义请求

```wrk -s [script.lua] [http://localhost:8080/]```

**设置请求超时**

```wrk -t [4] -c [100] --timeout [5s] [http://localhost:8080/]```

# SYNOPSIS

**wrk** [_options_] _url_

# PARAMETERS

**-t**, **--threads** _n_
> 使用的线程数量。

**-c**, **--connections** _n_
> 保持打开的 HTTP 连接数量。

**-d**, **--duration** _time_
> 测试时长（如 30s、1m、2h）。

**-s**, **--script** _file_
> 加载 Lua 脚本实现自定义行为。

**-H**, **--header** _header_
> 添加自定义 HTTP 请求头（可重复使用）。

**-L**, **--latency**
> 打印详细的延迟统计。

**--timeout** _time_
> 套接字/请求超时时长。

**-v**, **--version**
> 打印版本信息。

# DESCRIPTION

**wrk** 是一款现代 HTTP 压测工具，仅用单个多核 CPU 就能产生可观的负载。它将多线程设计与可扩展的事件通知系统（Linux 上为 epoll，BSD/macOS 上为 kqueue）相结合。

该工具测量每秒请求数、传输速率和延迟分布。它支持带 keep-alive 连接的 HTTP/1.1，并可通过可选的 LuaJIT 脚本实现自定义请求生成、响应处理和报告。

Lua 脚本可用于发送 POST 请求、构造动态载荷、为每个请求设置自定义请求头以及校验响应。

# CAVEATS

在大多数系统上，wrk 需要从源码构建，因为它不在标准软件仓库中。HTTPS 支持需要 libssl-dev。高连接数可能需要调整系统限制（ulimit、sysctl）。结果会因网络状况和服务器容量而异。

# HISTORY

wrk 由 **Will Glozer** 创建，大约于 **2012 年**首次发布。它被设计为 ab（Apache Bench）等老牌压测工具的现代替代品，通过高效利用现代操作系统特性获得更好的性能。Lua 脚本功能的加入使其能够支持简单 GET 请求之外的复杂测试场景。

# INSTALL

```apt: sudo apt install wrk```

```apk: sudo apk add wrk```

```zypper: sudo zypper install wrk```

```brew: brew install wrk```

```nix: nix profile install nixpkgs#wrk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ab](/man/ab)(1), [siege](/man/siege)(1), [hey](/man/hey)(1), [curl](/man/curl)(1)
