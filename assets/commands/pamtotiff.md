# TAGLINE

将 PAM 图像转换为 TIFF 格式

# TLDR

**将 PAM 转换为 TIFF**

```pamtotiff [input.pam] > [output.tiff]```

**使用 LZW 压缩转换**

```pamtotiff -lzw [input.pam] > [output.tiff]```

**使用 JPEG 压缩转换**

```pamtotiff -jpeg [input.pam] > [output.tiff]```

# SYNOPSIS

**pamtotiff** [_options_] [_file_]

# PARAMETERS

**-none**
> 不压缩。

**-lzw**
> LZW 压缩。

**-jpeg**
> JPEG 压缩。

**-packbits**
> PackBits 压缩。

**-append**
> 追加到现有的 TIFF 文件。

# DESCRIPTION

**pamtotiff** 将 PAM 图像转换为 TIFF 格式。支持 Alpha 通道和多种压缩方式。属于 Netpbm 工具集。

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

[tifftopnm](/man/tifftopnm)(1), [pnmtotiff](/man/pnmtotiff)(1)
