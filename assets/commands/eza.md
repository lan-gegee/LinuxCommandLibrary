# TAGLINE

集成 git 的现代 ls 替代品

# TLDR

**列出文件，带**图标和颜色

```eza --icons```

**以长格式显示并带** git 状态

```eza -l --git```

**显示隐藏文件**

```eza -a```

**树状视图**

```eza --tree --level [2]```

**按修改时间排序**

```eza -l --sort modified```

# SYNOPSIS

**eza** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要列出的文件或目录（默认：当前目录）。

**-l**, **--long**
> 以详细的列表格式显示。

**-a**, **--all**
> 显示隐藏文件（点文件）。

**--tree**
> 以树状结构显示。

**--level** _N_
> 树深度限制。

**--git**
> 显示每个文件的 git 状态。

**--icons**
> 显示文件类型图标。

**-h**, **--header**
> 显示列标题。

**--sort** _FIELD_
> 排序依据：name、size、modified、accessed、created。

**-r**, **--reverse**
> 反转排序顺序。

**--group-directories-first**
> 目录排在文件之前。

**--help**
> 显示帮助信息。

# DESCRIPTION

**eza** 是一个用 Rust 编写的现代 ls 替代品。开箱即用地提供彩色输出、git 集成、扩展属性显示和树状视图功能。

相比 ls，它在 git 状态集成、文件图标以及更适合人类阅读的输出默认值等方面有所改进。它能识别多种文件类型，并以醒目的颜色和图标显示。

eza 被设计为 ls 的直接替代品，同时加入开发者期望的现代文件列表特性。

# CAVEATS

需要支持颜色的终端。图标需要兼容字体（Nerd Font）。git 集成在大型仓库中会带来额外开销。不符合 POSIX 标准。

# HISTORY

eza 是 **exa** 的活跃维护分支，exa 自 2023 年起无人维护。eza 在保留 exa 现代化文件列表理念的同时继续开发新功能并修复缺陷，持续维护代码库。

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

[ls](/man/ls)(1), [tree](/man/tree)(1), [lsd](/man/lsd)(1), [exa](/man/exa)(1)

# RESOURCES

```[Source code](https://github.com/eza-community/eza)```

```[Homepage](https://eza.rocks/)```

<!-- verified: 2026-07-15 -->
