# TAGLINE

为 AI 和自动化设计的无头浏览器

# TLDR

**抓取 URL**并将渲染后的 HTML 输出到 stdout

```lightpanda fetch --dump html [url]```

**抓取 URL**并以 **markdown** 格式输出

```lightpanda fetch --dump markdown [url]```

在默认主机和端口上**启动 CDP 服务器**

```lightpanda serve```

在指定主机和端口上**启动 CDP 服务器**

```lightpanda serve --host [127.0.0.1] --port [9222]```

**抓取 URL**时遵守 robots.txt

```lightpanda fetch --obey_robots --dump html [url]```

通过 HTTP 代理**抓取 URL**

```lightpanda fetch --http_proxy [proxy_host:port] --dump html [url]```

# SYNOPSIS

**lightpanda** _command_ [_options_] [_url_]

# PARAMETERS

**fetch**
> 抓取一个 URL，执行 JavaScript，并将渲染后的页面内容输出到 stdout。

**serve**
> 启动一个 Chrome DevTools Protocol（CDP）服务器，供 Playwright、Puppeteer 或原生 CDP 客户端进行远程自动化。

**help**
> 显示可用命令和选项。

**--dump** _html_|_markdown_
> 抓取页面的输出格式。用 **html** 表示渲染后的 HTML，用 **markdown** 表示 Markdown 转换。（仅限 fetch）

**--with_base**
> 在输出的内容中添加 **\<base\>** 标签。（仅限 fetch）

**--host** _address_
> CDP 服务器的主机地址。默认 **127.0.0.1**。（仅限 serve）

**--port** _port_
> CDP 服务器的端口。默认 **9222**。（仅限 serve）

**--timeout** _seconds_
> 断开客户端前的无活动超时时间（秒）。默认 **10**。（仅限 serve）

**--obey_robots**
> 抓取并遵守目标网页的 robots.txt。

**--http_proxy** _host:port_
> 所有请求使用的 HTTP 代理。支持可选的 **username:password** 进行基本认证。

**--http_timeout** _milliseconds_
> 传输允许完成的最长时间（毫秒）。**0** 表示不设超时。默认 **10000**。

**--log_level** _level_
> 设置日志详细程度。默认 **info**。用 **debug** 可获得详细输出。

**--log_format** _format_
> 设置日志输出格式。用 **pretty** 可获得人类可读的输出。

# DESCRIPTION

**Lightpanda** 是一个用 **Zig** 从零构建并采用 **V8** JavaScript 引擎的开源无头浏览器，专为 AI 智能体、网页爬取、LLM 训练和测试自动化而设计。与传统浏览器的无头模式不同，Lightpanda 完全跳过图形渲染，只专注于 DOM 构建和 JavaScript 执行。

它暴露一个 **Chrome DevTools Protocol**（CDP）端点，与 **Playwright**、**Puppeteer** 和 **chromedp** 等现有自动化工具兼容，可作为无头 Chrome 的直接替代品。**fetch** 命令检索单个 URL 并输出渲染后的页面，而 **serve** 则启动一个持久的 CDP 服务器用于远程浏览器控制。

与无头 Chrome 相比，Lightpanda 的**内存占用减少 9 倍**，**执行速度快 11 倍**，特别适合高并发量的爬取和自动化工作负载。

# CAVEATS

Lightpanda 处于 **beta** 阶段，尚未实现完整的 Web 平台。依赖高级 CSS 布局、canvas、WebGL 或某些较新 Web API 的复杂 Web 应用可能无法正常工作。Windows 不受原生支持；请改用 WSL。作为非 Chromium 浏览器，某些带有浏览器指纹检测的网站行为可能不同。

# HISTORY

Lightpanda 由 **Francis** 和 **Pierre** 创建，他们此前曾使用无头 Chrome 进行大规模网页爬取，发现其资源消耗对于高并发工作负载而言过于沉重。他们花了两年多时间用 **Zig** 从零构建一个无头浏览器，选择该语言是因为其底层控制能力和性能特性。该项目于 **2025 年初在 Hacker News 上**公开发布，并以 **AGPL-3.0** 许可证开源发布。

# INSTALL

```aur: yay -S lightpanda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chromium](/man/chromium)(1), [curl](/man/curl)(1), [wget](/man/wget)(1), [puppeteer](/man/puppeteer)(1)
