# TAGLINE

将 HTML 页面转换为图片

# TLDR

**将 HTML 文件**转换为 PNG

```wkhtmltoimage [input.html] [output.png]```

**将网页**转换为图片

```wkhtmltoimage [https://example.com] [output.png]```

**设置输出尺寸**

```wkhtmltoimage --width [1024] --height [768] [input.html] [output.png]```

显式**指定输出格式**

```wkhtmltoimage --format [jpeg] [input.html] [output.jpg]```

**设置图片质量**（0-100）

```wkhtmltoimage --quality [85] [input.html] [output.jpg]```

**裁剪输出**

```wkhtmltoimage --crop-x [10] --crop-y [10] --crop-w [800] --crop-h [600] [input.html] [output.png]```

**禁用 JavaScript**

```wkhtmltoimage --disable-javascript [input.html] [output.png]```

以缩放系数渲染

```wkhtmltoimage --zoom [1.5] [input.html] [output.png]```

**等待 JavaScript**执行完毕

```wkhtmltoimage --javascript-delay [2000] [input.html] [output.png]```

# SYNOPSIS

**wkhtmltoimage** [_options_] _input_ _output_

# PARAMETERS

**--width** _int_
> 设置屏幕宽度（作为参考值）。

**--height** _int_
> 设置屏幕高度。

**-f**, **--format** _format_
> 输出格式：png、jpg、bmp、svg。

**--quality** _int_
> 输出质量 0-100（默认 94，用于 JPEG）。

**--crop-x** _int_
> 裁剪的 X 坐标。

**--crop-y** _int_
> 裁剪的 Y 坐标。

**--crop-w** _int_
> 裁剪的宽度。

**--crop-h** _int_
> 裁剪的高度。

**-n**, **--disable-javascript**
> 禁用 JavaScript 执行。

**--javascript-delay** _msec_
> 等待 JavaScript 执行完毕的毫秒数。

**--user-style-sheet** _path_
> 应用自定义 CSS 样式表。

**--cookie** _name_ _value_
> 设置 cookie（可重复使用）。

**--custom-header** _name_ _value_
> 设置自定义 HTTP 头（可重复使用）。

**--zoom** _float_
> 渲染的缩放系数（例如 2.0 表示放大两倍）。

**--disable-smart-width**
> 使用严格宽度而非参考宽度。

**--encoding** _encoding_
> 设置输入的默认文本编码。

**-p**, **--proxy** _proxy_
> 使用代理。

**--username** _username_
> HTTP 身份验证用户名。

**--password** _password_
> HTTP 身份验证密码。

**--run-script** _js_
> 在页面加载完成后运行额外的 JavaScript（可重复使用）。

**--load-error-handling** _handler_
> 页面加载失败时的处理方式：abort、ignore 或 skip（默认：abort）。

**--allow** _path_
> 允许从指定文件夹加载文件（可重复使用）。

**--no-images**
> 不加载也不输出图片。

**--stop-slow-scripts**
> 停止运行缓慢的 JavaScript。

**--window-status** _string_
> 等待 window.status 等于该字符串后再进行渲染。

**--log-level** _level_
> 设置日志级别：none、error、warn 或 info。

**-q**, **--quiet**
> 抑制输出消息（等同于 --log-level none）。

**-H**, **--extended-help**
> 显示完整帮助文档。

**-V**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**wkhtmltoimage** 使用 WebKit 渲染引擎将 HTML 页面转换为图片。它可以处理本地 HTML 文件，也可以抓取远程 URL，生成 PNG、JPEG、BMP 或 SVG 输出。

该工具以无头模式运行，不需要显示服务器，因此适合在服务器端生成图片。它支持执行 JavaScript、自定义样式表、cookie 以及 HTTP 身份验证。

它是 **wkhtmltopdf** 套件的一部分，与其 PDF 版本共享相同的渲染引擎和许多选项。

# CAVEATS

wkhtmltoimage 基于较旧的 Qt WebKit 版本，可能无法正确渲染现代 JavaScript 框架。对于复杂页面，可以考虑 Puppeteer 或 Playwright 等替代方案。该项目已进入维护模式，更新有限。

# HISTORY

wkhtmltoimage 由 **Jakob Truelsen** 作为 **wkhtmltopdf** 项目的一部分创建，大约于 **2008 年**首次发布。它利用 Qt 的 WebKit 实现进行渲染。该项目因服务器端 HTML 转 PDF/图片转换而广受欢迎。随着底层 Qt WebKit 被 Qt WebEngine 取代而逐渐废弃，其开发速度也已放缓。

# SEE ALSO

[wkhtmltopdf](/man/wkhtmltopdf)(1), [convert](/man/convert)(1), [puppeteer](/man/puppeteer)(1), [playwright](/man/playwright)(1)
