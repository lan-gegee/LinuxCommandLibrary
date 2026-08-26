# TAGLINE

为 PGM 图像应用 Bentley 效果

# TLDR

**为灰度图像应用 Bentley 效果**

```pgmbentley [input.pgm] > [output.pgm]```

**从 stdin 读取并写入 stdout**

```cat [input.pgm] | pgmbentley > [output.pgm]```

# SYNOPSIS

**pgmbentley** [_pgmfile_]

# DESCRIPTION

**pgmbentley** 为 PGM 图像应用"Bentley 效果"，根据周围像素的亮度垂直位移每个像素，从而产生熔化或滴落的外观，效果类似蜡受热软化后向下流淌。

如果不指定输入文件，则从标准输入读取图像。输出始终以 PGM 文件形式写入标准输出。

属于 Netpbm 工具集。

# CAVEATS

仅接受 PGM（灰度）输入。对于彩色图像，请先用 **ppmtopgm** 拆分通道，或采用其他流程处理。

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

[pgmoil](/man/pgmoil)(1), [pgmnoise](/man/pgmnoise)(1), [pnm](/man/pnm)(5)
