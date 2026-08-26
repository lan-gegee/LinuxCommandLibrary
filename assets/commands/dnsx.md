# TAGLINE

快速的多用途 DNS 工具包

# TLDR

**解析域名的 A 记录**

```cat [domains.txt] | dnsx -a```

**解析多种**记录类型

```cat [domains.txt] | dnsx -a -aaaa -mx -ns```

使用自定义解析器**解析**

```cat [domains.txt] | dnsx -r [8.8.8.8]```

以 **JSON 格式**输出

```cat [domains.txt] | dnsx -json```

**暴破子域名**

```dnsx -d [domain.com] -w [wordlist.txt]```

**反向 DNS** 查询

```cat [ips.txt] | dnsx -ptr```

对请求进行**速率限制**

```cat [domains.txt] | dnsx -rate-limit [100]```

# SYNOPSIS

**dnsx** [_options_]

# PARAMETERS

**-a**
> 查询 A 记录。

**-aaaa**
> 查询 AAAA 记录。

**-mx**
> 查询 MX 记录。

**-ns**
> 查询 NS 记录。

**-ptr**
> 查询 PTR 记录。

**-cname**
> 查询 CNAME 记录。

**-d** _DOMAIN_
> 用于子域名暴破的目标域名。

**-w** _FILE_
> 用于暴破的字典文件。

**-r** _RESOLVER_
> 自定义 DNS 解析器。

**-json**
> 以 JSON 格式输出。

**-rate-limit** _N_
> 每秒最大查询数。

**-help**
> 显示帮助信息。

# DESCRIPTION

**dnsx** 是一款面向安全侦察的快速多用途 DNS 工具包。它能高效执行 DNS 查询，支持多种记录类型、自定义解析器以及高性能并行执行。

该工具擅长批量 DNS 操作，包括解析、反向查询和子域名暴破。它接受来自 stdin 的输入，因此很容易集成到与其他工具配合的侦察流水线中。

dnsx 支持泛解析过滤、重试以及多种输出格式。其对性能的关注使它适合大规模 DNS 枚举任务。

# CAVEATS

过高的查询速率可能触发速率限制或封锁。仅可对已授权的目标执行。大型字典耗时较长且可能被检测到。DNS 应答可能被缓存或篡改。

# HISTORY

dnsx 由 **ProjectDiscovery** 开发，该公司也是 nuclei、httpx 等安全工具的开发者。它作为其开源安全工具包的一部分发布，旨在为侦察工作流提供快速可靠的 DNS 操作。

# INSTALL

```dnf: sudo dnf install dnsx```

```brew: brew install dnsx```

```nix: nix profile install nixpkgs#dnsx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [massdns](/man/massdns)(1)
