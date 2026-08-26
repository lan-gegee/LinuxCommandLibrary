# TAGLINE

面向终端的技术 SEO 与 GEO 爬虫

# TLDR

**抓取**整个网站并输出报告

```crawlie crawl [https://example.com] --format pretty```

**审计**单个页面

```crawlie audit [https://example.com/pricing]```

**将 HTML 报告保存**到文件

```crawlie crawl [https://example.com] --format html -o [report.html]```

**限制**抓取的页面数量

```crawlie crawl [https://example.com] --max-pages [100]```

发现错误时让 CI 构建**失败**

```crawlie crawl [https://example.com] --fail-on error```

**解释**某个发现为何重要

```crawlie explain [geo-not-answerable]```

# SYNOPSIS

**crawlie** _subcommand_ [_url_] [_options_]

# DESCRIPTION

**crawlie** 是一款快速的开源爬虫，用于审计网站的技术 SEO 和 GEO（生成式引擎优化，Generative Engine Optimization）问题。它从 **sitemap.xml** 出发，遵守 **robots.txt**，跟随站内链接，并应用一组规则，覆盖失效链接、缺失或重复的元数据、性能提示、移动端与国际化优化，以及 AI 搜索就绪度等方面。

结果可以打印到终端，也可以导出为 JSON、CSV 或可分享的 HTML 报告。同一引擎还以 MCP 服务器（**crawlie-mcp**）的形式提供，可在智能体工作流中使用。

# SUBCOMMANDS

**crawl** _url_
> 抓取整个网站，从 sitemap 出发并跟随站内链接。

**audit** _url_
> 审计单个页面或指定的一组页面。

**explain** _finding_
> 说明某个发现为何重要以及如何修复。

**reports**
> 列出本地报告历史。

**report** _id_
> 按 ID 获取某份已保存的报告。

# PARAMETERS

**--format** _fmt_
> 输出格式：**pretty**（终端）、**json**、**csv** 或 **html**（默认：json）。

**-o**, **--output** _file_
> 将报告写入文件而不是标准输出。

**--max-pages** _n_
> 可抓取的最大页面数（默认：500）。

**--max-depth** _n_
> 距种子 URL 的最大点击深度。

**--concurrency** _n_
> 并行请求的数量（默认：16）。

**--include** _glob_
> 只抓取匹配该模式的 URL。

**--exclude** _glob_
> 跳过匹配该模式的 URL。

**--no-robots**
> 不解析也不遵守 robots.txt。

**--no-sitemap**
> 不从 sitemap.xml 开始抓取。

**--no-external**
> 跳过检查外部链接。

**--severity** _level_
> 按严重程度过滤发现项：**error**、**warning** 或 **notice**。

**--save**
> 将结果存入本地报告历史。

**--fail-on** _level_
> 当存在 **error** 或 **warning** 级别的发现项时以非零状态码退出（在 CI 中很有用）。

# HISTORY

**crawlie** 使用 Rust 编写（另有一个 TypeScript 桌面端配套程序），以 MIT 许可证发布。它于 2026 年发布，是商业 SEO 爬虫的一款免费且对智能体友好的替代品，并加入了面向 AI 搜索引擎读取站点方式的 GEO 检查。

# SEE ALSO

[wget](/man/wget)(1), [curl](/man/curl)(1), [httrack](/man/httrack)(1), [scrapy](/man/scrapy)(1)

# RESOURCES

```[Source code](https://github.com/spronta/crawlie)```

<!-- verified: 2026-06-19 -->
