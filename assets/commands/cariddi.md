# TAGLINE

爬取 URL 以发现端点、机密和敏感数据

# TLDR

**从列表中爬取域名**

```cat [domains.txt] | cariddi```

**搜寻机密信息**

```cat [domains.txt] | cariddi -s```

**搜寻端点**

```cat [domains.txt] | cariddi -e```

**密集爬取子域名**

```cat [urls.txt] | cariddi -intensive```

**搜寻文件扩展名**

```cat [domains.txt] | cariddi -ext [3]```

**使用代理**

```cat [domains.txt] | cariddi -proxy [http://127.0.0.1:8080]```

**随机 User Agent**

```cat [domains.txt] | cariddi -rua```

# SYNOPSIS

**cariddi** [_options_]

# DESCRIPTION

**cariddi** 是一款侦察工具，可爬取 URL 并扫描端点、机密、API 密钥、文件扩展名和令牌。它通过标准输入接收域名列表，便于在自动化安全评估流水线中与子域名发现工具串联使用。

该工具对爬取到的页面进行被动分析，通过模式匹配提取硬编码凭据、身份验证令牌和 API 密钥等敏感数据。它支持可配置的爬取深度、并发数和代理设置，既能深入扫描又可控。

cariddi 面向漏洞赏金挖掘和授权渗透测试设计，结果可以纯文本或 JSON 格式输出，便于与其他安全工具集成。

# PARAMETERS

**-s**
> 搜寻机密信息

**-e**
> 搜寻端点

**-info**
> 搜寻有用信息

**-ext** _level_
> 搜寻文件扩展名（1=最有价值 到 7=价值较低）

**-intensive**
> 爬取子域名（*.target.com）

**-proxy** _url_
> HTTP 或 SOCKS5 代理

**-rua**
> 每个请求使用随机的浏览器 User Agent

**-d** _depth_
> 爬取深度限制

**-c** _n_
> 并发请求数

**-t** _seconds_
> 请求超时时间

**-o** _file_
> 输出文件

**-json**
> JSON 输出格式

**-plain**
> 纯文本输出

# DETECTION TARGETS

- API 密钥与机密
- 身份验证令牌
- 敏感文件扩展名
- 隐藏端点
- 信息泄露

# CAVEATS

仅用于授权的安全测试。与子域名发现工具配合良好。采用 GPL-3.0 许可证。

# INSTALL

```brew: brew install cariddi```

```nix: nix profile install nixpkgs#cariddi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[subfinder](/man/subfinder)(1), [httpx](/man/httpx)(1), [nuclei](/man/nuclei)(1)

# RESOURCES

```[Source code](https://github.com/edoardottt/cariddi)```

<!-- verified: 2026-06-22 -->
