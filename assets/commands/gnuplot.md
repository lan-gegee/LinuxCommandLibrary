# TAGLINE

命令驱动的绘图工具

# TLDR

**启动交互模式**

```gnuplot```

**运行脚本**

```gnuplot [script.gp]```

**快速绘图**

```gnuplot -e "plot sin(x)"```

**保持窗口打开**

```gnuplot -p -e "plot sin(x)"```

**设置终端类型**

```gnuplot -e "set terminal png; set output 'plot.png'; plot sin(x)"```

# SYNOPSIS

**gnuplot** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要运行的脚本文件。

**-e** _COMMAND_
> 执行命令。

**-p**, **--persist**
> 脚本执行后保持窗口打开。

**-c** _FILE_
> 带参数调用脚本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gnuplot** 是一个命令驱动的绘图工具，用于创建函数和数据的二维及三维图形。它支持多种输出格式，可生成出版级质量的图形。

该工具使用自己的脚本语言定制绘图。它支持 X11、PNG、PDF、SVG 等多种终端类型。它在科学可视化和数据分析领域被广泛使用。

# CONFIGURATION

**~/.gnuplot**
> 启动时执行的初始化文件，用于默认设置和自定义函数。

# CAVEATS

高级功能有一定学习曲线。脚本语法是 gnuplot 特有的。可用的终端类型很多。

# HISTORY

gnuplot 由 Thomas Williams 和 Colin Kelley 于 **1986** 年创建，现已成为科学与技术绘图的标准工具。

# INSTALL

```dnf: sudo dnf install gnuplot```

```pacman: sudo pacman -S gnuplot```

```apk: sudo apk add gnuplot```

```zypper: sudo zypper install gnuplot```

```brew: brew install gnuplot```

```nix: nix profile install nixpkgs#gnuplot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

