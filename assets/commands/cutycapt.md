# TAGLINE

WebKit 网页转图片工具

# TLDR

将网页**捕获为 PNG**

```cutycapt --url=[https://example.com] --out=[screenshot.png]```

**捕获为 PDF**

```cutycapt --url=[https://example.com] --out=[page.pdf]```

**设置视口大小**

```cutycapt --url=[url] --out=[out.png] --min-width=[1920] --min-height=[1080]```

**延时后捕获**

```cutycapt --url=[url] --out=[out.png] --delay=[2000]```

**禁用 JavaScript**

```cutycapt --url=[url] --out=[out.png] --javascript=off```

**配合 Xvfb 无头运行**

```xvfb-run cutycapt --url=[url] --out=[out.png]```

# SYNOPSIS

**cutycapt** --url=_url_ --out=_file_ [_options_]

# DESCRIPTION

**cutycapt** 将 WebKit 渲染的网页捕获为图片或文档。支持 PNG、JPEG、PDF、SVG、PS 等格式。使用 Qt WebKit 引擎渲染。

# PARAMETERS

**--url** _url_
> 要捕获的 URL（http://、file:// 等）

**--out** _file_
> 输出文件路径

**--out-format** _format_
> 输出格式（覆盖扩展名推断）

**--min-width** _pixels_
> 最小宽度（默认：800）

**--min-height** _pixels_
> 最小高度（默认：600）

**--max-width** _pixels_
> 最大宽度

**--max-height** _pixels_
> 最大高度

**--delay** _ms_
> 加载后的延时（默认：0）

**--max-wait** _ms_
> 最长等待时间（默认：90000）

**--zoom** _factor_
> 缩放系数

**--javascript** on|off
> 启用/禁用 JavaScript

**--plugins** on|off
> 启用/禁用插件

**--proxy** _host:port_
> HTTP 代理

**--header** _name:value_
> 自定义请求头

**--method** get|post|put
> HTTP 方法

# OUTPUT FORMATS

svg, pdf, ps, png, jpeg, tiff, gif, bmp, mng, ppm, xbm, xpm

# CAVEATS

需要 X 服务器。无头环境请使用 xvfb-run。基于较旧的 Qt WebKit（非 Chromium）。

# INSTALL

```apt: sudo apt install cutycapt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wkhtmltoimage](/man/wkhtmltoimage)(1), [chromium](/man/chromium)(1), [firefox](/man/firefox)(1)

# RESOURCES

```[Homepage](http://cutycapt.sourceforge.net)```

<!-- verified: 2026-06-26 -->
