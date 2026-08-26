# TAGLINE

GML 到 Graphviz DOT 格式的转换器

# TLDR

**将 GML 转换为 DOT**

```gml2gv [input.gml] -o [output.gv]```

**输出到 stdout**

```gml2gv [input.gml]```

# SYNOPSIS

**gml2gv** [_options_] [_files_]

# PARAMETERS

_FILES_
> GML 输入文件。省略时从 stdin 读取。

**-o** _FILE_
> 输出文件。省略时写入 stdout。

**-g** _NAME_
> 生成的图的名称。后续生成的图会追加一个整数。

**-v**
> 详细模式。

**-?**
> 显示用法信息并退出。

# DESCRIPTION

**gml2gv** 将图从 GML（Graph Modelling Language）格式转换为 Graphviz 使用的 DOT 格式。它让 GML 格式的图能够配合 Graphviz 可视化工具使用。

GML 是一种可移植的图描述格式。该转换器会保留图的结构，以便用 dot、neato 或其他 Graphviz 布局引擎进行渲染。

# CAVEATS

属于 Graphviz 的一部分。某些 GML 特性可能没有对应的 DOT 表达方式。请注意检查属性的保留情况。

# HISTORY

gml2gv 是 **Graphviz** 的一部分，提供常见图描述语言之间的格式转换。

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

[dot](/man/dot)(1), [gv2gml](/man/gv2gml)(1), [graphml2gv](/man/graphml2gv)(1)

# RESOURCES

```[Source code](https://gitlab.com/graphviz/graphviz)```

```[Homepage](https://graphviz.org/docs/cli/gml2gv/)```

<!-- verified: 2026-07-17 -->
