# TAGLINE

将 PAM 图像转换为 PNG 格式

# TLDR

**将 PAM 转换为 PNG**

```pamtopng [input.pam] > [output.png]```

**以最大压缩级别转换**

```pamtopng -compression [9] [input.pam] > [output.png]```

**创建交错式 PNG**

```pamtopng -interlace [input.pam] > [output.png]```

**转换并设置透明色**

```pamtopng -transparent [white] [input.pam] > [output.png]```

# SYNOPSIS

**pamtopng** [_options_] [_file_]

# PARAMETERS

**-compression** _n_
> 压缩级别（0-9，默认为 6）。

**-interlace**
> 创建交错（Adam7）PNG，以便渐进式加载。

**-transparent** _color_
> 设置完全透明的颜色。

**-background** _color_
> 用于 Alpha 混合的背景颜色。

**-gamma** _value_
> 图像的伽马值。

**-srgbintent** _intent_
> sRGB 渲染意图：absolute、relative、perceptual 或 saturation。

**-text** _file_
> 从文本文件添加 tEXt 块。

**-verbose**
> 向标准错误打印详细的进度信息。

# DESCRIPTION

**pamtopng** 将 Netpbm 的 PAM 图像转换为 PNG 格式。对于带 Alpha 通道的图像，它是比 **pnmtopng** 更值得选用的工具，因为它能正确处理 PAM 原生的 Alpha 支持。属于 Netpbm 工具集。

输入从指定文件或标准输入读取。输出写入标准输出。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pngtopam](/man/pngtopam)(1), [pnmtopng](/man/pnmtopng)(1)
