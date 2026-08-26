# TAGLINE

Python 网页抓取与爬虫框架

# TLDR

**创建新项目**

```scrapy startproject [project_name]```

**生成爬虫**

```scrapy genspider [spider_name] [domain.com]```

**运行爬虫**

```scrapy crawl [spider_name]```

**运行爬虫并保存到文件**

```scrapy crawl [spider_name] -o [output.json]```

**用于测试的交互式 shell**

```scrapy shell "[https://example.com]"```

**检查爬虫契约（contract）**

```scrapy check [spider_name]```

**列出可用的爬虫**

```scrapy list```

**抓取 URL 并显示响应**

```scrapy fetch [https://example.com]```

# SYNOPSIS

**scrapy** _command_ [_-o output_] [_-s setting=value_] [_options_] [_arguments_]

# PARAMETERS

**startproject** _NAME_
> 创建新的 Scrapy 项目。

**genspider** _NAME_ _DOMAIN_
> 从模板生成爬虫。

**crawl** _SPIDER_
> 运行一个爬虫。

**shell** [_URL_]
> 用于测试的交互式 shell。

**list**
> 列出可用的爬虫。

**check** [_SPIDER_]
> 运行契约检查。

**fetch** _URL_
> 抓取 URL 并打印。

**view** _URL_
> 在浏览器中打开 URL。

**parse** _URL_
> 用爬虫解析 URL。

**runspider** _FILE_
> 从文件运行爬虫。

**-o** _FILE_, **--output** _FILE_
> 将抓取到的条目追加到文件。格式根据扩展名推断（json、jsonl、csv、xml）。

**-O** _FILE_, **--overwrite-output** _FILE_
> 与 **-o** 相同，但会覆盖已存在的文件。

**-s** _NAME=VALUE_, **--set** _NAME=VALUE_
> 覆盖某项设置（例如 **-s LOG_LEVEL=INFO**）。

**-a** _NAME=VALUE_
> 向爬虫传递参数（通过 **self.<NAME>** 读取）。

**-t** _FORMAT_, **--output-format** _FORMAT_
> 当文件名不能表明格式时显式设置输出格式。

**--nolog**
> 完全禁用日志。

**--loglevel** _LEVEL_, **-L** _LEVEL_
> 设置日志级别：DEBUG、INFO、WARNING、ERROR、CRITICAL。

**--logfile** _FILE_
> 将日志输出写入文件。

**--profile** _FILE_
> 将 Python cProfile 统计数据写入文件。

# DESCRIPTION

**Scrapy** 是一个用于网页抓取和爬取的 Python 框架。它处理请求、解析和数据提取，内置支持链接跟随、cookie 处理，并遵守 robots.txt。

项目中包含爬虫（spider），即定义如何抓取网站的类。爬虫指定起始 URL，使用 CSS/XPath 选择器解析响应，并产出条目（item）或进一步的请求。

shell 命令提供交互式测试环境。你可以在编写爬虫代码之前在真实页面上试验选择器。Response 对象的方法与爬虫上下文中的一致。

条目定义被抓取的数据结构。条目管道（item pipeline）处理抓取的数据：验证、清洗以及存入数据库或文件。支持多种输出格式。

中间件负责请求/响应处理：用户代理、代理、重试、cookie。设置项控制行为：并发数、延迟、下载超时等。

扩展添加额外功能：统计收集、限流、自动节流以及自定义回调。

# CAVEATS

JavaScript 渲染的内容需要集成 Splash 或 Selenium。某些网站通过速率限制或验证码阻止爬虫。激进的抓取行为可能违反服务条款。应遵守 robots.txt。调试 shell 不保留状态。

# HISTORY

**Scrapy** 由 **Pablo Hoffman** 和 **Shane Evans** 于 **2008 年**前后在 Insophia 创建。它从内部工具发展为通用框架。该项目已成为最流行的 Python 抓取工具之一，商业公司 Scrapinghub（现 Zyte）为其提供支持和服务。

# INSTALL

```pacman: sudo pacman -S scrapy```

```brew: brew install scrapy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1), [beautifulsoup](/man/beautifulsoup)(1), [playwright](/man/playwright)(1)
