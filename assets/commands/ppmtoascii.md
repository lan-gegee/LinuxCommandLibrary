# TAGLINE

将 PPM 图像转换为 ASCII 字符画

# TLDR

**将 PPM 转换为 ASCII 字符画**（默认 1x2 单元尺寸）

```ppmtoascii [input.ppm]```

**以 2x4 单元尺寸转换**以获得更多细节

```ppmtoascii -2x4 [input.ppm]```

# SYNOPSIS

**ppmtoascii** [_-1x2_|_-2x4_] [_file_]

# PARAMETERS

**-1x2**
> 每个字符表示横向 1 像素、纵向 2 像素。这是默认值。

**-2x4**
> 每个字符表示横向 2 像素、纵向 4 像素，能呈现更多细节。

# DESCRIPTION

**ppmtoascii** 读取一幅 PPM 图像并输出较为粗糙的 ASCII 图形，其中包含 ANSI 终端控制字符，因此发送到彩色文本终端时会呈现粗糙的彩色效果。属于 Netpbm 工具集。

除分辨率选项外，**ppmtoascii** 还支持常见的 Netpbm 选项，例如用 **-quiet** 抑制提示性消息。

注意 **ppmtoterm** 也做类似的转换，但它把每个字符当作单个像素显示（每个像素使用同一个密集字符），而 **ppmtoascii** 则把 2 或 8 个像素合并成一个大致代表这些像素的字符。

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

[pbmtoascii](/man/pbmtoascii)(1), [ppmtoterm](/man/ppmtoterm)(1), [ppmtosixel](/man/ppmtosixel)(1)
