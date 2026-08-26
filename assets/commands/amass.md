# TAGLINE

攻击面测绘与资产发现

# TLDR

**被动枚举**子域名

```amass enum -passive -d [example.com]```

结合 DNS 解析和暴力破解的**主动**枚举

```amass enum -active -brute -d [example.com]```

使用**输出文件**进行枚举

```amass enum -d [example.com] -o [output.txt]```

从数据库获取发现的**子域名名称**

```amass subs -names -d [example.com]```

查找已发现资产之间的**关联**

```amass assoc -d [example.com]```

# SYNOPSIS

**amass** _command_ [_options_]

# DESCRIPTION

**amass** 是一个 OWASP 项目，用于深度攻击面测绘和资产发现。它执行 DNS 枚举和子域名暴力破解，并利用众多数据源，包括搜索引擎、证书透明度日志和各种 API。

该工具会构建组织外部网络足迹的完整地图，识别子域名、关联域名和网络区块。收集到的数据存储在图数据库中；**enum** 负责填充数据库，而 **subs**、**assoc** 和 **viz** 则从中呈现结果。

自 5.0 版本起，引擎与数据收集相互分离：**enum** 驱动采集引擎，分析类子命令则事后查询已存储的图数据库。

# PARAMETERS

**enum**
> 与采集引擎交互，执行资产发现和网络映射。

**subs**
> 分析并呈现图数据库中发现的子域名。

**assoc**
> 查找已发现资产之间的关联。

**track**
> 识别随时间新发现的资产。

**viz**
> 为收集到的数据生成图形可视化。

**-d** _domain_
> 目标域名（逗号分隔）。

**-passive**
> 仅使用被动数据源（不做 DNS 解析）。

**-active**
> 使用主动方法，如区域传送和证书抓取。

**-brute**
> 在搜索之后执行子域名暴力破解。

**-ip**
> 显示发现名称的 IP 地址。

**-names**
> 配合 **subs** 时，仅打印发现的名称。

**-o** _file_
> 输出文件路径。

**-dir** _path_
> 存放输出和图数据库的目录。

**-config** _file_
> YAML 配置文件。

**-timeout** _minutes_
> 运行多少分钟后退出。

# CONFIGURATION

**~/.config/amass/config.yaml**
> 主配置文件，用于数据源、API 密钥和枚举设置（v4 起为 YAML 格式）。

# CAVEATS

主动枚举会产生大量 DNS 流量，且可能被发现。许多数据源需要 API 密钥才能完整访问。结果因所配置的数据源而异。自 v5 起，结果会写入图数据库；请使用 **subs** 获取名称，而不是只依赖 **enum -o**。

# HISTORY

**amass** 由 Jeff Foley 创建，后来成为 OWASP 官方项目。它凭借在侦察和漏洞赏金挖掘领域的表现，在安全社区中得到广泛采用。

# INSTALL

```aur: yay -S amass```

```brew: brew install amass```

```nix: nix profile install nixpkgs#amass```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[subfinder](/man/subfinder)(1), [dnsenum](/man/dnsenum)(1), [nmap](/man/nmap)(1)

# RESOURCES

```[Source code](https://github.com/owasp-amass/amass)```

```[Homepage](https://owasp.org/www-project-amass/)```

```[Documentation](https://owasp-amass.github.io/docs)```

<!-- verified: 2026-06-11 -->
