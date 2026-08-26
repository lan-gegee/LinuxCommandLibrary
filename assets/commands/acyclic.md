# TAGLINE

将有向图变为无环图

# TLDR

**输出**图的副本，其中反转了足够的边使其成为无环图

```acyclic [graph.dot]```

将无环化结果**写入**文件

```acyclic -o [output.dot] [graph.dot]```

仅**测试**图是否无环（无输出，检查退出状态即可）

```acyclic -nv [graph.dot]```

# SYNOPSIS

**acyclic** [_-nv?_] [**-o** _outfile_] [_file_]

# DESCRIPTION

**acyclic** 是一个 Graphviz 过滤器，接收有向图作为输入，输出该图的副本，其中反转了足够多的边使图变为无环。被反转的边继承原边的全部属性。默认情况下程序从 stdin 读取并向 stdout 写入；可选的文件参数用于指定输入图的存储位置。

该工具可用于对图进行预处理，以满足要求无环输入的布局算法；也可用于验证依赖关系图——出现环通常意味着错误。退出状态会报告输入是无环的、含环的还是无向的。

# PARAMETERS

**-n**
> 不产生输出；返回值指示图是否无环。

**-v**
> 打印文件是无环、含环还是无向的信息。

**-o** _outfile_
> 将输出写入指定文件而非 stdout。

**-?**
> 打印用法信息。

# RETURN CODES

若图无环，**acyclic** 返回 **0**；若图含环，返回 **1**；若图为无向图，返回 **2**；发生任何错误时返回 **255**。

# CAVEATS

仅适用于 DOT 格式的有向图。acyclic 通过反转边（绝不删除边）使图无环。若图为 strict 图且包含长度为 2 的环，反转后的边会丢失属性。部分边属性是非对称的（指向头节点或尾节点），边反转时不会随之切换。

# HISTORY

**acyclic** 属于 Graphviz 项目，该项目自 **1991** 年起在 AT&T Labs Research 开发。收录此工具是为了给 **dot** 等层次布局算法提供图预处理支持，这些算法要求输入图为无环图。

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

[dot](/man/dot)(1), [tred](/man/tred)(1), [gc](/man/gc)(1), [gvpr](/man/gvpr)(1), [gvcolor](/man/gvcolor)(1), [ccomps](/man/ccomps)(1), [sccmap](/man/sccmap)(1)

# RESOURCES

```[Source code](https://gitlab.com/graphviz/graphviz)```

```[Homepage](https://graphviz.org/)```

```[Documentation](https://graphviz.org/docs/cli/acyclic/)```

<!-- verified: 2026-06-10 -->
