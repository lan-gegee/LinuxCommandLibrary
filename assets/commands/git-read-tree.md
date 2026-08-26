# TAGLINE

将树信息读入索引

# TLDR

**将树读入索引**

```git read-tree [tree-ish]```

**合并树**

```git read-tree -m [base] [ours] [theirs]```

**带前缀读取**

```git read-tree --prefix=[dir/] [tree-ish]```

**合并并更新工作区**

```git read-tree -m -u [base] [ours] [theirs]```

**重置索引**

```git read-tree --reset HEAD```

**清空索引**

```git read-tree --empty```

**试运行以检查错误**

```git read-tree -n -m [tree-ish]```

# SYNOPSIS

**git read-tree** [_options_] _tree-ish_

# PARAMETERS

_TREE-ISH_
> 要读取的树。

**-m**
> 合并模式。

**-u**
> 更新工作区。

**--reset**
> 与 -m 相同，但丢弃未合并的内容。

**--prefix=**_DIR/_
> 保留当前索引内容，并把树读入前缀指定的子目录中。

**-i**
> 只更新索引，不检查工作区与当前 head 的一致性。

**-n**, **--dry-run**
> 只检查错误，不更新索引或工作区。

**-v**
> 显示检出文件的进度。

**--trivial**
> 仅对平凡情况执行合并，冲突保持未解决状态。

**--aggressive**
> 在三方合并期间内部解决更多情况。

**--index-output** _FILE_
> 将结果写入指定文件而非 $GIT_INDEX_FILE。

**--empty**
> 不向索引导入树，而是将其清空。

**--no-sparse-checkout**
> 即使 core.sparseCheckout 为 true 也禁用稀疏检出支持。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git read-tree** 将树信息读入索引。它是一个底层（plumbing）命令，被 `git checkout` 和 `git merge` 等高层命令内部调用以操作暂存区。

该命令可以读取单棵树，也可以对树执行三方合并。除非指定 `-u` 标志同步工作目录，否则它只更新索引而不触碰工作区。

# CAVEATS

底层（plumbing）命令。通常由其他命令调用。可能覆盖索引状态。

# HISTORY

git read-tree 是 **Git** 实现索引操作的核心底层命令，被 checkout、merge 等命令内部使用。

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

[git-write-tree](/man/git-write-tree)(1), [git-ls-tree](/man/git-ls-tree)(1), [git-checkout](/man/git-checkout)(1), [git-merge](/man/git-merge)(1)
