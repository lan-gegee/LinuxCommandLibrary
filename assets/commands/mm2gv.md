# TAGLINE

将 Matrix Market 格式转换为 Graphviz

# TLDR

**将 Matrix Market 转换为图**

```mm2gv [matrix.mtx] -o [graph.gv]```

**输出 DOT 格式**

```mm2gv -T dot [matrix.mtx]```

**无向图**

```mm2gv -u [matrix.mtx]```

# SYNOPSIS

**mm2gv** [_options_] _file_

# PARAMETERS

_FILE_
> Matrix Market 文件。

**-o** _FILE_
> 输出文件。

**-T** _FORMAT_
> 输出格式。

**-u**
> 无向图。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mm2gv** 将 Matrix Market 格式转换为 Graphviz。Matrix Market 是一种稀疏矩阵格式。

该工具属于 Graphviz，可将稀疏矩阵可视化为图。

# CAVEATS

属于 Graphviz。仅支持 Matrix Market 格式。面向稀疏矩阵。

# HISTORY

mm2gv 是 **Graphviz** 的一部分，用于将 Matrix Market 稀疏矩阵转换为图格式。

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

[dot](/man/dot)(1), [gvpr](/man/gvpr)(1), [neato](/man/neato)(1)
