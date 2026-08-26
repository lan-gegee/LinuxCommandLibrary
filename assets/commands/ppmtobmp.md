# TAGLINE

将 PPM 图像转换为 BMP 格式

# TLDR

**将 PPM 转换为 BMP**

```ppmtobmp [input.ppm] > [output.bmp]```

**创建 Windows BMP**

```ppmtobmp -windows [input.ppm] > [output.bmp]```

**创建 OS/2 BMP**

```ppmtobmp -os2 [input.ppm] > [output.bmp]```

**强制每像素 8 位**

```ppmtobmp -bpp 8 [input.ppm] > [output.bmp]```

# SYNOPSIS

**ppmtobmp** [**-windows**|**-os2**] [**-bpp** _n_] [**-mapfile** _file_] [_ppmfile_]

# PARAMETERS

**-windows**
> 生成 Microsoft Windows BMP 文件。这是默认行为（自 2000 年 8 月起）。

**-os2**
> 生成 OS/2 BMP 文件。

**-bpp** _bits_
> 输出的每像素位数：1、4、8 或 24。默认情况下 ppmtobmp 会选择能够表示输入中所有颜色的最小值。

**-mapfile** _file_
> 使用指定文件作为 BMP 调色板（颜色映射表），而不是自动计算。当需要特定的调色板索引值时很有用。

# DESCRIPTION

**ppmtobmp** 将 PPM 图像转换为 BMP（Windows/OS2 位图）格式。属于 Netpbm 图像格式转换工具集。

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

[bmptopnm](/man/bmptopnm)(1), [pnmtopng](/man/pnmtopng)(1)
