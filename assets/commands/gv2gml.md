# TAGLINE

将 Graphviz DOT 格式转换为 GML

# TLDR

**将 DOT 转换为 GML**

```gv2gml [input.gv] -o [output.gml]```

**输出到标准输出**

```gv2gml [input.dot]```

**处理多个文件**

```gv2gml [file1.gv] [file2.gv] -o [output.gml]```

# SYNOPSIS

**gv2gml** [_-y_] [_-?_] [**-o** _outfile_] [_files_]

# PARAMETERS

_FILES_
> 输入的 DOT/GV 文件。未指定时从标准输入读取。

**-o** _outfile_
> 将输出写入 outfile 而非标准输出。

**-y**
> 使用 yWorks.com 的 GML 属性约定而非普通 GML 规范。

**-?**
> 显示用法信息并退出。

# DESCRIPTION

**gv2gml** 将以 DOT 语言表示的图转换为 GML（Graph Modelling Language），这是一种供 yEd 和 Gephi 等图分析与可视化工具使用的交换格式。

它是 **gml2gv** 的反方向对应工具，两者由同一份源码构建，根据程序名称分派行为。

# CAVEATS

不支持子图和簇。GML 无法声明默认的节点/边属性，因此 gv2gml 会在每个节点和边上显式重复每个属性。

# HISTORY

gv2gml 是 **Graphviz** 项目的一部分，由 **AT&T 实验室**创建，用于图格式转换。

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

[dot](/man/dot)(1), [gml2gv](/man/gml2gv)(1), [graphml2gv](/man/graphml2gv)(1), [gxl2gv](/man/gxl2gv)(1)

# RESOURCES

```[Homepage](https://graphviz.org/)```

```[Source code](https://gitlab.com/graphviz/graphviz)```

```[Documentation](https://graphviz.org/doc/info/command.html)```

<!-- verified: 2026-07-17 -->
