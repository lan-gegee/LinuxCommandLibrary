# TAGLINE

发现某个组织的域名和基础设施

# TLDR

**发现**某组织的根域名

```amass intel -org "[Company Name]"```

从 **ASN** 查找域名

```amass intel -asn [AS12345]```

按 **IP 范围**反向查找

```amass intel -cidr [192.168.1.0/24]```

从 **whois** 数据中查找域名

```amass intel -whois -d [example.com]```

# SYNOPSIS

**amass intel** [_-org name_] [_-asn number_] [_-cidr range_] [_options_]

# DESCRIPTION

**amass intel** 收集情报以识别某个组织拥有的域名和基础设施。它使用多种技术，包括 ASN 查询、WHOIS 分析、证书透明度日志和反向 IP 查找。

此命令通常在信息收集初期使用，用于在进行详细枚举之前找出所有根域名。

# PARAMETERS

**-org** _name_
> 用于匹配 AS 描述信息的搜索字符串

**-asn** _number_
> 逗号分隔的 ASN（可多次使用）

**-cidr** _range_
> 逗号分隔的 CIDR（可多次使用）

**-addr** _ips_
> 逗号分隔的 IP 和范围（例如 192.168.1.1-254）

**-whois**
> 对所有发现的域名执行反向 WHOIS 查询

**-d** _domain_
> 逗号分隔的域名（可多次使用）

**-active**
> 启用主动信息收集方法

**-ip**
> 显示发现名称对应的 IP 地址

**-o** _file_
> 输出文件

**-config** _file_
> 配置文件

# CONFIGURATION

**~/.config/amass/config.ini**
> Amass 配置文件，定义数据源、API 密钥和范围设置。

# CAVEATS

组织名称匹配是模糊的；请核查结果的准确性。WHOIS 数据可能受到隐私保护。ASN 信息可能未覆盖组织的全部资产。

# HISTORY

**amass intel** 的加入提供了组织级别的信息收集能力，与专注于域名的 enum 命令互为补充。

# INSTALL

```aur: yay -S amass```

```brew: brew install amass```

```nix: nix profile install nixpkgs#amass```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[amass](/man/amass)(1), [amass-enum](/man/amass-enum)(1), [amass-track](/man/amass-track)(1), [whois](/man/whois)(1)

# RESOURCES

```[Source code](https://github.com/owasp-amass/amass)```

```[Documentation](https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md)```

<!-- verified: 2026-06-11 -->
