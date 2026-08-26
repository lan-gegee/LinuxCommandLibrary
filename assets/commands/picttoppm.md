# TAGLINE

将 Macintosh PICT 图像转换为 PPM

# TLDR

**将 Macintosh PICT 文件转换为 PPM**

```picttoppm [input.pict] > [output.ppm]```

**以完整分辨率输出进行转换**

```picttoppm -fullres [input.pict] > [output.ppm]```

**转换时输出详细的诊断信息**

```picttoppm -verbose [input.pict] > [output.ppm]```

**转换没有 512 字节文件头的 PICT 文件**

```picttoppm -noheader [input.pict] > [output.ppm]```

# SYNOPSIS

**picttoppm** [_options_] [_file_]

# PARAMETERS

**-verbose** _n_
> 打印关于 PICT 文件和转换过程的诊断信息。详细程度为 0 到 2 级。

**-fullres**
> 强制图像保留完整分辨率而不是被缩小。禁用除图像之外的所有 PICT 操作。

**-noheader**
> 不假定文件的前 512 字节是文件头。适用于未存储在 PICT 文件数据分支（data fork）中的 PICT 数据。

**-quickdraw**
> 只执行纯 QuickDraw 操作。禁用对特殊 PostScript 打印机操作的解析。

**-fontdir** _file_
> 指定一个包含 BDF 字体的文件，供绘制文本时使用。

# DESCRIPTION

**picttoppm** 读取 Macintosh PICT 文件（版本 1 或 2）并输出 PPM 图像。PICT 是经典 Mac OS 的原生图形格式，以 QuickDraw 命令编码。属于 Netpbm 工具集。

# INSTALL

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ppmtopict](/man/ppmtopict)(1), [macptopbm](/man/macptopbm)(1)
