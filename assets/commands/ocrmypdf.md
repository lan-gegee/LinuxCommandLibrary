# TAGLINE

为扫描版 PDF 添加 OCR 文本层，使其可搜索、可选择

# TLDR

**为 PDF 添加 OCR 层**

```ocrmypdf [input.pdf] [output.pdf]```

**OCR 并纠正倾斜**

```ocrmypdf --deskew [input.pdf] [output.pdf]```

**OCR 并清理背景**

```ocrmypdf --clean [input.pdf] [output.pdf]```

**指定语言**

```ocrmypdf -l [deu] [input.pdf] [output.pdf]```

**多语言 OCR**

```ocrmypdf -l [eng+fra] [input.pdf] [output.pdf]```

**即使已有文本也强制 OCR**

```ocrmypdf --force-ocr [input.pdf] [output.pdf]```

**跳过已有文本的页面**

```ocrmypdf --skip-text [input.pdf] [output.pdf]```

**优化并减小体积**

```ocrmypdf --optimize [3] [input.pdf] [output.pdf]```

# SYNOPSIS

**ocrmypdf** [_-l lang_] [_--deskew_] [_--clean_] [_--force-ocr_] [_--optimize level_] [_options_] _input.pdf_ _output.pdf_

# PARAMETERS

**-l** _LANG_, **--language** _LANG_
> OCR 语言（Tesseract 语言代码）。

**--deskew**
> 在 OCR 前纠正页面倾斜。

**--clean**
> 在 OCR 前清理页面背景。

**--clean-final**
> 清理页面并将清理后的图像保留在输出中。

**--rotate-pages**
> 旋转页面以修正方向。

**--remove-background**
> 移除页面背景。

**--force-ocr**
> 对所有页面进行 OCR，替换已有文本。

**--skip-text**
> 跳过已有文本的页面。

**--redo-ocr**
> 对已有文本的页面重新进行 OCR。

**--optimize** _LEVEL_
> 优化输出（0=关闭，1-3 逐级增强）。

**--output-type** _TYPE_
> 输出类型：pdf、pdfa、pdfa-1、pdfa-2、pdfa-3。

**--pdfa-image-compression** _TYPE_
> 压缩方式：jpeg、lossless（无损）。

**-j** _NUM_, **--jobs** _NUM_
> 并行任务数。

**--image-dpi** _DPI_
> 无元数据图像的 DPI。

**-q**, **--quiet**
> 抑制输出。

**-v**, **--verbose** [_LEVEL_]
> 详细输出（0-2）。

**--sidecar** _FILE_
> 将 OCR 文本写入 sidecar 文件。

# DESCRIPTION

**ocrmypdf** 为扫描版 PDF 添加 OCR 文本层，使其可搜索、可选择。它使用 Tesseract OCR，默认输出适合归档质量的 PDF/A。

该工具在扫描图像的背后添加不可见文本，同时保留原始视觉效果。也就是说，文件看起来一模一样，但其中的文本可以被复制、搜索和建立索引。

图像预处理可以提高 OCR 准确率：deskew 纠正倾斜的扫描页，clean 去除噪点和瑕疵，rotate-pages 修正页面方向。对于低质量扫描件，这些选项能显著改善结果。

多种语言可以组合使用（eng+fra+deu）。必须先安装对应的 Tesseract 语言包。除非强制执行，否则该工具会检测已有文本以避免重复处理。

优化级别通过重新压缩图像来减小文件体积。级别 3 使用激进的 JBIG2 压缩，适合归档用途。PDF/A 输出确保长期可读性。

并行处理可以加速多页文档的处理。默认显示进度。sidecar 输出只提取文本，便于外部程序进一步处理。

# CAVEATS

OCR 准确率取决于扫描质量。分辨率过低或压缩严重的图像可能产生较差的结果。语言包需要单独安装。部分复杂版式可能无法很好地完成 OCR。转换为 PDF/A 可能丢失某些特性。处理大型 PDF 需要较多内存。

# HISTORY

**ocrmypdf** 由 **James R. Barlow** 自 **2013** 年前后开始开发。它在 Tesseract OCR 之上封装了智能 PDF 处理、图像预处理和 PDF/A 输出。该项目旨在提供让扫描版 PDF 可搜索的完整方案，把过去需要手动多步操作的流程自动化。

# INSTALL

```dnf: sudo dnf install ocrmypdf```

```apk: sudo apk add ocrmypdf```

```brew: brew install ocrmypdf```

```nix: nix profile install nixpkgs#ocrmypdf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tesseract](/man/tesseract)(1), [pdftk](/man/pdftk)(1), [pdfimages](/man/pdfimages)(1), [img2pdf](/man/img2pdf)(1)
