# TAGLINE

原生 Rust 网页抓取器，兼作 Firecrawl 兼容的自托管 API

# TLDR

**抓取一个页面**并在标准输出输出干净的 Markdown

```draco scrape [https://example.com]```

**以完整 JSON 信封抓取**（markdown、元数据、trace）

```draco scrape [https://example.com] --json --pretty```

通过分级升级**提取 SPA 的 JSON 数据**

```draco scrape [https://app.example.com] --format json --pretty```

通过多引擎共识**搜索网络**

```draco search "[rust web scraper]" --limit [10]```

**运行 Firecrawl 兼容的 HTTP 守护进程**

```draco serve```

**通过 MCP（stdio）暴露抓取工具**

```draco mcp```

# SYNOPSIS

**draco** **scrape** _url_ [_options_]

**draco** **search** _query_ [_options_]

**draco** **serve** [_options_]

**draco** **interact** _url_ [_options_]

**draco** **mcp**

# DESCRIPTION

**draco** 是一款用原生 Rust 编写的高速网页抓取器，定位为 Firecrawl 和 Browserbase 的更轻量、可自托管的替代品。它以贴近真实浏览器的 TLS/JA4 指纹获取页面，将正文提取为干净的 Markdown（并附带元数据），还能通过进程内 V8 isolate 升级处理客户端渲染的 SPA——无需部署无头 Chrome 集群或 Node 运行时。

对于普通 HTML，一次抓取通常只是一次带指纹的请求加解析。输出包括 Markdown（标题、绝对化链接、列表、代码块、GFM 表格；导航/页脚/广告已被剔除）、元数据（标题、描述、语言、canonical、favicon、Open Graph / Twitter / 文章标签、状态），以及可选的 **trace** / **timing** 步骤。scrape 的默认退出码：**0** 成功，**1** 错误，**2** 不支持，**3** needs_browser（例如 Cloudflare 这类真正的 JS 挑战墙）。

除一次性抓取外，Draco 还提供 **search**（并行多引擎 SERP 抓取并按倒数排名共识合并）、**serve**（常驻 HTTP 守护进程，默认在端口 **3002** 提供 Firecrawl 兼容的 REST API，包括 scrape、map、crawl、batch scrape、discover、search 和 interact）、**interact**（带 cookie 持久化和 JS **exec** 的有状态页面会话），以及 **mcp**（通过 stdio 或守护进程的 **POST /mcp** 提供模型上下文协议工具）。

JSON 提取会逐级升级：先读取静态内嵌状态（**__NEXT_DATA__**、JSON-LD、Nuxt），再重放 Next.js build-id 请求，最后在沙箱化 V8 isolate 中拦截运行时 fetch/XHR——该环境不绑定任何宿主能力。默认行为遵守 **robots.txt** 和速率限制；本工具仅用于公开数据以及你有权抓取的资产。

# SUBCOMMANDS

**scrape** _url_
> 获取 URL 并输出 Markdown（默认）或其他格式。CLI 的主要入口。

**search** _query_
> 基于 Draco 隐蔽 HTTP 栈的多引擎网络搜索；可选对每条结果进行抓取。

**serve**
> 运行常驻的 Firecrawl 兼容 HTTP API（默认 **http://127.0.0.1:3002**）。

**interact** _url_
> 针对页面打开一次性或 REPL 会话：执行 JS、导航、抓取实时 DOM。

**mcp**
> 通过 stdio 为智能体客户端（Claude Desktop、编辑器、编排器）提供 MCP。

# PARAMETERS

**--format** _fmt_
> scrape 的输出格式：**markdown**（默认）、**html**、**raw-html**、**links**、**json**、**endpoints** 或 **both**（markdown+json）。在支持的地方可重复使用。

**--json**
> 以 JSON 输出完整结果信封（markdown + 元数据 + trace）。

**--pretty**
> 对 JSON 输出进行美化打印。

**--extract** _JSONPATH_
> 从提取到的 JSON 中选取路径（配合 **--format json** 使用）。

**--proxy** _url_
> 通过代理路由流量（例如 **socks5://127.0.0.1:9050**）。

**--delay** _ms_
> 请求之间的礼貌性延迟。

**--timeout** _ms_
> 单次请求超时。

**--tier-max** _n_
> 限制升级层级上限（**0**/**1**/**2**）。**2** 启用 V8 运行时拦截和 SPA 渲染后转 Markdown（tier2 构建时的默认值）。

**--no-main-content**
> 禁用主内容提取启发式算法。

**--wait-for** _ms_
> 与运行时捕获 / hydration 相关的等待窗口。

**--capture-window-ms** _ms_
> 限制 Tier-2 捕获窗口的时长。

**--ignore-robots**
> 不遵守 robots.txt（仅在获得许可时使用）。

**--allow-unsafe-replay**
> 在运行时模式下允许重放改变状态的请求（否则这些请求会被存根化）。

**--runtime-log**
> 打印 isolate 诊断信息（异常、控制台错误、受代理的 fetch、捕获结束原因）。

**--limit** _n_
> 用于 **search**：结果数量上限（通常默认 5，且有范围上限）。

**--host**, **--port**, **--max-concurrency**
> 用于 **serve**：绑定地址、端口和并发抓取配额。

**--exec** _js_
> 用于 **interact**：对页面执行一次性 JavaScript 表达式/代码体。

# CAVEATS

Draco **不能**攻破 JavaScript 挑战墙（Cloudflare、DataDome 及类似服务）。真正的插页式挑战会直接短路为退出码 **3** / **needs_browser**。CDN 背后的正常 HTTP 200 不被视为挑战。

Tier-2 隔离依赖一个**不绑定宿主能力**的进程内 V8 上下文（页面 JS 无法访问文件系统或任意网络，除非经由引擎代理的 fetch）。它并非完整的 OS 监狱；旧的 **--no-jail** / **--strict-sandbox** 标志仍被接受但已失效。你仍需自行遵守目标网站的服务条款和适用法律。

完整支持的平台包括 Linux **x86_64-gnu** 和 macOS **aarch64-darwin**。不含默认特性的精简构建会省略 V8 和 serve 守护进程。

# HISTORY

**draco** 用 Rust 编写，是单二进制、可自托管的 Firecrawl 替代品，具备原生 Markdown 提取能力和可选的进程内 V8（用于 SPA hydration 与 API 发现）。它采用 **MIT OR Apache-2.0** 双许可。早期版本使用的 OS 进程监狱已在 **v0.14** 中退役，改为仅用 isolate 进行隔离以提升吞吐。

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1), [crawlie](/man/crawlie)(1), [trafilatura](/man/trafilatura)(1), [shot-scraper](/man/shot-scraper)(1)

# RESOURCES

```[Source code](https://github.com/0xchasercat/draco)```

<!-- verified: 2026-08-03 -->
