# TAGLINE

复制并规范化 PNM 图像格式

# TLDR

**复制 PNM 图像并规范化为 raw 格式**

```pnmtopnm [input.pnm] > [output.pnm]```

**将 PNM 图像转换为 plain（ASCII）格式**

```pnmtopnm -plain [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmtopnm** [**-plain**] [_pnmfile_]

# DESCRIPTION

**pnmtopnm** 将一幅 PNM 图像复制到标准输出。输出的 PNM 格式（PBM、PGM 或 PPM）和 maxval 与输入相同。虽然与 `cat` 类似，但它可以在 PNM 的 plain（ASCII）与 raw（二进制）两种子格式之间转换。使用 **-plain** 可生成 ASCII 输出；省略该选项则生成 raw（二进制）输出。

自 Netpbm 10.27 起，**pnmtopnm** 只是 **pamtopnm** 的另一个名称。属于 Netpbm 工具集。

# HISTORY

**pnmtopnm** 于 Netpbm 10.23（2004 年 7 月）引入，取代了 **pnmtoplainpnm**。在 Netpbm 10.27（2005 年 3 月）中，它成为 **pamtopnm** 的别名。

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

[pamtopnm](/man/pamtopnm)(1), [pnmtoplainpnm](/man/pnmtoplainpnm)(1), [netpbm](/man/netpbm)(1)
