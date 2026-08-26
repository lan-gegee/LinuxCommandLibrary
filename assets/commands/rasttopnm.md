# TAGLINE

将 Sun 光栅图像转换为 PNM 格式

# TLDR

**转换** Sun 光栅文件并以 PNM 输出到标准输出

```rasttopnm [input.ras] > [output.pnm]```

**从标准输入读取**并将 PNM 写到标准输出

```cat [input.ras] | rasttopnm > [output.pnm]```

**输出带色彩映射的光栅图的索引平面**（调试用）

```rasttopnm -index [input.ras] > [output.pgm]```

**转换并通过管道**输出为 PNG

```rasttopnm [input.ras] | pnmtopng > [output.png]```

# SYNOPSIS

**rasttopnm** [**-index**] [_rastfile_]

# PARAMETERS

_rastfile_
> Sun Rasterfile（.ras）输入。省略时从标准输入读取。

**-index**
> 对于带色彩映射的光栅图，将原始颜色索引平面以 PGM 格式输出，而不是通过色彩映射解引用生成 PPM。主要用于检查底层数据。

# DESCRIPTION

**rasttopnm** 将 Sun Rasterfile 图像（.ras）转换为 Portable Anymap（PNM）格式，并根据输入图像的颜色深度和色彩映射自动选择 PBM、PGM 或 PPM 输出。Sun Rasterfile 是 SunOS 和 Solaris 系统的原生图像格式，常由较老的 X11 工具生成。

输出写到标准输出。它是 **Netpbm** 工具包的一部分。

# CAVEATS

一些较少见的 Rasterfile 编码（例如使用特殊色彩映射的 RT_BYTE_ENCODED RLE）在某些 Netpbm 构建中可能不受支持。该转换器会选择能够无损表示输入的最窄 PNM 子类型。

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

[pnmtorast](/man/pnmtorast)(1), [xwdtopnm](/man/xwdtopnm)(1), [pnm](/man/pnm)(5)
