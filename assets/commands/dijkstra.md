# TAGLINE

最短路径图算法过滤器

# TLDR

**计算图中从源节点出发的最短路径**

```dijkstra -p [source_node] [input.dot]```

**输出所有节点对的距离矩阵**

```dijkstra -d [input.dot]```

**将处理后的图写入输出文件**

```dijkstra [input.dot] -o [output.dot]```

**计算最短路径并输出到文件**

```dijkstra -p [source_node] -o [output.dot] [input.dot]```

# SYNOPSIS

**dijkstra** [_options_] [_files_]

# PARAMETERS

**-o** _file_
> 输出文件。

**-p** _node_
> 设置用于最短路径计算的源节点。

**-d**
> 输出距离矩阵。

# DESCRIPTION

**dijkstra** 是一个专门的 Graphviz 过滤器，它实现 Dijkstra 最短路径算法用于图分析。它读取 DOT 格式的图描述，计算节点间的最短路径，并输出带有计算所得的距离或路径信息的修改后的图。

该工具可以计算距离矩阵，显示图中所有节点对之间的最短路径长度。它会修改图的属性以反映路径计算结果，这些结果随后可被其他 Graphviz 布局工具用于可视化。

此实用程序是 Graphviz 套件的一部分，主要用于网络分析、路由问题和图算法研究。它处理带权边的图，并能以与其他 Graphviz 工具兼容的多种格式输出结果。

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
