# TAGLINE

图表与流程图绘制程序

# TLDR

**启动 Dia** 图表编辑器

```dia```

**打开一个图表文件**

```dia [diagram.dia]```

**将图表导出**为图片

```dia -e [output.png] [diagram.dia]```

**导出为指定格式**

```dia -t [svg] -e [output.svg] [diagram.dia]```

**不启动 GUI 直接导出**

```dia --export=[output.png] --filter=[png] [diagram.dia]```

**列出可用的导出格式**

```dia --list-filters```

# SYNOPSIS

**dia** [_options_] [_file_...]

# PARAMETERS

_FILE_
> 要打开的图表文件。

**-e**, **--export** _FILE_
> 导出到指定文件。

**-t**, **--filter** _FORMAT_
> 导出格式：png、svg、eps、pdf 等。

**--size** _WxH_
> 位图导出的尺寸。

**--list-filters**
> 列出可用的导出过滤器。

**--nosplash**
> 启动时不显示启动画面。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Dia** 是一个类似 Microsoft Visio 的图表绘制程序。通过可自定义的形状库，它支持多种图表类型，包括流程图、网络拓扑图、UML 图和电路图等。

该应用提供基于 GTK 的界面，带有用于绘制、连接和格式化图元元素的工具。图表以 XML 格式（可选压缩）保存，并可导出为多种图像和矢量格式。

Dia 可通过自定义形状和 Python 脚本扩展，能适应专门的绘图需求。它被广泛用于技术文档和软件设计。

# CAVEATS

原生文件格式与其他绘图工具不同。某些导出格式可能丢失特性。复杂图表渲染可能较慢。字体渲染在不同平台上有所差异。

# HISTORY

Dia 由 **Alexander Larsson** 创建，首次发布于 **1998 年**。它作为商业绘图工具的自由软件替代品而开发，后来成为 GNOME 项目应用套件的一部分。

# INSTALL

```apt: sudo apt install dia```

```dnf: sudo dnf install dia```

```zypper: sudo zypper install dia```

```nix: nix profile install nixpkgs#dia```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[inkscape](/man/inkscape)(1), [graphviz](/man/graphviz)(1), [drawio](/man/drawio)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/dia)```

```[Homepage](https://wiki.gnome.org/Apps/Dia)```

<!-- verified: 2026-07-11 -->
