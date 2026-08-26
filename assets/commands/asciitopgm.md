# TAGLINE

将 ASCII 艺术转换为 PGM 灰度图像

# TLDR

**转换** ASCII 艺术为 PGM（注意：高度在前，宽度在后）

```asciitopgm [height] [width] < [ascii.txt] > [output.pgm]```

用除数**调亮**输出

```asciitopgm -divisor=[2] [height] [width] [ascii.txt] > [output.pgm]```

# SYNOPSIS

**asciitopgm** [_-divisor=integer_] _height_ _width_ [_asciifile_]

# DESCRIPTION

**asciitopgm** 将 ASCII 艺术文本转换为 PGM（Portable Graymap）图像格式。每个字符对应一个像素；大字符（如大写 M）产生深色像素，小字符（如句点）产生浅色像素。

它可用于把早期的 ASCII 作品转换为图像格式，或从文本图案生成图像。输出值的范围是 0 到最大 127。

# PARAMETERS

**height**
> 输出图像的高度，单位为像素（行数）

**width**
> 输出图像的宽度，单位为像素（列数）

**asciifile**
> 输入的 ASCII 文件（省略时从 stdin 读取）

**-divisor** _integer_
> 对每个字符的黑色程度值做除法，从而调亮输出。默认为 1；更大的正值会产生更亮的图像。

# CAVEATS

字符到灰度的映射不一定对所有 ASCII 艺术风格都理想。输出尺寸必须手动指定。

# HISTORY

**asciitopgm** 是 Netpbm 图像处理工具集的一部分，该工具集在 **1980** 年代末由 PBMPLUS 演化而来。

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

[pgmtopbm](/man/pgmtopbm)(1), [pnmtopng](/man/pnmtopng)(1), [img2txt](/man/img2txt)(1)

# RESOURCES

```[Homepage](https://netpbm.sourceforge.net/)```

```[Documentation](https://netpbm.sourceforge.net/doc/asciitopgm.html)```

<!-- verified: 2026-06-17 -->
