# TAGLINE

把一幅 PNM 图像粘贴到另一幅之上

# TLDR

**将图像粘贴到另一幅上**

```pnmpaste [small.pnm] [x] [y] [background.pnm] > [output.pnm]```

**粘贴到左上角**

```pnmpaste [overlay.pnm] 0 0 [base.pnm] > [output.pnm]```

**替换操作**

```pnmpaste -replace [patch.pnm] [100] [50] [image.pnm] > [output.pnm]```

**OR 操作**

```pnmpaste -or [mask.pbm] [x] [y] [image.pnm] > [output.pnm]```

# SYNOPSIS

**pnmpaste** [_options_] _from_ _x_ _y_ _to_

# PARAMETERS

**from**
> 要粘贴的图像。

**x**, **y**
> 在目标图像中的位置。

**to**
> 背景图像。

**-replace**
> 简单替换（默认）。

**-or**
> 按位 OR。

**-and**
> 按位 AND。

**-xor**
> 按位 XOR。

# DESCRIPTION

**pnmpaste** 把一幅 PNM 图像粘贴到另一幅的指定位置上。多种粘贴操作（replace、or、and、xor）可以产生不同的合成效果。

属于 Netpbm 的图像合成工具。

# EXAMPLES

```bash
# Paste logo at position 10,10
pnmpaste logo.ppm 10 10 background.ppm > result.ppm

# Paste at bottom-right (compute position)
pnmpaste small.ppm 300 200 large.ppm > result.ppm

# Combine with masks
pnmpaste -or mask.pbm 0 0 image.pbm > masked.pbm

# Multiple pastes
pnmpaste img1.ppm 0 0 base.ppm | pnmpaste img2.ppm 100 0 - > result.ppm
```

# CAVEATS

被粘贴的图像必须能放进背景范围之内。可使用负坐标实现偏移。属于 Netpbm。

# HISTORY

pnmpaste 是 **Jef Poskanzer** 所作 **Netpbm** 的一部分，提供基础的图像合成功能。

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

[pnmcomp](/man/pnmcomp)(1), [pnmcut](/man/pnmcut)(1), [pnmcat](/man/pnmcat)(1), [netpbm](/man/netpbm)(1)
