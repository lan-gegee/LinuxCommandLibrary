# TAGLINE

将 URL 抓取为 Markdown、JSON、文本或 HTML

# TLDR

**从 PyPI 安装** CLI

```pip install pyscrappy```

**抓取**页面并输出干净的 Markdown

```pyscrappy extract [https://example.com] [out.md]```

**改为写入**结构化 JSON

```pyscrappy extract [https://example.com] [out.json]```

**只提取**匹配 CSS 选择器的元素

```pyscrappy extract [https://example.com] [items.txt] --css-selector [.product]```

**先渲染** JavaScript（需要 **pyscrappy[browser]**）

```pyscrappy extract [https://example.com] [page.md] --render-js```

**询问**可调用内置爬虫的本地 Ollama 模型（需要 **pyscrappy[mcp]**）

```pyscrappy chat --model [qwen2.5] "[what's the current AAPL quote?]"```

# SYNOPSIS

**pyscrappy** **extract** _url_ _output_ [**--css-selector** _selector_] [**--render-js**]

**pyscrappy** **chat** _prompt_ [**--model** _name_] [**--host** _url_] [**--max-steps** _n_] [**-v**] [**--json**]

# DESCRIPTION

**pyscrappy** 是 PyScrappy——一个 Python 网页抓取工具包——的命令行界面。它可以抓取页面并把结果写入文件，或者（配合可选的 MCP extra）让本地的工具调用模型调用相同的爬虫。

**extract** 根据目标文件的扩展名推断输出格式：

- **.md** — 来自 **ScrapeResult.to_markdown** 的 Markdown
- **.json** — 来自 **ScrapeResult.to_json** 的结构化 JSON
- **.txt** — 提取的页面文本（设置 **--css-selector** 时仅为匹配的 CSS 文本）
- **.html** — 原始抓取到的 HTML（并非结构化的抓取结果）

默认抓取是静态 HTTP 请求。**--render-js** 改用无头浏览器渲染，需要先执行 **pip install 'pyscrappy[browser]'** 和 **playwright install chromium**。

**chat** 与兼容 Ollama 的 **/api/chat** 端点通信（默认 **http://localhost:11434**），暴露与 **pyscrappy-mcp** 相同的爬虫工具。它需要 Python 3.10+、**pip install 'pyscrappy[mcp]'** 以及支持工具调用的模型。循环轮次上限为 **8**，除非设置了 **--max-steps**。

该软件包还以 Python 库的形式提供站点专用爬虫（Wikipedia、股票、新闻、GitHub 等）和可选的自适应选择器。这些 API 不属于本 CLI。

# COMMANDS

**extract** _url_ _output_

> 抓取 _url_ 并写入 _output_。格式由文件扩展名决定（**.md**、**.json**、**.txt**、**.html**）。

**chat** _prompt_

> 向本地模型提问，模型通过调用 PyScrappy 爬虫来回答。

# OPTIONS

**--css-selector** _selector_

> 配合 **extract**：只保留匹配此 CSS 选择器的元素。对 **.txt** 输出，写入匹配的文本，每行一条。

**--render-js**

> 配合 **extract**：提取前先用无头浏览器渲染页面。

**--model** _name_

> 配合 **chat**：使用的 Ollama 模型（默认 **qwen2.5**）。

**--host** _url_

> 配合 **chat**：Ollama 基础 URL（默认 **http://localhost:11434**）。

**--max-steps** _n_

> 配合 **chat**：工具调用最大轮数（默认 **8**）。

**-v**, **--verbose**

> 配合 **chat**：把每次工具调用打印到 stderr。

**--json**

> 配合 **chat**：以 JSON 打印最近一次原始爬虫结果，而非模型的文字回答。

# CAVEATS

**extract** 只做单 URL 抓取。站点专用爬虫、并发辅助、代理和 TLS 模拟都在 Python API 中，不在这个 CLI 上。

JavaScript 密集的页面在不使用 **--render-js** 时往往只返回近乎空壳的结果。有些网站会阻止自动化客户端；库支持经代理或抓取 API 路由，但这些选项没有暴露给 **extract**。

缺少 MCP extra 时 **chat** 会报出明确的错误。它要求正在运行的 Ollama（或兼容）服务器和支持工具调用的模型；工具*选择*的质量取决于模型本身。

# SEE ALSO

[pyscrappy-mcp](/man/pyscrappy-mcp)(1), [scrapy](/man/scrapy)(1), [rdrview](/man/rdrview)(1), [htmlq](/man/htmlq)(1), [curl](/man/curl)(1), [httpie](/man/httpie)(1)

# RESOURCES

```[Source code](https://github.com/mldsveda/PyScrappy)```

```[Documentation](https://pyscrappy.vercel.app)```

<!-- verified: 2026-08-16 -->
