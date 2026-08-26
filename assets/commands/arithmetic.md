# TAGLINE

通过问答游戏练习基础数学

# TLDR

开始**算术问答**

```arithmetic```

指定要练习的一个或多个**运算符号**

```arithmetic -o [+|-|x|/]```

为题目数字指定**范围**

```arithmetic -r [7]```

# SYNOPSIS

**arithmetic** [**-o** _+-x/_] [**-r** _range_]

# DESCRIPTION

**arithmetic** 是一个简单的教育程序，通过算术题对用户进行测验。它会生成随机数学题并统计用户的正确率，以轻松有趣的方式练习心算。

默认情况下题目使用全部四种基本运算。范围选项控制题目中数字的大小。

# PARAMETERS

**-o** _operations_
> 指定要包含的运算：**+**（加法）、**-**（减法）、**x**（乘法）、**/**（除法）。默认为 **+** 和 **-**。

**-r** _range_
> 题目中使用的最大操作数（默认：**10**）。加法和乘法的操作数在 0 到 _range_ 之间；减法和除法的答案与第二个操作数都在该范围内，因此结果永远不会是负数或分数。

# CAVEATS

**arithmetic** 会反复出题，并对回答慢或答错的运算加大权重，使其更频繁出现。按 **Ctrl-D** 结束会话并打印答对题数和所用时间的汇总。

# HISTORY

**arithmetic** 是经典 BSD 游戏之一，源自 Unix 游戏合集，后被收入 **4.4BSD**。它随 **bsdgames** 软件包一起发布于大多数 Linux 发行版，作为一个简单的教育工具。

# INSTALL

```dnf: sudo dnf install bsd-games```

```pacman: sudo pacman -S bsd-games```

```apk: sudo apk add bsd-games```

```zypper: sudo zypper install bsd-games```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[bc](/man/bc)(1), [dc](/man/dc)(1)

# RESOURCES

```[Source code](https://github.com/jsm28/bsd-games)```

```[Homepage](https://www.polyomino.org.uk/computer/software/bsd-games/)```

<!-- verified: 2026-06-15 -->
