# TAGLINE

Ghostscript PostScript 和 PDF 解释器

# TLDR

**查看** PDF 文件

```gs -dQUIET -dBATCH file.pdf```

**压缩** PDF 文件体积用于电子书

```gs -dNOPAUSE -dQUIET -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -sOutputFile=output.pdf input.pdf```

将 **PDF 转换为 JPEG** 图像

```gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=jpeg -r150 -sOutputFile=output_%d.jpg input.pdf```

将**指定页面**转换为图像

```gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=jpeg -dFirstPage=1 -dLastPage=3 -sOutputFile=page%d.jpg input.pdf```

**合并** PDF 文件

```gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=merged.pdf file1.pdf file2.pdf```

将 **PostScript 转换为 PDF**

```gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=output.pdf input.ps```

列出可用的**设备**

```gs -h```

# SYNOPSIS

**gs** [_options_] [_files_]...

# PARAMETERS

**-sDEVICE=DEVICE**
> 选择输出设备（pdfwrite、jpeg、png16m 等）

**-sOutputFile=FILE**
> 指定输出文件名（用 %d 表示页码）

**-o FILE**
> -sOutputFile=FILE 的简写，同时隐含 -dNOPAUSE 和 -dBATCH

**-r RES 或 -rXRESxYRES**
> 设置输出分辨率（DPI）

**-dPDFSETTINGS=SETTING**
> PDF 质量预设（/screen、/ebook、/printer、/prepress）

**-dNOPAUSE**
> 页面之间不暂停

**-dBATCH**
> 处理完文件后退出

**-dQUIET 或 -q**
> 抑制常规输出消息

**-dSAFER**
> 限制文件操作（默认）

**-dFirstPage=N**
> 从第 N 页开始

**-dLastPage=N**
> 处理到第 N 页为止

**-sPAPERSIZE=SIZE**
> 设置纸张大小（a4、letter、legal 等）

**-I DIRECTORIES**
> 添加库搜索路径

**-h 或 -?**
> 显示帮助和可用设备

# DESCRIPTION

**gs**（Ghostscript）是 Adobe PostScript 和 PDF 语言的解释器。它可以进行格式转换、渲染到各种输出设备，以及处理 PDF 和 PostScript 文件。

Ghostscript 广泛用于 PDF 操作，包括合并、拆分、压缩和转换为图像格式。-dPDFSETTINGS 预设控制质量与文件大小：/screen（最低）、/ebook、/printer、/prepress（最高）。

# CAVEATS

可用设备取决于所安装的 Ghostscript。使用 gs -h 查看已安装的设备。PDFSETTINGS 预设对质量和文件大小的影响很大。

# HISTORY

**Ghostscript** 自 1986 年开始开发，免费提供 PostScript 和 PDF 解释功能。它在 Linux 系统上被广泛用于 PDF 操作。

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

[ps2pdf](/man/ps2pdf)(1), [pdf2ps](/man/pdf2ps)(1), [pdftops](/man/pdftops)(1)

# RESOURCES

```[Source code](https://github.com/ArtifexSoftware/ghostpdl)```

```[Homepage](https://www.ghostscript.com/)```

```[Documentation](https://ghostscript.readthedocs.io/)```

<!-- verified: 2026-07-17 -->
