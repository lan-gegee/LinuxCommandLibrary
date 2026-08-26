# TAGLINE

以规范 DOT 格式美化输出图文件

# TLDR

**美化输出图文件**

```nop [graph.gv]```

**检查 DOT 语法**而不产生输出

```nop -p [graph.gv]```

**从 stdin 美化输出**

```cat [graph.gv] | nop```

# SYNOPSIS

**nop** [**-p?**] [_files_...]

# PARAMETERS

_FILES_
> 一个或多个要处理的 DOT 图文件。未指定时从 stdin 读取。

**-p**
> 不产生输出；只检查输入是否为合法的 DOT 语法。

**-?**
> 打印用法信息。

# DESCRIPTION

**nop** 读取 DOT 格式的图流，并将每张图以美化（规范）格式打印到 stdout。如果未给定文件，则从 stdin 读取。

该工具是 Graphviz 软件包的一部分，可用于规范化 DOT 文件或校验图的语法。

# CAVEATS

属于 Graphviz 软件包。只处理 DOT 图语言文件。不执行任何布局计算。

# HISTORY

nop 是 **Graphviz** 的一部分；Graphviz 是最初由 **AT&T Labs Research** 开发的开源图可视化软件。

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

[acyclic](/man/acyclic)(1), [gvpr](/man/gvpr)(1), [gvcolor](/man/gvcolor)(1), [ccomps](/man/ccomps)(1), [sccmap](/man/sccmap)(1), [tred](/man/tred)(1)
