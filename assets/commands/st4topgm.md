# TAGLINE

将 SBIG ST-4 自动导星图像转换为 PGM

# TLDR

**转换** SBIG ST-4 图像文件为 PGM

```st4topgm [input.st4] > [output.pgm]```

**从标准输入读取**并转换为 PGM

```cat [input.st4] | st4topgm > [output.pgm]```

# SYNOPSIS

**st4topgm** [_st4file_]

# DESCRIPTION

**st4topgm** 读取 Santa Barbara Instrument Group（SBIG）ST-4 天文 CCD 自动导星相机所使用的原生格式图像，并将数据以 PGM（Portable Graymap）图像的形式写入标准输出。

它是 Netpbm 工具集的一部分。若未指定输入文件，则从标准输入读取。该程序不提供任何自定义选项；它支持 libnetpbm 的通用选项（例如 `-quiet`、`-plain`）。

# CAVEATS

ST-4 是一种过时的天文成像格式。反向转换请使用 **pgmtost4**。

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

[pgmtost4](/man/pgmtost4)(1), [sbigtopgm](/man/sbigtopgm)(1)
