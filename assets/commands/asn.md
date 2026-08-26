# TAGLINE

ASN/IP 查询、网络侦察与 OSINT 工具

# TLDR

带 AS 路径追踪地查询 **IP 地址**

```asn [8.8.8.8]```

按编号查询**自治系统**

```asn [AS15169]```

带追踪地查询**主机名**

```asn [github.com]```

执行带 RPKI 校验和劫持检测的**详细追踪**

```asn -d [8.8.8.8]```

查询但**不做追踪**

```asn -n [1.1.1.1]```

搜索名称匹配的**所有 ASN**

```asn -a [google]```

对多个目标进行 **Shodan 扫描**，查找 CVE、开放端口和主机名

```asn -s [1.1.1.1] [8.8.8.8]```

从日志文件中批量**定位 IP 地理位置并统计出现次数**

```asn -g < [access.log]```

列出分配给某个国家的所有 **CIDR 网段**

```asn -c [germany]```

以**格式化 JSON** 输出结果

```asn -J [AS15169]```

# SYNOPSIS

**asn** [_options_] [_target_]

**asn** [**-v**] **-l** [_server options_]

# PARAMETERS

**-t**
> 启用到目标的 AS 路径追踪（IP 目标的默认行为）。

**-n**
> 对 IP 目标禁用路径追踪。对 AS 目标禁用额外的 INETNUM/源站查询。

**-d**
> 启用详细追踪模式，包含 RPKI 校验、路由泄露检测和 BGP 劫持警告。

**-a**
> ASN 建议模式。查找所有与目标字符串匹配的 AS 编号和名称。

**-u**
> 中转/上游查询。分析 BGP 更新和 AS 路径以推断中转运营商。

**-c**
> 国家 CIDR 模式。输出分配给指定国家的所有 IPv4/IPv6 网段。

**-g**
> 批量地理定位模式。从输入中提取所有 IP 地址并进行地理定位，附带出现次数统计。

**-s**
> Shodan InternetDB 扫描。查询 CVE、CPE、标签、开放端口和主机名。支持多个混合目标及 stdin。

**-o**
> 强制将目标解释为组织名称，绕过自动目标类型检测。

**-j**
> 紧凑 JSON 输出，便于程序处理。

**-J**
> 格式化 JSON 输出，便于阅读。

**-m**
> 单色模式。禁用所有彩色输出。

**-4**
> 在追踪和服务器模式中强制仅使用 IPv4 连接。

**-l** [_bind_address_] [_bind_port_]
> 启动服务器模式。开启一个 Web 界面，支持基于浏览器的查询和 traceroute。默认绑定为 127.0.0.1:49200。

**-v**
> 详细/调试模式。显示所有查询的 URL，并将日志输出到 $HOME/asndebug.log。

**-h**
> 显示用法信息。

# SERVER OPTIONS

**--allow** _host[,host,...]_
> 只允许指定主机连接。

**--allowfile** _file_
> 使用主机列表文件限制连接。

**--deny** _host[,host,...]_
> 阻止指定主机连接。

**--denyfile** _file_
> 阻止文件中列出的主机。

**-m**, **--max-conns** _n_
> 最大同时连接数（默认：100）。

# DESCRIPTION

**asn** 是一个用 Bash 编写的功能全面的网络侦察与 OSINT 命令行工具。它可对 IP 地址、AS 编号、前缀、主机名、URL 和组织名称进行查询，综合来自众多数据源的信息生成详细报告。

对于 AS 编号，该工具会检索组织名称、RIR 分配区域、IXP 参与情况、全球 AS 排名、BGP 统计数据、对等互联关系，以及过去 12 个月的 BGP 事件历史（包括劫持和路由泄露）。

对于 IP 地址，它会结合 ASN 数据进行路由查询、来自多个威胁情报源的 IP 信誉评分、滥用投诉联系信息，以及可选的使用 mtr 的 AS 路径追踪。详细追踪模式会在每一跳增加 RPKI 路由源校验，检测潜在的路由泄露和 BGP 劫持。

其他模式支持：从日志文件批量定位 IP 地理位置、按国家枚举 CIDR 网段、基于 Shodan 的漏洞扫描、通过 BGP 更新分析识别中转运营商，以及按组织发现网络地址范围。

该工具还可以作为自托管的 Web 服务器运行，提供浏览器访问和 JSON API 以便与其他工具集成。服务器模式支持访问控制、自定义绑定地址，并可部署为 systemd 服务。

数据源包括 Team Cymru、PeeringDB、CAIDA ASRank、RIPEStat、ipinfo.io、ip-api、Shodan InternetDB、GreyNoise、IPQualityScore、Cloudflare Radar、ISC DSHIELD、NIST NVD 以及 Prefix WhoIs 项目。

# CONFIGURATION

**$HOME/.asnrc**
> 用于覆盖默认值的 Shell 配置文件。支持 MTR_ROUNDS、DETAILED_TRACE、FORCE_IPV4、MAX_CONCURRENT_SHODAN_REQUESTS、MONOCHROME_MODE 等设置，以及服务器绑定地址/端口。

**$HOME/.asn/ipinfo_token**
> ipinfo.io API 令牌，用于增强地理定位数据。

**$HOME/.asn/iqs_token**
> IPQualityScore API 令牌，用于高级威胁情报。

**$HOME/.asn/cloudflare_token**
> Cloudflare Radar API 令牌，用于 BGP 事件数据。

也支持 /etc/asn/ 中的系统级令牌文件，服务器模式部署时优先使用它们。

# CAVEATS

需要 Bash v4.2 或更高版本。使用 mtr 进行路径追踪需要 root 权限或 CAP_NET_RAW 能力。必须安装若干外部依赖：curl、whois、bind9-host（或等效工具）、mtr、jq、ipcalc、grepcidr、nmap、ncat 和 aha。部分功能的完整效果依赖可选的 API 令牌。该工具会查询大量外部服务，因此需要有效的互联网连接。

# HISTORY

**asn** 由 **nitefood** 创建，是一款在事件响应期间快速调查网络数据的 OSINT 命令行工具。它曾被 Security Trails 博客介绍为值得关注的 ASN 查询技术。该项目开源并采用 MIT 许可证，由社区持续贡献维护。它已从一个简单的查询脚本成长为具备服务器模式、JSON API 并集成主流威胁情报源的综合性网络侦察平台。

# INSTALL

```apk: sudo apk add asn```

```brew: brew install asn```

```nix: nix profile install nixpkgs#asn```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[mtr](/man/mtr)(8), [whois](/man/whois)(1), [nmap](/man/nmap)(1), [dig](/man/dig)(1), [traceroute](/man/traceroute)(1), [jq](/man/jq)(1), [curl](/man/curl)(1)
