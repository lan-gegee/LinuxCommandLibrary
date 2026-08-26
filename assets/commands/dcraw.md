# TAGLINE

通用 RAW 相机图像解码器

# TLDR

**以默认设置将 RAW 转换为 PPM**

```dcraw [image.raw]```

**转换为 16 位线性 TIFF**

```dcraw -T -4 [image.raw]```

**提取内嵌的 JPEG 缩略图**

```dcraw -e [image.raw]```

**使用自动白平衡转换**

```dcraw -a [image.raw]```

**使用相机白平衡转换**

```dcraw -w [image.raw]```

**输出到 stdout 为 PPM**

```dcraw -c [image.raw] > [output.ppm]```

**半尺寸输出**（更快，噪点更少）

```dcraw -h [image.raw]```

# SYNOPSIS

**dcraw** [_options_] _rawfile_...

# PARAMETERS

**-c**
> 写入 stdout。

**-e**
> 提取内嵌缩略图。

**-T**
> 输出 TIFF 而非 PPM。

**-4**
> 线性 16 位，无伽马曲线。

**-6**
> 带伽马曲线的 16 位输出。

**-w**
> 使用相机白平衡。

**-a**
> 根据整幅图像计算白平衡。

**-W**
> 不自动提亮图像。

**-h**
> 半尺寸输出（2x2 像素取平均）。

**-q** _n_
> 插值质量（0-3）。

**-o** _n_
> 输出色彩空间（0=raw、1=sRGB、2=AdobeRGB 等）。

**-v**
> 详细输出。

**-i**
> 仅识别文件，不解码。

# DESCRIPTION

**dcraw** 是一个通用 RAW 图像解码器，可将各厂商专有的相机 RAW 格式转换为标准 PPM 或 TIFF 图像。它支持来自所有主要制造商的数百种相机型号。

该工具执行去马赛克（将拜耳阵列转换为全彩）、白平衡、伽马校正和色彩空间转换。输出可以是 8 位或 16 位、线性或经伽马校正，取决于预期用途。

dcraw 常被其他应用程序（GIMP、digiKam）用作后端，或用于批处理流水线。其可预测、一致的行为使其在重视可复现性的自动化处理中很有价值。

# CAVEATS

开发已放缓（最后一次重大更新是 2018 年）；部分较新的相机可能不受支持。如需持续维护的替代品，可以考虑 libraw 或 RawTherapee。输出质量可能不及相机厂商专用软件。某些 RAW 特性（镜头校正、专有算法）未被复现。

# HISTORY

dcraw 由 **Dave Coffin** 自 **1997 年**开始编写，最初只是为了解码他自己相机的 RAW 文件。通过逆向工程工作，它逐步支持了几乎所有相机制造商的格式。该软件成为开源摄影领域的基石，早在厂商提供支持之前多年就使 Linux 上的 RAW 处理成为可能。Dave Coffin 以个人项目的形式维护它超过 20 年。

# INSTALL

```apt: sudo apt install dcraw```

```dnf: sudo dnf install dcraw```

```pacman: sudo pacman -S dcraw```

```zypper: sudo zypper install dcraw```

```brew: brew install dcraw```

```nix: nix profile install nixpkgs#dcraw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[exiftool](/man/exiftool)(1)
