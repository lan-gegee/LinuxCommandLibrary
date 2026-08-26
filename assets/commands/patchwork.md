# TAGLINE

绘制 squarified 矩形树图的 graphviz 布局程序

# TLDR

**创建矩形树图可视化**

```patchwork -Tpng [data.gv] -o [treemap.png]```

**生成 SVG 矩形树图**

```patchwork -Tsvg [data.gv] -o [treemap.svg]```

**生成 PDF 输出**

```patchwork -Tpdf [data.gv] -o [treemap.pdf]```

# SYNOPSIS

**patchwork** [_options_] [_files_...]

# PARAMETERS

**-T** _format_
> 输出格式（png、svg、pdf 等）。

**-o** _file_
> 输出文件。

**-G** _attr=val_
> 设置图属性。

**-N** _attr=val_
> 设置节点属性。

# DESCRIPTION

**patchwork** 是一个用于 squarified 矩形树图的 Graphviz 布局程序。它将层次数据显示为嵌套矩形，面积与数值成比例。属于 Graphviz 可视化套件的一部分。

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

[dot](/man/dot)(1), [osage](/man/osage)(1), [neato](/man/neato)(1)
