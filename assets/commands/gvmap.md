# TAGLINE

从图创建地理风格地图

# TLDR

**从图创建地图**

```gvmap [input.gv] > map.gv```

**在输出中包含边**

```gvmap -e [input.gv] > map.gv```

**指定配色方案**（1：柔和色，2：蓝黄色，3：白红色）

```gvmap -c [2] [input.gv] > colored.gv```

**指定输出文件**

```gvmap -o [output.gv] [input.gv]```

**使用顶层簇子图进行聚类**

```gvmap -D [input.gv] > map.gv```

# SYNOPSIS

**gvmap** [_options_] [_files_]

# PARAMETERS

_FILES_
> 输入的 DOT 文件。

**-o** _FILE_
> 输出文件。

**-e**
> 在最终输出中包含边。

**-c** _K_
> 使用配色方案 K（1：柔和色，2：蓝黄色，3：白红色等）。

**-C** _K_
> 簇的最大数量。默认为 0（无限制）。

**-D**
> 使用顶层簇子图来确定聚类。

**-O**
> 不进行颜色分配优化。

**-a** _K_
> 沿标签边界框添加的人工点的平均数量。

**-m** _V_
> 在绘图周围生成 V 点宽的边距。

**-r** _K_
> 用于定义海洋和湖泊边界的随机点数量。0 表示自动。

**-s** _V_
> 海岸线和湖岸线的深度（以点为单位）。0 表示自动。

**-t** _N_
> 尝试 N 次以改善簇的邻接性。

**-v**
> 详细模式。

**-z** _COLOR_
> 设置多边形线条颜色。默认为黑色。

**-h**
> 打印用法并退出。

# DESCRIPTION

**gvmap** 以带有节点位置信息（由 sfdp 等 Graphviz 布局引擎生成）的 DOT 格式图作为输入，将相关节点分组为簇，并将其绘制为地理风格的地图区域。

该工具分析图结构，将节点聚为国家或地区，通过配色方案增加视觉样式，并可在输出中包含边。它通常作为 **sfdp** 和 **gvmap.sh** 组成的管道的一部分使用。

# CAVEATS

属于 Graphviz 软件包的一部分。输入图必须带有节点位置信息；请先运行 **sfdp** 之类的布局引擎。**gvmap.sh** 包装脚本可自动完成整个流程。

# HISTORY

gvmap 作为 **Graphviz** 的一部分在 **AT&T 实验室**开发而成，用于创建地理风格的图可视化效果。

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
