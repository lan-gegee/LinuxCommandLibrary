# TAGLINE

根据命令行数据在终端上绘制图表

# TLDR

从 TSV 数据**绘制条形图**

```cat [data.tsv] | uplot bar```

从 CSV **绘制折线图**

```cat [data.csv] | uplot line -d,```

**绘制直方图**

```seq 100 | awk '{print rand()}' | uplot hist```

# SYNOPSIS

**uplot** _subcommand_ [_options_]

# DESCRIPTION

**YouPlot** 是一个命令行工具，使用 Unicode 字符直接在终端中渲染条形图、折线图、散点图、直方图和箱线图。它从标准输入读取制表符分隔或自定义分隔符的数据，非常适合管道接收其他命令的输出。

# HISTORY

**YouPlot** 由 **kojix2**（Red Data Tools）创建，以 **Ruby** 编写。

# INSTALL

```brew: brew install youplot```

```nix: nix profile install nixpkgs#youplot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnuplot](/man/gnuplot)(1), [termgraph](/man/termgraph)(1)
