# TAGLINE

图流编辑器，类似于面向图的 awk

# TLDR

**运行 gvpr 脚本**

```gvpr -f [script.gvpr] [input.gv]```

**内联程序**

```gvpr 'N[color=="red"]' [input.gv]```

**输出到文件**

```gvpr -o [output.gv] -f [script.gvpr] [input.gv]```

**按属性选择节点**

```gvpr 'N[degree>3]' [graph.gv]```

# SYNOPSIS

**gvpr** [_-icnqV?_] [**-o** _outfile_] [**-a** _args_] _'prog'_ | **-f** _progfile_ [_files_]

# PARAMETERS

_'prog'_
> 内联 gvpr 程序文本（一系列谓词-动作子句）。未给出 **-f** 时必填。

_FILES_
> DOT 格式的输入图文件。未指定时从标准输入读取。

**-f** _progfile_
> 从 progfile 读取 gvpr 程序，而非从命令行读取。

**-o** _outfile_
> 将输出写入 outfile 而非标准输出。

**-a** _args_
> 向程序传递以空白分隔的参数字符串，可通过 ARGV/ARGC 访问。

**-c**
> 将源图用作输出图，从而原位编辑会被输出。

**-i**
> 在根图上下文中，将输出派生为节点诱导子图扩展。

**-n**
> 禁用图的预读（影响 **$NG** 变量）。

**-q**
> 抑制警告消息。

**-V**
> 打印版本信息并退出。

**-?**
> 显示用法信息并退出。

# DESCRIPTION

**gvpr**（旧名 **gpr**）是一种图模式扫描和处理语言，类似 **awk**，但处理对象是图而非文本。程序由模式-动作子句组成（**BEGIN**、**BEG_G**、针对节点的 **N**、针对边的 **E**、**END_G**、**END**），依次与每个输入图进行匹配。

对于访问到的每个节点或边，gvpr 按顺序求值各谓词，并对第一个（或每个）匹配项执行关联的动作。该语言提供类 C 的类型、关联数组和内置图函数，可用于对 DOT 图进行过滤、转换、重构或统计计算。

# CAVEATS

属于 Graphviz 软件包的一部分。模式-动作语言有一定学习曲线，在大型图上运行复杂程序可能较慢。

# HISTORY

gvpr 作为 **Graphviz** 项目的一部分在 **AT&T 实验室**开发而成，用于为图结构提供类似 AWK 的处理能力，取代了更早的 **gpr** 工具。

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

[dot](/man/dot)(1), [awk](/man/awk)(1), [gc](/man/gc)(1), [nop](/man/nop)(1)

# RESOURCES

```[Homepage](https://graphviz.org/)```

```[Source code](https://gitlab.com/graphviz/graphviz)```

```[Documentation](https://graphviz.org/doc/info/command.html)```

<!-- verified: 2026-07-17 -->
