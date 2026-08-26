# TAGLINE

在 Tor 隐藏服务搜索引擎中检索内容

# TLDR

**搜索 onion 站点**

```onionsearch "[query]"```

**使用特定引擎搜索**

```onionsearch --engines [ahmia] "[query]"```

**使用 Tor SOCKS 代理**

```onionsearch --proxy [socks5h://127.0.0.1:9050] "[query]"```

**设置超时时间**

```onionsearch --timeout [30] "[query]"```

**限制结果数量**

```onionsearch --limit [50] "[query]"```

**输出到文件**

```onionsearch -o [results.txt] "[query]"```

# SYNOPSIS

**onionsearch** [_--engines engine_] [_--proxy url_] [_--limit n_] [_options_] _query_

# PARAMETERS

**--engines** _NAME_
> 要使用的搜索引擎（如 ahmia、torch、darksearchio）。

**--proxy** _URL_
> 用于 Tor 的 SOCKS 代理 URL（如 socks5h://127.0.0.1:9050）。

**--timeout** _SECONDS_
> 请求超时时间。

**--limit** _N_
> 最大结果数。

**-o**, **--output** _FILE_
> 输出文件。

**--len**
> 只显示结果数量。

**--list**
> 列出可用的引擎。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**onionsearch** 在 Tor 隐藏服务（.onion）搜索引擎中检索内容。它聚合来自多个暗网搜索引擎的结果。

支持多个搜索引擎，包括 Ahmia、Torch 等。结果会被收集并去重。

通过配置代理经由 Tor 进行匿名搜索。若不使用 Tor，许多引擎将无法访问。

结果包含 onion URL 和页面标题。输出格式便于后续分析处理。

# CAVEATS

完整功能需要 Tor 正在运行。搜索引擎可能不稳定。搜索结果可能包含非法内容。请仅出于安全研究目的负责任地使用。

# HISTORY

**onionsearch** 为需要检索暗网内容的安全研究人员而创建，为威胁情报收集提供 OSINT 能力。

# SEE ALSO

[tor](/man/tor)(1), [torsocks](/man/torsocks)(1), [proxychains](/man/proxychains)(1)
