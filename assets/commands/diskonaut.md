# TAGLINE

基于终端、带矩形树图可视化的磁盘空间浏览器

# TLDR

**分析当前目录**

```diskonaut```

**分析指定目录**

```diskonaut [/path/to/directory]```

显示**表观大小**而非磁盘占用

```diskonaut --apparent-size [directory]```

**禁用删除确认**提示

```diskonaut --disable-delete-confirmation [directory]```

# SYNOPSIS

**diskonaut** [_options_] [_folder_]

# PARAMETERS

_FOLDER_
> 要分析的目录（默认为当前目录）。

**-a**, **--apparent-size**
> 显示文件表观大小而非磁盘占用。

**-d**, **--disable-delete-confirmation**
> 删除文件或文件夹时跳过确认提示。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**diskonaut** 是一个基于终端的磁盘空间浏览器，以交互式矩形树图可视化展示目录大小。它支持键盘导航来探索磁盘占用情况，快速找出占用空间的目录和文件。

矩形树图视图用与大小成比例的嵌套矩形表示目录，直观呈现磁盘空间分布。通过导航可以深入目录并查看详细的大小信息。

diskonaut 用 Rust 编写并注重性能，能够快速分析大型目录树，同时保持界面响应流畅。

# CAVEATS

需要足够大的终端才能进行有意义的可视化。非常深的目录结构可能难以浏览。对大型文件系统的初次扫描需要时间。

# HISTORY

diskonaut 作为图形化磁盘用量分析工具的现代终端替代品而创建。它用 Rust 编写，将 TUI 应用的易用性与 GUI 工具中流行的矩形树图表示相结合。

# INSTALL

```dnf: sudo dnf install diskonaut```

```pacman: sudo pacman -S diskonaut```

```brew: brew install diskonaut```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ncdu](/man/ncdu)(1), [du](/man/du)(1), [duf](/man/duf)(1), [dust](/man/dust)(1)

# RESOURCES

```[Source code](https://github.com/imsnif/diskonaut)```

<!-- verified: 2026-07-11 -->
