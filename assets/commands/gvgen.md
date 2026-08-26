# TAGLINE

生成 DOT 格式的各类图

# TLDR

**生成有 5 个顶点的星形图**

```gvgen -s [5] > star.gv```

**生成网格图**

```gvgen -g [3],[4] > grid.gv```

**生成 6 个顶点的完全图**

```gvgen -k [6] > complete.gv```

**生成高度为 4 的二叉树**

```gvgen -t [4] > tree.gv```

**生成有 10 个顶点的随机图**

```gvgen -r [10],[0.3] > random.gv```

**生成有向环**并写入文件

```gvgen -d -c [8] -o [cycle.gv]```

# SYNOPSIS

**gvgen** [**-dv?**] [_-c n_] [_-C x,y_] [_-g[f] x,y_] [_-h n_] [_-k n_] [_-b x,y_] [_-B x,y_] [_-m n_] [_-M x,y_] [_-p n_] [_-r x,y_] [_-R x_] [_-s n_] [_-S n_] [_-t n_] [_-T x,y_] [_-w n_] [_-n prefix_] [_-N name_] [_-o outfile_]

# PARAMETERS

**-s** _n_
> 生成 n 个顶点上的星形图。

**-g** [**f**]_x_,_y_
> 生成 x 乘 y 的网格。如果给出 f，网格会被折叠，用边连接相对的角落顶点。

**-k** _n_
> 生成 n 个顶点上的完全图。

**-c** _n_
> 生成具有 n 个顶点和边的环。

**-p** _n_
> 生成 n 个顶点上的路径。

**-t** _n_
> 生成高度为 n 的完全二叉树。使用 **-t** _h_,_n_ 可生成 n 叉树。

**-r** _x_,_y_
> 生成随机图。x 和 y 分别指定顶点数量和边的密度（介于 0 到 1 之间）。

**-R** _x_
> 生成 x 个顶点上的随机有根树。

**-h** _n_
> 生成 n 维超立方体（2^n 个顶点）。

**-b** _x_,_y_
> 生成 x 乘 y 的完全二部图。

**-C** _x_,_y_
> 生成 x 乘 y 的圆柱体。

**-B** _x_,_y_
> 生成 x 乘 y 的球体（带两个盖的圆柱体）。

**-m** _n_
> 生成每边有 n 个顶点的三角网格。

**-M** _x_,_y_
> 生成 x 乘 y 的莫比乌斯带。

**-T** _x_,_y_
> 生成 x 乘 y 的环面。

**-S** _n_
> 生成 n 阶谢尔宾斯基图。

**-w** _n_
> 生成 n 个顶点上的轮形图。

**-d**
> 使生成的图为有向图。

**-n** _prefix_
> 在整型节点名前添加前缀。

**-N** _name_
> 将 name 用作图的名称。

**-o** _outfile_
> 将输出写入指定文件而非标准输出。

**-u** _seed_
> 指定随机数生成器的种子。

**-v**
> 详细输出。

**-?**
> 打印用法信息。

# DESCRIPTION

**gvgen** 以 DOT 格式生成各种简单的、规则结构的抽象图。它创建的标准图结构可用于测试、可视化和算法演示。

该工具支持星形、网格、树、完全图、环、路径、随机图、超立方体、二部图、圆柱体、环面、莫比乌斯带、谢尔宾斯基图等。输出为 Graphviz DOT 格式，可用布局引擎进行可视化。

# CAVEATS

属于 Graphviz 软件包的一部分。如果不通过 **-u** 指定种子，每次运行生成的随机图都会不同。大型图的渲染可能较慢。

# HISTORY

gvgen 作为 **Graphviz** 项目的一部分开发而成，用于提供测试和演示所需的示例图生成功能。

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

[dot](/man/dot)(1), [neato](/man/neato)(1), [sfdp](/man/sfdp)(1), [gvpack](/man/gvpack)(1)
