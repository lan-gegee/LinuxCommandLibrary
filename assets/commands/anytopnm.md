# TAGLINE

将任意图像格式转换为 PNM（Netpbm）

# TLDR

将任意图像**转换**为 PNM 格式

```anytopnm [input.jpg] > [output.pnm]```

以**详细输出**模式转换

```anytopnm -v [input.png] > [output.pnm]```

# SYNOPSIS

**anytopnm** [_-v_] _file_

# DESCRIPTION

**anytopnm** 是一款 Netpbm 工具，可将几乎所有格式的图像转换为 PNM（Portable Any Map）格式。它充当包装器，自动检测输入格式并调用相应的转换器。

PNM 是 Netpbm 工具集中的中间格式，适用于图像处理管道——借助统一格式可以简化任意两种格式之间的相互转换。

# PARAMETERS

**-v**
> 显示转换步骤的详细输出

_file_
> 输入图像文件（省略时使用 stdin，但 stdin 必须可寻址）

# CAVEATS

依赖已安装对应格式的专用转换器。某些格式可能需要额外的库。输出始终是 PNM；要转换为其他目标格式请使用其他工具。

# HISTORY

**anytopnm** 是 Netpbm 软件包的一部分，Netpbm 由 Jef Poskanzer 在 **20 世纪 80 年代**末创建的 PBMPLUS 工具集演化而来。

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

[pnmtopng](/man/pnmtopng)(1), [pnmtojpeg](/man/pnmtojpeg)(1), [netpbm](/man/netpbm)(1), [convert](/man/convert)(1)
