# TAGLINE

基于文本的网页浏览器和分页器

# TLDR

**打开 URL**

```w3m [https://example.com]```

**打开本地文件**

```w3m [file.html]```

**将页面转储为文本**

```w3m -dump [https://example.com]```

**连同源码一起转储**

```w3m -dump_source [https://example.com]```

**从标准输入渲染 HTML**

```cat [file.html] | w3m -T text/html```

**以单色模式打开**

```w3m -M [https://example.com]```

**使用指定的浏览器宽度**

```w3m -cols [80] -dump [https://example.com]```

**打开书签文件**

```w3m -B```

# SYNOPSIS

**w3m** [_options_] [_URL or file_]

# DESCRIPTION

**w3m** 是一款在终端中运行的基于文本的网页浏览器。它能渲染带有表格、框架和图片的 HTML 页面（需配合合适的终端），是最强大的终端浏览器之一。

该浏览器支持标签页、书签、Cookie 和表单输入。它还可以像 less 那样作为本地 HTML 文件的分页器。-dump 选项使其适合在脚本中将 HTML 转换为纯文本。

w3m 同时支持 HTTP 和 HTTPS，支持基本身份验证，并可与外部程序协作完成下载和图片显示。

# PARAMETERS

**-dump**
> 将渲染后的页面输出到标准输出后退出。

**-dump_source**
> 将 HTML 源码输出到标准输出。

**-T** _type_
> 指定内容类型。

**-cols** _num_
> 设置显示宽度。

**-M**
> 单色模式。

**-B**
> 打开书签文件。

**-m**
> 在某些终端中启用鼠标。

**-cookie**
> 启用 Cookie。

**-no-cookie**
> 禁用 Cookie。

**-pauth** _user:pass_
> 代理身份验证。

**-N**
> 以标签页方式打开多个 URL。

**-I** _encoding_
> 指定文档的输入字符编码。

**-O** _encoding_
> 指定转储输出的字符编码。

**-o** _option=value_
> 设置配置选项。

# NAVIGATION KEYS

**Space/PgDn**：向下翻页
**b/PgUp**：向上翻页
**Enter**：跟随链接
**Tab**：下一个链接
**U**：输入 URL
**B**：后退
**H**：历史记录
**T**：新建标签页
**q**：退出

# CAVEATS

不支持 JavaScript。某些现代网页无法正确渲染。图片支持需要兼容的终端。HTTPS 可能需要根据 SSL 库进行配置。

# HISTORY

**w3m** 由 **Akinori Ito** 于 **1995 年**在日本东北大学创建。名字最初代表 "WWW-wo-Miru"（日语意为“看 WWW”）。它陆续加入了表格渲染和图片支持等特性，能力超越了早期的文本浏览器。多年来该项目由多位开发者维护。

# INSTALL

```apt: sudo apt install w3m```

```dnf: sudo dnf install w3m```

```pacman: sudo pacman -S w3m```

```apk: sudo apk add w3m```

```zypper: sudo zypper install w3m```

```brew: brew install w3m```

```nix: nix profile install nixpkgs#w3m```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lynx](/man/lynx)(1), [links](/man/links)(1), [elinks](/man/elinks)(1), [curl](/man/curl)(1)
