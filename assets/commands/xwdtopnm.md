# TAGLINE

将 XWD 截图转换为 PNM 格式

# TLDR

**将 XWD 文件转换为 PNM**

```xwdtopnm [input.xwd] > [output.pnm]```

**从 stdin 读取并写入 stdout**

```cat [input.xwd] | xwdtopnm > [output.pnm]```

# SYNOPSIS

**xwdtopnm** [_file_]

# DESCRIPTION

**xwdtopnm** 读取 X Window Dump（XWD）图像作为输入，生成 PNM（Portable aNy Map）图像作为输出。XWD 文件通常由 X11 的 **xwd** 工具创建，用于捕获窗口截图。

如果未指定输入文件，**xwdtopnm** 会从标准输入读取。输出始终写入标准输出。输出格式（PBM、PGM 或 PPM）取决于输入图像的颜色深度。

此工具是 **Netpbm** 工具集的一部分，这是一组图像转换和处理工具。

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

[pnmtoxwd](/man/pnmtoxwd)(1), [pnmtopng](/man/pnmtopng)(1), [pnmtojpeg](/man/pnmtojpeg)(1), [netpbm](/man/netpbm)(1)
