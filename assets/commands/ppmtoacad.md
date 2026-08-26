# TAGLINE

将 PPM 图像转换为 AutoCAD 格式

# TLDR

**将 PPM 转换为 AutoCAD DXF**

```ppmtoacad [input.ppm] > [output.dxf]```

**指定缩放比例**

```ppmtoacad -scale [0.1] [input.ppm] > [output.dxf]```

# SYNOPSIS

**ppmtoacad** [_options_] [_file_]

# PARAMETERS

**-scale** _n_
> 输出的缩放系数。

**-dxb**
> 输出 DXB 二进制格式。

# DESCRIPTION

**ppmtoacad** 将 PPM 图像转换为 AutoCAD DXF（Drawing Exchange Format）幻灯片文件，供 CAD 应用程序使用。属于 Netpbm 工具集。

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

[ppmtoilbm](/man/ppmtoilbm)(1), [pnmtops](/man/pnmtops)(1)
