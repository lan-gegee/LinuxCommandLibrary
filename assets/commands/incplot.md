# TAGLINE

使用 Unicode 在终端中绘制图表的 CLI 工具

# TLDR

**绘制来自 stdin 的数据**

```echo "1 2 3 4 5" | incplot```

**从 CSV 文件绘图**

```cat [data.csv] | incplot```

**以指定的图表类型绘图**

```cat [data.csv] | incplot --chart [bar]```

# SYNOPSIS

**incplot** [_options_]

# DESCRIPTION

**incplot** 是一款命令行工具，使用 **Unicode 字符**在终端中绘制美观的图表。它会根据管道传入的数据自动推断显示内容和方式，具备诸多智能特性：从终端自动检测配色方案、自动过滤极端值、自动调整尺寸，以及带公制前缀缩放的数值标签。

该工具专为用户易用性和简洁性而设计——只需把数据管道传进来，无需多少配置即可得到可读的图表。

# CAVEATS

需要支持 Unicode 的终端才能正确渲染。输出质量取决于终端字体和字符支持。它面向快速可视化，而非出版级图表。

# HISTORY

**incplot** 由 **InCom-0** 创建，用 **C++** 编写。它的设计理念是作为一款快速可视化工具，优先考虑易用性和自动排版而非手动配置。

# INSTALL

```aur: yay -S incplot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnuplot](/man/gnuplot)(1), [youplot](/man/youplot)(1)
