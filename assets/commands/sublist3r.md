# TAGLINE

使用搜索引擎进行子域名枚举

# TLDR

**枚举子域名**

```sublist3r -d [example.com]```

**保存到文件**

```sublist3r -d [example.com] -o [subdomains.txt]```

**使用指定引擎**

```sublist3r -d [example.com] -e [google,bing,virustotal]```

**设置线程数**

```sublist3r -d [example.com] -t [10]```

**启用暴力枚举**

```sublist3r -d [example.com] -b```

**详细输出**

```sublist3r -d [example.com] -v```

**显示端口**

```sublist3r -d [example.com] -p [80,443]```

# SYNOPSIS

**sublist3r** [_-d domain_] [_-o file_] [_-e engines_] [_options_]

# PARAMETERS

**-d**, **--domain** _DOMAIN_
> 目标域名。

**-o**, **--output** _FILE_
> 输出文件。

**-e**, **--engines** _LIST_
> 搜索引擎。

**-b**, **--bruteforce**
> 启用暴力枚举。

**-t**, **--threads** _N_
> 线程数。

**-p**, **--ports** _PORTS_
> 扫描端口。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**sublist3r** 是一款 OSINT 侦察工具，通过查询多个搜索引擎和数据源来发现目标域名的子域名。它汇总来自 Google、Bing、Yahoo、Baidu、Ask、Netcraft、VirusTotal 等来源的结果，构建完整的子域名列表。

除了被动的搜索引擎枚举，sublist3r 还能使用常见子域名字典执行主动的 DNS 暴力枚举。它还包含端口扫描功能，用于识别哪些已发现的子域名在指定端口上运行着活跃服务，有助于在安全评估中对目标排定优先级。

该工具专为授权的渗透测试和漏洞赏金侦察而设计。多线程支持可加快枚举速度，结果可保存到文件供其他安全工具进一步处理。

# CAVEATS

仅限授权测试。可能受速率限制约束。某些引擎需要 API 密钥。

# HISTORY

**Sublist3r** 由 **Ahmed Aboul-Ela** 创建，用于子域名枚举。它被广泛用于渗透测试和漏洞赏金挖掘。

# SEE ALSO

[amass](/man/amass)(1), [subfinder](/man/subfinder)(1), [dnsrecon](/man/dnsrecon)(1)
