# TAGLINE

将 Palm Pilot 图像格式转换为 PNM

# TLDR

**将 Palm 图像转换为 PNM**

```palmtopnm [input.palm] > [output.pnm]```

**只显示图像信息**

```palmtopnm -verbose [input.palm] > /dev/null```

# SYNOPSIS

**palmtopnm** [_options_] [_file_]

# PARAMETERS

**-verbose**
> 打印图像信息。

**-rendition** _n_
> 从多版本图像中选择特定版本。

# DESCRIPTION

**palmtopnm** 将 Palm Pilot 图像格式转换为 PNM。Palm 图像曾用于 Palm OS 掌上电脑。属于 Netpbm 工具集。

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

[pnmtopalm](/man/pnmtopalm)(1), [pnmtopng](/man/pnmtopng)(1)
