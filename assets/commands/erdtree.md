# TAGLINE

集成 Git 的现代文件系统树工具

# TLDR

**显示**目录树

```erdtree [directory]```

**显示**目录和文件的大小

```erdtree -s [directory]```

在树旁**显示** git 状态

```erdtree --git [directory]```

**限制**树的深度

```erdtree -L 3 [directory]```

只**显示**目录

```erdtree -d [directory]```

# SYNOPSIS

**erdtree** [_options_] [_directory_]

# PARAMETERS

**-d, --dirs-only**
> 只显示目录

**-L, --level** _N_
> 将树深度限制为 N 层

**-s, --size**
> 显示文件和目录大小

**-h, --human-readable**
> 以人类可读的格式显示大小

**--git**
> 显示 git 状态（已修改、未跟踪、已忽略）

**--no-git**
> 禁用 git 集成

**--ignore** _PATTERN_
> 忽略匹配模式的文件

**-I, --ignore-git**
> 遵循 .gitignore 规则

**-a, --all**
> 显示隐藏文件

**-P, --prune**
> 剪除空目录

**--sort** _TYPE_
> 排序依据：name、size、time、git

**--dirs-first**
> 目录排在文件之前

**-o, --output** _FILE_
> 输出到文件而非标准输出

**-v, --version**
> 显示版本并退出

**--help**
> 显示帮助并退出

# DESCRIPTION

**erdtree** 是 tree 命令的现代替代品，额外提供磁盘占用统计、git 集成和更美观的格式化等功能。它将 tree 与 du 的功能结合在一起，界面简洁、运行快速。

该工具可以显示文件大小、git 状态指示符，并支持自定义排序。它的设计目标是在提供更多实用信息的同时，比传统 tree 实现更快。

# CAVEATS

大型目录可能需要较长时间处理。检查 git 状态会带来额外开销。符号链接的处理取决于所选选项。Unicode 文件名需要终端正确支持。

# HISTORY

**erdtree** 由 Benji Nguyen 创建，作为传统 tree 命令的现代替代品，在保持兼容性的同时解决了性能与功能上的局限。

# INSTALL

```pacman: sudo pacman -S erdtree```

```zypper: sudo zypper install erdtree```

```brew: brew install erdtree```

```nix: nix profile install nixpkgs#erdtree```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tree](/man/tree)(1), [du](/man/du)(1), [ls](/man/ls)(1), [exa](/man/exa)(1), [lsd](/man/lsd)(1)
