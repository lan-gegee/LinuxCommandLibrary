# TAGLINE

从 PDF 制作海报

# TLDR

**将 A1 原稿制作为打印在 A4 页面上的 A3 海报**

```pdfposter -p a3 -m a4 [input.pdf] [output.pdf]```

**将输入放大 4 倍**

```pdfposter -s 4 [input.pdf] [output.pdf]```

**以 A4 纸张输出 A0 海报**

```pdfposter -p a0 -m a4 [input.pdf] [output.pdf]```

**使用自定义纸张尺寸（含边距）**

```pdfposter -m 160x247mm [input.pdf] [output.pdf]```

**预览而不写出输出（试运行）**

```pdfposter -n -p 2xa4 [input.pdf] [output.pdf]```

# SYNOPSIS

**pdfposter** [_options_] _infile_ _outfile_

# PARAMETERS

**-p** _BOX_, **--poster-size** _BOX_
> 目标海报尺寸（例如 `a0`、`2xa4`、`30x40cm`）。

**-s** _NUMBER_, **--scale** _NUMBER_
> 应用于输入的线性缩放系数。

**-m** _BOX_, **--media-size** _BOX_
> 输出介质（页面）尺寸（默认：A4）。

**-A**, **--art-box**
> 对输入页面使用 ArtBox 而非 TrimBox。

**-n**, **--dry-run**
> 显示将要执行的操作而不写出输出。

**-v**, **--verbose**
> 详细输出（重复使用可获得更多信息）。

**--help-media-names**
> 列出可识别的介质与距离名称。

**--version**
> 显示版本信息。

# DESCRIPTION

**pdfposter** 对 PDF 文档进行缩放和平铺，使单页内容可以打印在多张纸上并拼合成大幅海报。

期望的输出尺寸通过 **-p**/**--poster-size** 或直接的 **-s**/**--scale** 系数定义；**-m**/**--media-size** 选择平铺块渲染所用的纸张。支持许多标准介质名称（A4、A3、Letter 等），也接受 `10x15cm` 或 `160x247mm` 这样的显式距离。

仅使用输入的第一页。程序会计算所需的平铺块数量并写出一个多页 PDF，这些页面打印拼接后即可还原缩放后的原稿。

# CAVEATS

基于 pypdf/PyPDF2 构建的 Python 工具。仅对输入的第一页进行平铺。如需预选页面，请配合 `pdfjam` 或 `pdftk` 使用。

# HISTORY

**pdfposter** 由 **Hartmut Goebel** 编写，作为作用于 PostScript 的 `poster`(1) 的 Python 替代品。自 2000 年代中期起已被各大 Linux 发行版收录。

# INSTALL

```apk: sudo apk add pdfposter```

```zypper: sudo zypper install pdfposter```

```nix: nix profile install nixpkgs#pdfposter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdfjam](/man/pdfjam)(1), [poster](/man/poster)(1), [pdfnup](/man/pdfnup)(1), [pdftk](/man/pdftk)(1)
