# TAGLINE

执行 DNS 枚举和子域名发现

# TLDR

**被动**子域名枚举

```amass enum -passive -d [example.com]```

结合暴力破解的**主动**枚举

```amass enum -active -brute -d [example.com]```

使用**配置文件**进行枚举

```amass enum -config [config.ini] -d [example.com]```

显示发现名称的**来源**

```amass enum -d [example.com] -src```

输出包含 **IP 地址**

```amass enum -d [example.com] -ip -o [results.txt]```

# SYNOPSIS

**amass enum** [_-d domain_] [_-passive_] [_-active_] [_-brute_] [_options_]

# DESCRIPTION

**amass enum** 执行 DNS 枚举和网络映射。它使用多种被动和主动技术发现子域名，包括查询数据源、证书透明度日志、DNS 暴力破解和区域传送。

这是子域名发现的主要命令，为不同的信息收集需求提供了丰富的配置选项。

# PARAMETERS

**-d** _domain_
> 目标域名（可重复使用以指定多个域名）

**-passive**
> 仅使用被动数据源（不直接查询目标）

**-active**
> 执行主动 DNS 解析

**-brute**
> 启用子域名暴力破解

**-w** _file_
> 用于暴力破解的字典文件

**-src**
> 显示每个名称由哪个来源发现

**-ip**
> 在输出中包含 IP 地址

**-ipv4**
> 仅显示 IPv4 地址

**-ipv6**
> 仅显示 IPv6 地址

**-o** _file_
> 保存发现名称的输出文件

**-json** _file_
> 以 JSON 格式输出

**-config** _file_
> 包含 API 密钥和设置的配置文件

**-timeout** _minutes_
> 枚举的超时时间

# CONFIGURATION

**~/.config/amass/config.ini**
> Amass 配置文件，定义数据源、API 密钥、解析器和范围设置。

# CAVEATS

主动模式产生的 DNS 流量可能触发告警。暴力破解可能耗时较长。许多数据源需要在配置文件中设置 API 密钥。

# HISTORY

自 amass 首次发布以来，**amass enum** 就一直是其核心功能。它已扩展到包含数十个数据源和多种枚举技术。

# INSTALL

```aur: yay -S amass```

```brew: brew install amass```

```nix: nix profile install nixpkgs#amass```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[amass](/man/amass)(1), [amass-intel](/man/amass-intel)(1), [amass-track](/man/amass-track)(1), [subfinder](/man/subfinder)(1)

# RESOURCES

```[Source code](https://github.com/owasp-amass/amass)```

```[Documentation](https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md)```

<!-- verified: 2026-06-11 -->
