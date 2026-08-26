# TAGLINE

将 Sun 图标图像转换为 PNM 格式

# TLDR

**转换** Sun 图标为 PNM（写入标准输出）

```sunicontopnm [input.icon] > [output.pnm]```

**从标准输入转换**

```sunicontopnm < [input.icon] > [output.pnm]```

# SYNOPSIS

**sunicontopnm** [_iconfile_]

# DESCRIPTION

**sunicontopnm** 读取 Sun 图标格式的图像（历史上 SunOS 工作站使用的单色图标格式），并将对应的 PBM（或 PNM）图像写入标准输出。未指定输入文件时，从标准输入读取图标。

由于 Sun 图标只存储黑白像素，输出始终是单色的。该程序是 **Netpbm** 工具集的一部分，该工具集提供了构建图像格式转换流水线的基础组件。

# CAVEATS

Sun 图标文件是一种过时的格式。该工具主要用于归档用途的转换。配套工具 **pbmtosunicon** 执行相反的 PBM 到 Sun 图标格式的转换。

# HISTORY

属于 **Netpbm** 软件包。Sun 图标格式可追溯到 20 世纪 80 年代 SunOS 的 SunView/NeWS 时代；该转换器自 20 世纪 90 年代初起就已成为 pbmplus / Netpbm 的一部分。

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

[pbmtosunicon](/man/pbmtosunicon)(1), [xbmtopbm](/man/xbmtopbm)(1), [pnm](/man/pnm)(5)
