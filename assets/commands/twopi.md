# TAGLINE

Graphviz 径向图布局引擎

# TLDR

**生成径向布局**并输出为 PNG

```twopi -Tpng -o [output.png] [input.dot]```

**渲染为 SVG 格式**

```twopi -Tsvg -o [output.svg] [input.dot]```

**为圆心指定根节点**

```twopi -Groot=[node_name] -Tpng -o [output.png] [input.dot]```

**设置环之间的径向间距**（单位：英寸）

```twopi -Granksep=[1.5] -Tpng -o [output.png] [input.dot]```

**使用 Voronoi 图消除节点重叠**

```twopi -Goverlap=false -Tpng -o [output.png] [input.dot]```

**从标准输入处理**

```cat [graph.dot] | twopi -Tpng > [output.png]```

# SYNOPSIS

**twopi** [**-G**_name_=_value_] [**-N**_name_=_value_] [**-E**_name_=_value_] [**-T**_format_] [**-o** _outfile_] [_files_]

# PARAMETERS

**-T** _format_
> 输出格式：png、svg、pdf、ps、jpg、gif 等多种格式。

**-o** _file_
> 输出文件名。若省略，则输出到标准输出。

**-G**_name_=_value_
> 设置图的属性。常用属性：root、ranksep、overlap。

**-N**_name_=_value_
> 设置默认节点属性。

**-E**_name_=_value_
> 设置默认边属性。

**-K** _layout_
> 指定布局引擎（默认：twopi）。

**-V**
> 打印版本信息。

**-s** _scale_
> 将输入缩放设为 _scale_。若省略，默认值为 72。

**-?**
> 打印用法信息。

# DESCRIPTION

**twopi** 是一个 Graphviz 布局程序，使用径向布局算法绘制图。它选择一个节点作为中心并放在原点，其余节点按其与中心的图距离递增，排列在同心圆上。

距中心距离为 1 的节点位于第一个环上，距离为 2 的节点位于第二个环上，依此类推。这种布局特别适合可视化层次结构、网络拓扑以及关系从中心点向外辐射的树形结构。

中心节点可通过 **root** 属性指定；否则 twopi 会随机选择一个离叶节点（度为 1 的节点）最远的节点。如果不存在叶节点，则任选一个节点。环之间的间距由 **ranksep** 控制（默认 0.75 英寸）。节点重叠可以通过 **overlap** 属性解决：**false** 使用 Voronoi 图，**scale** 将布局整体放大，**true**（默认）不做任何重新定位。

输入必须采用 DOT 图语言格式。twopi 是 Graphviz 套件的一员，与 dot、neato、circo、fdp 和 sfdp 并列。

# CAVEATS

对于大型图，随着外层环包含的节点呈指数级增长，径向布局可能变得杂乱。自动选择中心不一定总能产生最佳效果；手动指定根节点通常能提升布局质量。内存占用随图规模增长。

# HISTORY

**twopi** 于 **20 世纪 90 年代**作为 **AT&T Labs Research** 中 **Graphviz** 项目的一部分开发。径向布局算法基于 Graham Wills 在 **1997 年**图形绘制研讨会（Graph Drawing Symposium）上发表的工作。Graphviz 于 **2000 年**开源，至今仍在积极维护。

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

[dot](/man/dot)(1), [neato](/man/neato)(1), [circo](/man/circo)(1), [fdp](/man/fdp)(1), [sfdp](/man/sfdp)(1)
