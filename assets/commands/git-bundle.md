# TAGLINE

创建和操作可移植的 bundle 文件

# TLDR

**创建整个仓库的 bundle**

```git bundle create [repo.bundle] --all```

**创建分支的 bundle**

```git bundle create [branch.bundle] [branch]```

**创建某提交以来的 bundle**

```git bundle create [recent.bundle] [commit]..HEAD```

**校验 bundle**

```git bundle verify [repo.bundle]```

**从 bundle 克隆**

```git clone [repo.bundle] [directory]```

**列出 bundle 内容**

```git bundle list-heads [repo.bundle]```

# SYNOPSIS

**git** **bundle** _command_ [_options_] [_refs_]

# SUBCOMMANDS

**create**
> 创建 bundle。

**verify**
> 校验 bundle。

**list-heads**
> 列出引用。

**unbundle**
> 解出对象。

# PARAMETERS

**--all**
> 包含所有引用。

# DESCRIPTION

**git bundle** 用于创建和操作 bundle 文件，以便离线传输仓库数据。bundle 是包含 Git 对象和引用的可移植二进制归档，相当于独立的仓库快照。

其主要用途是在没有网络的情况下共享仓库数据，例如隔离网络环境或网络缓慢的场景。bundle 可以包含整个仓库，也可以只包含特定分支和提交范围。在从中克隆或拉取时，它们表现得像只读远程。

与归档不同，bundle 保留了 Git 历史，并且可以从中增量拉取。bundle 经过加密校验以确保数据完整性。常见的工作流是：在一台机器上创建 bundle，物理传输到另一台机器后进行克隆或拉取。

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

[git-archive](/man/git-archive)(1), [git-clone](/man/git-clone)(1), [git-fetch](/man/git-fetch)(1), [git-pull](/man/git-pull)(1)
