# TAGLINE

在 PPM 图像上绘制图形和文字

# TLDR

**用脚本在 PPM 图像上绘图**

```ppmdraw -script "[line 0 0 100 100]" [input.ppm] > [output.ppm]```

**使用脚本文件**

```ppmdraw -scriptfile [commands.txt] [input.ppm] > [output.ppm]```

# SYNOPSIS

**ppmdraw** [_options_] [_file_]

# PARAMETERS

**-script** _commands_
> 以内联方式提供绘制命令。

**-scriptfile** _file_
> 包含绘制命令的文件。

# DESCRIPTION

**ppmdraw** 使用一种脚本语言在 PPM 图像上绘制图形和文字。支持线条、圆形、文字和填充图形。属于 Netpbm 工具集。

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

[ppmlabel](/man/ppmlabel)(1), [pbmtext](/man/pbmtext)(1)
