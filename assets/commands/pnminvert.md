# TAGLINE

反转 PNM 图像的颜色

# TLDR

**反转图像颜色**

```pnminvert [input.pnm] > [output.pnm]```

**从标准输入读取并反转**

```cat [image.pnm] | pnminvert > [output.pnm]```

# SYNOPSIS

**pnminvert** [_file_]

# DESCRIPTION

**pnminvert** 通过反转全部像素值，生成 PNM 图像的照片底片效果。每个采样值都被替换为最大值减去原值，相当于明暗互换。

该工具适用于所有 PNM 类型：PBM（黑白位翻转）、PGM（灰度值取反）以及 PPM（每个颜色通道独立取反）。未给出文件时从标准输入读取。输出总是写入标准输出。

属于 Netpbm 工具集。更通用的 **paminvert** 已取代本工具，并且还能处理 PAM 图像。

# CAVEATS

`pnminvert` 除 libnetpbm 通用选项之外没有自己的选项。输出总是写入标准输出，必须重定向才能保存为文件。

# HISTORY

**pnminvert** 作为 **Netpbm** 软件包的一部分创建，用于可移植位图图像处理。

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

[paminvert](/man/paminvert)(1), [pnmarith](/man/pnmarith)(1), [pnmgamma](/man/pnmgamma)(1)
