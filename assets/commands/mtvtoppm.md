# TAGLINE

将 MTV 光线追踪格式转换为 PPM

# TLDR

**将 MTV 光线追踪器输出转换为 PPM**

```mtvtoppm [input.mtv] > [output.ppm]```

# SYNOPSIS

**mtvtoppm** [_file_]

# DESCRIPTION

**mtvtoppm** 读取 MTV 光线追踪图像文件作为输入，并生成 PPM 图像作为输出。MTV 指 Mark T. VandeWettering 的 MTV 光线追踪程序的输出格式（以其姓名首字母命名）。该格式是一种简单的无压缩真彩色栅格格式。文件通常使用 .pic 或 .mtv 扩展名。属于 Netpbm 工具集。

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

[rawtoppm](/man/rawtoppm)(1), [qrttoppm](/man/qrttoppm)(1)
