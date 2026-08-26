# TAGLINE

将 PGM 图像转换为 Usenix FaceSaver 格式，用于存储人脸图像

# TLDR

**将 PGM 转换为 Usenix FaceSaver 格式**

```pgmtofs [input.pgm] > [output.fs]```

# SYNOPSIS

**pgmtofs** [_file_]

# DESCRIPTION

**pgmtofs** 将 PGM 图像转换为 Usenix FaceSaver 格式，该格式用于在电子邮件和新闻系统中存储人脸图像。属于 Netpbm 工具集。

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

[fstopgm](/man/fstopgm)(1), [pbmtoybm](/man/pbmtoybm)(1)
