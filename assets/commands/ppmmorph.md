# TAGLINE

在图像之间创建变形过渡序列

# TLDR

**在两幅图像之间做变形**

```ppmmorph -n [10] [control.ctl] [image1.ppm] [image2.ppm] > [sequence.ppm]```

**生成中间帧**

```ppmmorph -n [30] [morph.ctl] [start.ppm] [end.ppm]```

# SYNOPSIS

**ppmmorph** [_options_] _controlfile_ _image1_ _image2_

# PARAMETERS

**-n** _count_
> 中间帧的数量。

**controlfile**
> 定义对应点关系。

# DESCRIPTION

**ppmmorph** 在两幅图像之间创建变形（morphing）序列。控制点定义两幅图像中相互对应的特征，工具据此生成平滑的过渡。

属于 Netpbm 工具集。

# CONTROL FILE FORMAT

```
# Lines of corresponding points
# x1 y1 x2 y2 for image1 point to image2 point
100 50  150 60
200 100 250 110
```

# EXAMPLES

```bash
# Create 10-frame morph
ppmmorph -n 10 morph.ctl face1.ppm face2.ppm > sequence.ppm

# Split into individual frames
ppmmorph -n 20 morph.ctl a.ppm b.ppm | pamsplit frame%d.ppm

# Create animation
ppmmorph -n 30 ctrl.txt img1.ppm img2.ppm | \
  pamtogif > morph.gif
```

# CAVEATS

需要仔细放置控制点。点越多结果越平滑。两幅图像尺寸应相同。

# HISTORY

ppmmorph 是 **Netpbm** 的组成部分，实现了 20 世纪 90 年代因电影特效而流行的变形技术。

# SEE ALSO

[pnmpaste](/man/pnmpaste)(1), [ppmfade](/man/ppmfade)(1), [netpbm](/man/netpbm)(1)
