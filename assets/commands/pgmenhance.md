# TAGLINE

增强 PGM 灰度图像的边缘

# TLDR

以默认强度（9）**增强图像锐度**

```pgmenhance [input.pgm] > [output.pgm]```

**以自定义强度增强**（1 = 最低，9 = 最高）

```pgmenhance -[3] [input.pgm] > [output.pgm]```

**从 stdin 读取**

```cat [input.pgm] | pgmenhance -[5] > [output.pgm]```

# SYNOPSIS

**pgmenhance** [_-N_] [_pgmfile_]

# PARAMETERS

**-** _N_
> 增强强度，从 **1**（最低）到 **9**（最高）。默认为 **9**。

# DESCRIPTION

**pgmenhance** 读取一幅 PGM 图像作为输入，增强其边缘，并写出一幅 PGM 图像作为输出。这种增强技术源自 Philip R. Thompson 的 **xim** 程序。属于 **Netpbm** 工具集。

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

[pgmnorm](/man/pgmnorm)(1), [pgmedge](/man/pgmedge)(1), [pamedge](/man/pamedge)(1)
