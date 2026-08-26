# TAGLINE

面向 JPEG 和 PNG 文件的快速命令行图像缩放与旋转工具

# TLDR

将图像或目录**缩放**到指定分辨率

```imgp -x [1366x1000] [path/to/directory] [path/to/file]```

按百分比**缩放**图像并覆盖源文件

```imgp -x [75] -w [path/to/file]```

将图像**顺时针旋转** 90 度

```imgp -o [90] [path/to/file]```

# SYNOPSIS

**imgp** [_options_] [_paths_]

# PARAMETERS

**-x**, **--res** _RES_
> 目标分辨率（WxH）或缩放百分比

**-o**, **--rotate** _DEGREES_
> 顺时针旋转图像（90、180、270）

**-w**, **--overwrite**
> 覆盖源图像

**-q**, **--quality** _VALUE_
> JPEG 质量（1-95，默认 75）

**-n**, **--enlarge**
> 允许放大图像

**-e**, **--erase**
> 移除 EXIF 元数据

**-c**, **--convert**
> 在 PNG 和 JPEG 之间转换

# DESCRIPTION

**imgp** 是一款快速的命令行图像缩放与旋转工具，适用于 JPEG 和 PNG 文件。它可以处理单个文件或整个目录，使批量操作非常高效。

该工具在缩放时默认保持宽高比，并可并行处理图像以提升性能。它会保留 EXIF 方向元数据，同时支持基于百分比的缩放和绝对分辨率目标。

# CAVEATS

仅支持 JPEG 和 PNG 格式。默认创建新文件而不是覆盖。超大批量操作可能消耗较多内存。

# HISTORY

imgp 由 Arun Prakash Jana 创建，是其高效命令行工具集的一员。它的设计目标是提供快速、可脚本化的图像处理能力，而无需面对 ImageMagick 这类大型工具的复杂性。

# INSTALL

```dnf: sudo dnf install imgp```

```zypper: sudo zypper install imgp```

```brew: brew install imgp```

```nix: nix profile install nixpkgs#imgp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[convert](/man/convert)(1), [mogrify](/man/mogrify)(1), [jpegtran](/man/jpegtran)(1)
