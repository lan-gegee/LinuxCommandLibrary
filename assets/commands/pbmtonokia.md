# TAGLINE

将 PBM 位图转换为多种诺基亚手机格式，用于徽标和图形

# TLDR

**将 PBM 转换为 Nokia 格式**

```pbmtonokia [input.pbm] > [output.nok]```

**指定输出格式**

```pbmtonokia -fmt [ngg] [input.pbm] > [output.ngg]```

# SYNOPSIS

**pbmtonokia** [_options_] [_file_]

# PARAMETERS

**-fmt** _type_
> 输出格式（nol、ngg、npm、hx）。

# DESCRIPTION

**pbmtonokia** 将 PBM 位图转换为多种诺基亚手机格式，用于徽标和图形。属于 Netpbm 工具集。

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

[pbmtoxbm](/man/pbmtoxbm)(1), [pbmtoicon](/man/pbmtoicon)(1)
