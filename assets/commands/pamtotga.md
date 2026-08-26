# TAGLINE

将 PAM/PNM 图像转换为 TGA 格式

# TLDR

**将 PAM 转换为 TGA 格式**

```pamtotga [input.pam] > [output.tga]```

**转换为颜色映射输出**

```pamtotga -cmap [input.pam] > [output.tga]```

**转换为单色**

```pamtotga -mono [input.pam] > [output.tga]```

**不使用 RLE 压缩进行转换**

```pamtotga -norle [input.pam] > [output.tga]```

**在 TGA 头部设置图像 ID**

```pamtotga -name=[label] [input.pam] > [output.tga]```

# SYNOPSIS

**pamtotga** [_options_] [_file_]

# PARAMETERS

**-mono**
> 输出单色 8 位 TGA。输入必须是 PBM、PGM，或元组类型为 BLACKANDWHITE 或 GRAYSCALE 的 PAM。

**-cmap**
> 使用调色板输出颜色映射的 TGA。输入的不同颜色不得超过 256 种，且不能有透明度。

**-cmap16**
> 类似 -cmap，但使用 16 位（每通道 5 位）的颜色映射表项而不是 24 位。

**-rgb**
> 输出 24 位非映射彩色 TGA。

**-norle**
> 禁用 RLE（行程长度编码）压缩。

**-name=**_name_
> 在 TGA 头部设置图像 ID。

**-verbose**
> 打印有关转换过程的信息。

# DESCRIPTION

**pamtotga** 将 PAM/PNM 图像转换为 TGA（Targa）格式。支持 24 位以及带 Alpha 的 32 位。默认情况下会选择约束最多、最兼容的类型（优先级：单色高于颜色映射高于非映射）。RLE 压缩默认启用。属于 Netpbm 工具集。

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

[tgatoppm](/man/tgatoppm)(1), [ppmtotga](/man/ppmtotga)(1)
