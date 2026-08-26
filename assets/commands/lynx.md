# TAGLINE

基于文本的网页浏览器

# TLDR

**浏览网站**

```lynx [https://example.com]```

**浏览本地文件**

```lynx [file.html]```

**以纯文本输出页面**

```lynx -dump [url]```

**接受 Cookie**

```lynx -accept_all_cookies [url]```

**下载文件**

```lynx -source [url] > [file]```

**使用指定配置**

```lynx -cfg=[config.cfg] [url]```

**输出页面但不带链接列表**

```lynx -dump -nolist [url]```

**发送 POST 请求**

```lynx -post_data [url] < [data_file]```

**设置自定义用户代理**

```lynx -useragent="[MyAgent/1.0]" [url]```

# SYNOPSIS

**lynx** [_options_] [_url_]

# PARAMETERS

_URL_
> 要浏览的 URL 或文件。

**-dump**
> 以纯文本输出页面。

**-source**
> 输出页面源码。

**-accept_all_cookies**
> 接受所有 Cookie。

**-cfg** _FILE_
> 配置文件。

**-nolist**
> 输出文档时不在末尾附上引用链接列表。

**-post_data**
> 通过 stdin 以 POST 方式发送表单数据。

**-useragent** _STRING_
> 设置自定义 User-Agent 请求头。

**-auth** _USER:PASS_
> HTTP 基本认证凭据。

**-head**
> 发送 HEAD 请求并显示响应头。

**-width** _N_
> 用于排版的屏幕宽度（默认 80）。

**-traversal**
> 从该 URL 开始爬取链接。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lynx** 是一款基于文本的网页浏览器。它在终端中渲染 HTML，不显示图形。

该工具适用于脚本编写、无障碍访问以及在服务器上浏览网页。支持链接和表单。

# CAVEATS

不支持 JavaScript。不支持图片。依靠键盘导航。CSS 支持有限。

# HISTORY

Lynx 于 1992 年诞生于**堪萨斯大学**，是目前仍在维护的最古老的网页浏览器之一。

# INSTALL

```apt: sudo apt install lynx```

```dnf: sudo dnf install lynx```

```pacman: sudo pacman -S lynx```

```apk: sudo apk add lynx```

```zypper: sudo zypper install lynx```

```brew: brew install lynx```

```nix: nix profile install nixpkgs#lynx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[w3m](/man/w3m)(1), [links](/man/links)(1), [curl](/man/curl)(1), [wget](/man/wget)(1)
