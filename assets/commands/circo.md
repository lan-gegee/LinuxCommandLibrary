# TAGLINE

Graphviz 圆形图布局引擎

# TLDR

**以圆形布局渲染图为 PNG**

```circo -Tpng [input.dot] -o [output.png]```

**渲染为 SVG 格式**

```circo -Tsvg [input.dot] -o [output.svg]```

**渲染为 PDF 格式**

```circo -Tpdf [input.dot] -o [output.pdf]```

**从 stdin 读取并输出到 stdout**

```cat [input.dot] | circo -Tpng > [output.png]```

**显示可用的输出格式**

```circo -T?```

# SYNOPSIS

**circo** [**-T**_format_] [**-o** _outfile_] [**-K**_layout_] [**-G**_name=value_] [**-N**_name=value_] [**-E**_name=value_] [_files..._]

# DESCRIPTION

**circo** 是一个 Graphviz 布局引擎，生成圆形的图布局。它会识别双连通分量并将节点排列到圆上，尽可能把边放在圆的周长附近，以最小化边的交叉。

该工具对块-割点树使用递归径向算法。外平面组件则采用平面布局。它适用于电信网络和环形结构。

# PARAMETERS

**-T**_format_
> 输出格式：png、svg、pdf、ps、dot、json、gif、jpg 等

**-o** _outfile_
> 将输出写入文件而非 stdout

**-G**_name=value_
> 设置图属性

**-N**_name=value_
> 设置默认节点属性

**-E**_name=value_
> 设置默认边属性

**-K**_layout_
> 覆盖布局引擎

**Circo-specific graph attributes:**

**root=**_nodename_
> 用作布局根节点的节点

**mindist=**_value_
> 节点之间的最小间距（默认：1.0）

**oneblock=**_true_
> 将整张图画在一个圆周围

# CAVEATS

属于 Graphviz 软件包的一部分；所有布局引擎（dot、neato、circo、twopi、fdp、sfdp）共享相同的命令行接口，并以插件形式实现。

# HISTORY

**Circo** 实现了 Six 和 Tollis（GD '99、ALENEX '99）以及 Kaufmann 和 Wiese（GD '02）描述的算法。Graphviz 最初由 AT&T Labs Research 开发。

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

[dot](/man/dot)(1), [neato](/man/neato)(1), [twopi](/man/twopi)(1), [fdp](/man/fdp)(1), [sfdp](/man/sfdp)(1)

# RESOURCES

```[Source code](https://gitlab.com/graphviz/graphviz)```

```[Documentation](https://graphviz.org/docs/layouts/circo/)```

<!-- verified: 2026-06-22 -->
