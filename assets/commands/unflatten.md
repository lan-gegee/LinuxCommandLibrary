# TAGLINE

改善 Graphviz 图的纵横比

# TLDR

**调整图布局**并写入输出文件

```unflatten [input.dot] -o [output.dot]```

**将叶子边的长度错开**，范围在 1 与指定上限之间

```unflatten -l [3] [input.dot]```

**扇形展开**入度和出度均为 1 的节点（需要 -l）

```unflatten -f -l [3] [input.dot]```

**将不相连的节点**组成长为至多指定长度的链

```unflatten -c [5] [input.dot]```

**通过管道交给 dot 处理**以获得更好的布局

```unflatten -l [4] [input.dot] | dot -Tpng -o [output.png]```

# SYNOPSIS

**unflatten** [_-l limit_] [_-f_] [_-c len_] [_-o file_] _input_

# PARAMETERS

**-l** _len_
> 将叶子边的最小长度在 1 与 _len_ 之间错开

**-f**
> 扇形展开入度和出度均为 1 的节点（仅在与 -l 一起使用时生效）

**-c** _len_
> 将不相连的节点组成为至多 _len_ 个节点的链

**-o** _file_
> 将输出写入 _file_ 而不是 stdout

# DESCRIPTION

**unflatten** 是一个 Graphviz 预处理器，它通过打散长节点链来改善有向图的纵横比。其原理是错开链中节点的位置并转换部分边，从而增大图相对于高度的宽度。

该工具设计为在 **dot** 布局引擎之前使用的预处理步骤。当图中大量节点排成长长的垂直链时，dot 往往会产生又高又窄的布局。先运行 unflatten 调整图结构，dot 就能产生更均衡、更易读的结果。

选项控制发生错开前的最大链长度，以及是否应扇形展开叶子节点。该工具读取 DOT 格式输入并生成修改后的 DOT 输出，可以直接通过管道传给 dot 或其他 Graphviz 布局引擎。

# CAVEATS

设计为 **dot** 布局引擎之前的预处理步骤。没有 **-l** 时 **-f** 选项无效。必须安装 Graphviz。

# HISTORY

**unflatten** 是 **Graphviz** 的一部分，用于改善含有长节点链的图的纵横比。

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

[dot](/man/dot)(1), [neato](/man/neato)(1), [gvpr](/man/gvpr)(1)
