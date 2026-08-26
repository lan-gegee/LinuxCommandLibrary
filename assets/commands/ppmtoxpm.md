# TAGLINE

将 PPM 转换为 X11 pixmap 格式

# TLDR

**将 PPM 转换为 XPM**

```ppmtoxpm [input.ppm] > [output.xpm]```

**以自定义名称转换**

```ppmtoxpm -name [icon] [input.ppm] > [icon.xpm]```

# SYNOPSIS

**ppmtoxpm** [_options_] [_file_]

# PARAMETERS

**-name** _name_
> 输出中的变量名。

**-hexonly**
> 只使用十六进制颜色代码。

**-rgb** _file_
> RGB 颜色名称文件。

# DESCRIPTION

**ppmtoxpm** 将 PPM 图像转换为 X11 pixmap 格式（.xpm）。XPM 是一种用于 X11 彩色图像的 C 源码格式。属于 Netpbm 工具集。

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

[xpmtoppm](/man/xpmtoppm)(1), [pbmtoxbm](/man/pbmtoxbm)(1)
