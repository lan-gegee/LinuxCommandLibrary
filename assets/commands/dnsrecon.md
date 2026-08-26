# TAGLINE

功能全面的 DNS 侦察工具

# TLDR

对域名执行**标准枚举**

```dnsrecon -d [example.com]```

执行**区域传送**

```dnsrecon -d [example.com] -n [nameserver.example.com] -t axfr```

使用字典**暴力破解**子域名

```dnsrecon -d [example.com] -D [path/to/dictionary.txt] -t brt```

对 IP 段执行**反向查询**

```dnsrecon -r [192.168.1.0/24]```

扫描并将结果保存到 **JSON 文件**

```dnsrecon -d [example.com] -j [path/to/results.json]```

对域名服务器进行**缓存侦测**（cache snooping）

```dnsrecon -d [example.com] -t snoop -n [nameserver.example.com] -D [path/to/dictionary.txt]```

**DNSSEC 区域漫游**

```dnsrecon -d [example.com] -t zonewalk```

结合 **SPF 反向查询**的标准枚举，并保存到 **SQLite 数据库**

```dnsrecon -d [example.com] -s --db [path/to/database.sqlite]```

# SYNOPSIS

**dnsrecon** [_options_]

# DESCRIPTION

**dnsrecon** 是一款功能全面的 DNS 侦察工具，通过多种枚举技术来绘制 DNS 基础设施。它将区域传送（AXFR）、暴力子域名发现、缓存侦测、DNSSEC 区域漫游和反向查询整合到一个工具中。

该工具支持多种扫描类型：标准枚举、提取完整区域数据的区域传送、用自定义字典暴力发现子域名、检查域名服务器上缓存记录的缓存侦测，以及利用 NSEC 记录枚举区域的 DNSSEC 区域漫游。结果可导出为多种格式，包括 JSON、CSV 和 SQLite 数据库，便于分析。它还能执行 Google 枚举以通过搜索引擎结果查找子域名，并进行 SPF 记录分析来发现相关 IP 段。该工具广泛用于渗透测试和安全评估，可全面摸清一个组织的 DNS 足迹。

# PARAMETERS

**-d**, **--domain** _DOMAIN_
> 目标域名。

**-n**, **--name_server** _NS_SERVER_
> 要使用的域名服务器。若未指定，则使用目标的 SOA。

**-r**, **--range** _RANGE_
> 用于反向查询暴破的 IP 段，格式为 (first-last) 或 (range/bitmask)。

**-t**, **--type** _TYPE_
> 枚举类型：std、rvl、brt、srv、axfr、bing、yand、crt、snoop、tld、zonewalk。

**-D**, **--dictionary** _DICTIONARY_
> 用于暴破的子域名与主机名字典文件。

**-a**
> 在标准枚举的同时执行 AXFR。

**-s**
> 在标准枚举的同时对 SPF 记录中的 IPv4 段执行反向查询。

**-z**
> 在标准枚举的同时执行 DNSSEC 区域漫游。

**-f**
> 从暴破结果中过滤掉被泛解析解析出来的记录。

**--threads** _THREADS_
> 用于并行处理的线程数。

**--lifetime** _LIFETIME_
> 等待服务器响应查询的时间（秒），默认为 3。

**--tcp**
> 使用 TCP 协议发起查询。

**-j**, **--json** _JSON_
> 保存所查找到的记录的 JSON 文件。

**-c**, **--csv** _CSV_
> 保存所查找到的记录的逗号分隔值（CSV）文件。

**-x**, **--xml** _XML_
> 保存所查找到的记录的 XML 文件。

**--db** _DB_
> 保存所查找到的记录的 SQLite 3 文件。

**-v**
> 启用详细输出。

**-V**
> 显示版本信息。

# CAVEATS

仅可用于已授权的目标。区域传送通常会被域名服务器阻止。暴破速度取决于字典大小，可能较慢。Google 枚举可能受到速率限制。

# INSTALL

```apk: sudo apk add dnsrecon```

```nix: nix profile install nixpkgs#dnsrecon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [nslookup](/man/nslookup)(1), [host](/man/host)(1), [dnsmap](/man/dnsmap)(1), [dnsenum](/man/dnsenum)(1), [fierce](/man/fierce)(1)
