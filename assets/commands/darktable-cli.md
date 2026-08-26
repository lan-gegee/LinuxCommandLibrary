# TAGLINE

用于批量处理 RAW 照片的命令行界面

# TLDR

**将 RAW 文件导出为 JPEG**

```darktable-cli [input.raw] [output.jpg]```

**使用指定 XMP sidecar 导出**

```darktable-cli [input.raw] [preset.xmp] [output.jpg]```

**导出为 16 位 TIFF**

```darktable-cli [input.raw] [output.tiff] --bpp 16```

**按指定尺寸导出**

```darktable-cli [input.raw] [output.jpg] --width [1920] --height [1080]```

**导出目录中的所有 RAW 文件**

```for f in *.raw; do darktable-cli "$f" "${f%.raw}.jpg"; done```

**导出时应用样式**

```darktable-cli [input.raw] [output.jpg] --style "[style_name]"```

# SYNOPSIS

**darktable-cli** [_options_] _input_ [_xmp_] _output_

# PARAMETERS

**--width** _pixels_
> 最大输出宽度。

**--height** _pixels_
> 最大输出高度。

**--bpp** _bits_
> 每像素位数（8、16、32）。

**--hq** _true_|_false_
> 高质量重采样。

**--upscale** _true_|_false_
> 允许放大。

**--style** _name_
> 应用具名的 darktable 样式。

**--style-overwrite**
> 用样式覆盖现有历史记录。

**--out-ext** _ext_
> 输出格式扩展名（jpg、tif、png 等）。

**--core**
> 向 darktable 核心传递选项。

**--verbose**
> 启用详细输出。

# DESCRIPTION

**darktable-cli** 是 darktable 的命令行界面，无需图形界面即可批量处理 RAW 照片。它把保存在 XMP sidecar 文件中的 darktable 非破坏性编辑应用于生成最终图像。

该工具使用与 GUI 应用相同的处理引擎，确保结果完全一致。如果输入文件旁边存在同名 XMP 文件（扩展名为 .xmp），其中的编辑会被自动应用。也可以显式指定 XMP 文件。

常见用途包括批量导出已编辑的照片、自动化处理流水线、服务器端图像处理，以及从同一 RAW 文件生成不同尺寸的输出。

# CAVEATS

GPU 加速需要 OpenCL（与 GUI 相同）。单张图像的处理是单线程的；批处理时应并行调用。大 RAW 文件需要大量内存。XMP 编辑必须与所用的 darktable 版本兼容。

# HISTORY

darktable 由 **Johannes Hanika** 创建，于 **2009 年**首次发布，是一款受 Adobe Lightroom 启发的开源摄影工作流应用。CLI 接口的加入使得脚本化处理和与其他工具的集成成为可能。darktable 已成长为顶级的开源 RAW 处理应用之一。

# INSTALL

```apt: sudo apt install darktable```

```dnf: sudo dnf install darktable```

```pacman: sudo pacman -S darktable```

```apk: sudo apk add darktable```

```zypper: sudo zypper install darktable```

```nix: nix profile install nixpkgs#darktable```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rawtherapee-cli](/man/rawtherapee-cli)(1), [dcraw](/man/dcraw)(1), [exiftool](/man/exiftool)(1)
