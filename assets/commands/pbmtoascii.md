# TAGLINE

将 PBM 位图图像转换为 ASCII 字符画

# TLDR

**将 PBM 转换为 ASCII 字符画**

```pbmtoascii [input.pbm]```

**以指定网格尺寸转换**

```pbmtoascii -[2x4] [input.pbm]```

# SYNOPSIS

**pbmtoascii** [_options_] [_file_]

# PARAMETERS

**-1x2**
> 1x2 单元格尺寸。

**-2x4**
> 2x4 单元格尺寸（默认）。

# DESCRIPTION

**pbmtoascii** 将 PBM 位图图像转换为 ASCII 字符画。使用文本字符渲染图像。属于 Netpbm 工具集。

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

[ppmtoascii](/man/ppmtoascii)(1), [asciitopgm](/man/asciitopgm)(1)
