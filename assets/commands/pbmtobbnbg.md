# TAGLINE

将 PBM 位图转换为 BBN BitGraph 终端格式

# TLDR

**将 PBM 文件转换为 BBN BitGraph 格式**

```pbmtobbnbg [input.pbm] > [output.bg]```

**从标准输入读取**

```cat [input.pbm] | pbmtobbnbg > [output.bg]```

# SYNOPSIS

**pbmtobbnbg** [_pbmfile_]

# DESCRIPTION

**pbmtobbnbg** 读取 PBM 图像作为输入，并输出 BBN BitGraph 图形终端格式的数据。未指定文件时从标准输入读取。

BitGraph 是由 BBN（Bolt Beranek and Newman）制造的图形终端。该工具属于 **Netpbm** 工具集。

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

[pbmtoplot](/man/pbmtoplot)(1), [pbmtoascii](/man/pbmtoascii)(1), [pbm](/man/pbm)(1), [netpbm](/man/netpbm)(1)
