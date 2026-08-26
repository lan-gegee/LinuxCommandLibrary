# TAGLINE

将 Andrew Toolkit 位图图像转换为 PBM 格式

# TLDR

**转换** Andrew Toolkit 位图为 PBM

```atktopbm [input.atk] > [output.pbm]```

# SYNOPSIS

**atktopbm** [_atkfile_]

# DESCRIPTION

**atktopbm** 将 Andrew Toolkit 光栅格式的文件转换为 PBM（Portable Bitmap）格式。Andrew Toolkit 是卡内基梅隆大学开发的一套部件集与应用框架。

此转换器用于处理遗留的 ATK 格式图形。

# PARAMETERS

**atkfile**
> 输入的 ATK 光栅文件（或 stdin）

# CAVEATS

ATK 格式已经过时。主要用于转换旧文件。很少有现代应用程序会生成 ATK 位图。

# HISTORY

属于 Netpbm 的一部分，支持 **1980 年代**卡内基梅隆大学开发的 Andrew Toolkit 格式。

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

[pbmtoatk](/man/pbmtoatk)(1), [pnmtopng](/man/pnmtopng)(1)

# RESOURCES

```[Homepage](https://netpbm.sourceforge.net/)```

```[Documentation](https://netpbm.sourceforge.net/doc/atktopbm.html)```

<!-- verified: 2026-06-17 -->
