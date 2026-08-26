# TAGLINE

IPinfo API 的官方命令行客户端

# TLDR

**查询你自己的 IP 地址**

```ipinfo myip```

**查询特定 IP 地址的详情**

```ipinfo [8.8.8.8]```

**查询 ASN 信息**

```ipinfo [AS15169]```

**批量查询**多个 IP 或 CIDR 段

```ipinfo bulk [1.1.1.0/30] [8.8.8.8]```

**提取特定字段**（城市、国家、组织、主机名等）

```ipinfo [8.8.8.8] -f [city]```

**以 CSV 格式输出**

```cat ips.txt | ipinfo -c```

使用 API 令牌**进行身份验证**以获得更高的速率限制

```ipinfo init [your_token]```

**汇总**一组 IP 的详情

```cat ips.txt | ipinfo summarize```

# SYNOPSIS

**ipinfo** [_command_] [_IP_|_ASN_] [_options_]

# PARAMETERS

**init** _token_
> 保存用于身份验证请求的 API 令牌。

**myip**
> 查询你自己的 IP 地址详情。

**bulk** _ips_
> 处理多个 IP 或 CIDR 段。

**summarize** _ips_
> 为一组 IP 生成汇总报告。

**-f**, **--field** _FIELD_
> 仅返回指定字段（如 ip、city、region、country、org、hostname）。

**-c**, **--csv**
> 以 CSV 格式输出结果。

**--nocolor**
> 关闭彩色输出（或设置 `NO_COLOR` 环境变量）。

**--token** _TOKEN_
> 为本次调用传入 API 令牌。

**completion**
> 生成 Shell 补全脚本（bash、zsh、fish）。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**ipinfo** 是 IPinfo.io API 的官方命令行客户端。它返回 IP 情报数据，包括地理位置、ISP、组织、ASN、主机名和滥用投诉联系信息。

该工具接受 IP 地址（IPv4/IPv6）、ASN 和 CIDR 段。可以一次查询多个输入，也可以从其他命令管道传入。输出可呈现为人类可读的文本、JSON 或 CSV 格式，并可提取特定字段供脚本使用。

该 CLI 还附带多个辅助程序，如 **grepip**、**prips**、**cidr2range**、**cidr2ip**、**range2cidr** 和 **mmdb**，用于处理 IP 列表和 MMDB 数据库。

# CAVEATS

需要联网才能访问 ipinfo.io。匿名请求受到严格的速率限制；通过 `ipinfo init` 注册免费令牌可获得更高的配额。私有地址、保留地址和多播地址无法进行地理定位。地理定位的准确性因地区和网络类型而异。

# HISTORY

由 **IPinfo.io** 开发，这是一家成立于 **2013 年**的地理定位数据提供商。该 CLI 使用 Go 编写，封装了与 Web 服务相同的公共 API。

# INSTALL

```brew: brew install ipinfo```

```nix: nix profile install nixpkgs#ipinfo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [whois](/man/whois)(1), [dig](/man/dig)(1), [jq](/man/jq)(1)
