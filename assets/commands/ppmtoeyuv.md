# TAGLINE

将 PPM 转换为 Berkeley Encoder YUV 格式

# TLDR

**将 PPM 图像转换为 EYUV 格式**

```ppmtoeyuv [input.ppm] > [output.eyuv]```

**从 stdin 转换**

```cat [input.ppm] | ppmtoeyuv > [output.eyuv]```

# SYNOPSIS

**ppmtoeyuv** [_ppmfile_]

# DESCRIPTION

**ppmtoeyuv** 将 PPM 图像转换为 Berkeley Encoder YUV（EYUV）格式，该格式被 MPEG 编码器使用。可从文件参数或标准输入读取。输出写到标准输出。属于 Netpbm 工具集。

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

[eyuvtoppm](/man/eyuvtoppm)(1), [ppmtoyuv](/man/ppmtoyuv)(1), [ppmtojpeg](/man/ppmtojpeg)(1)
