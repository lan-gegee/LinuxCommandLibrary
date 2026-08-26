# TAGLINE

将 PDF 文件转换为可缩放矢量图形格式

# TLDR

**将 PDF 页面转换为 SVG**

```pdf2svg [input.pdf] [output.svg]```

**转换指定页面**

```pdf2svg [input.pdf] [output.svg] [2]```

**转换所有页面**

```pdf2svg [input.pdf] [output_%d.svg] all```

# SYNOPSIS

**pdf2svg** _input.pdf_ _output.svg_ [_page_|all]

# PARAMETERS

**input.pdf**
> 输入的 PDF 文件。

**output.svg**
> 输出的 SVG 文件。

**page**
> 页码（从 1 开始）。

**all**
> 转换所有页面。

# DESCRIPTION

**pdf2svg** 将 PDF 文件转换为可缩放矢量图形（SVG）格式。它保留矢量图形、文本和格式，使输出适合网页使用和编辑。

该工具使用 **Poppler** 解析 PDF，使用 **Cairo** 渲染 SVG。若要在一次运行中转换每一页，可将 **all** 作为页面参数，并在输出文件名中加入 **%d** 占位符——pdf2svg 会在写入时替换为页码（例如 `pdf2svg book.pdf page_%d.svg all` 会生成 `page_1.svg`、`page_2.svg` 等）。

# CAVEATS

每个 SVG 文件只含一页（不支持多页 SVG 输出）。复杂的 PDF 可能生成非常大的 SVG。字体通常会转换为轮廓路径，这保留了渲染保真度但丢失了可选中的文本。

# HISTORY

pdf2svg 由 **David Barton** 创建，使用 Poppler 解析 PDF、Cairo 渲染 SVG。

# INSTALL

```apt: sudo apt install pdf2svg```

```dnf: sudo dnf install pdf2svg```

```pacman: sudo pacman -S pdf2svg```

```zypper: sudo zypper install pdf2svg```

```brew: brew install pdf2svg```

```nix: nix profile install nixpkgs#pdf2svg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[inkscape](/man/inkscape)(1), [pdftohtml](/man/pdftohtml)(1), [rsvg-convert](/man/rsvg-convert)(1)
