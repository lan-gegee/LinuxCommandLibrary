# TAGLINE

校验网站和文档中的链接

# TLDR

**检查网站链接**

```linkchecker [https://example.com]```

**检查本地 HTML 文件**

```linkchecker [index.html]```

**递归检查**

```linkchecker -r [https://example.com]```

**输出到文件**

```linkchecker -o html -F html/[report.html] [url]```

**同时检查外部链接**

```linkchecker --check-extern [url]```

**限制深度**

```linkchecker -r --depth=[3] [url]```

# SYNOPSIS

**linkchecker** [_options_] _url_

# PARAMETERS

_URL_
> 要检查的 URL 或文件。

**-r**
> 递归检查。

**--depth** _N_
> 最大递归深度。

**--check-extern**
> 检查外部链接。

**-o** _TYPE_
> 输出类型（text、html、csv、xml）。

**-F** _FILE_
> 输出到文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**linkchecker** 校验网站和文档中的链接。它能找出失效链接、重定向和错误。

该工具支持 HTTP、HTTPS、FTP 和本地文件。它可以递归检查并生成报告。

# CAVEATS

在大型网站上可能很慢。可能触发速率限制。默认遵守 robots.txt。

# HISTORY

LinkChecker 由 **Bastian Kleineidam** 创建，是一个面向网页内容的综合链接校验工具。

# INSTALL

```apt: sudo apt install linkchecker```

```dnf: sudo dnf install linkchecker```

```nix: nix profile install nixpkgs#linkchecker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wget](/man/wget)(1), [curl](/man/curl)(1), [lychee](/man/lychee)(1)
