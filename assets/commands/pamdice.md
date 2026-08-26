# TAGLINE

将图像切分成小块

# TLDR

**将图像切成小块**

```pamdice -width=[100] -height=[100] -outstem=[tile] [input.pam]```

**带重叠地切分**

```pamdice -width=[100] -height=[100] -hoverlap=[10] -voverlap=[10] [input.pam]```

# SYNOPSIS

**pamdice** [_options_] [_file_]

# PARAMETERS

**-width** _PIXELS_
> 小块宽度。

**-height** _PIXELS_
> 小块高度。

**-outstem** _PREFIX_
> 输出文件名前缀。

**-hoverlap** _PIXELS_
> 水平重叠量。

**-voverlap** _PIXELS_
> 垂直重叠量。

# DESCRIPTION

**pamdice** 将图像切分成小块。会创建多个输出文件。

该工具把图像划分为网格。属于 Netpbm 的一部分。

# CAVEATS

属于 Netpbm。会创建多个文件。可用 pamundice 重新拼合。

# HISTORY

pamdice 是 **Netpbm** 的一部分，用于把图像切分成小块。

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

[pamundice](/man/pamundice)(1), [pnmcut](/man/pnmcut)(1), [netpbm](/man/netpbm)(1)
