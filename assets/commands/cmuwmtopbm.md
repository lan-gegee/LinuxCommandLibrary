# TAGLINE

CMU window manager 位图转 PBM 转换器

# TLDR

将 CMU window manager 位图**转换为** PBM

```cmuwmtopbm [input.cmuwm] > [output.pbm]```

**从 stdin 转换**

```cat [input.cmuwm] | cmuwmtopbm > [output.pbm]```

# SYNOPSIS

**cmuwmtopbm** [_cmuwmfile_]

# DESCRIPTION

**cmuwmtopbm** 将 CMU window manager 位图文件转换为 PBM（Portable BitMap）格式。它是 Netpbm 软件包的一部分。

CMU window manager（CMU WM）是卡内基梅隆大学早期开发的一个 X Window System 窗口管理器。此工具将其位图格式转换为可移植的 Netpbm 格式。

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

[pbmtocmuwm](/man/pbmtocmuwm)(1), [netpbm](/man/netpbm)(1)

# RESOURCES

```[Homepage](https://netpbm.sourceforge.net/)```

```[Documentation](https://netpbm.sourceforge.net/doc/cmuwmtopbm.html)```

<!-- verified: 2026-06-22 -->
