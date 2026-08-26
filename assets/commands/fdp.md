# TAGLINE

力导向图布局引擎

# TLDR

**从** DOT 文件**生成图**

```fdp -Tpng [graph.dot] -o [output.png]```

**输出 SVG 格式**

```fdp -Tsvg [graph.dot] -o [output.svg]```

**从 stdin 处理**

```echo 'graph { a -- b }' | fdp -Tpng -o [output.png]```

**设置图的属性**

```fdp -Gsize="10,10" -Tpng [graph.dot] -o [output.png]```

# SYNOPSIS

**fdp** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要处理的 DOT 图文件。

**-T** _FORMAT_
> 输出格式：png、svg、pdf、ps 等。

**-o** _FILE_
> 输出文件。

**-G** _ATTR=VALUE_
> 设置图属性。

**-N** _ATTR=VALUE_
> 设置节点属性。

**-E** _ATTR=VALUE_
> 设置边属性。

**-K** _LAYOUT_
> 覆盖布局引擎。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fdp** 是一个 Graphviz 布局引擎，使用力导向布局算法绘制无向图。它通过模拟相连与不相连节点之间的物理力来确定节点位置。

弹簧模型算法将边视为弹簧，将节点视为带电粒子。它迭代调整位置直到达到平衡，为多种类型的图生成美观的布局。

fdp 适用于无向图，其中节点聚类和边的长度应反映图的结构。

# CAVEATS

对非常大的图可能无法收敛。随机初始布局意味着结果不确定。更适合无向图而非有向图。

# HISTORY

fdp 是 **Graphviz**（AT&T 实验室的图可视化软件）的一部分。它实现了为图绘制研究开发的力导向布局算法，是 dot 层次化布局之外的另一种选择。

# INSTALL

```apt: sudo apt install graphviz```

```dnf: sudo dnf install graphviz```

```pacman: sudo pacman -S graphviz```

```apk: sudo apk add graphviz```

```zypper: sudo zypper install graphviz```

```brew: brew install graphviz```

```nix: nix profile install nixpkgs#graphviz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dot](/man/dot)(1), [neato](/man/neato)(1), [sfdp](/man/sfdp)(1)

# RESOURCES

```[Source code](https://gitlab.com/graphviz/graphviz)```

```[Homepage](https://graphviz.org/)```

<!-- verified: 2026-07-15 -->
