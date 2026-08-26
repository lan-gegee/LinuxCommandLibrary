# TAGLINE

将图分解为连通分量

# TLDR

**打印各分量**，每个分量作为独立的图

```ccomps -x [input.dot]```

**将每个分量写入**由 outfile 派生的带编号文件

```ccomps -x -o [out.dot] [input.dot]```

**只打印最大的分量**

```ccomps -z -x [input.dot]```

**统计分量数量**，仅向 stderr 输出计数

```ccomps -sv [input.dot]```

**提取包含指定节点的分量**

```ccomps -X [node_name] [input.dot]```

**按大小范围输出分量**（至少 5 个节点）

```ccomps -x -X%5- [input.dot]```

# SYNOPSIS

**ccomps** [**-svnxCe?**] [**-z**] [**-X**[_#%_]_v_] [**-o** _outfile_] [_files_]

# DESCRIPTION

**ccomps** 将图分解为其连通分量，并把各分量打印到标准输出。默认情况下，每个节点都会归入某个分量；加上 **-C** 后，cluster 子图结构也会参与连通性的判定。

对于无向图，它计算连通分量；对于有向图，它将边视为无向（弱连通）。该工具适合从图中过滤掉不相连的子图、分离出包含目标节点的分量，或在使用 **dot**、**neato** 等布局前对图进行预处理。

未给定输入文件时，图将从标准输入读取。

# PARAMETERS

**-s**
> 静默：不输出图；配合 **-v** 可用于只检查连通性。

**-x**
> 将每个连通分量作为独立图打印（而不是作为子图嵌入）。

**-X** _node_name_
> 只打印包含指定节点的分量。

**-X#** _index_[**-**[_last_]]
> 只打印给定索引处的分量或索引范围（last 可选）。

**-X%** _min_[**-**[_max_]]
> 只打印节点数落在给定大小范围内的分量。

**-z**
> 按大小对分量排序，最大者优先。仅在配合 **-x** 或 **-X#** 时有意义。

**-C**
> 计算分量时，除普通边连通性外还使用 cluster 子图。

**-e**
> 不在连通分量中诱导出边。

**-n**
> 不投影子图结构：分量只包含相关的节点和边。

**-v**
> 详细模式：向 stderr 打印节点数、边数和分量数。

**-o** _outfile_
> 将输出写到 _outfile_。有多个分量时文件会被编号（_outfile_、_outfile_\_1 等）。

**-?**
> 打印用法信息。

# CAVEATS

输入必须为 **DOT** 格式。对有向图只计算弱连通分量。内存占用随图的规模增长。若要让 **-X** _node_name_ 形式按预期工作，节点名必须唯一。**-X** 标志有多重含义：普通名称、以 **#** 为前缀的索引，或以 **%** 为前缀的大小选择器。

# HISTORY

**ccomps** 是 **Graphviz** 套件的一部分，最初于 **20 世纪 90 年代初**在 **AT&T Labs Research** 由 **Stephen North**、**Eleftherios Koutsofios**、**Emden Gansner** 等人开发。Graphviz 于 **2004** 年开源，至今仍在积极维护。

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

[dot](/man/dot)(1), [neato](/man/neato)(1), [gc](/man/gc)(1), [gvpr](/man/gvpr)(1)
