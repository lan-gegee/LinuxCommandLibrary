# TAGLINE

将 PBM 位图转换为 HP LaserJet PCL 格式以便直接打印

# TLDR

**将 PBM 转换为 HP LaserJet 格式**

```pbmtolj [input.pbm] > [output.lj]```

**指定分辨率**

```pbmtolj -resolution [300] [input.pbm] > [output.lj]```

# SYNOPSIS

**pbmtolj** [_options_] [_file_]

# PARAMETERS

**-resolution** _n_
> 打印分辨率（75、100、150、300、600）。

**-float**
> 不设置光标位置。

**-delta**
> 使用 delta 行压缩。

# DESCRIPTION

**pbmtolj** 将 PBM 位图转换为 HP LaserJet PCL 格式以便直接打印。支持多种分辨率和压缩方式。属于 Netpbm 工具集。

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

[ppmtolj](/man/ppmtolj)(1), [pbmtoepson](/man/pbmtoepson)(1)
