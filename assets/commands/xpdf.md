# TAGLINE

轻量级 X11 PDF 查看器

# TLDR

**打开 PDF 文件**

```xpdf [document.pdf]```

**打开并定位到指定页**

```xpdf [document.pdf] [5]```

**设置初始缩放**（百分比、"page"、"width"）

```xpdf -z [150] [document.pdf]```

**全屏模式**

```xpdf -fullscreen [document.pdf]```

**使用所有者密码打开**

```xpdf -opw [owner_password] [document.pdf]```

**反色**（深色背景）模式

```xpdf -rv [document.pdf]```

**远程控制模式**

```xpdf -remote [name] [document.pdf]```

# SYNOPSIS

**xpdf** [_-z zoom_] [_-fullscreen_] [_-opw password_] [_options_] _file.pdf_ [_page_]

# PARAMETERS

**-z** _ZOOM_
> 初始缩放（百分比、page、width）。

**-fullscreen**
> 全屏模式。

**-opw** _PASSWORD_
> 所有者密码。

**-upw** _PASSWORD_
> 用户密码。

**-remote** _NAME_
> 以远程模式启动。

**-g** _GEOMETRY_
> 窗口几何尺寸。

**-rv**
> 反色模式。

**-papercolor** _COLOR_
> 纸张背景颜色。

**-mattecolor** _COLOR_
> 页面周围的衬底颜色。

**-cfg** _FILE_
> 配置文件。

**-v**
> 显示版本。

**-h**
> 显示帮助。

# KEY BINDINGS

**n**, **Space**, **PgDn**
> 下一页。

**p**, **Backspace**, **PgUp**
> 上一页。

**+**, **-**
> 放大/缩小。

**z**
> 缩放至整页。

**w**
> 缩放至页宽。

**/**
> 向前搜索。

**?**
> 向后搜索。

**q**
> 退出。

# DESCRIPTION

**xpdf** 是一个面向 X11 的轻量级 PDF 查看器。它以极少的资源占用来渲染 PDF 文档。

该查看器提供基本的 PDF 功能：导航、缩放、搜索和打印。它能处理大多数标准 PDF 特性。

远程模式允许从脚本进行控制。发送到命名实例的命令可以打开文件、导航和控制显示。

通过 ~/.xpdfrc 可以自定义外观和行为。字体路径、颜色和按键绑定均可调整。

xpdf 软件包还包含命令行工具：[pdftotext](/man/pdftotext)(1)、[pdftops](/man/pdftops)(1)、[pdfinfo](/man/pdfinfo)(1) 和 [pdfimages](/man/pdfimages)(1)。这些工具被广泛使用，且不依赖于查看器本身。

# CAVEATS

功能少于 Evince 或 Okular。某些现代 PDF 特性可能无法渲染。仅支持 X11。开发进度比同类软件慢。

# HISTORY

**xpdf** 由 **Derek Noonburg** 自 **1995** 年起创建。它是最早的开源 PDF 查看器之一，并催生了 Poppler 库——许多现代查看器都在使用它。

# INSTALL

```apt: sudo apt install xpdf```

```dnf: sudo dnf install xpdf```

```pacman: sudo pacman -S xpdf```

```apk: sudo apk add xpdf```

```brew: brew install xpdf```

```nix: nix profile install nixpkgs#xpdf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[evince](/man/evince)(1), [okular](/man/okular)(1), [mupdf](/man/mupdf)(1), [zathura](/man/zathura)(1)
