# TAGLINE

光学字符识别程序

# TLDR

**对图像进行 OCR 识别**

```gocr [image.pbm]```

**设置识别模式**

```gocr -m [mode] [image.pbm]```

**输出到文件**

```gocr -o [output.txt] [image.pbm]```

**设置字符过滤**

```gocr -C "[a-zA-Z0-9]" [image.pbm]```

# SYNOPSIS

**gocr** [_options_] _image_

# PARAMETERS

_IMAGE_
> 要处理的图像文件。

**-o** _FILE_
> 输出文件。

**-m** _MODE_
> 识别模式。

**-C** _CHARS_
> 预期出现的字符。

**-i** _FORMAT_
> 输入格式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gocr** 是一个光学字符识别（OCR）程序，读取图像并输出识别出的文本。它支持多种图像格式，包括 PBM、PGM、PPM，还可以针对特定字符集进行调优。

该工具通过处理扫描文档和图像来提取文字，并可通过标准输入和输出集成到文档处理流水线中。

# CAVEATS

准确率因图像质量而异。对干净的扫描件效果最佳。如需更高准确率，可以考虑 tesseract。

# HISTORY

**gocr**（又称 **JOCR**，因为 GOCR 这个名称在 SourceForge 上已被占用）由 **Jörg Schulenburg** 于 20 世纪 90 年代末创建，是一个遵循 GPL 的免费 OCR 程序。

# INSTALL

```apt: sudo apt install gocr```

```dnf: sudo dnf install gocr```

```pacman: sudo pacman -S gocr```

```zypper: sudo zypper install gocr```

```brew: brew install gocr```

```nix: nix profile install nixpkgs#gocr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tesseract](/man/tesseract)(1), [ocrmypdf](/man/ocrmypdf)(1)

# RESOURCES

```[Homepage](https://jocr.sourceforge.net/)```

<!-- verified: 2026-07-17 -->
