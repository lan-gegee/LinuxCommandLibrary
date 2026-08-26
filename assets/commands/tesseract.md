# TAGLINE

开源光学字符识别引擎

# TLDR

**从图片提取文本**

```tesseract [image.png] [output]```

**提取到 stdout**

```tesseract [image.png] stdout```

**指定语言**

```tesseract -l [deu] [image.png] [output]```

**多种语言**

```tesseract -l [eng+fra] [image.png] [output]```

**输出为 PDF**

```tesseract [image.png] [output] pdf```

**输出为 hOCR**（带坐标的 HTML）

```tesseract [image.png] [output] hocr```

**输出为 TSV**

```tesseract [image.png] [output] tsv```

**列出可用语言**

```tesseract --list-langs```

# SYNOPSIS

**tesseract** _imagename_ _outputbase_ [_-l lang_] [_--psm mode_] [_--oem mode_] [_configfiles_]

# PARAMETERS

**-l** _LANG_
> OCR 使用的语言（eng、deu、fra 等）。

**--psm** _NUM_
> 页面分割模式（0-13）。

**--oem** _NUM_
> OCR 引擎模式（0=旧式、1=LSTM、2=两者）。

**--dpi** _NUM_
> 覆盖图片 DPI。

**-c** _VAR=VALUE_
> 设置配置变量。

**--tessdata-dir** _PATH_
> 语言数据的存放位置。

**--user-words** _FILE_
> 用户词表。

**--user-patterns** _FILE_
> 用户模式文件。

**--list-langs**
> 列出可用语言。

**--print-parameters**
> 打印配置参数。

**pdf**
> 输出可搜索 PDF。

**hocr**
> 输出带坐标的 HTML。

**tsv**
> 输出制表符分隔值。

**alto**
> 输出 ALTO XML。

# DESCRIPTION

**Tesseract** 是一个开源 OCR（光学字符识别）引擎。它从图片中提取文本，支持超过 100 种语言。

LSTM 神经网络引擎（默认）对大多数文本比旧式引擎准确率更高。通过引擎模式选择（--oem）可以切换或组合引擎。

页面分割模式（--psm）告诉 Tesseract 预期内容：单个字符、单词、行、块还是整页。选择正确的模式能显著提高准确率。

输出格式包括纯文本、可搜索 PDF（图像上的文本层）、hOCR（带边界框的 HTML）、TSV（逐词详细数据）和 ALTO（XML 归档格式）。

图片质量对结果影响很大。最佳效果来自：高分辨率（300+ DPI）、良好的对比度、端正的对齐、尽量少的噪点。使用 ImageMagick 或类似工具做预处理会有帮助。

语言数据文件（traineddata）必须单独安装。通过自定义训练可以为特定字体、历史文献或专门文本创建模型。

# CONFIGURATION

**TESSDATA_PREFIX**
> 指定语言数据文件（traineddata）所在目录的环境变量；默认为 Tesseract 安装目录内的 tessdata 目录

**--tessdata-dir** _PATH_
> 在命令行覆盖语言数据目录的位置

# CAVEATS

准确率随图片质量而变化。复杂版面可能无法正确分割。手写识别能力有限。自定义训练需要大量投入。语言数据文件较大。处理速度取决于图片尺寸和复杂度。

# HISTORY

**Tesseract** 于 **1985** 至 **1994** 年间在 HP 实验室开发，随后于 **2005** 年开源。Google 接手开发，并于 **2016** 年加入 LSTM 神经网络支持（4.0 版）。它至今仍是最广泛使用的开源 OCR 引擎，已集成到众多应用和工作流中。

# INSTALL

```apt: sudo apt install tesseract-ocr```

```dnf: sudo dnf install tesseract```

```pacman: sudo pacman -S tesseract```

```apk: sudo apk add tesseract-ocr```

```zypper: sudo zypper install tesseract-ocr```

```brew: brew install tesseract```

```nix: nix profile install nixpkgs#tesseract```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ocrmypdf](/man/ocrmypdf)(1), [imagemagick](/man/imagemagick)(1), [pdftoppm](/man/pdftoppm)(1)
