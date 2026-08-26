# TAGLINE

仅用 CPU 对截图、图片、PDF 和网页进行 OCR

# TLDR

**对本地图片 OCR**，结果保存为 ./textsnaps/ 下的文本文件

```textsnap [path/to/image.png]```

**对 URL 上的图片 OCR**

```textsnap [https://example.com/image.png]```

**对网页 OCR**（先渲染页面，再提取文本）

```textsnap [https://example.com/article]```

**对剪贴板中已有的图片 OCR**，无需参数

```textsnap```

**将输出写入指定文件**

```textsnap [image.png] -o [out.txt]```

**去除 Markdown**，只输出纯文本

```textsnap [image.png] --plaintext```

**将解码器限制**在 1024 个生成 token 以内

```textsnap [image.png] --max-tokens 1024```

**使用自定义的本地模型目录**

```textsnap [image.png] --model-dir [path/to/model]```

**在 stderr 显示进度诊断信息**

```textsnap -v [image.png]```

# SYNOPSIS

**textsnap** [_options_] [_FILE_|_URL_]

# PARAMETERS

**-o**, **--output** _PATH_
> 将 OCR 文本写入 _PATH_。默认：**./textsnaps/_name_\_ocr.txt**。

**-v**, **--verbose**
> 将进度诊断信息打印到 stderr。

**--plaintext**
> 将默认的 Markdown 输出转换为纯文本（无表格、无标题）。

**--model-dir** _PATH_
> 使用 _PATH_ 中的 ONNX 模型文件，而不是缓存下载的模型。

**--max-tokens** _N_
> 将解码器限制为最多生成 _N_ 个 token（默认 **2048**）。

**--max-pixels** _N_
> 将每张图片视觉编码器的像素预算限制为 _N_。

**--no-verify**
> 跳过对已下载模型文件的 SHA-256 校验。

**--generate-checksums**
> 重新下载模型并重写校验和清单。

# DESCRIPTION

**textsnap** 是一款命令行 OCR 工具，基于导出为 ONNX 的 **PaddleOCR-VL-1.5** 视觉语言模型构建。它从文件路径、URL 或系统剪贴板读取图片，把识别出的文本写入 **./textsnaps/** 目录下的文件，并只在 stdout 上打印输出路径，因此可以顺畅地融入 shell 管道。

该模型完全在 CPU 上运行，无需 GPU、无需调用云端。默认输出为 Markdown，以保留表格、标题和列表等结构；**--plaintext** 会将其扁平化，供只需要原始文本的调用者使用。网页 URL 会先渲染再进行 OCR，这使该工具可以作为"截图转文本"管道，处理那些难以直接复制的内容。

# INPUT MODES

**无参数**
> 从系统剪贴板读取图片。OCR 文本也会被复制回剪贴板。

**本地文件**
> 处理本地图片。支持的格式：PNG、JPG、JPEG、WebP、BMP、GIF、TIFF。

**图片 URL**
> 获取远程图片并进行 OCR。

**网页 URL**
> 渲染页面并对得到的截图进行 OCR。

# CONFIGURATION

**~/.cache/textsnap/**
> 首次使用时下载的 ONNX 模型文件缓存（约 **890 MB**）。包含视觉编码器（q4 量化）、自回归解码器（q4 量化）、token 嵌入（fp32），以及一个 **model_checksums.sha256** 清单。

**./textsnaps/**
> 默认输出目录，首次运行时在当前工作目录创建。

**TEXTSNAP_DECODE_THREADS**
> 覆盖解码器线程数的环境变量。默认为物理核心数。

# CAVEATS

首次运行会下载模型包（约 890 MB），请预留初始等待时间和磁盘空间。该工具仅使用 CPU，因此大图片或长 PDF 的 OCR 比 GPU 方案耗时更长。网页 OCR 需要软件包提供的可用无头浏览器组件。

# HISTORY

**textsnap** 由 **kouhxp** 于 2026 年以 MIT 许可证发布。内置模型 **PaddleOCR-VL-1.5** 由 **PaddlePaddle** 以 Apache-2.0 许可证发布。该 CLI 通过 PyPI 分发，依赖 **onnxruntime** 和 **huggingface_hub**。

# SEE ALSO

[tesseract](/man/tesseract)(1), [pdftotext](/man/pdftotext)(1), [imagemagick](/man/imagemagick)(1), [curl](/man/curl)(1)
