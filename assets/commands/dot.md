# TAGLINE

层次化有向图渲染器

# TLDR

**渲染图为** PNG 图像

```dot -Tpng [graph.dot] -o [output.png]```

**渲染为 SVG**

```dot -Tsvg [graph.dot] -o [output.svg]```

**渲染为 PDF**

```dot -Tpdf [graph.dot] -o [output.pdf]```

**从标准输入渲染**

```echo "digraph { A -> B }" | dot -Tpng -o [output.png]```

**使用指定的布局**引擎

```dot -Kneato [graph.dot] -Tpng -o [output.png]```

**以自定义** DPI 渲染

```dot -Gdpi=[300] -Tpng [graph.dot] -o [output.png]```

根据输入文件**自动命名输出**

```dot -Tpng -O [graph1.dot] [graph2.dot]```

**把计算出的布局**连同坐标以 DOT 格式输出

```dot -Tdot [graph.dot] -o [laid_out.dot]```

**列出此构建支持的输出格式**

```dot -T?```

# SYNOPSIS

**dot** [**-K**_engine_] [**-T**_format_] [**-o**_outfile_] [_files_...]

# PARAMETERS

_FILES_
> DOT 语言格式的输入文件。未给出时读取标准输入。

**-T**_FORMAT_[**:**_RENDERER_]
> 输出格式：`png`、`svg`、`pdf`、`ps`、`json`、`dot`、`plain` 等。**-T?** 可列出你的构建支持的格式。

**-o** _FILE_
> 将输出写入 _FILE_ 而非标准输出。

**-O**
> 由输入文件名加格式后缀派生各输出文件名。适合批量处理。

**-K**_ENGINE_
> 使用指定布局引擎替代默认值：`dot`、`neato`、`fdp`、`sfdp`、`circo`、`twopi`、`osage`、`patchwork`。正是这一选项让同一个二进制文件可以充当其中任何一员。

**-G**_NAME_=_VALUE_
> 设置图属性，例如 **-Grankdir=LR** 或 **-Gdpi=300**。

**-N**_NAME_=_VALUE_
> 设置节点默认属性，例如 **-Nshape=box**。

**-E**_NAME_=_VALUE_
> 设置边默认属性，例如 **-Ecolor=blue**。

**-n**[**1**|**2**]
> 无操作布局：直接采用输入中 `pos` 属性给出的节点位置，而不重新计算。

**-x**
> 布局前先精简图。

**-y**
> 反转输出中的 y 坐标。

**-v**
> 详细输出：报告计时和进度信息。

**-q**[_LEVEL_]
> 抑制警告。

**-V**
> 打印 Graphviz 版本并退出。

# DESCRIPTION

**dot** 使用层次化分层布局绘制**有向**图：它先把节点分配到各个层级，使边始终朝同一方向，再在每个层级内排列节点以减少交叉。因此对于任何具有自然流向的内容，如调用图、构建依赖、状态机和组织结构图，dot 都是合适的选择。

它读取 **DOT 语言**——一种小型声明式语法，`digraph { a -> b }` 就是一个完整的程序——并输出到多种格式：位图（`png`、`jpg`）、矢量图（`svg`、`pdf`、`ps`）和数据格式（`json`、`plain`，以及 `dot` 本身，它会带上计算出的坐标完整往返图结构，供其他工具再次渲染）。

dot 是 Graphviz 布局家族的一员。其他成员仅在算法上不同，并且都可以通过此二进制文件的 **-K** 选项选用：`neato` 和 `fdp` 对无向图使用力导向布局，`circo` 是环形布局，`twopi` 是径向布局，`sfdp` 则是适用于超大图的可扩展多层级变体。

# CAVEATS

层次化布局的可扩展性不佳：超过几千个节点后 dot 会变慢，而且结果通常无论如何都难以阅读——此时应改用 `sfdp` 并配合过滤。布局是确定性的但不稳定，输入的一点小改动就可能重排整张图，这使得渲染出的图表难以做差异比较。可用的输出格式和字体取决于软件包的构建方式，所以才需要 **-T?**。另请注意 `dot` 既是程序名也是语言名，"dot 文件"可能指其中任一种。

# HISTORY

dot 源于 **AT&T 贝尔实验室**及其后的 AT&T 实验室研究部门约自 **1991 年**开始的图绘制研究；它实现的分层算法承袭自 Sugiyama 的工作，在这一谱系中则出自 Gansner、Koutsofios、North 和 Vo 之手。Graphviz 于 **2000 年**开源，此后其 DOT 语言已成为图描述的通用语言，被性能分析器、编译器、文档生成器和无数临时脚本输出使用。

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

[neato](/man/neato)(1), [circo](/man/circo)(1), [fdp](/man/fdp)(1), [twopi](/man/twopi)(1), [graphviz](/man/graphviz)(7)

# RESOURCES

```[Source code](https://gitlab.com/graphviz/graphviz)```

```[Homepage](https://graphviz.org)```

```[Documentation](https://graphviz.org/doc/info/command.html)```

<!-- verified: 2026-07-14 -->
