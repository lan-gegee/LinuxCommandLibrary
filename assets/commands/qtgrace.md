# TAGLINE

基于 Qt 的科学 2D 绘图工具（Grace 的重新实现）

# TLDR

**绘制**一个或多个数据文件（前两列作为 X Y）

```qtgrace [path/to/file1.dat] [path/to/file2.dat]```

使用 **-nxy** 将**所有列**绘为 X Y1 Y2 ...

```qtgrace -nxy [path/to/file.dat]```

使用**对数** x 轴绘图

```qtgrace -log x [path/to/file.dat]```

以 **X Y DY** 方式绘图，两轴均用对数刻度

```qtgrace -log xy -settype xydy [path/to/file.dat]```

**显示帮助**

```qtgrace -help```

# SYNOPSIS

**qtgrace** [_options_] [_datafile_...]

# DESCRIPTION

**qtgrace** 是 **Grace**（xmgrace）的 Qt 重新实现版。Grace 是一款所见即所得的工具，用于显示、分析和制作二维科学图表。它保留了 Grace 大部分命令行接口，可用于非交互式和脚本化绘图。

数据文件通常是空白符分隔的列。选项控制坐标轴刻度、数据组类型（例如带误差棒的数据使用 **xydy**）、多列布局和批量输出。GUI 提供交互式编辑；CLI 则适合从脚本生成可复现的图表。

# PARAMETERS

**-nxy** _file_
> 将 _file_ 的所有列绘为 X Y1 Y2 ...

**-log** _x_|_y_|_xy_
> 在指定轴或两个轴上使用对数刻度

**-settype** _type_
> 数据组类型（例如 **xy**、**xydy**）

**-help**
> 显示帮助并退出

# HISTORY

**Grace** 起源于科学绘图软件 ACE/gr 的延续项目。**QtGrace** 将 Grace 的界面移植到 Qt 工具包上，提供 Windows、macOS 和 Linux 原生构建，同时保留兼容的 CLI 选项。

# INSTALL

```aur: yay -S qtgrace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnuplot](/man/gnuplot)(1), [matplotlib](/man/matplotlib)(1)

# RESOURCES

```[Homepage](https://sourceforge.net/projects/qtgrace/)```

```[Documentation](https://plasma-gate.weizmann.ac.il/Grace/)```

<!-- verified: 2026-07-14 -->
