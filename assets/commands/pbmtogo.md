# TAGLINE

将 PBM 位图转换为 GraphOn 终端图形格式

# TLDR

**将 PBM 文件转换为 GraphOn 格式**

```pbmtogo [input.pbm] > [output.go]```

**从标准输入转换**

```cat [input.pbm] | pbmtogo > [output.go]```

# SYNOPSIS

**pbmtogo** [_file_]

# PARAMETERS

_file_
> 输入的 PBM 文件。未指定时从标准输入读取。

# DESCRIPTION

**pbmtogo** 读取 PBM（Portable Bitmap）图像作为输入，并输出 GraphOn 图形格式的数据。GraphOn 是一家生产带图形能力终端仿真器的公司。该工具属于 Netpbm 图像格式转换工具集。

输出发送到标准输出，可以重定向到文件。

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

[pbm](/man/pbm)(1), [netpbm](/man/netpbm)(1), [pbmtoascii](/man/pbmtoascii)(1), [pbmtoplot](/man/pbmtoplot)(1)
