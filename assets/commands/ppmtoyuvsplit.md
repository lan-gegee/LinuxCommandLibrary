# TAGLINE

将 PPM 拆分为用于 MPEG 编码的 YUV 分量文件

# TLDR

**将 PPM 拆分为 YUV 分量文件**

```ppmtoyuvsplit [base] [input.ppm]```

**从 stdin 读取**

```cat [input.ppm] | ppmtoyuvsplit [base]```

# SYNOPSIS

**ppmtoyuvsplit** _basename_ [_ppmfile_]

# PARAMETERS

_basename_
> 输出文件的基础名。会生成 _basename_.Y、_basename_.U 和 _basename_.V。

_ppmfile_
> 输入的 PPM 图像文件。省略时从 stdin 读取。

# DESCRIPTION

**ppmtoyuvsplit** 读取一幅 PPM 图像，生成三个单独的原始输出文件：_basename_.Y（亮度）、_basename_.U 和 _basename_.V（色度）。输出为 Stanford MPEG 编解码器所要求的次采样 YUV，其中 YUV 值按 CCIR.601 缩放。

Y 文件每个像素占一个字节。U 和 V 文件使用 4:1 降采样——每个字节代表一个 2x2 像素块（这 4 个像素的算术平均值）。因此 Y 文件的大小是 U 或 V 文件的四倍。

属于 **Netpbm** 工具集。

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

[yuvsplittoppm](/man/yuvsplittoppm)(1), [ppmtoyuv](/man/ppmtoyuv)(1), [ppmtoeyuv](/man/ppmtoeyuv)(1), [ppmtompeg](/man/ppmtompeg)(1)
