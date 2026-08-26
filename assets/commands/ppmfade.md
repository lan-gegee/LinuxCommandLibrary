# TAGLINE

创建图像之间的渐变过渡

# TLDR

**创建渐变过渡**

```ppmfade -f [first.ppm] -l [last.ppm]```

**渐隐到黑色**

```ppmfade -f [image.ppm] -mode black```

**指定帧数**

```ppmfade -f [first.ppm] -l [last.ppm] -frames [30]```

# SYNOPSIS

**ppmfade** [_options_]

# PARAMETERS

**-f** _FILE_
> 第一幅图像。

**-l** _FILE_
> 最后一幅图像。

**-frames** _N_
> 帧数。

**-mode** _MODE_
> 渐变模式（mix、black 等）。

**-base** _NAME_
> 输出文件名的基础名。

# DESCRIPTION

**ppmfade** 生成一系列 PPM 帧，用于在两幅图像之间创建渐变过渡。输出是一组带编号的文件，可以组装成动画或视频序列。

提供多种渐变模式，包括两幅图像之间的交叉淡化（crossfade）、渐隐到黑和渐隐到白。中间帧的数量决定过渡的速度和平滑程度。属于 Netpbm 工具集。

# CAVEATS

会生成带编号的输出文件。属于 Netpbm 套件。

# HISTORY

ppmfade 作为 **Netpbm** 的一部分被创建，用于视频淡入淡出效果。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm-extras```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ppmmix](/man/ppmmix)(1), [ppmmorph](/man/ppmmorph)(1), [ppm](/man/ppm)(5)
