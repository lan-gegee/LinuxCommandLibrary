# TAGLINE

图形化磁盘用量分析器

# TLDR

**分析**磁盘用量

```baobab```

分析**指定目录**

```baobab [/path/to/directory]```

# SYNOPSIS

**baobab** [_directory_]

# DESCRIPTION

**baobab**（又名 GNOME Disk Usage Analyzer）是一款用于可视化磁盘空间占用的图形工具。它以树状视图显示目录大小，并提供交互式的矩形树图或环形图可视化。

借助该应用，可以轻松找出占用磁盘空间的大文件和大目录。

# FEATURES

- 目录树状视图
- 矩形树图可视化
- 环形图（旭日图）视图
- 文件与文件夹大小
- 交互式导航
- 远程文件系统支持
- 扫描历史记录

# INTERFACE

提供多种可视化模式：
- **List view** - 传统目录树
- **Treemap** - 矩形面积图
- **Rings chart** - 以同心圆展示层级关系

# CAVEATS

扫描大文件系统可能较慢。远程文件系统需要网络访问。某些目录需要提升权限才能扫描。结果可能不反映真实磁盘占用（稀疏文件、压缩）。

# HISTORY

**Baobab** 由 Fabio Marzocca 于 **2005** 年前后创建，此后成为 GNOME 标准的磁盘用量分析器，名字来源于猴面包树。

# INSTALL

```apt: sudo apt install baobab```

```dnf: sudo dnf install baobab```

```pacman: sudo pacman -S baobab```

```apk: sudo apk add baobab```

```zypper: sudo zypper install baobab```

```brew: brew install baobab```

```nix: nix profile install nixpkgs#baobab```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[du](/man/du)(1), [ncdu](/man/ncdu)(1)
