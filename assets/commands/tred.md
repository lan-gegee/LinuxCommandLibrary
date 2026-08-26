# TAGLINE

计算有向图的传递归约

# TLDR

**计算图的传递归约**

```tred [input.dot] > [output.dot]```

从标准输入处理

```cat [graph.dot] | tred > [reduced.dot]```

**显示详细输出**，包含被移除边的信息

```tred -v [input.dot]```

在用 dot 渲染**之前先对图做归约**

```tred [graph.dot] | dot -Tpng -o [output.png]```

# SYNOPSIS

**tred** [**-v**] [**-?**] [_files_]

# PARAMETERS

**-v**
> 详细输出。将被移除边的信息打印到标准错误。

**-?**
> 打印用法信息并退出。

# DESCRIPTION

**tred** 计算有向图的传递归约。它会移除由传递性蕴含的边，在保持可达关系不变的前提下简化图结构。

在传递归约中，如果存在从节点 A 经节点 B 到节点 C 的路径（A→B→C），那么直接的边 A→C 会作为冗余被移除。这对简化依赖图、继承层次结构以及其他因隐含关系而使可视化变得杂乱的有向图特别有用。

该工具从输入文件或标准输入读取 DOT 格式的图，并将归约后的图输出到标准输出。节点和子图会被保留，只移除冗余的边。无向图会被静默忽略。

tred 常用作 **dot** 的预处理器，以减少稠密图布局中的视觉杂乱。

# CAVEATS

如果图中有环，其传递归就不是唯一的。在这种情况下，tred 会发出警告。当前实现若在内部改用位图数据结构还可以更快。

# HISTORY

**tred** 隶属于 **Graphviz** 项目，最初于 **20 世纪 90 年代**在 **AT&T Labs Research** 开发，由 **Stephen C. North** 和 **Emden R. Gansner** 作为图形可视化工具包的一部分创建。Graphviz 于 **2000 年**开源，此后成为图布局和可视化的标准工具。

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

[dot](/man/dot)(1), [acyclic](/man/acyclic)(1), [gc](/man/gc)(1), [gvpr](/man/gvpr)(1), [ccomps](/man/ccomps)(1), [sccmap](/man/sccmap)(1)
