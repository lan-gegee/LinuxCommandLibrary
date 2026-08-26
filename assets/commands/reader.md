# TAGLINE

终端阅读视图，呈现更干净的网页内容

# TLDR

**在终端中阅读网页**

```reader [https://example.com/article]```

**阅读本地 HTML 文件**

```reader [path/to/file.html]```

# SYNOPSIS

**reader** [_options_] _url_or_file_

# DESCRIPTION

**reader** 在终端中模拟浏览器的阅读模式功能。它解析网页内容并以易于阅读的格式显示，去除导航、广告和其他干扰元素。它可以借助 Sixel 把嵌入图片渲染为彩色块状图形，并与 vi 和 Neovim 编辑器集成。

# HISTORY

**reader** 由 **mrusme** 创建，使用 **Go** 编写。

# INSTALL

```apk: sudo apk add reader```

```nix: nix profile install nixpkgs#reader```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lynx](/man/lynx)(1), [w3m](/man/w3m)(1), [curl](/man/curl)(1)
