# TAGLINE

已移除的交互式 DOT 图查看器与编辑器

# TLDR

**dotty 已从 Graphviz 中移除。**请改用仍在维护的查看器。

用 **xdot** 交互式查看图

```xdot [graph.dot]```

渲染为 **SVG** 并在浏览器中打开

```dot -Tsvg [graph.dot] -o [graph.svg]```

用 **Gephi**、**yEd** 或实时预览编辑器可视化地编辑图

```dot -Tx11 [graph.dot]```

# SYNOPSIS

**dotty** [**-V**] [**-f**] [**-lm** _mode_] [_files_...]

# PARAMETERS

_FILES_
> 要打开的 DOT 文件。

**-V**
> 打印版本并退出。

**-f**
> 即使图已带有布局坐标也强制加载并重新排版。

**-lm** _MODE_
> 设置布局模式：**sync** 或 **async**。

# DESCRIPTION

**dotty** 曾是随 Graphviz 发布的 DOT 语言交互式图查看器和编辑器。与渲染静态图像的 **dot** 不同，dotty 会打开一个窗口，可以在其中平移、缩放、编辑和重新排版图，还能用鼠标增删节点和边。

它不是用 C 写的，而是用 **lefty**——一种同样随 Graphviz 附带的小型可编程图形语言。lefty 负责窗口和交互，布局则调用 `dot` 或 `neato` 完成。这种设计让 dotty 高度可脚本化，因为它的全部行为都是可以修改的源代码，但也把它绑死在一种无人使用的语言上。

**此命令已不存在。** lefty 连同 dotty 和 lneato 于 **2021 年 9 月**在构建系统中被禁用，**2022 年 1 月**起从 graphviz.org 发布的软件包中移除，最终从仓库中删除。当前的 Graphviz 发行版不包含其中任何一个。代码仍保留在项目的 git 历史中，供需要构建旧版本的人使用。

# CAVEATS

如果某个发行版仍在提供 **dotty**，那说明它打包的是旧版 Graphviz。该命令需要 X11，无法针对当前的 Graphviz 源码构建，也不会再获得任何修复。

交互式查看方面，**xdot** 是通常的替代品：它维护活跃，读取同样的 DOT 文件，支持平移、缩放和点击跳转。手动编辑图的话，yEd 或 Gephi 等通用图编辑器远比当年的 dotty 强大；而只是想快速看一眼的话，用 `dot -Tsvg` 渲染成 SVG 再用浏览器打开毫无成本。

# HISTORY

dotty 出自 **AT&T 贝尔实验室**及其后 AT&T 实验室研究部门的早期 Graphviz 工作，时间在 **20 世纪 90 年代初**，当时交互式 X11 查看器还是探索大图的唯一便捷途径。它由 Eleftherios Koutsofios 在自己的 **lefty** 语言之上编写。

它的移除过程即使按 Graphviz 的标准也称得上格外谨慎。维护者怀疑 lefty 已多年无人使用，但鉴于 Graphviz 部署之广，他们把移除分阶段安排在数年之内，给仍然依赖它的用户留出反对的时间。结果几乎没有人反对。

# INSTALL

```apt: sudo apt install graphviz```

```dnf: sudo dnf install graphviz```

```pacman: sudo pacman -S graphviz```

```zypper: sudo zypper install graphviz```

```brew: brew install graphviz```

```nix: nix profile install nixpkgs#graphviz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dot](/man/dot)(1), [xdot](/man/xdot)(1), [neato](/man/neato)(1), [graphviz](/man/graphviz)(7)

# RESOURCES

```[Source code](https://gitlab.com/graphviz/graphviz)```

```[Homepage](https://graphviz.org)```

```[Documentation](https://graphviz.org/docs/cli/dotty/)```

<!-- verified: 2026-07-14 -->
