# TAGLINE

基于 ncurses 界面的交互式磁盘用量分析工具

# TLDR

**分析**当前目录的**磁盘用量**

```ncdu```

**分析指定目录**

```ncdu [/path/to/directory]```

**分析时排除匹配模式**

```ncdu --exclude [*.log]```

**以静默模式扫描**（适合慢速磁盘）

```ncdu -q [/path/to/directory]```

将扫描结果**导出**到文件

```ncdu -o [scan.json] [/path/to/directory]```

从文件**加载扫描结果**

```ncdu -f [scan.json]```

**启用文件删除功能**

```ncdu [/path] && ncdu```

**以 root 身份扫描**（针对整个文件系统）

```sudo ncdu /```

# SYNOPSIS

**ncdu** [_options_] [_path_]

# DESCRIPTION

**ncdu**（NCurses Disk Usage）是一款带 ncurses 界面的交互式磁盘用量分析工具。它扫描目录树，然后按大小排序展示结果，可在目录间导航，找出占用空间的文件。

界面按大小排序列出目录内容，并用图形条显示相对大小。用户可用方向键导航、进入目录，还可以选择直接删除文件或目录。

ncdu 特别适用于查找服务器上的大文件、清理磁盘空间以及了解存储使用模式。

# PARAMETERS

**-q**
> 静默模式，不显示扫描进度。

**-x**
> 不跨文件系统扫描。

**--exclude** _pattern_
> 排除匹配模式的文件。

**-X** _file_, **--exclude-from** _file_
> 从文件读取排除模式。

**-o** _file_
> 将扫描结果导出为 JSON 文件。

**-f** _file_
> 从文件加载扫描结果。

**-e**
> 启用 shell 扩展（用于导出）。

**-r**
> 只读模式（禁用删除）。

**--si**
> 使用 10 进制（SI）单位。

**--color** _scheme_
> 配色方案（dark、off）。

# KEYBOARD CONTROLS

**Up/Down**: Navigate
**Enter**: Enter directory
**d**: Delete selected item
**n**: Sort by name
**s**: Sort by size
**C**: Sort by count
**g**: Show percentage/graph
**i**: Show item info
**r**: Refresh/recalculate
**q**: Quit

# CAVEATS

删除是永久性的且不经过回收站。扫描大型文件系统耗时较长。由于硬链接的存在，文件计数可能与其他工具不同。非 root 运行时可能会跳过无权访问的目录。

# HISTORY

**ncdu** 由 **Yoran Heling** 于 **2007 年**创建，作为基于 ncurses 的交互式磁盘用量分析工具，是 du 的替代品。它的设计目的是解决用传统工具难以定位大文件的问题。ncdu 已成为系统管理的常用工具，2.0 版（用 Zig 重写）于 **2022 年**发布。

# INSTALL

```apt: sudo apt install ncdu```

```dnf: sudo dnf install ncdu```

```pacman: sudo pacman -S ncdu```

```apk: sudo apk add ncdu```

```zypper: sudo zypper install ncdu```

```brew: brew install ncdu```

```nix: nix profile install nixpkgs#ncdu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[du](/man/du)(1), [df](/man/df)(1), [dust](/man/dust)(1), [duf](/man/duf)(1)
