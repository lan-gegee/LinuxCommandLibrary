# TAGLINE

根据 ls-tree 格式创建树对象

# TLDR

**从 ls-tree 输出创建树**

```git ls-tree HEAD | git mktree```

**从文件创建树**

```git mktree < [tree-listing.txt]```

**允许缺失的对象**

```git mktree --missing```

# SYNOPSIS

**git mktree** [_options_]

# PARAMETERS

**--missing**
> 允许缺失的对象。

**-z**
> 以 NUL 结尾的输入。

**--batch**
> 处理多个树。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git mktree** 根据 ls-tree 格式的输入创建树对象。它从标准输入读取文件模式、对象类型、哈希和名称，创建一个包含这些条目的新树对象。该命令是 `git ls-tree` 的逆操作。

这个底层（plumbing）工具支持在脚本中以编程方式创建和操作树。输入必须格式正确，每行需指定模式、类型、哈希和文件名。使用 `--batch` 时，它接受以空行分隔的多棵树描述，每批写出一个树对象，并打印各自的结果哈希。

# CAVEATS

底层（plumbing）命令。输入必须格式正确。除非使用 --missing，否则对象必须已存在。

# HISTORY

git mktree 是 **Git** 用于创建树对象的底层核心命令，使 Git 的树结构可以被程序化操作。

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

[git-ls-tree](/man/git-ls-tree)(1), [git-write-tree](/man/git-write-tree)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-mktree)```

<!-- verified: 2026-07-17 -->
