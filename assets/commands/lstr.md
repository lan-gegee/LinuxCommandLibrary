# TAGLINE

快速极简的目录树查看器

# TLDR

**显示目录树**

```lstr```

**显示指定路径的目录树**

```lstr [path/to/directory]```

**启动交互式 TUI 模式**

```lstr interactive```

**显示带 Git 状态的目录树**并遵循 .gitignore

```lstr -G -g```

**显示大小、权限和图标**

```lstr -s -p --icons```

**限制递归深度**

```lstr -L [2]```

**按大小排序，目录优先**

```lstr --sort size --dirs-first```

# SYNOPSIS

**lstr** [_options_] [_path_]

**lstr interactive** [_options_] [_path_]

# PARAMETERS

**-a**, **--all**
> 列出所有文件和目录，包括隐藏项。

**-d**, **--dirs-only**
> 只显示目录。

**-g**, **--gitignore**
> 遵循 `.gitignore` 及其他标准忽略文件。

**-G**, **--git-status**
> 显示文件和目录的 Git 状态标记。

**--icons**
> 显示特定于文件的图标（需要 Nerd Font）。

**--hyperlinks**
> 在支持的终端中将路径渲染为可点击的超链接。

**-L**, **--level** _DEPTH_
> 限制树的深度。

**-p**, **--permissions**
> 显示文件权限（类 Unix 系统）。

**-s**, **--size**
> 显示文件大小。

**--sort** _TYPE_
> 按 **name**、**size**、**modified** 或 **extension** 排序。

**--dirs-first**
> 目录排在文件之前。

**--case-sensitive**
> 使用区分大小写的排序。

**--natural-sort**
> 使用感知版本号的（"自然"）排序方式。

**-r**, **--reverse**
> 反转排序顺序。

**--dotfiles-first**
> 隐藏文件和文件夹排在前面。

**--color** _WHEN_
> 为输出着色（**always**、**auto**、**never**）。

**--expand-level** _LEVEL_
> 初始展开深度（仅限交互模式）。

# DESCRIPTION

**lstr** 是一个用 Rust 编写的快速、极简的目录树查看器。它并行扫描目录，并为经典的 **tree** 命令带来现代特性：`.gitignore` 支持、Git 状态标记、Nerd Font 图标、可点击超链接以及多种排序模式。

**interactive** 子命令会启动一个键盘驱动的 TUI（基于 ratatui 构建）用于浏览目录树。非交互式输出的设计使其可以干净地管道传送给 **fzf** 等工具。

# CAVEATS

图标显示需要终端中安装 Nerd Font。

# HISTORY

**lstr** 由 **bgreenwell** 创建，使用 **Rust** 编写。

# INSTALL

```brew: brew install lstr```

```nix: nix profile install nixpkgs#lstr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tree](/man/tree)(1), [ls](/man/ls)(1), [eza](/man/eza)(1)
