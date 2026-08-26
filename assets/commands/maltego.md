# TAGLINE

OSINT 与图形化关联分析工具

# TLDR

**启动 Maltego**

```maltego```

**启动社区版**

```maltego ce```

**带配置无界面运行**

```maltego -i [config.mtgx]```

# SYNOPSIS

**maltego** [_options_]

# PARAMETERS

**ce**
> 社区版模式。

**-i** _file_
> 导入配置。

**--help**
> 显示帮助。

# DESCRIPTION

**Maltego** 是一款 OSINT（开源情报）与图形化关联分析工具。它将人员、组织、域名、IP 地址和基础设施等实体之间的关系可视化。

Maltego 使用 transform（变换）自动从各种来源收集数据，并以图的形式展示连接关系。

# ENTITY TYPES

```
- Infrastructure: Domains, IPs, DNS
- Personal: Names, Email, Social
- Network: AS Numbers, Netblocks
- Documents: Files, URLs
```

# EDITIONS

```
Community (CE) - Free, limited transforms
Classic        - Commercial
XL             - Enterprise scale
```

# CAVEATS

需要 Java。社区版功能受限。Transform 服务器可能有速率限制。高级 transform 需要订阅。

# HISTORY

Maltego 由南非的 **Paterva** 开发，于 **2008 年**首次发布。它已成为渗透测试和情报收集领域的标准工具。

# INSTALL

```nix: nix profile install nixpkgs#maltego```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[recon-ng](/man/recon-ng)(1)
