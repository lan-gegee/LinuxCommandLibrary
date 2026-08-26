# TAGLINE

HTTP 压力测试工具

# TLDR

**测试**指定的网站

```goldeneye.py [url]```

使用自定义 **user-agent 列表**和 **200 个并发套接字**进行测试

```goldeneye.py [url] -u [useragents.txt] -s 200```

测试时不**验证 SSL** 证书

```goldeneye.py [url] -n```

以**调试模式**测试

```goldeneye.py [url] -d```

显示**帮助**

```goldeneye.py -h```

# SYNOPSIS

**goldeneye.py** _url_ [_options_]

# PARAMETERS

**-u**, **--useragents** _FILE_
> 存放轮换使用的 user agent 列表的文件

**-s**, **--sockets** _NUM_
> 并发套接字数量

**-w**, **--workers** _NUM_
> 工作进程数量

**-n**, **--nosslcheck**
> 不验证 SSL 证书

**-d**, **--debug**
> 启用调试输出

**-m**, **--method** _METHOD_
> HTTP 方法：GET、POST、RANDOM

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**goldeneye.py** 是一款 HTTP 压力测试工具，用于检验 Web 服务器和应用程序在高负载条件下的承受能力。它通过随机化的请求头和 user agent 建立并发 HTTP 连接，模拟流量模式并找出性能瓶颈。

> **警告**：本工具仅限用于对你拥有或已获明确授权的系统进行授权安全测试和负载测试。未经授权对不属于你的系统使用属于违法行为，且有悖道德。

# CAVEATS

在大多数司法辖区，未经授权对本工具所指向的系统使用它是违法的。请仅将其用于合法的负载测试、持有书面许可的渗透测试，或针对你自己系统的安全研究。

# HISTORY

**GoldenEye** 由 **Jan Seidl**（jseidl）创建，是对更早的 "GoldenEye" C 工具背后第 7 层 DoS 技术的概念验证实现：利用 HTTP Keep-Alive 和 no-cache 请求头来耗尽服务器的连接池。

# SEE ALSO

[ab](/man/ab)(1), [siege](/man/siege)(1), [wrk](/man/wrk)(1)

# RESOURCES

```[Source code](https://github.com/jseidl/GoldenEye)```

<!-- verified: 2026-07-17 -->
