# TAGLINE

将 PyScrappy 爬虫以智能体工具形式暴露的 MCP 服务器

# TLDR

**安装** MCP extra（Python 3.10+）

```pip install 'pyscrappy[mcp]'```

**向 Claude Code 注册**服务器

```claude mcp add pyscrappy pyscrappy-mcp```

**通过 stdio 运行**（默认，适用于本地 MCP 客户端）

```pyscrappy-mcp```

**在指定主机和端口上以 Streamable HTTP 提供服务**

```pyscrappy-mcp --http --host [127.0.0.1] --port [8000]```

**通过旧式 SSE 传输提供服务**

```pyscrappy-mcp --sse --port [8000]```

# SYNOPSIS

**pyscrappy-mcp** [**--http** | **--sse**] [**--host** _address_] [**--port** _n_]

# DESCRIPTION

**pyscrappy-mcp** 是随 PyScrappy 附带的 Model Context Protocol 服务器。它将工具集的爬虫注册为强类型的 MCP 工具，让智能体（Claude、Cursor、本地 LLM 宿主等）可以抓取结构化的页面数据并获得 Markdown 或 JSON 形式的结果。

传输方式默认为 **stdio**，适用于本地客户端。**--http** 使用 Streamable HTTP；**--sse** 使用较旧的 SSE 传输。主机和端口仅对网络传输生效（默认 **127.0.0.1** 和 **8000**）。仅当确实需要接受远程连接时才使用 **--host 0.0.0.0**。

无需 MCP 宿主时，可通过 **pyscrappy chat** 使用同一套工具，它直接与 Ollama 通信。

内置工具包括通用的 **scrape_url** 以及针对特定站点的辅助工具（Wikipedia、股票、新闻、GitHub、Hacker News、YouTube、Amazon 等）。**list_available_scrapers** 列出已注册的名称；**scrape_with** 可调度到任何已注册的爬虫，包括第三方 **pyscrappy-*** 插件。**lookup_movie** 需要在 **OMDB_API_KEY** 中提供免费的 OMDb 密钥。

成功的工具响应会在进程内缓存几分钟，以降低重复请求的延迟。TTL 由 **PYSCRAPPY_MCP_CACHE_TTL** 控制（单位秒，默认 **300**）。

该服务器需要 **pyscrappy[mcp]** extra（FastMCP）以及 Python 3.10 或更高版本。核心的 **pyscrappy** extract CLI 在 Python 3.9 上不装此 extra 也能正常工作。

# OPTIONS

**--http**

> 以 Streamable HTTP 而非 stdio 提供服务。与 **--sse** 互斥。

**--sse**

> 以旧式 SSE 传输而非 stdio 提供服务。与 **--http** 互斥。

**--host** _address_

> **--http** / **--sse** 的绑定地址（默认 **127.0.0.1**）。

**--port** _n_

> **--http** / **--sse** 的绑定端口（默认 **8000**）。

# CONFIGURATION

**OMDB_API_KEY**

> **lookup_movie** 工具（OMDb）所需的 API 密钥。未设置时该工具返回错误载荷而非影片数据。

**PYSCRAPPY_MCP_CACHE_TTL**

> 成功抓取结果的进程内缓存存活时间，单位秒。默认 **300**。非数值会回退为默认值。

Claude Desktop 不会继承登录 shell 的 **PATH**。如果应用找不到 **pyscrappy-mcp**，请把 **which pyscrappy-mcp** 输出的绝对路径写入 **claude_desktop_config.json**。

# CAVEATS

此进程应由 MCP 宿主启动。在 stdio 模式下它通过 stdin/stdout 讲协议；不要向其管道传入其他命令。

JavaScript 密集的页面在静态抓取时常返回空结果。此时 **scrape_url** 工具会提示用 **render_js=true** 重试，而这需要 **pyscrappy[browser]**。部分零售和社交网站会阻止自动化客户端，除非在库中配置代理或抓取 API。

缓存是进程级的，服务器退出即消失。

# SEE ALSO

[pyscrappy](/man/pyscrappy)(1), [claude](/man/claude)(1), [scrapy](/man/scrapy)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/mldsveda/PyScrappy)```

```[Documentation](https://pyscrappy.vercel.app)```

<!-- verified: 2026-08-16 -->
