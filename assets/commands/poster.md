# TAGLINE

将 PostScript 图像缩放为海报尺寸

# TLDR

**缩放为海报尺寸**

```poster -p [A0] -s [1.0] [input.ps] > [output.ps]```

**创建 2x2 拼贴海报**

```poster -mA4 -p 2x2A4 [input.ps] > [output.ps]```

**缩放到指定尺寸**

```poster -m[A4] -p[100x80cm] [input.ps] > [output.ps]```

**添加便于拼接的裁切标记**

```poster -c -m[letter] -p[2x2letter] [input.ps] > [output.ps]```

# SYNOPSIS

**poster** [_options_] _infile_ > _outfile_

# PARAMETERS

**-p** _size_
> 海报尺寸。

**-m** _size_
> 介质（纸张）尺寸。

**-s** _scale_
> 缩放因子。

**-c**
> 添加裁切标记。

**-o** _offset_
> 页面偏移。

**-w** _width_
> 白色边距。

# DESCRIPTION

**poster** 将 PostScript 图像放大到更大尺寸，并拆分到多页上，以便用普通打印机打印后拼装成海报。它会计算目标海报尺寸在可用介质尺寸上的最优拼贴方式，并处理页面重叠和对齐标记。

该工具支持标准纸张尺寸（A0-A4、letter、legal）、网格规格（2x2A4、3x3letter）以及以厘米或英寸表示的自定义尺寸。可以添加裁切标记来指导打印页面的物理拼装。重叠边距确保相邻页面之间拼接整洁。

# EXAMPLES

```bash
# Scale to A0 on A4 sheets
poster -mA4 -pA0 image.ps > poster.ps

# 2x2 poster from A4
poster -mA4 -p2x2A4 document.ps > tiled.ps

# With cut marks and overlap
poster -c -mA4 -pA1 -o5mm image.ps > poster.ps

# Custom dimensions
poster -mA4 -p100x70cm diagram.ps > big.ps
```

# SIZE FORMATS

```
Standard: A0, A1, A2, A3, A4, letter, legal
Grid: 2x2A4, 3x3letter
Custom: 100x70cm, 40x30in
```

# CAVEATS

输入必须是 PostScript。PDF 请先用 pdf2ps 等工具转换。输出可能需要按说明进行拼装。

# HISTORY

poster 由 **Jos van Eijndhoven** 编写，用于从标准打印机生成大幅面打印件。

# INSTALL

```apt: sudo apt install poster```

```dnf: sudo dnf install poster```

```zypper: sudo zypper install poster```

```brew: brew install poster```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ps2pdf](/man/ps2pdf)(1)
