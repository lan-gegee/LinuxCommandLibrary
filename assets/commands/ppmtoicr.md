# TAGLINE

将 PPM 转换为 NCSA ICR 格式

# TLDR

**将 PPM 转换为 NCSA ICR 格式**

```ppmtoicr [input.ppm] > [output.icr]```

**以自定义窗口名转换**

```ppmtoicr -windowname [myimage] [input.ppm] > [output.icr]```

**以像素放大系数转换**

```ppmtoicr -expand [2] [input.ppm] > [output.icr]```

**通过管道从 stdin 读取**

```cat [input.ppm] | ppmtoicr > [output.icr]```

# SYNOPSIS

**ppmtoicr** [_options_] [_file_]

# PARAMETERS

**-windowname** _name_
> 设置 ICR 输出中窗口的名称。默认为 "untitled"。

**-expand** _n_
> 将每个像素放大 _n_ 倍。每个像素变成一个 _n_ x _n_ 的像素块。默认为 1（不放大）。

**-rle**
> 在输出中使用行程长度编码（RLE）压缩。

# DESCRIPTION

**ppmtoicr** 读取一幅 PPM 图像并将其转换为 NCSA ICR（Image Capture Raster）格式。ICR 格式曾被 NCSA Telnet 用于在远程显示器的 X11 窗口中显示光栅图像。输出写到标准输出。属于 Netpbm 工具集。

如果未指定输入文件，则从标准输入读取图像。

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

[ppmtoxpm](/man/ppmtoxpm)(1), [pnmtops](/man/pnmtops)(1)
