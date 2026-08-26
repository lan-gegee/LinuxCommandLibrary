# TAGLINE

将 RLA/RPF 图像转换为 PAM 格式

# TLDR

**将 RLA/RPF 转换为 PAM**

```rlatopam [input.rla] > [output.pam]```

# SYNOPSIS

**rlatopam** [_file_]

# DESCRIPTION

**rlatopam** 将 Wavefront RLA 和 RLA/RPF 图像文件转换为 PAM 格式。RLA 被 Maya 和 3ds Max 等 3D 渲染软件使用。属于 Netpbm 工具集。

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

[pamtotiff](/man/pamtotiff)(1), [sgitopnm](/man/sgitopnm)(1)
