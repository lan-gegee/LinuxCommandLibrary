# TAGLINE

在命令行中管理 Cloudflare

# TLDR

**列出 DNS 记录**

```flarectl dns list --zone [example.com]```

**创建 DNS 记录**

```flarectl dns create --zone [example.com] --name [www] --type [A] --content [1.2.3.4]```

**删除 DNS 记录**

```flarectl dns delete --zone [example.com] --id [record_id]```

**列出区域**

```flarectl zone list```

**清除缓存**

```flarectl zone purge --zone [example.com] --everything```

**列出防火墙规则**

```flarectl firewall rules list --zone [example.com]```

# SYNOPSIS

**flarectl** _command_ _subcommand_ [_options_]

# SUBCOMMANDS

**zone**
> 管理区域。

**dns**
> 管理 DNS 记录。

**firewall**
> 管理防火墙规则。

**user**
> 用户信息。

# PARAMETERS

**--zone** _zone_
> 区域名称。

**--name** _name_
> 记录名称。

**--type** _type_
> 记录类型。

**--content** _content_
> 记录内容。

# DESCRIPTION

**Flarectl** 是用于管理 Cloudflare 服务的官方命令行界面。它提供对 Cloudflare API 的编程访问，可以自动化 DNS 管理、区域配置、防火墙规则和 CDN 设置，而无需使用网页控制台。

该工具支持常见操作，包括创建和修改 DNS 记录、管理缓存和安全功能等区域设置、配置防火墙规则和访问控制，以及获取分析数据。身份验证使用存储在环境变量或配置文件中的 API 令牌或旧版 API 密钥。

Flarectl 对基础设施即代码工作流、CI/CD 流水线以及跨多个域名的批量操作特别有用。默认情况下它以人类可读的格式输出结果，也可提供 JSON 输出以便脚本化和自动化。

# INSTALL

```apk: sudo apk add flarectl```

```brew: brew install flarectl```

```nix: nix profile install nixpkgs#flarectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cloudflared](/man/cloudflared)(1)

# RESOURCES

```[Source code](https://github.com/cloudflare/cloudflare-go)```

<!-- verified: 2026-07-15 -->
