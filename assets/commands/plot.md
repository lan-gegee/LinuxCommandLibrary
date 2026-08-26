# TAGLINE

将 GNU 元文件转换为其他图形格式

# TLDR

**将元文件转换为 PNG**

```plot -T png [input.meta] > [output.png]```

**将元文件转换为 SVG**

```plot -T svg [input.meta] > [output.svg]```

**转换为 PostScript** 并指定页面尺寸

```plot -T ps --page-size [a4] [input.meta] > [output.ps]```

**在 X 窗口中显示元文件**

```plot -T X [input.meta]```

**从 stdin 读取**并以 PNM 输出

```cat [input.meta] | plot -T pnm > [output.pnm]```

**从多页元文件中提取单页**

```plot -T png -p [3] [input.meta] > [page3.png]```

# SYNOPSIS

**plot** [_options_] [_file_...]

# PARAMETERS

**-T** _type_, **--output-format** _type_
> 输出类型：X、png、pnm、gif、svg、ai、ps、cgm、fig、pcl、hpgl、regis、tek、meta（默认：meta）。

**-p** _n_, **--page-number** _n_
> 只输出元文件中的第 n 页。

**-s**, **--merge-pages**
> 将所有页面和帧合并为一页。

**--page-size** _size_
> ps、svg、ai、cgm、fig、pcl、hpgl 输出的页面尺寸（默认：letter）。接受 ISO 尺寸（a0-a4）和 ANSI 尺寸（a-e）。

**--bg-color** _color_
> 背景颜色名称（默认：white）。

**--bitmap-size** _WxH_
> X、png、pnm、gif 输出的位图尺寸（像素）（默认：570x570）。

**--pen-color** _color_
> 初始画笔颜色（默认：black）。

**-f** _size_, **--font-size** _size_
> 以显示宽度的比例表示的字号（默认：0.0525）。

**-F** _name_, **--font-name** _name_
> 初始字体名称。

**-W** _width_, **--line-width** _width_
> 以显示尺寸的比例表示的线宽。负值使用格式默认值。

**--max-line-length** _length_
> 折线在刷新前可包含的最大点数（默认：500）。

**--rotation** _angle_
> 旋转图形（0、90、180、270 度）。

**--emulate-color** _option_
> 设为 yes 时用灰度层次替换颜色。

**-O**, **--portable-output**
> 输出人类可读的 GNU 元文件格式而非二进制格式。

**--help**
> 显示帮助。

**--help-fonts**
> 显示所选输出格式可用的字体。

**--list-fonts**
> 单列列出可用字体。

**--version**
> 显示版本。

# DESCRIPTION

**plot** 是 GNU **plotutils** 软件包的一部分。它将 GNU 图形元文件（由 **graph** 等工具生成）转换为其他图形格式。输入文件可在命令行指定，也可从 stdin 读取。**-T** 选项用于选择输出格式。

支持的输出格式包括 X Window System 显示、PNG、PNM（PBM/PGM/PPM）、伪 GIF、SVG、Adobe Illustrator、PostScript、WebCGM、xfig、HP-GL/2、PCL 5、ReGIS 和 Tektronix。

# CAVEATS

**plot** 命令转换的是元文件；它不能直接绘制数据。请使用 plotutils 中的 **graph** 从数据生成元文件，再通过管道传给 **plot** 进行格式转换。交互式数据绘图请使用 gnuplot。

# HISTORY

**plot** 是 GNU **plotutils** 的一部分，最初由 **Robert Maier** 编写。plotutils 软件包提供生成二维矢量图形的工具，源自传统的 Unix 绘图实用程序。

# INSTALL

```apt: sudo apt install plotutils```

```dnf: sudo dnf install plotutils```

```pacman: sudo pacman -S plotutils```

```zypper: sudo zypper install plotutils```

```brew: brew install plotutils```

```nix: nix profile install nixpkgs#plotutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnuplot](/man/gnuplot)(1), [graph](/man/graph)(1)
