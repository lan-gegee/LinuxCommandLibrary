# TAGLINE

将 PostScript 文件转换为 PDF 格式

# TLDR

**将 PS 转换为 PDF**

```ps2pdf [input.ps] [output.pdf]```

**以指定的质量设置转换**

```ps2pdf -dPDFSETTINGS=/prepress [input.ps] [output.pdf]```

**为屏幕查看优化转换**

```ps2pdf -dPDFSETTINGS=/screen [input.ps] [output.pdf]```

**将 EPS 转换为 PDF**

```ps2pdf [input.eps] [output.pdf]```

# SYNOPSIS

**ps2pdf** [_options_] _input.ps_ [_output.pdf_]

# DESCRIPTION

**ps2pdf** 使用 Ghostscript 将 PostScript 文件转换为 PDF 格式。它是 gs（Ghostscript）的便捷封装，带有 PDF 输出选项。

该工具常用于文档处理流水线和打印工作流。

# PARAMETERS

**-dPDFSETTINGS=** _setting_
> 质量预设：
> - /screen：低分辨率
> - /ebook：中等分辨率
> - /printer：高分辨率
> - /prepress：最高分辨率

**-dCompatibilityLevel=** _level_
> PDF 版本（1.3、1.4、1.5 等）。

**-dEmbedAllFonts=** _bool_
> 嵌入所有字体。

**-dSubsetFonts=** _bool_
> 对嵌入字体做子集化。

**-sPAPERSIZE=** _size_
> 纸张尺寸（a4、letter 等）。

# CAVEATS

输出质量取决于输入。嵌入字体会增大体积。部分 PS 特性可能无法转换。需要安装 Ghostscript。

# HISTORY

**ps2pdf** 是 **Ghostscript** 的一部分，后者由 **L. Peter Deutsch** 于 **1988 年**创建。Ghostscript 提供 PostScript 和 PDF 解释功能，使 ps2pdf 成为标准的转换工具。

# INSTALL

```apt: sudo apt install ghostscript```

```dnf: sudo dnf install ghostscript```

```pacman: sudo pacman -S ghostscript```

```apk: sudo apk add ghostscript```

```zypper: sudo zypper install ghostscript```

```brew: brew install ghostscript```

```nix: nix profile install nixpkgs#ghostscript```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gs](/man/gs)(1), [pdf2ps](/man/pdf2ps)(1), [epstopdf](/man/epstopdf)(1), [pdflatex](/man/pdflatex)(1)
