# TAGLINE

基于 RSS 和 Hacker News 源构建排版好的每日新闻 PDF

# TLDR

**在本地运行完整流水线**

```python -m papernews build```

**抓取**新文章

```python -m papernews gather```

**用 Claude 概括**已抓取的文章

```python -m papernews summarize```

**为 PDF 版面重写**文章正文

```python -m papernews rewrite```

**将当前一期渲染**为 PDF

```python -m papernews render```

**启动**Web 服务器和调度器

```python -m papernews web```

# SYNOPSIS

**papernews** _subcommand_

# PARAMETERS

**gather**
> 从已配置的来源拉取新条目并提取文章正文

**summarize**
> 为已抓取的文章生成简短导语

**rewrite**
> 生成干净且经过翻译的文章正文供渲染使用

**render**
> 用存储的文章构建 LaTeX PDF

**build**
> 依次运行 gather、summarize、rewrite 和 render

**web**
> 启动 HTTP 服务，提供后台采集和 PDF 分发

# DESCRIPTION

**papernews** 是一个自托管工具，能把 RSS 源和 Hacker News 帖子变成一份排版统一的 PDF。它抓取 **sources.toml** 中列出的来源、提取文章正文、用 Claude 对其进行概括和重写，然后用 **xelatex** 渲染结果。

输出适合在 reMarkable 等电子墨水设备上安静地离线阅读，不过任何 PDF 阅读器都能打开。典型的一期包含封面页、目录、国际新闻摘要，以及采用双栏 Latin Modern 排版的完整文章正文。

在服务器模式下，**papernews** 提供 **/** 作为落地页，并通过 **/digest.pdf** 返回当前缓存的一期。后台调度器按固定间隔或 cron 计划重新执行采集。状态保存在本地的 SQLite 中，因此内容在重启后依然可用。

已配置的来源可以是 Hacker News 排行榜，也可以是任意 Atom/RSS 源。非英文文章可以在重写步骤中被翻译成英文。

# CONFIGURATION

**sources.toml**
> 定义源的顺序、来源类型（**hn** 或 **rss**）、数量限制以及 HN 过滤阈值

**papernews/template.tex.j2**
> 控制页面尺寸、字体、封面版式和文章格式

**.env**
> 存放 **ANTHROPIC_API_KEY** 以及采集调度变量，如 **INGEST_INTERVAL_SECONDS** 或 **INGEST_SCHEDULE**

# CAVEATS

概括和重写步骤会调用 Anthropic API，因此文章文本会被送出本机处理。抓取和渲染则完全在本地完成。

渲染需要 **xelatex** 及相关 TeX 软件包。首次生成 PDF 可能需要一到两分钟，此后有了缓存，后续请求就会很快。

这是一个业余项目；配置方式和输出质量可能随版本变化。

# SEE ALSO

[curl](/man/curl)(1), [docker](/man/docker)(1)
