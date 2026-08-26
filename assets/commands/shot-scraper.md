# TAGLINE

自动化网站截图工具

# TLDR

对网页**截图**

```shot-scraper [https://example.com]```

以自定义尺寸**截图**

```shot-scraper [https://example.com] -w [800] -h [600] -o [output.png]```

按 CSS 选择器**截取特定元素**

```shot-scraper [https://example.com] -s '[.header]' -o [header.png]```

在截图前执行 JavaScript 再**截图**

```shot-scraper [https://example.com] --javascript "[document.body.style.backgroundColor = 'white']"```

**截取 retina 截图**（2 倍缩放）

```shot-scraper [https://example.com] --retina -o [output.png]```

截图前**等待元素出现**

```shot-scraper [https://example.com] --wait-for "[document.querySelector('.loaded')]"```

以指定质量**保存为 JPEG**

```shot-scraper [https://example.com] -o [output.jpg] --quality [80]```

以**交互模式**在截图前手动浏览页面

```shot-scraper [https://example.com] --interactive```

# SYNOPSIS

**shot-scraper** _URL_ [_options_]

**shot-scraper** **install**

**shot-scraper** **javascript** _URL_ _script_ [_options_]

**shot-scraper** **pdf** _URL_ [_options_]

**shot-scraper** **accessibility** _URL_ [_options_]

**shot-scraper** **har** _URL_ [_options_]

# PARAMETERS

**-o**, **--output** _FILE_
> 输出文件名。使用 **-** 表示标准输出。

**-w**, **--width** _PIXELS_
> 浏览器视口宽度。默认：1280。

**-h**, **--height** _PIXELS_
> 浏览器视口高度。默认：整页。

**-s**, **--selector** _SELECTOR_
> 用于替代整页截取的 CSS 选择器。

**--selector-all** _SELECTOR_
> 截取所有匹配选择器的元素。

**--padding** _PIXELS_
> 在选中元素周围添加内边距。

**--js-selector** _EXPRESSION_
> 用于过滤元素的 JavaScript 表达式。

**--wait** _MS_
> 页面加载后等待的毫秒数。

**--wait-for** _EXPRESSION_
> 等待直到 JavaScript 表达式为真。

**-j**, **--javascript** _CODE_
> 在截图前执行的 JavaScript 代码。

**--quality** _PERCENT_
> 以指定质量（1-100）保存为 JPEG。

**--retina**
> 使用 2 的设备缩放因子。

**--scale-factor** _N_
> 自定义设备像素比。

**--omit-background**
> 透明背景（仅限 PNG）。

**-b**, **--browser** _NAME_
> 要使用的浏览器：chromium、firefox、webkit、chrome。

**--browser-arg** _ARG_
> 向浏览器传递命令行参数。

**--user-agent** _STRING_
> 自定义 User-Agent 头。

**-i**, **--interactive**
> 截图前暂停，等待手动操作。

**--bypass-csp**
> 绕过内容安全策略（CSP）限制。

**--log-requests** _FILE_
> 以换行分隔的 JSON 记录 HTTP 请求日志。

**--timeout** _MS_
> 失败前的超时时间（毫秒）。

# DESCRIPTION

**shot-scraper** 是一个基于 Playwright 构建的命令行工具，用于对网站进行自动化截图。它可以截取整页、特定元素，或在截取前执行 JavaScript。该工具面向文档编写、自动化测试和网络爬取工作流而设计。

除了截图，shot-scraper 还可以在页面上执行 JavaScript 并返回结果、生成 PDF、导出无障碍树以及捕获 HAR（HTTP Archive）文件。它与 CI/CD 流水线集成良好，尤其是 GitHub Actions，可用于定期生成更新的截图。

首次使用前，请运行 **shot-scraper install** 下载所需的浏览器二进制文件。

# CAVEATS

需要 Python 和 Playwright 浏览器二进制文件（通过 **shot-scraper install** 安装）。截图默认宽度为 1280px、高度为整页，对于很长的页面可能产生较大的文件。对于动态加载的内容，JavaScript 执行时机可能需要通过 **--wait** 或 **--wait-for** 调整。

# HISTORY

**shot-scraper** 由 Simon Willison 开发，于 **2022 年**首次发布。它旨在利用 Playwright 的浏览器自动化能力来自动化文档截图和网络爬取任务。该工具因在 CI/CD 流水线中生成自动截图而广受欢迎，知名用户包括路透社的数据仪表盘项目。开发持续活跃，定期发布新功能版本。

# INSTALL

```nix: nix profile install nixpkgs#shot-scraper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[playwright](/man/playwright)(1), [puppeteer](/man/puppeteer)(1), [chromium](/man/chromium)(1), [firefox](/man/firefox)(1)
