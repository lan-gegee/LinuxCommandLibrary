# TAGLINE

用于簇状图的 Graphviz 布局引擎

# TLDR

**将簇状图排版**为 PNG

```osage -Tpng [graph.gv] -o [output.png]```

**生成 SVG 输出**

```osage -Tsvg [graph.gv] -o [output.svg]```

**生成 PDF 输出**

```osage -Tpdf [graph.gv] -o [output.pdf]```

**设置图的装箱模式**

```osage -Gpackmode=columns [graph.gv] -Tpng -o [output.png]```

# SYNOPSIS

**osage** [_options_] [_files_...]

# PARAMETERS

**-T** _format_
> 输出格式（png、svg、pdf、dot、ps 等）

**-o** _file_
> 输出文件

**-G** _attr=val_
> 设置图属性（如 pack、packmode）

**-N** _attr=val_
> 设置默认节点属性

**-E** _attr=val_
> 设置默认边属性

**-K** _layout_
> 覆盖布局引擎

**-O**
> 根据输入自动生成输出文件名

**-v**
> 详细模式

**-V**
> 打印版本并退出

# DESCRIPTION

**osage** 是一个面向簇状图的 Graphviz 布局引擎。它使用数组装箱算法递归地排列各簇子图，将每个簇视为待排布的矩形。在每一层，先对每个簇子图的内部进行布局，然后再确定簇与节点之间的相对位置。

图的 **pack** 和 **packmode** 属性控制每一层的布局方式。所有节点和簇定位完成后，才根据 **splines** 属性对边进行布线。

# CAVEATS

装箱阶段会忽略边，只在之后才布线。最适合簇结构比边的走向更重要的图。

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

[dot](/man/dot)(1), [neato](/man/neato)(1), [patchwork](/man/patchwork)(1), [fdp](/man/fdp)(1)
