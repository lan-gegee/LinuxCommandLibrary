# TAGLINE

将 HTML 页面转换为 PDF

# TLDR

**将 HTML 转换为 PDF**

```wkhtmltopdf [input.html] [output.pdf]```

**将 URL 转换为 PDF**

```wkhtmltopdf [https://example.com] [output.pdf]```

**设置页面大小**

```wkhtmltopdf --page-size [A4] [input.html] [output.pdf]```

**设置方向**

```wkhtmltopdf --orientation [Landscape] [input.html] [output.pdf]```

**添加页边距**

```wkhtmltopdf --margin-top [20mm] --margin-bottom [20mm] [input.html] [output.pdf]```

**禁用 JavaScript**

```wkhtmltopdf --disable-javascript [input.html] [output.pdf]```

**添加页眉和页脚**

```wkhtmltopdf --header-center "[title]" --footer-center "[page]/[topage]" [input.html] [output.pdf]```

**多个页面**

```wkhtmltopdf [page1.html] [page2.html] [output.pdf]```

# SYNOPSIS

**wkhtmltopdf** [_--page-size size_] [_--orientation orient_] [_--margin-* size_] [_options_] _input_ _output_

# PARAMETERS

**--page-size** _SIZE_
> 纸张大小：A4、Letter、Legal 等。

**--orientation** _ORIENT_
> 横向或纵向。

**--margin-top** _SIZE_
> 上边距（如 10mm、1in）。

**--margin-bottom** _SIZE_
> 下边距。

**--margin-left** _SIZE_
> 左边距。

**--margin-right** _SIZE_
> 右边距。

**--dpi** _DPI_
> 输出分辨率。

**--zoom** _FACTOR_
> 缩放系数。

**--grayscale**
> 生成灰度 PDF。

**--disable-javascript**
> 不运行 JavaScript。

**--javascript-delay** _MS_
> 打印前的等待时间。

**--header-html** _FILE_
> HTML 页眉文件。

**--header-center** _TEXT_
> 居中的页眉文本。

**--footer-html** _FILE_
> HTML 页脚文件。

**--footer-center** _TEXT_
> 居中的页脚文本。

**--toc**
> 包含目录。

**--cover** _FILE_
> 封面页 HTML。

**--cookie** _NAME_ _VALUE_
> 设置 cookie。

**--username** _USER_
> HTTP 身份验证用户名。

**--password** _PASS_
> HTTP 身份验证密码。

**--no-images**
> 不加载图片。

**--lowquality**
> 生成较低质量的 PDF/PS 以减小文件体积。

**--encoding** _ENCODING_
> 设置默认文本编码。

# DESCRIPTION

**wkhtmltopdf** 使用 WebKit 渲染引擎将 HTML 转换为 PDF。它像浏览器一样渲染页面，然后输出为 PDF。

多个输入页面会合并为一个 PDF。目录可以根据标题自动生成。封面页和页眉/页脚用于框住正文内容。

页眉和页脚支持变量：[page]、[topage]、[title]、[section]、[subsection]、[date]、[time]、[webpage]。这些变量可实现自动页码和活动页眉。

可以通过 CSS 打印媒体规则控制分页。该工具支持 page-break-before、page-break-after 及相关属性。

JavaScript 延迟用于处理异步加载的动态内容。对于重度依赖 JavaScript 的页面，增加延迟可确保渲染完整。

身份验证选项支持基本认证、cookie 和自定义请求头，从而可以转换受保护的页面。

# CAVEATS

基于旧版 QtWebKit —— 部分现代 CSS/JS 可能无法正常工作。项目已不再维护。处理不可信内容存在安全隐患。大页面会占用大量内存。某些字体可能无法正确嵌入。可以考虑 WeasyPrint 或 Chrome headless 作为替代方案。

# HISTORY

**wkhtmltopdf** 由 **Jakob Truelsen** 大约于 **2008 年**创建。它在无头浏览器出现之前就提供了命令行的 HTML 转 PDF 功能。尽管基于较旧的 WebKit 版本，它仍被广泛使用。随着无头 Chrome/Firefox 成为替代方案，其开发逐渐放缓。

# INSTALL

```dnf: sudo dnf install wkhtmltopdf```

```nix: nix profile install nixpkgs#wkhtmltopdf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wkhtmltoimage](/man/wkhtmltoimage)(1), [weasyprint](/man/weasyprint)(1), [chromium](/man/chromium)(1), [pandoc](/man/pandoc)(1), [htmldoc](/man/htmldoc)(1)
