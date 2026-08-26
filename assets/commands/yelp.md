# TAGLINE

GNOME 桌面帮助浏览器

# TLDR

**打开帮助浏览器**

```yelp```

**打开特定帮助文档**

```yelp [help:gnome-terminal]```

**打开 man 手册页**

```yelp [man:ls]```

**打开 info 页面**

```yelp [info:bash]```

**打开本地文件**

```yelp [file:///usr/share/doc/package/manual.html]```

**打开 Mallard 文档**

```yelp [ghelp:gedit]```

# SYNOPSIS

**yelp** [_options_] [_uri_]

# PARAMETERS

**--help**
> 显示帮助选项。

**--version**
> 显示版本。

# URI SCHEMES

**help:**：GNOME 帮助文档。

**ghelp:**：旧式 GNOME 帮助（DocBook）。

**man:**：系统手册页。

**info:**：GNU info 页面。

**file://**：本地 HTML 文件。

# DESCRIPTION

**yelp** 是 GNOME 的帮助浏览器，为查看各种文档格式提供统一界面。它支持 Mallard、DocBook、man 手册页、info 页面和 HTML 文档。

该应用与 GNOME 应用集成；在大多数 GNOME 应用中按 F1 会启动 yelp 并打开相关帮助。它具有交互式搜索、书签和导航历史功能。

Yelp 使用 XSLT 将 XML 文档渲染为 HTML。freedesktop.org 的帮助系统规范确保了各 GNOME 应用间一致的帮助访问体验。

# CAVEATS

以 GNOME 为中心；其他桌面可能使用不同的帮助系统。某些文档需要安装特定的软件包。更新后搜索索引可能需要重建。

# HISTORY

**yelp** 是作为 GNOME 的标准帮助浏览器而创建的。名字由 Daniel Lundin 建议。它与 GNOME 一同演进，支持了主要文档格式从 DocBook 向 Mallard 的过渡。

# INSTALL

```apt: sudo apt install yelp```

```dnf: sudo dnf install yelp```

```pacman: sudo pacman -S yelp```

```apk: sudo apk add yelp```

```zypper: sudo zypper install yelp```

```nix: nix profile install nixpkgs#yelp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[man](/man/man)(1), [info](/man/info)(1)
