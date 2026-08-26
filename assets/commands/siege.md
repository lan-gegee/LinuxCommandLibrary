# TAGLINE

HTTP 负载测试和基准测试工具

# TLDR

以默认设置（15 个并发用户）**测试 URL**

```siege [https://example.com/]```

以指定并发数和时长进行**基准测试**

```siege -c [50] -t [1M] [https://example.com/]```

**运行基准模式**（请求之间无延迟）

```siege -b -c [100] -t [30S] [https://example.com/]```

从文件**测试多个 URL**

```siege -f [urls.txt]```

**模拟互联网流量**（随机选择 URL）

```siege -i -f [urls.txt] -c [25] -t [5M]```

以请求间自定义延迟**运行**

```siege -d [2] -c [10] [https://example.com/]```

显示单次请求的**响应头**

```siege -g [https://example.com/]```

**显示当前配置**

```siege -C```

# SYNOPSIS

**siege** [_options_] [_URL_]

# PARAMETERS

**-c**, **--concurrent** _num_
> 并发模拟用户数（默认：15）

**-r**, **--reps** _num_|**once**
> 每个用户的重复次数；"once" 表示每个 URL 只运行一次

**-t**, **--time** _NUMm_
> 运行时长及修饰符：S（秒）、M（分钟）、H（小时）

**-d**, **--delay** _num_
> 每个用户各请求之间的随机延迟（0 到 num 秒）

**-b**, **--benchmark**
> 基准模式；去除延迟以获得最大吞吐量

**-f**, **--file** _file_
> 从文本文件读取 URL

**-i**, **--internet**
> 通过随机化 URL 顺序模拟互联网流量

**-g**, **--get** _URL_
> 显示单次请求的 HTTP 头

**-p**, **--print** _URL_
> 显示响应头和响应体

**-A**, **--agent** _string_
> 覆盖 User-Agent 头

**-H**, **--header** _"header: value"_
> 添加自定义请求头

**-T**, **--content-type** _type_
> 覆盖 Content-Type 头

**-v**, **--verbose**
> 显示带颜色标记响应的详细输出

**-q**, **--quiet**
> 抑制输出；适合脚本使用

**-L**, **--log** _file_
> 将结果写入指定的日志文件

**-m**, **--mark** _"string"_
> 在统计信息前记录一条标记消息；便于识别测试轮次

**-R**, **--rc** _file_
> 使用替代的配置文件

**--no-follow**
> 不跟随 3xx 重定向

**-C**, **--config**
> 显示当前配置设置

# DESCRIPTION

**siege** 是一个多线程 HTTP/HTTPS 负载测试和基准测试工具。它模拟多个并发用户访问 Web 服务器，以测量压力下的性能。报告的指标包括响应时间、事务速率、吞吐量、并发数和可用性。

该工具有三种工作模式：**regression**（按顺序测试 URL）、**internet simulation**（通过 **-i** 随机化访问模式）和 **brute force benchmarking**（通过 **-b** 测试最大吞吐量）。

默认情况下，每个模拟用户在请求之间随机暂停，以模拟真实的流量。**-d** 选项控制延迟范围，而 **-b** 则完全消除延迟，用于纯吞吐量测试。

配置保存在 **~/.siege/siege.conf**。URL 可以在命令行上指定，也可以用 **-f** 从文件读取，支持 POST 数据和自定义请求头。

# CONFIGURATION

**~/.siege/siege.conf**
> 用户配置文件，包含默认并发数、延迟、日志记录、协议版本等设置。由 **siege.config** 生成。

**~/.siege/urls.txt**
> 未提供 **-f** 选项或 URL 参数时使用的默认 URL 文件。

# CAVEATS

高并发级别可能压垮目标服务器，并可能构成拒绝服务攻击。对不属于你的服务器进行负载测试之前，务必先获得许可。部分托管服务商在其服务条款中禁止负载测试。

# HISTORY

**siege** 由 **Jeffrey Fulmer**（JoeDog）开发，于 **2000 年**前后首次发布。它旨在帮助 Web 开发者衡量其代码在负载下的性能。该工具一直得到积极维护和更新，以支持 HTTPS 和 HTTP/1.1 等现代 HTTP 特性。

# INSTALL

```apt: sudo apt install siege```

```dnf: sudo dnf install siege```

```pacman: sudo pacman -S siege```

```zypper: sudo zypper install siege```

```brew: brew install siege```

```nix: nix profile install nixpkgs#siege```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ab](/man/ab)(1), [wrk](/man/wrk)(1), [curl](/man/curl)(1), [hey](/man/hey)(1), [vegeta](/man/vegeta)(1)
