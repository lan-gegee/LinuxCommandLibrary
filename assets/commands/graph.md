# TAGLINE

二维数据绘图工具

# TLDR

**绘制文件中的数据**

```graph [data.txt] > [plot.ps]```

**按指定范围绘图**

```graph -x [0] [10] -y [0] [100] [data.txt] > [plot.ps]```

**创建 PNG 输出**

```graph -T png [data.txt] > [plot.png]```

**带标题绘图**

```graph --title-font-size [0.05] -L "[My Graph]" [data.txt] > [plot.ps]```

**多个数据集**

```graph [data1.txt] [data2.txt] > [plot.ps]```

# SYNOPSIS

**graph** [_options_] [_files_]

# PARAMETERS

**-T** _type_
> 输出格式：X、png、pnm、gif、svg、ai、ps、cgm、fig、pcl、hpgl、regis、meta、tek。默认为 meta（GNU 图形元文件，可用 plot 查看）。

**-x** _min_ _max_
> X 轴范围。

**-y** _min_ _max_
> Y 轴范围。

**-L** _label_
> 顶部标签（标题）。

**-X** _label_
> X 轴标签。

**-Y** _label_
> Y 轴标签。

**-m** _type_
> 线条模式（0-5）。

**-S** _type_
> 符号类型。

**-C**
> 使用彩色。

**-g** _type_
> 网格类型（0-3）。

# DESCRIPTION

**graph** 是 GNU plotutils 的组成部分，用于根据数据文件创建二维图形。它从输入读取 x,y 坐标，并生成 PostScript、PNG、SVG 等多种格式的出版级质量图形。

该工具支持多个数据集、多种线条和符号样式，并为科学与技术绘图提供丰富的自定义选项。

# INPUT FORMAT

```
# Comment line
1 2.5
2 3.7
3 4.2
# Blank line separates datasets

1 1.5
2 2.8
```

# CAVEATS

属于 plotutils 软件包。交互性有限。对于复杂图形请考虑使用 gnuplot。默认输出类型是 GNU 元文件格式；使用 **-T** 选择具体格式，如 png、svg 或 ps。

# HISTORY

graph 属于 **GNU plotutils**，由 GNU 项目维护。该软件包提供一系列遵循 Unix 简单、可组合工具哲学的绘图工具。

# INSTALL

```apt: sudo apt install plotutils```

```dnf: sudo dnf install plotutils```

```pacman: sudo pacman -S plotutils```

```zypper: sudo zypper install plotutils```

```brew: brew install plotutils```

```nix: nix profile install nixpkgs#plotutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnuplot](/man/gnuplot)(1), [plot](/man/plot)(1)
