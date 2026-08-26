# TAGLINE

从当前索引创建树对象

# TLDR

**从索引写入树对象**

```git write-tree```

**以指定前缀写入**

```git write-tree --prefix=[subdir/]```

**允许缺失对象**

```git write-tree --missing-ok```

# SYNOPSIS

**git** **write-tree** [_options_]

# PARAMETERS

**--prefix** _prefix_
> 写入子树。

**--missing-ok**
> 允许存在缺失的对象。

# DESCRIPTION

**git write-tree** 根据当前索引内容创建一个树对象，并将生成的树对象的 SHA 打印到标准输出。它是一个底层 plumbing 命令，`git commit` 内部使用它把暂存的文件结构快照成 Git 对象数据库中的一个树对象。

运行此命令前索引必须处于完全合并的状态；通常先用 `git update-index` 将索引与工作目录同步。

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

[git-commit-tree](/man/git-commit-tree)(1), [git-read-tree](/man/git-read-tree)(1), [git-update-index](/man/git-update-index)(1)

# RESOURCES

```[Documentation](https://git-scm.com/docs/git-write-tree)```

<!-- verified: 2026-07-17 -->
