# TAGLINE

将 PNG 图像转换为 PAM 格式

# TLDR

**将 PNG 转换为 PAM**

```pngtopam [input.png] > [output.pam]```

**转换时保留 Alpha 通道**

```pngtopam -alpha [input.png] > [output.pam]```

# SYNOPSIS

**pngtopam** [_options_] [_file_]

# PARAMETERS

**-alphapam**
> 输出元组类型由该 PNG 决定的 PAM（支持透明度）。

**-alpha**
> 仅提取 Alpha 通道，输出为 PGM 风格的 PAM。

**-mix**
> 当存在透明度时，将图像与背景色合成。

**-background** _color_
> 指定与 -mix 搭配使用的背景色（例如 "rgb:FF/FF/FF" 或颜色名称）。

**-gamma** _value_
> 设置用于显示校正的 Gamma 值。

**-text**
> 将 PNG 中的 tEXt 数据块输出到标准错误。

**-verbose**
> 将有关转换过程的信息打印到标准错误。

# DESCRIPTION

**pngtopam** 将 PNG 图像转换为 PAM（Portable Arbitrary Map，便携式任意映射）图像。它是 Netpbm 工具集的一部分，在指定 **-alphapam** 时可保留透明度。如果输入不含透明度，输出通常是 RGB 或灰度 PAM。

# CAVEATS

未给出文件时从标准输入读取。若不使用 **-alphapam** 或 **-alpha**，透明信息可能丢失。对于需要 Alpha 通道支持的图像，它取代了较旧的 **pngtopnm**。

# HISTORY

属于 **Netpbm** 软件包，其渊源可追溯至 Jef Poskanzer 在 20 世纪 80 年代末开发的 pbmplus。PAM 在 Netpbm 10.x 中引入，用于统一处理 PBM/PGM/PPM/PAM。

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

[pamtopng](/man/pamtopng)(1), [pngtopnm](/man/pngtopnm)(1), [pnmtopng](/man/pnmtopng)(1)
