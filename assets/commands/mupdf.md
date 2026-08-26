# TAGLINE

轻量级 PDF、XPS 和 EPUB 查看器

# TLDR

**打开 PDF 文件**

```mupdf [document.pdf]```

**打开到指定页**

```mupdf [document.pdf] [page_number]```

**以自定义分辨率打开**（DPI）

```mupdf -r [150] [document.pdf]```

**打开受密码保护的 PDF**

```mupdf -p [password] [document.pdf]```

**以自定义排版打开 EPUB**

```mupdf -W [600] -H [800] -S [14] [book.epub]```

# SYNOPSIS

**mupdf** [_options_] _file_ [_page_]

# PARAMETERS

**-p** _password_
> 加密 PDF 的密码。

**-r** _resolution_
> 通过 DPI 设置缩放级别（默认：72）。

**-A** _bits_
> 抗锯齿质量，0-8（默认：8）。

**-C** _RRGGBB_
> 白色调颜色，十六进制（默认：FFFFF0）。

**-B** _RRGGBB_
> 黑色调颜色，十六进制（默认：303030）。

**-W** _width_
> EPUB 排版的页面宽度（磅）。

**-H** _height_
> EPUB 排版的页面高度（磅）。

**-S** _size_
> EPUB 排版的字体大小（磅）。

**-U** _CSS-file_
> EPUB 渲染使用的用户样式表。

**-I**
> 反转显示颜色。

**-J**
> 禁用 PDF 表单中的 JavaScript。

**-X**
> 禁用 EPUB 文档自带样式。

# KEY BINDINGS

**q**
> 退出。

**+/-**
> 放大/缩小。

**W**
> 适应页面宽度。

**H**
> 适应页面高度。

**Z**
> 自动适应页面。

**Space/PgDn**
> 下一页。

**b/PgUp**
> 上一页。

**_number_ g**
> 跳转到指定页码。

**G**
> 跳转最后一页。

**/**
> 向前搜索。

**?**
> 向后搜索。

**n/N**
> 下一个/上一个搜索结果。

**r**
> 重新加载文档。

**i**
> 切换 ICC 色彩管理。

**[/]**
> 向左/向右旋转。

**f**
> 切换全屏。

**h/j/k/l**
> 向左/向下/向上/右滚动。

# DESCRIPTION

**mupdf** 是一款轻量级 PDF、XPS 和 EPUB 查看器。它使用抗锯齿图形技术高质量地渲染文档。

该查看器注重速度和简洁。即使包含复杂图形，文档也能快速渲染。与功能完备的阅读器相比，内存占用保持在较低水平。

导航使用类似 vi 的键盘快捷键。页面跳转、搜索和缩放均可通过键盘完成，鼠标滚动和拖拽同样可用。

渲染引擎能正确处理透明度、渐变和嵌入字体。它支持包括注释、表单和 JavaScript（有限）在内的 PDF 特性。

颜色反转有助于在弱光环境下阅读。重新打开文档时，查看器会记住缩放级别和页面位置。

# CAVEATS

界面极简——没有工具栏或菜单。表单填写功能较基础。JavaScript 支持有限。无法编辑注释。某些 PDF 的渲染结果可能与 Adobe Reader 不同。

# HISTORY

**MuPDF** 由 Ghostscript 的维护者 **Artifex Software** 从约 **2006 年**开始开发。它的定位是轻量、高质量的渲染器。mupdf 查看器是 MuPDF 库的参考应用，该库被 Sumatra PDF 等许多其他项目采用。

# INSTALL

```apt: sudo apt install mupdf```

```dnf: sudo dnf install mupdf```

```pacman: sudo pacman -S mupdf```

```apk: sudo apk add mupdf```

```zypper: sudo zypper install mupdf```

```brew: brew install mupdf```

```nix: nix profile install nixpkgs#mupdf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zathura](/man/zathura)(1), [evince](/man/evince)(1), [okular](/man/okular)(1), [xpdf](/man/xpdf)(1), [mutool](/man/mutool)(1)
