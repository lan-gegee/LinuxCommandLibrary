# TAGLINE

将 PPM 转换为 Motif UIL 图标格式

# TLDR

**将 PPM 转换为 UIL 格式**

```ppmtouil [input.ppm] > [output.uil]```

**指定名称**

```ppmtouil -name [iconname] [input.ppm] > [output.uil]```

# SYNOPSIS

**ppmtouil** [_options_] [_file_]

# PARAMETERS

**-name** _string_
> UIL 图标的名称。

# DESCRIPTION

**ppmtouil** 将 PPM 图像转换为 UIL（User Interface Language）格式，用于 Motif X11 GUI 开发。属于 Netpbm 工具集。

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

[pamtouil](/man/pamtouil)(1), [ppmtoxpm](/man/ppmtoxpm)(1)
