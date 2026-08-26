# TAGLINE

写入和校验提交图文件

# TLDR

**写入提交图**

```git commit-graph write```

**连同所有可达提交一起写入**

```git commit-graph write --reachable```

**校验提交图**

```git commit-graph verify```

# SYNOPSIS

**git** **commit-graph** _command_ [_options_]

# SUBCOMMANDS

**write**
> 写入提交图文件。

**verify**
> 校验提交图。

# PARAMETERS

**--reachable**
> 包含所有可达的提交。

**--stdin-commits**
> 从标准输入读取提交。

**--stdin-packs**
> 扫描标准输入中列出的 pack 索引以查找提交。

**--append**
> 追加到现有提交图。

**--split**[=_STRATEGY_]
> 使用增量式提交图。

**--changed-paths**
> 为变更路径计算布隆过滤器，加速 **git log -- path** 等历史查询。

**--object-dir** _DIR_
> 用于存储提交图的对象目录。

**--shallow**
> 配合 **verify** 时，仅检查增量提交图的顶端文件。

# DESCRIPTION

**git commit-graph** 管理 commit-graph 文件。这是一项性能优化特性，以针对快速图遍历操作优化的格式存储提交元数据。这些文件能显著加速历史悠久的仓库中的常见操作，如 git log、git merge-base 和可达性检查。

提交图存储了提交 DAG（有向无环图）的预计算表示，包括父提交关系、代数（generation number）和树对象 ID。这避免了在图遍历时反复解析提交对象，为大型仓库带来巨大的性能提升。

write 子命令生成或更新提交图，可以针对所有可达提交（--reachable），也可以针对通过标准输入提供的提交（--stdin-commits）。增量提交图（--split）可以在新增提交时高效更新，无需重写整个文件。

现代 Git 版本已将提交图维护纳入 git gc 和 git maintenance，因此很少需要手动调用。verify 子命令用于检查提交图的完整性，确保数据结构与仓库状态保持一致。

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

[git-gc](/man/git-gc)(1), [git-maintenance](/man/git-maintenance)(1), [git-log](/man/git-log)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-commit-graph)```

<!-- verified: 2026-07-17 -->
