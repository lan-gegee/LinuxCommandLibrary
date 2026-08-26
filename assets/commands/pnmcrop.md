# TAGLINE

自动裁剪 PNM 图像的边框

# TLDR

**裁剪图像边框**

```pnmcrop [input.pnm] > [output.pnm]```

**仅裁剪白色边框**

```pnmcrop -white [input.pnm] > [output.pnm]```

**仅裁剪黑色边框**

```pnmcrop -black [input.pnm] > [output.pnm]```

**裁剪指定的侧边**

```pnmcrop -left -right [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmcrop** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入的 PNM 文件。

**-white**
> 裁剪白色边框。

**-black**
> 裁剪黑色边框。

**-left**
> 仅裁剪左侧。

**-right**
> 仅裁剪右侧。

**-top**
> 仅裁剪顶部。

**-bottom**
> 仅裁剪底部。

**-verbose**
> 显示裁剪信息。

# DESCRIPTION

**pnmcrop** 自动检测并移除 PNM 图像四周颜色均匀的边框。它会找出图像边缘完全由边框颜色构成的行与列，并将它们修剪掉。

默认情况下会自动检测边框颜色，但 **-white** 和 **-black** 可以强制指定边框颜色。借助 **-left**、**-right**、**-top** 和 **-bottom** 标志还可以选择性地只裁剪某一侧。属于 Netpbm 工具集。

# CAVEATS

边框颜色必须均匀一致。属于 Netpbm 套件。

# HISTORY

pnmcrop 作为 **Netpbm** 的一部分创建，用于自动去除图像边框。

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

[pnmcut](/man/pnmcut)(1), [pnmpad](/man/pnmpad)(1), [pamcut](/man/pamcut)(1)
