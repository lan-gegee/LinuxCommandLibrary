# TAGLINE

以指定的视口尺寸截取网站屏幕截图

# TLDR

**截取网站屏幕截图**

```pageres [https://example.com]```

**指定视口尺寸**

```pageres [https://example.com] [1024x768]```

**多个尺寸**

```pageres [https://example.com] [1024x768] [1920x1080]```

**裁剪至视口**（默认截取整页）

```pageres [https://example.com] [1024x768] --crop```

**设置输出文件名**

```pageres [https://example.com] --filename=[screenshot]```

**截图前的延迟时间**

```pageres [https://example.com] --delay=[3]```

**设置输出目录**

```pageres [https://example.com] -d [./screenshots]```

**截取特定元素**

```pageres [https://example.com] --selector=[.header]```

**在截图前隐藏某个元素**

```pageres [https://example.com] --hide=[.cookie-banner]```

# SYNOPSIS

**pageres** [_options_] _url_ [_sizes_...]

# PARAMETERS

**-d**, **--dest** _DIR_
> 输出目录。

**--filename** _TEMPLATE_
> 文件名模板。

**--delay** _SECONDS_
> 截图前的延迟秒数。

**-c**, **--crop**
> 将图像裁剪为指定的视口高度（默认截取整个可滚动页面）。

**--overwrite**
> 覆盖已有文件。

**--format** _FORMAT_
> 图像格式：_png_（默认）或 _jpg_。

**--scale** _FACTOR_
> 像素密度缩放倍数。

**--selector** _SELECTOR_
> 只截取匹配 CSS 选择器的 DOM 元素。

**--hide** _SELECTOR_
> 截图前隐藏匹配选择器的元素（可重复指定）。

**--clickElement** _SELECTOR_
> 截图前点击匹配的元素。

**--css** _CSS_
> 截图前注入自定义 CSS。

**--cookie** _COOKIE_
> Cookie 字符串（可重复指定）。

**--header** _HEADER_
> HTTP 头（可重复指定）。

**--username** _USER_
> HTTP basic auth 用户名。

**--password** _PASS_
> HTTP basic auth 密码。

**--user-agent** _UA_
> User agent 字符串。

**--transparent**
> 使用透明背景代替白色背景。

**--darkMode**
> 模拟用户的深色配色方案偏好。

**--timeout** _SECONDS_
> 请求超时时间（秒）。

**-v**, **--verbose**
> 打印详细的错误输出。

# DESCRIPTION

**pageres** 以指定的视口尺寸截取网站的屏幕截图。它非常适合响应式设计测试。

可以在单条命令中指定多个视口尺寸。每个尺寸会生成单独的图像。

整页截图会捕捉首屏以下的内容。裁剪模式则只保留可见视口内的画面。

延迟可以让 JavaScript 和动画执行完毕。自定义 CSS 可以隐藏或修改元素。

输出支持 PNG 和 JPEG 格式。文件名可以包含 URL 和尺寸变量。

# CAVEATS

需要无头 Chrome/Chromium。依赖大量 JavaScript 的网站可能需要设置延迟。某些网站会阻止自动化截图。

# HISTORY

**pageres** 由 **Sindre Sorhus** 开发，用于响应式设计测试。它为网站截图自动化提供了命令行接口。

# SEE ALSO

[chromium](/man/chromium)(1), [puppeteer](/man/puppeteer)(1), [shot-scraper](/man/shot-scraper)(1)
