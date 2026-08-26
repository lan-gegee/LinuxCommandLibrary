# TAGLINE

将 PPM 转换为 Mitsubishi 打印机格式

# TLDR

**将 PPM 转换为 Mitsubishi 打印机格式**

```ppmtomitsu [input.ppm] > [output.mitsu]```

**指定纸张尺寸**

```ppmtomitsu -A [input.ppm] > [output.mitsu]```

# SYNOPSIS

**ppmtomitsu** [_options_] [_file_]

# PARAMETERS

**-A**
> A 尺寸纸。

**-L**
> L 尺寸纸。

**-tiny**
> 微型输出模式。

# DESCRIPTION

**ppmtomitsu** 将 PPM 图像转换为 Mitsubishi 染料热升华打印机格式（S340-10）。属于 Netpbm 工具集。

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

[pnmtops](/man/pnmtops)(1), [ppmtolj](/man/ppmtolj)(1)
