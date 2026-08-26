# TAGLINE

可扩展的力导向图布局引擎

# TLDR

**布局图形**

```sfdp [input.dot] -o [output.png]```

**输出为 SVG**

```sfdp -Tsvg [input.dot] -o [output.svg]```

**大型图形布局**

```sfdp -Goverlap=prism [input.dot] -o [output.png]```

**使用自定义参数**

```sfdp -Gsize="10,10" [input.dot] -o [output.png]```

# SYNOPSIS

**sfdp** [_-T format_] [_-o file_] [_-G options_] _input_

# PARAMETERS

**-T** _FORMAT_
> 输出格式（png、svg、pdf）。

**-o** _FILE_
> 输出文件。

**-G** _ATTR=VAL_
> 图属性。

**-N** _ATTR=VAL_
> 节点属性。

**-E** _ATTR=VAL_
> 边属性。

**-Goverlap** _MODE_
> 重叠消除方式。

# DESCRIPTION

**sfdp** 是一个可扩展的力导向布局引擎，用于对大型无向图进行布局。它是 Graphviz 套件的一部分，读取 DOT 格式的图，生成的可视化布局适用于拥有数千到数万个节点的图。

该算法采用多级方法：先把图逐步粗化为越来越小的表示形式，在最粗糙的层级上计算初始布局，然后逐层细化回来。这一策略使它能够处理比 **neato** 或 **fdp** 等简单力导向方法大得多的图，同时仍能产生美观的效果，揭示社区结构和聚类。

输出可以渲染为多种格式，包括 PNG、SVG 和 PDF。图、节点和边的属性通过标准 Graphviz 属性系统控制视觉外观。

# CAVEATS

内存占用高。大图速度慢。属于 Graphviz 软件包的一部分。

# HISTORY

**sfdp** 是 **Graphviz** 的一部分，为大型图布局实现了可扩展的力导向布局算法。

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

[dot](/man/dot)(1), [neato](/man/neato)(1), [fdp](/man/fdp)(1), [twopi](/man/twopi)(1)
