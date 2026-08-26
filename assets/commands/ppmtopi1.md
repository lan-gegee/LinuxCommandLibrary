# TAGLINE

将 PPM 转换为 Atari Degas PI1 格式

# TLDR

**将 PPM 转换为 Atari Degas PI1**

```ppmtopi1 [input.ppm] > [output.pi1]```

# SYNOPSIS

**ppmtopi1** [_file_]

# DESCRIPTION

**ppmtopi1** 以 PPM 图像作为输入，生成 Atari Degas .pi1 文件作为输出。PI1 是 Atari ST 计算机上 Degas 使用的低分辨率（320x200、16 色）格式。除所有 Netpbm 程序通用的选项外，没有其他命令行选项。输入从指定文件读取，未给出文件时从标准输入读取。输出写到标准输出。属于 Netpbm 工具集。

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

[pi1toppm](/man/pi1toppm)(1), [ppmtoneo](/man/ppmtoneo)(1), [pbmtopi3](/man/pbmtopi3)(1), [ppmtopgm](/man/ppmtopgm)(1)
