# TAGLINE

发现子域名及相关域名

# TLDR

**查找**子域名和相关资产

```assetfinder [example.com]```

仅查找**子域名**

```assetfinder --subs-only [example.com]```

# SYNOPSIS

**assetfinder** [_--subs-only_] _domain_

# DESCRIPTION

**assetfinder** 用于发现与目标组织相关的域名和子域名。它查询多种数据源，包括证书透明度日志、DNS 数据库和网络存档，以找出关联资产。

该工具适用于安全评估中的信息收集，以及发现组织的外部攻击面。

# PARAMETERS

**--subs-only**
> 仅显示子域名

**domain**
> 要调查的目标域名

# CONFIGURATION

部分数据源需要 API 凭据，通过环境变量提供：

**FB_APP_ID**, **FB_APP_SECRET**
> Facebook 证书透明度数据源所用的应用凭据。

**VT_API_KEY**
> VirusTotal 的 API 密钥。

**SPYSE_API_TOKEN**
> Spyse（findsubdomains）的 API 令牌。

# CAVEATS

仅进行被动侦察，不会向目标产生流量。结果依赖于公开数据源，可能包含陈旧或已失效的域名。

# HISTORY

**assetfinder** 由 Tom Hudson（tomnomnom）创建，是一款面向安全侦察的快速、简洁的子域名发现工具。

# INSTALL

```apt: sudo apt install assetfinder```

```aur: yay -S assetfinder```

```nix: nix profile install nixpkgs#assetfinder```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[amass](/man/amass)(1), [subfinder](/man/subfinder)(1), [findomain](/man/findomain)(1)

# RESOURCES

```[Source code](https://github.com/tomnomnom/assetfinder)```

<!-- verified: 2026-06-17 -->
