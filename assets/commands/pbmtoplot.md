# TAGLINE

将 PBM 图像转换为 Unix plot 格式

# TLDR

**将 PBM 图像转换为 Unix plot 格式**

```pbmtoplot [input.pbm] > [output.plot]```

**从 stdin 转换**

```cat [input.pbm] | pbmtoplot > [output.plot]```

# SYNOPSIS

**pbmtoplot** [_pbmfile_]

# DESCRIPTION

**pbmtoplot** 读取 PBM 图像作为输入，并输出 Unix plot(5) 格式文件。plot 格式是一种与设备无关的矢量图形格式，曾用于向绘图仪及其他图形设备输出。

未指定输入文件时，程序从标准输入读取。输出总是写入标准输出。没有对应的反向转换工具（不存在 plottopbm）。

属于 **Netpbm** 工具集。

# CAVEATS

Unix plot 格式已基本过时。转换是单向的；没有将 plot 格式转回 PBM 的对应工具。

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

[pbmtoascii](/man/pbmtoascii)(1), [pbmtogem](/man/pbmtogem)(1)
