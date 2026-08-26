# TAGLINE

将 PBM 转换为 Microdesign MDA 格式

# TLDR

**将 PBM 转换为 Microdesign Area 格式**

```pbmtomda [input.pbm] > [output.mda]```

**反转颜色**

```pbmtomda -i [input.pbm] > [output.mda]```

**生成双倍分辨率的 MDA 输出**

```pbmtomda -d [input.pbm] > [output.mda]```

# SYNOPSIS

**pbmtomda** [**-d**] [**-i**] [_pbmfile_]

# PARAMETERS

**-d**
> 生成双倍分辨率的 MDA 输出，而不是默认的单倍分辨率。

**-i**
> 反转图像，使 PBM 中的黑色像素在 MDA 输出中变为白色。

_pbmfile_
> 输入的 PBM 文件。省略时从标准输入读取图像。

# DESCRIPTION

**pbmtomda** 读取 PBM（Portable Bitmap）图像，并以 Microdesign Area（MDA）格式写入标准输出。MDA 是基于 CP/M 的 Amstrad PCW 电脑上 Microdesign 图形程序使用的原生图形格式。输出是不带头部的原始 MDA 数据，适合粘贴到 Microdesign 文档中。

属于 Netpbm 工具集。

# CAVEATS

仅生成未压缩的 MDA 数据；要生成独立文件，必须另行添加 Microdesign 文件头。

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

[mdatopbm](/man/mdatopbm)(1), [pbmtolj](/man/pbmtolj)(1), [pbm](/man/pbm)(5)
