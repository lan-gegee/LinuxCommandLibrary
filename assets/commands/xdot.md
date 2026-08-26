# TAGLINE

交互式 Graphviz 图形查看器

# TLDR

在交互式查看器中**打开 dot 文件**

```xdot [path/to/graph.dot]```

**使用指定的布局引擎打开**

```xdot -f [neato] [path/to/graph.dot]```

**从 stdin 读取图形**

```[command] | xdot```

**以自定义窗口大小打开**

```xdot -g [800x600] [path/to/graph.dot]```

对环形图**使用 circo 布局**

```xdot -f circo [path/to/graph.dot]```

内联**生成并查看**图形

```echo "digraph { A -> B -> C }" | xdot```

# SYNOPSIS

**xdot** [_-f filter_] [_-n_] [_-g WxH_] [_file_]

# PARAMETERS

**-f** _filter_
> 使用指定的 Graphviz 布局引擎（dot、neato、twopi、circo、fdp、sfdp、osage、patchwork）。默认为 dot。

**-n**
> 假定输入已完成布局（不再计算布局）。

**-g** _WxH_
> 设置初始窗口几何尺寸（宽 x 高）。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**xdot** 是一款用于查看 Graphviz DOT 语言所描述图形的交互式查看器。它提供基于 GTK 的图形界面，支持平滑缩放和平移来浏览图形可视化结果。

与静态图片导出不同，xdot 以交互方式渲染图形，允许用户放大复杂图形、平移查看大型图表以及探索节点之间的关系。查看器支持鼠标滚轮缩放、点击拖拽平移和键盘导航。点击带有 URL 属性的节点或边会打开相应的链接。

该工具通过 **-f** 选项支持所有标准的 Graphviz 布局引擎，适用于各种图形类型：层次结构（dot）、无向弹簧模型（neato、fdp）、放射状（twopi）、环状（circo）和聚簇布局（osage、patchwork）。

Xdot 可以从文件或 stdin 读取输入，因此在动态生成图形的管道中很有用。检测到文件变化时会自动重新加载，这对迭代式图形开发很方便。

# CAVEATS

需要图形显示（X11 或带 XWayland 的 Wayland）。某些复杂的 DOT 属性渲染结果可能与静态 Graphviz 输出不完全一致。包含数千个节点的大型图形渲染性能可能较慢。并非所有 Graphviz 特性都支持交互式渲染。

# HISTORY

**xdot** 由 Jose Fonseca 创建，是一个使用 PyGTK（后来是 PyGObject/GTK3）的 Python 应用程序。它的开发是为了满足静态图片导出无法提供的交互式图形浏览需求。该工具作为开源项目持续维护，已被大多数 Linux 发行版打包收录。

# INSTALL

```pacman: sudo pacman -S xdot```

```brew: brew install xdot```

```nix: nix profile install nixpkgs#xdot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dot](/man/dot)(1), [neato](/man/neato)(1), [twopi](/man/twopi)(1), [circo](/man/circo)(1), [fdp](/man/fdp)(1), [graphviz](/man/graphviz)(1)
