# TAGLINE

用 Rust 编写的现代 ls 替代品

# TLDR

带颜色**列出文件**

```exa```

以**长格式**显示详细信息

```exa -l```

**显示隐藏文件**

```exa -a```

**树状视图**

```exa --tree```

**显示 git 状态**

```exa -l --git```

**按修改时间排序**

```exa -l --sort=modified```

**以人类可读格式显示文件大小**

```exa -lh```

**扩展属性**

```exa -l --extended```

# SYNOPSIS

**exa** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要列出的文件或目录。

**-l**, **--long**
> 长格式。

**-a**, **--all**
> 显示隐藏文件。

**--tree**
> 树状视图。

**--git**
> 显示 git 状态。

**-s**, **--sort** _FIELD_
> 按指定字段排序。

**-h**, **--header**
> 显示表头行。

**--icons**
> 显示文件图标。

**--color** _WHEN_
> 颜色模式：always、auto、never。

**--help**
> 显示帮助信息。

# DESCRIPTION

**exa** 是一个用 Rust 编写的现代 ls 替代品。它提供彩色输出、git 集成、树状视图，以及以友好格式呈现的更详细的文件信息。

该工具默认使用人类可读的大小单位和合理的配色。git 集成可在仓库目录中显示文件状态。扩展属性和元数据也易于查看。

在大多数操作上 exa 比 ls 更快，同时提供多得多的功能。

# CAVEATS

输出格式与 ls 不同。可能破坏依赖 ls 输出的脚本。图标需要字体支持。自 2023 年起不再维护（见 eza 分支）。

# HISTORY

exa 由 **Benjamin Sago**（ogham）于 **2014 年**前后创建，作为现代化的 ls 替代品。其开发于 **2023 年**停止，由活跃维护的分支 **eza** 延续。

# INSTALL

```apt: sudo apt install eza```

```dnf: sudo dnf install eza```

```pacman: sudo pacman -S eza```

```apk: sudo apk add eza```

```zypper: sudo zypper install eza```

```brew: brew install eza```

```nix: nix profile install nixpkgs#eza```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ls](/man/ls)(1), [eza](/man/eza)(1), [lsd](/man/lsd)(1), [tree](/man/tree)(1)

# RESOURCES

```[Source code](https://github.com/ogham/exa)```

<!-- verified: 2026-07-15 -->
