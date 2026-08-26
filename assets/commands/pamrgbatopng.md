# TAGLINE

将带 Alpha 通道的 PAM 图像转换为 PNG 格式，并保留透明度

# TLDR

**将 RGBA PAM 转换为保留透明度的 PNG**

```pamrgbatopng [input.pam] > [output.png]```

# SYNOPSIS

**pamrgbatopng** [_file_]

# DESCRIPTION

**pamrgbatopng** 将带 Alpha 通道的 PAM 图像转换为 PNG 格式，同时保留透明度。输入必须是 RGBA PAM（4 个通道）。属于 Netpbm 工具集。

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

[pngtopam](/man/pngtopam)(1), [pnmtopng](/man/pnmtopng)(1)
