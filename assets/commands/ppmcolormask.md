# TAGLINE

根据 PPM 图像中的一种或多种颜色创建 PBM 掩码

# TLDR

**掩蔽单一颜色**（现代语法）

```ppmcolormask -color=[red] [input.ppm] > [mask.pbm]```

**一次掩蔽多种颜色**

```ppmcolormask -color=[red,pink,salmon] [input.ppm] > [mask.pbm]```

**使用十六进制/RGB 颜色**

```ppmcolormask -color=[rgb:ff/00/00] [input.ppm] > [mask.pbm]```

**使用 Berlin-Kay 模糊颜色匹配**

```ppmcolormask -color=[bk:red,bk:orange] [input.ppm] > [mask.pbm]```

**过时的位置参数形式**（单一精确颜色）

```ppmcolormask [red] [input.ppm] > [mask.pbm]```

**通过管道输入非 PPM 图像**

```jpegtopnm [photo.jpg] | ppmcolormask -color=[white] > [mask.pbm]```

# SYNOPSIS

**ppmcolormask** **-color=**_color_list_ [_ppmfile_]

**ppmcolormask** _color_ [_ppmfile_]

# PARAMETERS

**-color=**_color_list_
> 必需。要掩蔽的颜色列表，以逗号分隔。每种颜色可以是命名颜色（`red`）、十六进制/rgb 表示（`rgb:ff/00/00`、`#ff0000`），或带 `bk:` 前缀的 Berlin-Kay 模糊匹配。

**-quiet**
> libnetpbm 通用选项：抑制 stderr 上的提示性消息。

# DESCRIPTION

**ppmcolormask** 读取一幅 PPM 图像并写入一幅相同尺寸的 PBM 位图。在输出中，匹配 **-color** 列表中任意颜色的像素为**黑色**；其余所有像素为**白色**。生成的掩码可用于提供给 **pamcomp** 之类的程序（作为 alpha 通道），或与 **pnmpaste** 配合进行区域替换。

Berlin-Kay（`bk:`）形式基于 HSV 值应用 Sugeno 型模糊推理，因此某种命名颜色的相近色调都能匹配。位置参数形式（不带 `-color`）仅为向后兼容而保留，且只支持一种精确颜色。

如果省略 _ppmfile_，则从标准输入读取数据；输出总是写到标准输出。

# CAVEATS

非 `bk:` 匹配是精确匹配——JPEG 或缩放带来的微小舍入差异可能导致漏掉像素。若需要按范围或容差匹配，请使用 **pambackground**（用于背景选取），或先用 **ppmquant** 对图像预量化。

输出始终是 PBM，因此掩码无法编码部分透明；如果确实需要透明效果，可用 **pgmtopbm** 转换格式或使用 `pnmtopng -transparent`。

# HISTORY

**ppmcolormask** 属于最初由 **Jef Poskanzer** 编写的 **Netpbm** 工具集。`-color` 形式（接受颜色列表和 Berlin-Kay 匹配）在 Netpbm 10.32 中取代了位置参数颜色形式。

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

[pamcomp](/man/pamcomp)(1), [ppmchange](/man/ppmchange)(1), [pambackground](/man/pambackground)(1), [pbmmask](/man/pbmmask)(1), [pnmtopng](/man/pnmtopng)(1), [pnmcomp](/man/pnmcomp)(1), [netpbm](/man/netpbm)(1)
