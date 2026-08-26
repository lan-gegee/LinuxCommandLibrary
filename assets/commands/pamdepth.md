# TAGLINE

更改图像位深

# TLDR

**降为 8 位**（maxval 255）

```pamdepth [255] [input.pam] > [output.pam]```

**升为 16 位**（maxval 65535）

```pamdepth [65535] [input.pam] > [output.pam]```

**降为 1 位**（黑白）

```pamdepth [1] [input.pam] > [output.pam]```

**通过管道从 stdin 读取**

```pnmtopam [input.ppm] | pamdepth [255] > [output.pam]```

# SYNOPSIS

**pamdepth** _maxval_ [_file_]

# PARAMETERS

_MAXVAL_
> 新的 maxval（1–65535）。每个样本按 _new\_maxval / old\_maxval_ 的比例重新缩放；所得位深是能容纳 _MAXVAL_ 的最小的二的幂（例如 _255_ → 8 位，_65535_ → 16 位）。

_FILE_
> 输入的 PAM、PPM、PGM 或 PBM 图像。省略时默认读取标准输入。

# DESCRIPTION

**pamdepth** 重新缩放 Netpbm/PAM 图像的 maxval（每样本分辨率）。增大 maxval 是无损的；减小 maxval 会损失精度，但绝不会改变图像的元组类型或宽高。

如果输入已经具有所要求的 maxval，**pamdepth** 会原样复制输出。使用 **pamdepth 1** 可将灰度图像降为双级图像；使用 **pamdepth 65535** 可将 8 位图像扩展为更深的位深，以便后续处理避免量化误差。

# CAVEATS

减小 maxval 会截断精度。要在元组类型之间转换（例如 RGB 转灰度），请使用 **pamtopnm** 或相关工具，而不是 **pamdepth**。

# HISTORY

pamdepth 是 **Netpbm** 的一部分，用于位深转换。

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

[pnmdepth](/man/pnmdepth)(1), [pamrecolor](/man/pamrecolor)(1), [netpbm](/man/netpbm)(1)
