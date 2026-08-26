# TAGLINE

合并并打包互不相交的图

# TLDR

**合并已布局的图**

```gvpack [graph1.dot] [graph2.dot] > [merged.dot]```

**在图级别打包**（防止交错）

```gvpack -g [graph1.dot] [graph2.dot] > [merged.dot]```

**在节点级别打包**（忽略簇）

```gvpack -n [graph1.dot] [graph2.dot] > [merged.dot]```

**不打包直接合并**

```gvpack -u [graph1.dot] [graph2.dot] > [merged.dot]```

**按数组布局排列并设置边距**

```gvpack -array -m [20] [graph1.dot] [graph2.dot] > [merged.dot]```

**在输出上设置图属性**

```gvpack -G "label=[My Graph]" [graph1.dot] [graph2.dot] > [merged.dot]```

**完整流程：分解、布局、打包、渲染**

```ccomps -x [graph.dot] | dot | gvpack | neato -s -n2 -Tpng -o [output.png]```

# SYNOPSIS

**gvpack** [_options_] [_files_]

# PARAMETERS

**-g**
> 在图级别打包。占用更多空间，但可以防止一张图的各部分出现在另一张图的各部分之间。

**-n**
> 在节点级别打包，忽略簇。

**-u**
> 不打包直接合并。只是合并为单个图。

**-array**[_flags_][_n_]
> 将图按数组布局排列。可选标志：c（按列优先）、t/b/l/r（对齐上/下/左/右）、u（使用 sortv 属性）。可选 _n_ 设置列数（配合 c 则为行数）。

**-m** _margin_
> 每个部分周围的打包边距（以点为单位）。

**-o** _file_
> 输出到文件而非标准输出。

**-s** _name_
> 根图的名称（默认为 root）。

**-G** _name=value_
> 为生成的联合图添加属性。

**-v**
> 详细模式。

# DESCRIPTION

**gvpack** 读入一个图流，将其组合成单一布局，并生成一个作为输入图并集的单个图。输入必须是带布局信息的 dot 格式（由 dot 或 neato 等布局引擎在不加 -T 标志时生成）。默认情况下按簇级别打包，防止图的部分之间相互重叠。输出可以用 **neato -s -n2** 加所需的输出格式进行渲染。

# CAVEATS

所有输入图必须全是有向图或全是无向图。跨图的同名节点会被自动重命名以避免冲突。

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

[dot](/man/dot)(1), [neato](/man/neato)(1), [ccomps](/man/ccomps)(1), [fdp](/man/fdp)(1), [twopi](/man/twopi)(1)
