# TAGLINE

子域名暴力破解扫描器

# TLDR

使用**内置字典**扫描子域名

```dnsmap [example.com]```

指定**自定义字典**

```dnsmap [example.com] -w [path/to/wordlist.txt]```

将结果保存到 **CSV 文件**

```dnsmap [example.com] -c [path/to/file.csv]```

**忽略**误报的 IP

```dnsmap [example.com] -i [123.45.67.89,98.76.54.32]```

# SYNOPSIS

**dnsmap** _domain_ [_options_]

# DESCRIPTION

**dnsmap** 是一款子域名暴力枚举工具，通过 DNS 查询发现未列入公开 DNS 记录的子域名。它的工作原理是尝试从字典中解析候选子域名，识别哪些能成功解析到 IP 地址。

该工具内置常见子域名列表（www、mail、ftp 等），也可指定自定义字典做更彻底的枚举。DNS 泛解析配置会导致所有子域名都解析到同一 IP 的误报；使用 -i 标志可以过滤掉这些已知的泛解析地址。结果可保存为 CSV 格式以便进一步分析。该工具常用于渗透测试侦察阶段，用来绘制组织的 DNS 足迹并发现潜在攻击面，例如开发服务器、预发布环境或被遗忘的子域名。

# PARAMETERS

**-w** _wordlist_
> 使用自定义字典文件

**-c** _file_
> 将结果输出到 CSV 文件

**-i** _IPs_
> 忽略的 IP 列表（逗号分隔）（误报）

**-d** _delay_
> 查询间隔（毫秒）

**-r** _file_
> 将结果保存到普通文本文件

# CAVEATS

只能用于已授权的域名。可能触发安全告警。DNS 泛解析会造成误报；可用 -i 过滤。

# INSTALL

```apt: sudo apt install dnsmap```

```dnf: sudo dnf install dnsmap```

```brew: brew install dnsmap```

```nix: nix profile install nixpkgs#dnsmap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dnsrecon](/man/dnsrecon)(1), [fierce](/man/fierce)(1), [nslookup](/man/nslookup)(1)

# RESOURCES

```[Source code](https://github.com/makefu/dnsmap)```

<!-- verified: 2026-07-11 -->
