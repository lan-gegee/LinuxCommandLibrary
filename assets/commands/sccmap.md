# TAGLINE

查找 Graphviz 图中的强连通分量

# TLDR

**查找强连通分量**

```sccmap [graph.dot]```

**输出到文件**

```sccmap -o [output.dot] [graph.dot]```

**显示统计信息**

```sccmap -v [graph.dot]```

**打印每个 SCC 的节点数**

```sccmap -S [graph.dot]```

**安静模式**

```sccmap -s [graph.dot]```

# SYNOPSIS

**sccmap** [_-dsSv_] [_-o file_] [_options_] _files_

# PARAMETERS

**-o** _FILE_
> 输出文件。

**-v**
> 详细统计信息。

**-s**
> 安静模式。

**-S**
> 打印每个强连通分量的节点数。

**-d**
> 分解图并为每个节点标注其所属 SCC 的编号。

# DESCRIPTION

**sccmap** 将有向图分解为强连通分量（SCC）。SCC 是节点的一个极大子集，其中任意节点都可从其他任意节点到达。它读取 DOT 格式的图，并将每个分量输出为独立的子图。

使用 **-v** 标志时，它会报告统计信息，包括分量的数量和大小，这有助于理解大型有向图的结构。Graphviz 图可视化软件包的一部分。

# CAVEATS

仅支持有向图。输入为 DOT 格式。Graphviz 软件包的一部分。

# HISTORY

**sccmap** 是 **Graphviz** 的一部分，后者是 AT&T Labs Research 开发的图可视化软件。

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

[dot](/man/dot)(1), [neato](/man/neato)(1), [tred](/man/tred)(1), [ccomps](/man/ccomps)(1), [acyclic](/man/acyclic)(1)
