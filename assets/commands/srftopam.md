# TAGLINE

将 Garmin SRF 车辆图像转换为 PAM

# TLDR

**将 Garmin SRF 转换为 PAM**

```srftopam [input.srf] > [output.pam]```

# SYNOPSIS

**srftopam** [_file_]

# DESCRIPTION

**srftopam** 将 Garmin SRF 格式（一种用于车辆图标的 Sun Raster Format 变体）的图像转换为 PAM（Portable Arbitrary Map）格式。SRF 格式用于在 Garmin GPS 导航设备上显示自定义车辆图标。该工具是 Netpbm 图像处理工具集的一部分，后者提供了众多图像格式之间的转换器。

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

[pamtosrf](/man/pamtosrf)(1), [pngtopam](/man/pngtopam)(1)
