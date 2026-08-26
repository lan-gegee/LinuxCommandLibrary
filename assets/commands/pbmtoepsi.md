# TAGLINE

将 PBM 位图转换为 Encapsulated PostScript Interchange 格式

# TLDR

**将 PBM 转换为 EPSI 格式**

```pbmtoepsi [input.pbm] > [output.epsi]```

**仅输出边界框注释**（不含图像数据）

```pbmtoepsi -bbonly [input.pbm] > [output.epsi]```

以每英寸点数**指定输出分辨率**

```pbmtoepsi -dpi [300] [input.pbm] > [output.epsi]```

# SYNOPSIS

**pbmtoepsi** [_-dpi N[xN]_] [_-bbonly_] [_pbmfile_]

# PARAMETERS

**-bbonly**
> 只创建边界框注释，不包含图像预览。

**-dpi** _N[xN]_
> 输出设备的分辨率，单位为每英寸点数（默认 72）。使用 "NxM" 可分别指定水平和垂直分辨率。

**-quiet**
> 不显示提示信息（libnetpbm 通用选项）。

# DESCRIPTION

**pbmtoepsi** 将 PBM 位图转换为 Encapsulated PostScript Interchange（EPSI）格式。EPSI 包含一个低分辨率预览位图，供不支持 PostScript 的应用显示，同时保留用于打印的全分辨率 PostScript 表示。属于 Netpbm 工具集。

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

[pnmtops](/man/pnmtops)(1), [pbmtoepson](/man/pbmtoepson)(1)
