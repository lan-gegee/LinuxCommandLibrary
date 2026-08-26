# TAGLINE

将 Lisp Machine 位图格式转换为 PGM 灰度图

# TLDR

**将 Lisp Machine 位图转换为 PGM**

```lispmtopgm [input.lispm] > [output.pgm]```

**从 stdin 读取**

```cat [input.lispm] | lispmtopgm > [output.pgm]```

# SYNOPSIS

**lispmtopgm** [_lispmfile_]

# DESCRIPTION

**lispmtopgm** 将 Lisp Machine 位图文件转换为 PGM（Portable Graymap）图像。它读取在 TI Explorer 和 Symbolics Lisp Machines 上由 `tv:write-bit-array-file` 函数写出的位图。

多平面 Lisp Machine 位图本质上是彩色的，但由于文件格式缺少颜色映射表，输出以灰度 PGM 形式生成。如果未给出输入文件，则从标准输入读取位图。

# CAVEATS

Lisp Machine 格式通常会将图像宽度填充到 32 像素的倍数，但并非总是如此。宽度非 32 对齐的文件可能短少最多 7 位，无法被妥善处理。没有工具专属选项；只适用标准的 libnetpbm 选项。

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

[pgmtolispm](/man/pgmtolispm)(1), [pbmtolj](/man/pbmtolj)(1)
