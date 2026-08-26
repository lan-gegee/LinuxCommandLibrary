# TAGLINE

通过将页面重排为打印拼版，从 PDF 文件创建可打印的小册子

# TLDR

以合理的默认值创建名为 file-book.pdf 的**小册子**

```pdfbook2 [path/to/file.pdf]```

创建 **paper size** 设为 A4 的小册子

```pdfbook2 -p a4paper [path/to/file.pdf]```

创建**内侧边距**缩减为 50 像素的小册子

```pdfbook2 -p a4paper -i 50 [path/to/file.pdf]```

用**印帖**整理大文件以便装订

```pdfbook2 -p a4paper --signature 24 [path/to/file.pdf]```

# SYNOPSIS

**pdfbook2** [_options_] _file.pdf_

# PARAMETERS

**-p**, **--paper** _size_
> 设置纸张大小（a4paper、letterpaper 等）

**-s**, **--short-edge**
> 使用短边装订（默认为长边）

**-n**, **--no-crop**
> 重新拼版前不裁剪页面

**-o**, **--outer-margin** _pixels_
> 设置外侧边距（默认：40）

**-i**, **--inner-margin** _pixels_
> 设置内侧边距（默认：150）

**-t**, **--top-margin** _pixels_
> 设置顶部边距（默认：30）

**-b**, **--bottom-margin** _pixels_
> 设置底部边距（默认：30）

**--signature** _num_
> 每帖的页数（必须能被 4 整除）

**--signature\*** _num_
> 与 --signature 相同，但允许最后一帖不满页

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**pdfbook2** 通过将页面重排为打印拼版，从 PDF 文件创建可打印的小册子。输出专为横向模式、长边翻转的双面打印设计，最终得到可折叠装订的小册子。

对于较大的文档，signature 选项会将小册子分成更小的部分（印帖），可以嵌套后一起装订。每帖必须包含能被 4 整除的页数。

# CAVEATS

要以**横向模式**配合**长边翻转**打印才能得到正确结果。signature 值必须能被 4 整除。默认边距可能需要根据打印机能力调整。需要 pdflatex 和 pdfpages LaTeX 包。

# HISTORY

作为 pdfpages 和 pdflatex 的 Python 封装编写，用于简化小册子的制作。取代了从现有 PDF 文档制作可打印小册子的手动 LaTeX 流程。在自助出版和 zine 制作社区中很常见。

# INSTALL

```pacman: sudo pacman -S texlive-binextra```

```apk: sudo apk add texlive-binextra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdfjam](/man/pdfjam)(1), [pdfcrop](/man/pdfcrop)(1), [pdflatex](/man/pdflatex)(1)
