# TAGLINE

把完整网页保存为单个 HTML 文件

# TLDR

**将网页保存为单个 HTML 文件**

```monolith [https://example.com] -o [page.html]```

**包含 JavaScript**

```monolith -j [https://example.com] -o [page.html]```

**排除图片**

```monolith -i [https://example.com] -o [page.html]```

**与网络隔离**（不发外部请求）

```monolith -I [https://example.com] -o [page.html]```

**设置自定义 User-Agent**

```monolith -u "[Mozilla/5.0...]" [https://example.com] -o [page.html]```

**从本地文件保存**

```monolith [file:///path/to/page.html] -o [output.html]```

**设置超时时间**

```monolith -t [30] [https://example.com] -o [page.html]```

# SYNOPSIS

**monolith** [_-o output_] [_-jicfIe_] [_-t timeout_] [_-u agent_] _url_

# PARAMETERS

**-o** _FILE_, **--output** _FILE_
> 输出文件。

**-j**, **--no-js**
> 排除 JavaScript。

**-c**, **--no-css**
> 排除 CSS。

**-i**, **--no-images**
> 排除图片。

**-f**, **--no-frames**
> 排除 iframe。

**-F**, **--no-fonts**
> 排除字体。

**-v**, **--no-video**
> 排除视频。

**-a**, **--no-audio**
> 排除音频。

**-I**, **--isolate**
> 禁用网络请求。

**-e**, **--ignore-errors**
> 遇到资源错误时继续处理。

**-t** _SEC_, **--timeout** _SEC_
> 请求超时时间。

**-u** _AGENT_, **--user-agent** _AGENT_
> 自定义 User-Agent。

**-b** _URL_, **--base-url** _URL_
> 相对路径的基础 URL。

**-d** _DOMAIN_, **--domain** _DOMAIN_
> 限定在指定域名内。

**-k**, **--insecure**
> 接受无效证书。

**-s**, **--silent**
> 抑制输出。

# DESCRIPTION

**monolith** 把完整网页保存为单个 HTML 文件。它把所有资源——CSS、图片、字体、JavaScript——以 data URL 形式嵌入 HTML 中，生成完全自包含的文档。

与浏览器的"另存为"（会生成一堆资源文件夹）不同，monolith 产出一个可离线工作的文件。这非常适合归档、文档化和分享。

隔离模式（-I）通过移除外部引用创建真正离线的页面。结合移除 JavaScript 的 -j，可以得到没有任何网络依赖的静态快照。

当不需要完全保真时，资源排除选项可减小文件体积。排除图片或字体能显著缩小输出。该工具能正确处理 CSS @import 和相对 URL。

本地文件可以通过 file:// URL 处理。这样可以把带有外部资源的现有 HTML 转换为自包含文档。

使用 -e 处理错误时，个别资源加载失败也会继续处理，这对存在失效链接或被屏蔽资源的页面很有用。

# CAVEATS

资源繁多的页面会产生很大的文件。Base64 编码会增加体积。动态 JavaScript 内容无法捕获。某些网站会阻止自动化访问。受 Cookie 保护的内容不可访问。SPA 可能无法完整渲染。

# HISTORY

**monolith** 由 **Sunshine**（nicholaides）创建于约 **2019 年**。它以 Rust 编写，为网页归档提供了 wget/curl 之外的现代选择。相比传统归档方式，单文件的输出格式简化了存储和分享。

# INSTALL

```pacman: sudo pacman -S monolith```

```apk: sudo apk add monolith```

```brew: brew install monolith```

```nix: nix profile install nixpkgs#monolith```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wget](/man/wget)(1), [curl](/man/curl)(1), [httrack](/man/httrack)(1)
