# TAGLINE

同时支持文本模式和图形模式的网页浏览器

# TLDR

**以图形模式浏览**

```links2 -g [https://example.com]```

**以文本模式浏览**

```links2 [https://example.com]```

**将渲染后的页面输出到 stdout**

```links2 -dump [https://example.com]```

**以指定文本宽度输出**

```links2 -dump -width [120] [https://example.com]```

**输出页面源码**

```links2 -source [https://example.com]```

**以指定分辨率在图形模式下启动**

```links2 -g -mode [1024x768x24] [https://example.com]```

# SYNOPSIS

**links2** [_options_] [_url_]

# PARAMETERS

**-g**
> 以图形模式启动。

**-t**
> 强制文本模式。

**-driver** _driver_
> 选择图形驱动（x、svgalib、fb、directfb）。

**-mode** _WxHxD_
> 图形模式的分辨率和色深（例如 1024x768x24）。

**-depth** _N_
> 图形模式下的色深。

**-anonymous**
> 匿名浏览模式（禁用本地文件访问和书签）。

**-dump**
> 将渲染后的页面文本输出到 stdout 并退出。

**-width** _N_
> -dump 模式下的文本宽度（字符数）。

**-source**
> 将原始 HTML 页面源码输出到 stdout 并退出。

**-version**
> 打印版本并退出。

# DESCRIPTION

**links2** 是一个同时支持文本模式和图形模式的网页浏览器。在图形模式下，它可以显示图片并以更直观的方式渲染页面，同时保持轻量。它是原版 links 浏览器的增强版本。

在文本模式下，它的用法与 lynx 或 w3m 类似。在图形模式（-g）下，它借助 X11、framebuffer 或 SVGAlib 提供完整的可视化浏览体验。

**-dump** 选项对脚本编写很有用，可将网页转换为纯文本输出。

# CAVEATS

图形模式需要 X11 或 framebuffer 支持。并非所有系统都提供所有图形驱动。不支持 JavaScript。

# INSTALL

```apt: sudo apt install links2```

```nix: nix profile install nixpkgs#links2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[links](/man/links)(1), [lynx](/man/lynx)(1), [w3m](/man/w3m)(1), [curl](/man/curl)(1), [wget](/man/wget)(1)
