# TAGLINE

列出树对象的内容

# TLDR

**列出树内容**

```git ls-tree HEAD```

**递归列出**

```git ls-tree -r HEAD```

**只显示名称**

```git ls-tree --name-only HEAD```

**列出特定目录**

```git ls-tree HEAD [src/]```

**显示大小**

```git ls-tree -l HEAD```

# SYNOPSIS

**git ls-tree** [_options_] _tree-ish_ [_path_]

# PARAMETERS

_TREE-ISH_
> 要列出的树或提交。

_PATH_
> 限定到指定路径。

**-r**
> 递归进入子树。

**-d**
> 只显示树。

**--name-only**
> 只显示名称。

**--name-status**
> 显示名称和状态。

**-l**, **--long**
> 显示对象大小。

**--abbrev** _N_
> 缩短哈希长度。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git ls-tree** 列出树对象的内容，显示特定提交目录结构中的文件名、模式、类型和对象哈希。它提供了仓库在任意提交时点文件布局的快照。

该命令对脚本编写很有用，也有助于理解 Git 内部如何存储目录内容。递归模式（`-r`）会显示所有子目录下的全部文件，而 `--name-only` 提供干净的输出，适合通过管道传给其他命令。

# CAVEATS

显示特定提交时的树。这是面向脚本的底层（plumbing）命令。输出为机器可读格式。

# HISTORY

git ls-tree 是 **Git** 用于检查树对象的底层核心命令，属于 Git 底层接口的一部分。

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

[git-ls-files](/man/git-ls-files)(1), [git-ls-remote](/man/git-ls-remote)(1), [git-show](/man/git-show)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-ls-tree)```

<!-- verified: 2026-07-17 -->
