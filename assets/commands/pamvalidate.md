# TAGLINE

验证 PAM/PNM 图像文件

# TLDR

**验证 PAM 文件**

```pamvalidate [input.pam]```

**验证并复制到输出**

```pamvalidate [input.pam] > [output.pam]```

# SYNOPSIS

**pamvalidate** [_file_]

# DESCRIPTION

**pamvalidate** 验证 PAM/PNM 图像文件。检查格式是否正确并输出有效的图像。适用于对不可信图像进行净化处理。属于 Netpbm 工具集。

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

[pnmfile](/man/pnmfile)(1)
