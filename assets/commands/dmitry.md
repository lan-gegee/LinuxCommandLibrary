# TAGLINE

信息收集侦察工具

# TLDR

**执行 whois 查询**

```dmitry -w [domain.com]```

**获取 netcraft 信息**

```dmitry -n [domain.com]```

**搜索子域名**

```dmitry -s [domain.com]```

**搜索电子邮箱地址**

```dmitry -e [domain.com]```

**执行 TCP 端口扫描**

```dmitry -p [domain.com]```

**端口扫描并抓取 banner**

```dmitry -pb [domain.com]```

**执行全部信息收集**

```dmitry -winsepo [output.txt] [domain.com]```

# SYNOPSIS

**dmitry** [_options_] _host_

# PARAMETERS

_HOST_
> 目标域名或 IP 地址。

**-w**
> 执行 whois 查询。

**-n**
> 获取 Netcraft 信息。

**-s**
> 搜索子域名。

**-e**
> 搜索电子邮件地址。

**-p**
> 执行 TCP 端口扫描。

**-b**
> 从发现的端口读取 banner（需配合 -p）。

**-f**
> 报告被过滤的端口（需配合 -p）。

**-t** _SECONDS_
> 设置端口扫描模块的 TTL（默认 2 秒）。

**-o** _FILE_
> 将输出保存到文件。

**-i**
> 对主机 IP 执行 whois 查询。

**-h**
> 显示帮助信息。

# DESCRIPTION

**dmitry**（Deepmagic Information Gathering Tool）是一款 UNIX 命令行工具，用于渗透测试中的信息收集。它通过多种被动和主动技术收集目标主机的数据。

该工具集成了多项侦察功能：whois 查询、Netcraft 查询、子域名枚举、邮箱地址收集和 TCP 端口扫描。结果可以汇总到一个报告文件中。

dmitry 面向安全评估的信息收集阶段设计，帮助测试人员在进行更主动的测试之前了解目标环境。

# CAVEATS

部分查询可能被限速。端口扫描必须获得授权后才能执行。邮箱收集依赖公开数据的可用性。结果可能因目标配置而异。

# HISTORY

dmitry 为安全专业人员开发的侦察工具。它将多种信息收集技术整合到一个实用程序中，简化了渗透测试项目的初期阶段工作。

# INSTALL

```apt: sudo apt install dmitry```

```nix: nix profile install nixpkgs#dmitry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [whois](/man/whois)(1), [dig](/man/dig)(1), [theHarvester](/man/theHarvester)(1)
