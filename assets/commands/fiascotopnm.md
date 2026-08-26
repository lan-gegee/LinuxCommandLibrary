# TAGLINE

小波压缩到 PNM 的转换器

# TLDR

**将 FIASCO 转换为 PNM**

```fiascotopnm [input.fiasco] > [output.pnm]```

**转换指定的帧**

```fiascotopnm --frame [5] [input.fiasco] > [output.pnm]```

# SYNOPSIS

**fiascotopnm** [_options_] _file_

# PARAMETERS

**--frame** _num_
> 要提取的帧号。

# DESCRIPTION

**fiascotopnm** 把用 FIASCO（Fractal Image And Sequence COdec）算法压缩的图像解码为 PNM（Portable Any Map）格式。FIASCO 采用类似于 JPEG2000 的基于小波的压缩技术。

该工具是 Netpbm 图像处理工具集的一部分，能够从 FIASCO 编码的图像序列中提取单个帧。它既可以处理静态图像，也可以处理视频帧序列，让压缩数据能够用标准图像工具继续加工。

fiascotopnm 适用于处理旧式的 FIASCO 压缩图像，或者与把 FIASCO 用作中间格式的系统对接。

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

[pnmtofiasco](/man/pnmtofiasco)(1), [pnm](/man/pnm)(5)

# RESOURCES

```[Homepage](https://netpbm.sourceforge.net/)```

<!-- verified: 2026-07-15 -->
