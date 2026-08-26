# TAGLINE

统计图的组成部分数量

# TLDR

**统计**图中的节点和边（默认行为）

```gc [graph.dot]```

**统计**连通分量数

```gc -c [graph.dot]```

**统计**所有内容：节点、边、连通分量和簇

```gc -a [graph.dot]```

只**统计**节点

```gc -n [graph.dot]```

**递归**进入子图并报告各自的计数

```gc -r [graph.dot]```

从标准输入**读取**图

```cat [graph.dot] | gc -a```

# SYNOPSIS

**gc** [**-necCaDUrsv?**] [_files_]

# DESCRIPTION

**gc** 是 **wc** 的图论版本：它读取一个或多个 DOT 格式的图，并将其节点、边、连通分量和簇的数量输出到标准输出。不带选项时报告节点和边的数量。给定多个图时，最后会输出一行总计。

每个输入文件可以包含多个图。每个图输出一行，后跟图的名称，因此结果可以直接交给其他文本工具处理。若未指定文件，**gc** 从标准输入读取。

簇是名称以 **cluster** 开头的子图，与 **dot** 绘制分组框时使用的约定相同。

# PARAMETERS

**-n**
> 统计节点。

**-e**
> 统计边。

**-c**
> 统计连通分量。

**-C**
> 统计簇（名称以 **cluster** 开头的子图）。

**-a**
> 统计以上全部；等价于 **-encC**。

**-r**
> 递归进入子图，报告各自的数量。

**-s**
> 静默模式：抑制输出，仅设置退出状态码。

**-D**
> 仅处理有向图。

**-U**
> 仅处理无向图。

**-v**
> 详细输出。

**-?**
> 打印用法信息。

# CAVEATS

输入必须是有效的 **DOT** 格式；格式错误的图会报错而不是给出计数。对有向图而言，统计的是弱连通分量。**-D** 和 **-U** 会跳过类型不符的图，因此过滤后的运行可能什么也不输出。

此命令与垃圾回收无关。在 PowerShell 中，**gc** 是 **Get-Content** 的别名；某些版本控制封装工具也把它别名为提交快捷方式，所以请先确认 **PATH** 上实际是什么程序。

# HISTORY

**gc** 属于 **Graphviz** 套件，由 **Stephen North**、**Eleftherios Koutsofios**、**Emden Gansner** 等人自 **20 世纪 90 年代初**起在 **AT&T Labs Research** 开发。Graphviz 于 **2004 年**开源，至今仍在积极维护。

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

[wc](/man/wc)(1), [acyclic](/man/acyclic)(1), [ccomps](/man/ccomps)(1), [sccmap](/man/sccmap)(1), [tred](/man/tred)(1), [gvpr](/man/gvpr)(1), [dot](/man/dot)(1)

# RESOURCES

```[Source code](https://gitlab.com/graphviz/graphviz)```

```[Homepage](https://graphviz.org/)```

```[Documentation](https://graphviz.org/docs/cli/gc/)```

<!-- verified: 2026-07-16 -->
