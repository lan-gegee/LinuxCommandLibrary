# TAGLINE

被动子域名发现工具

# TLDR

**查找子域名**

```subfinder -d [example.com]```

**输出到文件**

```subfinder -d [example.com] -o [subdomains.txt]```

**使用所有数据源**

```subfinder -d [example.com] -all```

**仅显示活跃主机**

```subfinder -d [example.com] -active```

**静默模式**（仅输出子域名）

```subfinder -d [example.com] -silent```

**多个域名**

```subfinder -dL [domains.txt]```

# SYNOPSIS

**subfinder** [_options_]

# DESCRIPTION

**subfinder** 是一个子域名发现工具，使用被动数据源查找目标域名的子域名。它查询证书透明度日志、DNS 数据集和各种 API。

该工具专为授权的安全评估和漏洞赏金挖掘而设计。

# PARAMETERS

**-d** _domain_
> 目标域名。

**-dL** _file_
> 域名列表文件。

**-o** _file_
> 输出文件。

**-oJ**
> JSON 输出。

**-all**
> 使用所有数据源。

**-active**
> 验证子域名是否活跃。

**-silent**
> 仅输出子域名。

**-v**
> 详细输出。

**-t** _n_
> 线程数。

**-timeout** _n_
> 超时时间（秒）。

**-rl** _n_
> 速率限制。

# CONFIGURATION

**~/.config/subfinder/provider-config.yaml**
> Shodan、Censys、SecurityTrails、VirusTotal 等数据源的 API 密钥和凭据。

# CAVEATS

API 密钥能改善结果。受速率限制约束。仅限授权测试。结果取决于可用数据。

# HISTORY

**subfinder** 由 **projectdiscovery** 创建，是一款快速的子域名枚举工具。它是其安全工具包的一部分，在漏洞赏金社区中被广泛使用。

# INSTALL

```dnf: sudo dnf install subfinder```

```zypper: sudo zypper install subfinder```

```brew: brew install subfinder```

```nix: nix profile install nixpkgs#subfinder```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[amass](/man/amass)(1), [findomain](/man/findomain)(1), [assetfinder](/man/assetfinder)(1), [dnsx](/man/dnsx)(1)
