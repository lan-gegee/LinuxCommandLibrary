# TAGLINE

过滤和搜索 MRT 格式的 BGP 路由数据

# TLDR

**从 MRT 转储中过滤**匹配指定子网的路由

```bgpgrep [path/to/rib.mrt.gz] -subnet [192.0.2.0/24]```

**按 AS 路径模式过滤路由**

```bgpgrep [path/to/rib.mrt.gz] -aspath "[64496 64497]"```

**列出**来自指定对等体的路由

```bgpgrep [path/to/rib.mrt.gz] -peer [198.51.100.1]```

**查找**通往指定地址的路由

```bgpgrep [path/to/rib.mrt.gz] -supernet [8.8.8.8/32]```

**检测路由数据中的 bogon ASN**

```bgpgrep [path/to/rib.mrt.gz] -bogon-asn```

**用逻辑运算符组合过滤器**

```bgpgrep [path/to/rib.mrt.gz] -bogon-asn -or -subnet [fullbogons.txt]```

**按时间戳范围过滤**

```bgpgrep [path/to/updates.mrt.gz] -timestamp "[>=2021-07-01]" -and -timestamp "[<2021-07-08]"```

# SYNOPSIS

**bgpgrep** [_file ..._] [_filter expressions_]

# PARAMETERS

**-peer** _address|asn_
> 匹配从指定对等体（以 IP 地址或 AS 号标识）收到的路由。

**-aspath** _pattern_
> 匹配 AS 路径符合给定模式（pattern）的路由。支持 AS 号序列以及类似正则表达式的语法。

**-supernet** _prefix_
> 匹配是指定前缀的超网（或与之相等）的路由。

**-subnet** _prefix|file_
> 匹配是指定前缀子网的路由，或针对文件中的前缀列表进行匹配。

**-communities** _expression_
> 匹配具有特定 BGP community 值的路由。支持通配符模式。

**-bogon-asn**
> 匹配 AS 路径中包含 bogon（保留/未分配）AS 号的路由。

**-loops**
> 检测 AS 路径环路。

**-timestamp** _condition_
> 使用比较运算符按时间戳过滤（例如 ">=2021-07-01"）。

**-and**
> 过滤条件之间的逻辑与（组合多个过滤器时的默认行为）。

**-or**
> 过滤条件之间的逻辑或。

**-not**
> 取反其后的过滤条件。

# DESCRIPTION

**bgpgrep** 是 Micro BGP Suite 的一部分，这是一组用于过滤和分析 MRT（Multi-threaded Routing Toolkit）格式 BGP 路由数据的 shell 工具。它可以处理来自 RIPE RIS、RouteViews 等路由采集器的 BGP 表转储和更新文件。

输出的每一行都以一个字符作为前缀来指示消息类型：`=` 表示 RIB 快照，`+` 表示宣告，`-` 表示撤回，`#` 表示 BGP 状态变化。输出采用竖线分隔的格式，第 9 个字段包含对等体地址和 ASN，便于与 `cut`、`awk` 等标准命令行工具集成。

该工具支持按前缀、AS 路径模式、对等体、community 和时间戳过滤。多个过滤器可以使用布尔运算符（`-and`、`-or`、`-not`）组合，并支持用括号分组。它同时处理 IPv4 和 IPv6 前缀，并支持压缩的 MRT 文件（gzip、bzip2）。

# CAVEATS

输入必须是 MRT 格式（常见的 BGP 转储格式）。过滤选项名采用单横线长格式（例如 `-peer`，而不是 `--peer`）。AS 路径匹配模式使用 bgpgrep 特有的语法，与标准正则表达式不同。

# SEE ALSO

[traceroute](/man/traceroute)(1), [whois](/man/whois)(1)
