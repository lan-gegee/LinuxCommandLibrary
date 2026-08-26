# TAGLINE

将 PPM 转换为 HP PaintJet 格式

# TLDR

**将 PPM 转换为 HP PaintJet 格式**

```ppmtopj [input.ppm] > [output.pj]```

**指定伽马校正**

```ppmtopj -gamma [1.0] [input.ppm] > [output.pj]```

**在 8.5 x 11 页面上居中放置图像**

```ppmtopj -center [input.ppm] > [output.pj]```

**使用行程长度编码**

```ppmtopj -rle [input.ppm] > [output.pj]```

**应用抖动渲染模式**

```ppmtopj -render dither [input.ppm] > [output.pj]```

# SYNOPSIS

**ppmtopj** [**-gamma** _val_] [**-xpos** _val_] [**-ypos** _val_] [**-back** dark|lite] [**-rle**] [**-center**] [**-render** _mode_] [_ppmfile_]

# PARAMETERS

**-gamma** _val_
> 伽马校正值（默认 0）。

**-xpos** _val_
> 沿 x 方向移动 val 个像素。

**-ypos** _val_
> 沿 y 方向移动 val 个像素。

**-back** dark|lite
> 通过指明背景是浅色还是深色来增强前景。

**-rle**
> 对图像做行程长度编码（可能导致图像变大）。

**-center**
> 在 8.5 x 11 页面上居中放置图像。

**-render** _mode_
> 内部渲染算法：none、snap、bw、dither（默认）、diffuse、monodither、monodiffuse、clusterdither、monoclusterdither。

# DESCRIPTION

**ppmtopj** 读取一幅 PPM 图像并将其转换为 HP PaintJet 打印机格式以便直接打印。要获得最佳效果，输入应为 8 色 RGB 形式（原色全开与全关的二进制组合）。属于 Netpbm 工具集。

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

[pjtoppm](/man/pjtoppm)(1), [ppmtopjxl](/man/ppmtopjxl)(1)
