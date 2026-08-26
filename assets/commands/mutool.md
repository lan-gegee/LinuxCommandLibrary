# TAGLINE

muPDF 命令行工具

# TLDR

**将 PDF 转换为图像**

```mutool draw -o [page%d.png] [input.pdf]```

**从 PDF 提取文本**

```mutool draw -F txt [input.pdf]```

**显示 PDF 信息**

```mutool info [input.pdf]```

**合并 PDF**

```mutool merge -o [output.pdf] [file1.pdf] [file2.pdf]```

**提取页面**

```mutool merge -o [output.pdf] [input.pdf] [1-5]```

**清理 PDF**

```mutool clean [input.pdf] [output.pdf]```

# SYNOPSIS

**mutool** _command_ [_options_] _files_

# PARAMETERS

_COMMAND_
> 要执行的操作。

**draw**
> 将文档渲染为图像/文本。

**info**
> 显示文档信息。

**merge**
> 合并/提取页面。

**clean**
> 重写 PDF 文件。

**convert**
> 在不同格式之间转换文件。

**extract**
> 从 PDF 中取出图像和字体文件。

**pages**
> 输出页面尺寸和方向信息。

**poster**
> 将页面切分为分块，用于大幅面打印。

**show**
> 将指定对象和流打印到 stdout。

**run**
> 执行一个可访问 MuPDF 的 JavaScript 程序。

**create**
> 从图形命令输入生成新 PDF。

**-o** _FILE_
> 输出文件（draw、merge 及其他子命令使用）。

**-r** _RESOLUTION_
> 渲染分辨率（DPI，默认：72，用于 draw）。

**-F** _FORMAT_
> 强制使用特定输出格式（用于 draw）。

**-w** _WIDTH_
> 页面渲染宽度（像素，用于 draw）。

**-h** _HEIGHT_
> 页面渲染高度（像素，用于 draw）。

**-p** _PASSWORD_
> 加密文件的密码。

# DESCRIPTION

**mutool** 是 MuPDF 的命令行工具，用于处理 PDF 及其他文档格式。它可以将页面渲染为图像、提取文本和图像、合并与拆分 PDF，还能运行带有 MuPDF 绑定的 JavaScript 程序。轻量而快速。

# CAVEATS

属于 MuPDF。部分功能需要特定构建版本。编辑能力有限。

# HISTORY

mutool 是 **MuPDF** 的一部分，后者是由 Artifex Software 创建的轻量级 PDF 渲染器。

# INSTALL

```apt: sudo apt install mupdf-tools```

```pacman: sudo pacman -S mupdf-tools```

```apk: sudo apk add mupdf-tools```

```brew: brew install mupdf-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdftk](/man/pdftk)(1), [gs](/man/gs)(1), [qpdf](/man/qpdf)(1)
