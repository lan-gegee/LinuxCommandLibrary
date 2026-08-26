# TAGLINE

图聚类布局工具

# TLDR

从图**生成聚类布局**

```cluster [input.dot] -o [output.dot]```

**使用指定算法聚类**

```cluster -C [algorithm] [input.dot]```

# SYNOPSIS

**cluster** [_options_] [_files_]

# DESCRIPTION

**cluster** 是 Graphviz 软件包中的一个图布局工具，用于识别并突出显示图结构中的簇（社区或分组）。它读取 DOT 格式的图，并为它们标注聚类信息。

该工具通过分析图的连通性来检测节点的自然分组。这些分组随后会在输出中表示为子图簇，可再由 dot 或 neato 等其他 Graphviz 布局引擎进一步处理以进行可视化。

它是 Graphviz 套件的一部分，与 dot、neato、fdp、sfdp、twopi 和 circo 并列，每个工具都为图可视化提供不同的布局算法。

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

[dot](/man/dot)(1), [neato](/man/neato)(1), [graphviz](/man/graphviz)(1)

# RESOURCES

```[Source code](https://gitlab.com/graphviz/graphviz)```

```[Homepage](https://graphviz.org/)```

<!-- verified: 2026-06-22 -->
