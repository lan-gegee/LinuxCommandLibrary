# TAGLINE

将图像转换为 PDF 且不重新编码，保留原始图像数据

# TLDR

**将图像转换为 PDF**

```img2pdf [image1.jpg] [image2.png] -o [output.pdf]```

**转换目录中的所有图像**

```img2pdf [*.jpg] -o [output.pdf]```

**将页面尺寸设为 A4**

```img2pdf --pagesize [A4] [image.jpg] -o [output.pdf]```

**在保持宽高比的前提下使图像适配页面**

```img2pdf --fit [into] --pagesize [A4] [image.jpg] -o [output.pdf]```

**设置特定的图像尺寸**

```img2pdf --imgsize [150mmx100mm] [image.jpg] -o [output.pdf]```

**以自定义页边距进行转换**

```img2pdf --border [1cm:1cm] [image.jpg] -o [output.pdf]```

**设置 PDF 标题和作者**

```img2pdf --title "[Document Title]" --author "[Author Name]" [image.jpg] -o [output.pdf]```

**输出符合 PDF/A-1b 标准的文档**

```img2pdf --pdfa [image.jpg] -o [output.pdf]```

**从 stdin 管道传入图像**

```cat [image.jpg] | img2pdf -o [output.pdf]```

# SYNOPSIS

**img2pdf** [_options_] [_images ..._] **-o** _output.pdf_

# PARAMETERS

**-o**, **--output** _file_
> 输出的 PDF 文件（必需）。

**--pagesize** _size_
> 页面尺寸：A4、Letter、Legal 或 WxH（例如 210mmx297mm）。

**--imgsize** _LxL_
> 图像在 PDF 页面上的尺寸：带单位的 WxH（例如 150mmx100mm）。

**--fit** _mode_
> 适配模式：into、fill、exact、shrink、enlarge。

**--border** _margin_
> 页面边框/边距（例如 1cm、1cm:2cm）。

**--rotation** _angle_
> 旋转页面：auto、none、ifvalid、0、90、180、270。

**--title** _string_
> PDF 标题元数据。

**--author** _string_
> PDF 作者元数据。

**--subject** _string_
> PDF 主题元数据。

**--keywords** _string_
> PDF 关键词元数据。

**--creationdate** _date_
> PDF 创建日期。

**--moddate** _date_
> PDF 修改日期。

**--viewer-panes** _panes_
> 阅读器初始窗格：outlines（大纲）、thumbs（缩略图）。

**--viewer-initial-page** _n_
> 初始显示的页面。

**--viewer-fullscreen**
> 以全屏模式打开。

**-D**, **--nodate**
> 不写入时间戳，以获得确定性输出。

**-S**, **--colorspace** _space_
> 强制指定色彩空间：RGB、L（灰度）。

**-a**, **--auto-orient**
> 使页面方向与输入图像一致。

**--pdfa**
> 输出符合 PDF/A-1b 标准的文档。

**--first-frame-only**
> 仅转换多帧图像的第一帧（例如动画 GIF、多页 TIFF）。

**--pillow-limit-break**
> 禁用 Pillow 的解压炸弹大小限制，以便处理超大图像。

**--from-file** _FILE_
> 从 FILE 读取输入图像列表（以 NUL 分隔的路径）。

**-v**, **--verbose**
> 启用详细模式，向标准错误打印消息。

# DESCRIPTION

**img2pdf** 将图像转换为 PDF 且不重新编码，从而保留原始图像质量。与会对图像栅格化的工具不同，img2pdf 将原始 JPEG、PNG、TIFF 或其他图像数据直接嵌入到 PDF 结构中。

这种无损方式意味着一个 5MB 的 JPEG 会变成约 5MB 的 PDF（外加极少的 PDF 结构开销），且没有任何质量损失。而重新编码的工具要么损失质量，要么在同等质量下生成大得多的文件。

支持的输入格式包括 JPEG、JPEG2000、PNG（含透明度）、TIFF、GIF 等。该工具会自动处理色彩空间、位深和多页 TIFF。

页面尺寸设置提供灵活选项：自然图像尺寸（按指定 DPI）、配合适配模式的固定页面尺寸，或显式指定的尺寸。适配模式控制图像的放置方式：**into** 在页面内完整容纳，**fill** 填满页面（可能裁剪），**exact** 拉伸到精确尺寸，**shrink** 只缩小较大的图像，**enlarge** 只放大较小的图像。

多张图像会按参数顺序组成多页 PDF。通过 stdin 管道传入输入可便于与图像处理流水线集成。

# CAVEATS

仅适用于栅格图像（不支持矢量格式）。某些阅读器可能难以处理大型嵌入图像。并非所有 PDF 特性都受支持（不支持加密，压缩控制有限）。Pillow 默认限制输入图像的大小；可使用 **--pillow-limit-break** 覆盖此限制。

# HISTORY

**img2pdf** 由 Johannes Schauer Marin Rodrigues 创建，旨在解决将图像转换为 PDF 时避免质量损失的常见问题。ImageMagick 等现有工具会重新编码图像，导致质量下降或文件体积膨胀。该工具用 Python 编写，并以 pip 包形式发布。

# INSTALL

```pacman: sudo pacman -S img2pdf```

```apk: sudo apk add py3-img2pdf```

```brew: brew install img2pdf```

```nix: nix profile install nixpkgs#img2pdf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[convert](/man/convert)(1), [pdftk](/man/pdftk)(1), [pdfunite](/man/pdfunite)(1), [tesseract](/man/tesseract)(1)
