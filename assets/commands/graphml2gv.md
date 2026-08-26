# TAGLINE

GraphML 转 Graphviz DOT 格式转换器

# TLDR

**将 GraphML 转换为 DOT**

```graphml2gv [input.graphml] -o [output.gv]```

**输出到标准输出**

```graphml2gv [input.graphml]```

**处理多个文件**

```graphml2gv [file1.graphml] [file2.graphml] -o [output.gv]```

# SYNOPSIS

**graphml2gv** [_options_] [_files_]

# PARAMETERS

_FILES_
> GraphML 输入文件。若省略，则从标准输入读取。

**-o** _FILE_
> 将输出写入指定文件。

**-g** _gname_
> 使用 gname 作为生成图的名称。对于多张图，会追加一个整数。

**-v**
> 启用详细输出模式。

**-?**
> 打印用法信息并退出。

# DESCRIPTION

**graphml2gv** 将 GraphML 格式的图转换为 Graphviz DOT 格式。它让 GraphML 数据能够配合 Graphviz 可视化工具使用。

该工具负责在基于 XML 的 GraphML 格式与 GV（旧称 DOT）语言之间进行翻译。由于 GV 和 GraphML 的图模型和图形模型差异很大，这种转换是近似的。GraphML 的超边（hyperedge）或包含图的边等特性在 GV 中没有对应物。目前 graphml2gv 仅支持基本的图拓扑。

# CAVEATS

属于 Graphviz 软件包的一部分。不支持超边和嵌套图等 GraphML 特性。需要有效的 GraphML 输入。

# HISTORY

graphml2gv 是 **Graphviz** 项目的一部分，该项目由 **AT&T 实验室** 创建，用于处理图可视化的格式转换。

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

[gv2gml](/man/gv2gml)(1), [gml2gv](/man/gml2gv)(1), [dot](/man/dot)(1), [neato](/man/neato)(1), [graphviz](/man/graphviz)(1)
