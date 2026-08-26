# TAGLINE

可视化已安装软件包之间的依赖关系

# TLDR

生成 **SVG 和 PNG** 图形

```pacgraph```

仅生成 **SVG** 图形

```pacgraph -s```

将摘要打印到**控制台**

```pacgraph -c```

覆盖默认的**文件名/位置**

```pacgraph -f [path/to/file]```

更改**非依赖软件包**的颜色

```pacgraph -t [color]```

更改**依赖软件包**的颜色

```pacgraph -d [color]```

更改**背景颜色**

```pacgraph -b [color]```

更改**软件包之间连线**的颜色

```pacgraph -l [color]```

# SYNOPSIS

**pacgraph** [_options_]

# PARAMETERS

**-s**, **--svg**
> 仅生成 SVG 输出（不生成 PNG）

**-c**, **--console**
> 将摘要打印到控制台而不生成图形

**-f**, **--file** _path_
> 输出文件名（不含扩展名）

**-t**, **--top** _color_
> 显式安装软件包的颜色

**-d**, **--dep** _color_
> 依赖软件包的颜色

**-b**, **--background** _color_
> 图形的背景颜色

**-l**, **--link** _color_
> 依赖连线的颜色

**-p**, **--point** _size_
> 字体点数大小

**-n**, **--no-compression**
> 禁用 SVGZ 压缩

**-e**, **--explicits**
> 仅包含显式安装的软件包

**-o**, **--optdeps**
> 包含可选依赖

**--show-req-by**
> 显示依赖所列软件包的软件包（反向依赖）

**-m** _repo_
> 只绘制指定的软件包/仓库及其依赖

# DESCRIPTION

**pacgraph** 可视化基于 Arch 的系统上已安装软件包之间的依赖关系。它生成的图形把软件包表示为节点，节点大小按磁盘占用量确定，并用连线将软件包与其依赖连接起来。

输出可以是 SVG 图像、PNG 图像或控制台文本摘要。该工具帮助用户了解系统的软件包结构、识别大型软件包并可视化依赖链。颜色用于区分显式安装的软件包和依赖软件包。

# CAVEATS

装有大量软件包的大型系统会生成复杂、难以阅读的图形。PNG 生成需要额外的依赖（通常是 graphviz 或 PIL）。**-f** 选项中不要包含文件扩展名。

# HISTORY

为 Arch Linux 开发，用于直观呈现软件包之间的关系。帮助用户了解磁盘占用在各软件包之间的分布情况，并通过显示哪些软件包几乎没有反向依赖来发现清理的机会。

# INSTALL

```aur: yay -S pacgraph```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pactree](/man/pactree)(8), [expac](/man/expac)(1)
