# TAGLINE

通过 TinyPNG API 压缩图片的 CLI 工具

# TLDR

**压缩目录中的所有图像**

```tinifier --api-key [KEY] [./images/]```

**递归压缩并使用 4 个线程**

```tinifier -t 4 -r --api-key [KEY] [./images/]```

**压缩时保留文件修改时间和 EXIF 数据**

```tinifier --preserve-time --api-key [KEY] [photo.png]```

**只压缩特定扩展名的文件**

```tinifier --api-key [KEY] --ext [png,webp] [./images/]```

**跳过体积缩减不足 5% 的文件**

```tinifier --api-key [KEY] --skip-if-diff-less [5] [./images/]```

**保留原始文件与压缩版本并存**

```tinifier --api-key [KEY] --keep-original-file [./images/]```

# SYNOPSIS

**tinifier** [_options_] _path_...

# PARAMETERS

**-k**, **--api-key** _KEY_
> TinyPNG API 密钥。可提供多个密钥并以逗号分隔，超出配额时自动切换。

**-t**, **--threads** _N_
> 并行线程数（默认：16）。

**-r**, **--recursive**
> 递归搜索所列目录中的文件。

**-e**, **--ext** _EXTENSIONS_
> 要压缩的文件扩展名（默认：png,jpeg,jpg,webp,avif）。

**-p**, **--preserve-time**
> 保留原始文件的修改日期/时间，包括 EXIF 数据。

**--keep-original-file**
> 在压缩文件旁边保留未压缩的原始文件。

**--skip-if-diff-less** _N_
> 若压缩节省的空间小于 N 百分比则跳过该文件（默认：1）。

**--max-errors** _N_
> 停止前允许的最大错误数（默认：10，0 表示不限制）。

**--retry-attempts** _N_
> 操作的重试次数（默认：3）。

**--delay-between-retries** _DURATION_
> 重试之间的延迟（默认：1s）。

**-c**, **--config-file** _PATH_
> 配置文件路径。

# DESCRIPTION

**tinifier** 使用 TinyPNG API 并行压缩图像。它支持 PNG、JPEG、WebP 和 AVIF 文件。可以提供多个 API 密钥，在配额用尽时自动切换。该工具支持递归扫描目录，并可根据需要保留原始文件元数据。

# CAVEATS

需要 TinyPNG API 密钥（免费层：每月 500 次压缩）。文件会上传到 TinyPNG 服务器进行压缩。需要网络连接。

# HISTORY

**tinifier** 由 **tarampampam** 创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S tinifier```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[optipng](/man/optipng)(1), [jpegoptim](/man/jpegoptim)(1), [pngquant](/man/pngquant)(1), [imagemagick](/man/imagemagick)(1)
