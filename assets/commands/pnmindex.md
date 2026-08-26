# TAGLINE

从图像创建缩略图索引页

# TLDR

**创建图像索引**

```pnmindex [image1.pnm] [image2.pnm] [image3.pnm] > [index.pnm]```

**指定尺寸**

```pnmindex -size [100] [*.pnm] > [index.pnm]```

**添加标题**

```pnmindex -title ["My Gallery"] [*.pnm] > [index.pnm]```

**多列排列**

```pnmindex -across [4] [*.pnm] > [index.pnm]```

# SYNOPSIS

**pnmindex** [_options_] _pnmfiles_...

# PARAMETERS

**-size** _n_
> 缩略图的最大尺寸（像素）。每幅图像都会被缩放到恰好放入 N x N 的方框内，并保持宽高比。默认：100。

**-across** _n_
> 每行缩略图的数量。默认：6。

**-colors** _n_
> 输出图像的最大颜色数。默认：256。

**-title** _title_
> 在图像顶部添加标题字符串。

**-black**
> 使用黑底白字的标签，而非默认的白底黑字标签。

**-noquant**
> 禁用颜色量化。默认情况下会对 PPM 输入做减色处理。

**-quant**
> 启用颜色量化（对 PPM 输入是默认行为）。

**-quiet**
> 不显示提示信息。

# DESCRIPTION

**pnmindex** 由多幅 PNM 图像生成一个可视化索引（拼贴表）。每幅图像都会缩放为缩略图并排入网格。

适合用来制作图像预览和画廊页面。

# EXAMPLES

```bash
# Create index of all PPM files
pnmindex *.ppm > index.ppm

# Thumbnails 150 pixels, 5 across
pnmindex -size 150 -across 5 photos/*.ppm > gallery.ppm

# With title on black background
pnmindex -title "Photos" -black images/*.pnm > contact.ppm

# Convert to JPEG
pnmindex *.pnm | pnmtojpeg > index.jpg
```

# CAVEATS

图像数量很大时可能产生极其巨大的输出。若要再拆分开来，可考虑 pamundice。

# HISTORY

pnmindex 是 **Netpbm** 的一部分，自早期 Pbmplus 版本起就提供拼贴表生成功能。

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

[pnmcat](/man/pnmcat)(1), [pnmscale](/man/pnmscale)(1), [pnmtile](/man/pnmtile)(1), [pnmmontage](/man/pnmmontage)(1), [pnmtojpeg](/man/pnmtojpeg)(1), [pamundice](/man/pamundice)(1), [netpbm](/man/netpbm)(1)
