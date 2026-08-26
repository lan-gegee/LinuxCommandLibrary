# TAGLINE

在终端中用数字生成迷你图（sparkline）

# TLDR

**由数字生成迷你图**

```spark [1] [5] [22] [13] [53]```

**通过 stdin 从逗号分隔的输入生成迷你图**

```echo "[1,2,3,4,5]" | spark```

**从文件生成迷你图**

```spark < [data.txt]```

**可视化序列产生的随机数据**

```seq [100] | sort -R | head -20 | spark```

**显示帮助**

```spark -h```

# SYNOPSIS

**spark** [**-h**] [_numbers_...]

# DESCRIPTION

**spark** 从一列数字生成迷你图（sparkline），在终端中将其渲染为 Unicode 方块字符（▁▂▃▄▅▆▇█）。数值按比例映射到八个高度级别，最小值对应最矮的柱条，最大值对应最高的柱条。

数字可以通过命令行参数、stdin 管道或文件提供。输入支持逗号分隔、空格分隔和换行分隔的格式，便于通过管道与其他 Unix 工具集成。

输出是使用标准 Unicode 字符的纯文本，因此在任何支持 Unicode 的终端中都能工作。迷你图适合一目了然地展示数据趋势，无需完整的绘图工具。

# CAVEATS

终端必须支持 Unicode。分辨率有限（8 个级别）。没有坐标轴或标签。以 bash shell 脚本编写，除 bash 外无其他依赖。

# HISTORY

**spark** 由 **Zach Holman** 创建，是一个用于命令行数据可视化的简单 bash 脚本。这一概念启发了 Ruby、Python、Haskell、Java 及其他语言的众多替代实现。

# INSTALL

```brew: brew install spark```

```nix: nix profile install nixpkgs#spark```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnuplot](/man/gnuplot)(1), [termgraph](/man/termgraph)(1)
