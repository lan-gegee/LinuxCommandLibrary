# TAGLINE

将图分解为双连通分量

# TLDR

**将图分解为双连通分量**

```bcomps [input.gv] > [output.gv]```

**打印块和割点的数量**

```bcomps -v [input.gv]```

**将每个分量打印为独立的图**

```bcomps -x [input.gv]```

**打印块-割点树**

```bcomps -t [input.gv]```

**将各分量写入单独的文件**

```bcomps -o [output.gv] [input.gv]```

**静默模式，仅显示统计信息**

```bcomps -sv [input.gv]```

# SYNOPSIS

**bcomps** [_-stvx?_] [_-o_ _outfile_] [_files_]

# DESCRIPTION

**bcomps** 将图分解为其双连通分量，并把分量打印到标准输出。双连通分量是指移除任意单个顶点后仍然保持连通的极大子图。

该工具是 Graphviz 图可视化套件的一部分，处理 DOT 语言图文件。

# PARAMETERS

**-s**
> 静默模式；不打印输出的图（隐含 -v）

**-t**
> 打印底层的块-割点树

**-v**
> 打印块和割点的数量

**-x**
> 将每个双连通分量作为独立的根图打印

**-o** _outfile_
> 将每个根图写入由 outfile 派生的不同文件

**-?**
> 显示帮助信息

# OUTPUT FORMAT

默认情况下，每个输入图会连同作为子图的块一起打印。子图名称由输入图名、"_bcc_" 和块编号拼接而成。

同时使用 -o 和 -x 时，每个块会被写入单独的文件。如果 _outfile_ 没有后缀，第 i 个图的第 n 个块写入 outfile_n_i（第 0 个图的第 0 个块直接写入 _outfile_ 本身）。如果 _outfile_ 带后缀（如 base.sfx），文件遵循相同模式并附加 .sfx。块-割点树写入 outfile_n_T。

# RETURN VALUES

**0**
> 所有输入图都是双连通的

**非零**
> 任意图有多个块，或发生了错误

# CAVEATS

输入文件必须为 Graphviz DOT 格式。该工具用于识别分隔各个分量的关节点（割点）。大图可能需要较长的处理时间。

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

[ccomps](/man/ccomps)(1), [gc](/man/gc)(1), [dot](/man/dot)(1), [gvpr](/man/gvpr)(1), [sccmap](/man/sccmap)(1), [tred](/man/tred)(1), [acyclic](/man/acyclic)(1)
