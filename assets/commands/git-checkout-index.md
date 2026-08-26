# TAGLINE

将索引中的文件复制到工作目录

# TLDR

**将所有文件复制到工作区**

```git checkout-index -a```

**复制特定文件**

```git checkout-index [file]```

**强制复制**

```git checkout-index -f [file]```

**复制到其他目录**

```git checkout-index --prefix=[dir/] -a```

**复制全部内容，包括未合并的文件**

```git checkout-index -a -f```

# SYNOPSIS

**git** **checkout-index** [_options_] [_files_...]

# PARAMETERS

**-a**, **--all**
> 检出所有文件。

**-f**, **--force**
> 强制覆盖。

**--prefix** _string_
> 输出前缀。

**-u**, **--index**
> 检出后更新索引文件中的 stat 信息。

**-n**, **--no-create**
> 不创建新文件，只刷新已有文件。

**-z**
> 输入路径用 NUL 而非换行符分隔（配合 **--stdin** 使用）。

**--stdin**
> 从标准输入读取要检出的路径列表。

**--stage**=(_1_|_2_|_3_|_all_)
> 从指定 stage 复制未合并的文件，而不是默认值。

# DESCRIPTION

**git checkout-index** 是一个底层管道命令（plumbing），用于将 Git 暂存区（索引）中的文件复制到工作目录。它对哪些索引条目会被生成为工作区文件提供细粒度控制。

与更高层的 git checkout 不同，该命令只操作索引本身，不切换分支也不更新 HEAD。它主要用于 Git 内部操作，以及需要精确控制工作区内容生成的专用脚本中。

--prefix 选项可将索引提取到另一个位置，适用于创建干净的检出或导出特定版本。要理解 Git 的三树架构（工作目录、索引和 HEAD）以及文件状态如何在三者之间流动，这个命令必不可少。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-checkout](/man/git-checkout)(1), [git-read-tree](/man/git-read-tree)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-checkout-index)```

<!-- verified: 2026-07-17 -->
