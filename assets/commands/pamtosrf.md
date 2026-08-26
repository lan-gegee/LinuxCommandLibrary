# TAGLINE

将 PAM 图像转换为 Garmin GPS 自定义车辆图标所用的 SRF 格式

# TLDR

**将 PAM 转换为 SRF 格式**

```pamtosrf [input.pam] > [output.srf]```

# SYNOPSIS

**pamtosrf** [_file_]

# DESCRIPTION

**pamtosrf** 将 PAM 图像转换为 SRF（Garmin vehicle image）格式，该格式用于 Garmin GPS 设备上的自定义车辆图标。属于 Netpbm 工具集。

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

[srftopam](/man/srftopam)(1), [pnmtopng](/man/pnmtopng)(1)
