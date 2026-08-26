# TAGLINE

将 PBM 位图转换为 Epson ESC/P2 打印机格式

# TLDR

**将 PBM 转换为 Epson ESC/P2 格式**

```pbmtoescp2 [input.pbm] > [output.escp2]```

**指定分辨率**

```pbmtoescp2 -resolution [360] [input.pbm] > [output.escp2]```

# SYNOPSIS

**pbmtoescp2** [_options_] [_file_]

# PARAMETERS

**-resolution** _n_
> 打印分辨率（180、360、720）。

**-compress**
> 启用压缩。

# DESCRIPTION

**pbmtoescp2** 将 PBM 位图转换为 Epson ESC/P2 打印机格式。ESC/P2 用于现代喷墨打印机。属于 Netpbm 工具集。

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

[pbmtoepson](/man/pbmtoepson)(1), [pbmtolj](/man/pbmtolj)(1)
