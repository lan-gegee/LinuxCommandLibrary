# TAGLINE

将 PPM 转换为自定义文本格式

# TLDR

**使用模板将 PPM 转换为文本**

```ppmtoarbtxt [template.txt] [input.ppm] > [output.txt]```

# SYNOPSIS

**ppmtoarbtxt** _template_ [_file_]

# PARAMETERS

_template_
> 定义输出格式的模板文件。

# DESCRIPTION

**ppmtoarbtxt** 使用模板将 PPM 图像转换为任意文本格式。模板规定像素值如何格式化。适用于自定义导出格式。属于 Netpbm 工具集。

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

[ppmtoascii](/man/ppmtoascii)(1), [ppmtoterm](/man/ppmtoterm)(1)
