# TAGLINE

用于批量查询的高性能 DNS 存根解析器

# TLDR

**从文件解析域名**

```massdns -r [resolvers.txt] -t A [domains.txt]```

**输出到文件**

```massdns -r [resolvers.txt] -t A -o S [domains.txt] > [results.txt]```

**并发查询**

```massdns -r [resolvers.txt] -s [10000] [domains.txt]```

**查询特定记录类型**

```massdns -r [resolvers.txt] -t [MX] [domains.txt]```

**简单输出格式**

```massdns -r [resolvers.txt] -t A -o S [domains.txt]```

# SYNOPSIS

**massdns** [_options_] _domainlist_

# DESCRIPTION

**massdns** 是一个面向批量查询的高性能 DNS 存根解析器。它并行使用多个解析器，每小时可解析数百万个域名。

该工具专为授权安全评估中的子域名枚举和 DNS 侦察设计。它会自动处理解析器轮换和错误恢复。

# PARAMETERS

**-r** _file_
> 解析器列表文件。

**-t** _type_
> 查询类型（A、AAAA、MX、NS 等）。

**-o** _format_
> 输出格式（S=简单，F=完整，J=JSON）。

**-s** _rate_
> 每秒查询数。

**-w** _file_
> 将输出写入文件。

**-c** _num_
> 并发查询数。

**--root**
> 允许绑定特权端口。

**-q**
> 安静模式。

# CAVEATS

需要高质量的解析器列表。高查询速率可能触发速率限制。各解析器可靠性不一。仅限授权测试使用。

# HISTORY

**massdns** 由 **B. Blechschmidt** 为安全研究中的高速 DNS 解析需求而创建。它填补了单次查询工具与高效解析数百万域名需求之间的空白。

# INSTALL

```dnf: sudo dnf install massdns```

```brew: brew install massdns```

```nix: nix profile install nixpkgs#massdns```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [host](/man/host)(1), [subfinder](/man/subfinder)(1), [dnsx](/man/dnsx)(1)
