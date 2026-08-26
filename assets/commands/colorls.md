# TAGLINE

带颜色和图标的增强版 ls

# TLDR

**列出文件**并显示颜色和图标

```colorls```

**列出包括隐藏文件在内的所有文件**

```colorls -a```

**以长格式列出**详细信息

```colorls -l```

**以目录树视图列出**

```colorls --tree```

**按修改时间排序**

```colorls -t```

**只列出目录**

```colorls -d```

**只列出文件**

```colorls -f```

**以人类可读格式显示文件大小**

```colorls -lh```

# SYNOPSIS

**colorls** [_-alrtdfsgh_] [_--tree_] [_--report_] [_--gs_] [_--sd_] [_path ..._]

# PARAMETERS

**-a**, **--all**
> 显示隐藏文件（以 . 开头）。

**-l**, **--long**
> 以长格式显示权限、所有者、大小和日期。

**-r**, **--reverse**
> 反转排序顺序。

**-t**, **--sort-time**
> 按修改时间排序（最新的在前）。

**-d**, **--dirs**
> 只显示目录。

**-f**, **--files**
> 只显示文件。

**-s**, **--sort-size**
> 按文件大小排序。

**-1**
> 每行一个条目。

**--tree** [_depth_]
> 显示目录树（可选限制深度）。

**--report**, **--r**
> 显示文件和目录的简要统计。

**--gs**, **--git-status**
> 显示每个文件的 git 状态。

**--sd**, **--sort-dirs**
> 目录排在前面。

**--sf**, **--sort-files**
> 文件排在前面。

**-h**, **--human-readable**
> 以人类可读格式显示文件大小（K、M、G）。

**--light**
> 使用浅色配色方案。

**--dark**
> 使用深色配色方案（默认）。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.config/colorls/dark_colors.yaml**
> 深色终端背景的配色方案。

**~/.config/colorls/light_colors.yaml**
> 浅色终端背景的配色方案。

**~/.config/colorls/file_aliases.yaml**
> 自定义文件类型关联和图标映射。

# DESCRIPTION

**colorls** 是一个 Ruby gem，为标准的 ls 命令提供增强、多彩的替代方案。它显示文件列表时带有图标（基于 Nerd Fonts）、按文件类型着色，并提供 git 状态集成和树形视图等额外功能。

每种文件类型都有独特的图标和颜色：目录、可执行文件、图片、文档、归档等。这种视觉区分让人更容易快速浏览目录内容。图标需要安装 Nerd Font（打过补丁、内置图标的字体）才能正确显示。

Git 集成可显示仓库中文件的状态：已修改、已暂存、未跟踪等。树形视图以层级方式展示目录结构，类似于 **tree** 命令，但采用 colorls 的样式。

可以通过 **~/.config/colorls/dark_colors.yaml** 和 **~/.config/colorls/light_colors.yaml** 自定义颜色，通过 **~/.config/colorls/file_aliases.yaml** 自定义文件类型关联。

# CAVEATS

需要 Ruby 和 colorls gem（gem install colorls）。图标需要安装并在终端中配置 Nerd Font。对包含大量文件的目录，性能可能比标准 ls 慢。某些终端模拟器可能无法正确渲染颜色或图标。

# HISTORY

**colorls** 由 Athitya Kumar 创建并以 Ruby gem 的形式发布。它凭借美观的外观和实用的特性在终端美化社区广受欢迎。该项目源于人们对更具视觉信息量的目录列表工具的需求。类似项目还有 **exa**（现为 **eza**）和 **lsd**，它们以不同语言实现了相近的功能。

# INSTALL

```nix: nix profile install nixpkgs#colorls```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ls](/man/ls)(1), [exa](/man/exa)(1), [eza](/man/eza)(1), [lsd](/man/lsd)(1), [tree](/man/tree)(1)

# RESOURCES

```[Source code](https://github.com/athityakumar/colorls)```

<!-- verified: 2026-06-22 -->
