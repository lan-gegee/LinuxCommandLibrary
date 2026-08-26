# TAGLINE

将 Wireless Bitmap 转换为 PBM 格式

# TLDR

**将 WBMP 转换为 PBM**

```wbmptopbm [input.wbmp] > [output.pbm]```

# SYNOPSIS

**wbmptopbm** [_file_]

# PARAMETERS

_file_
> 输入的 WBMP 文件（省略时从标准输入读取）

# DESCRIPTION

**wbmptopbm** 将 WBMP（Wireless Bitmap）格式的图像转换为 PBM（Portable Bitmap）格式。WBMP 是一种单色位图格式，曾用于 WAP（Wireless Application Protocol）移动网页。它是 Netpbm 工具集的一部分。

输出写入到标准输出。

# CAVEATS

WBMP 只支持单色（1 位）图像，因此输出的 PBM 始终是黑白的。

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

[pbmtowbmp](/man/pbmtowbmp)(1), [netpbm](/man/netpbm)(1)
