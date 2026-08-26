# TAGLINE

将 PBM 位图转换为特定 HP DeskJet 打印机使用的 HP PPA 格式

# TLDR

**将 PBM 转换为 HP PPA 格式**

```pbmtoppa [input.pbm] > [output.ppa]```

**指定伽马校正**

```pbmtoppa -g [1.0] [input.pbm] > [output.ppa]```

# SYNOPSIS

**pbmtoppa** [_options_] [_file_]

# PARAMETERS

**-g** _value_
> 伽马校正值。

**-b** _n_
> 黑度值。

# DESCRIPTION

**pbmtoppa** 将 PBM 位图转换为特定 HP DeskJet 打印机使用的 HP PPA（Printing Performance Architecture）格式。属于 Netpbm 工具集。

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

[pbmtolj](/man/pbmtolj)(1), [pbmtoepson](/man/pbmtoepson)(1)
