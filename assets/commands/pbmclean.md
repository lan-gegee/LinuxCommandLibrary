# TAGLINE

移除孤立像素

# TLDR

**去除位图中的噪点**

```pbmclean [input.pbm] > [output.pbm]```

**设置最小连通数量**

```pbmclean -minneigh=[4] [input.pbm] > [output.pbm]```

**翻转黑白后进行清理**

```pbmclean -black [input.pbm] > [output.pbm]```

# SYNOPSIS

**pbmclean** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入的 PBM 文件。

**-minneigh** _N_
> 最小邻居数量。

**-black**
> 清理黑色像素。

**-white**
> 清理白色像素。

# DESCRIPTION

**pbmclean** 移除孤立像素，用于清理有噪点的位图。

该工具可去除斑点。属于 Netpbm 的一部分。

# CAVEATS

Netpbm 的组成部分。仅支持 PBM 格式。可能移除细小细节。

# HISTORY

pbmclean 属于 **Netpbm**，用于清理位图图像。

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

[pbm](/man/pbm)(5), [pgmedge](/man/pgmedge)(1), [netpbm](/man/netpbm)(1)
