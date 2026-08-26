# TAGLINE

修改已跟踪文件的索引条目

# TLDR

**将文件标记为未改动**

```git update-index --assume-unchanged [file]```

**将文件标记为已改动**

```git update-index --no-assume-unchanged [file]```

**跳过工作树**

```git update-index --skip-worktree [file]```

**刷新索引**

```git update-index --refresh```

**将文件加入索引**

```git update-index --add [file]```

**从索引中移除文件**

```git update-index --remove [file]```

**从 stdin 读取要更新的路径**

```find . -name "*.txt" | git update-index --add --stdin```

# SYNOPSIS

**git** **update-index** [_options_] [_files_...]

# PARAMETERS

**--assume-unchanged**
> 忽略文件的改动。

**--no-assume-unchanged**
> 恢复跟踪改动。

**--skip-worktree**
> 设置 skip-worktree 位。

**--no-skip-worktree**
> 清除 skip-worktree 位。

**--add**
> 将文件加入索引。

**--remove**
> 从索引中移除文件。

**--refresh**
> 刷新 stat 信息；若路径需要更新则报错，除非同时给出 **-q**。

**-q**
> 与 **--refresh** 搭配：即使路径需要更新也安静地继续，而不是报错退出。

**--really-refresh**
> 类似 **--refresh**，但无条件检查 stat 信息，忽略 assume-unchanged 位。

**--chmod=(+|-)x**
> 为更新的路径设置或取消可执行位。

**--stdin**
> 从标准输入而不是命令行读取路径列表，每行一个（配合 **-z** 时以 NUL 分隔）。

**--index-info**
> 从标准输入读取索引条目（模式、对象、路径），直接添加、替换或移除条目。

**--cacheinfo** _mode_,_object_,_path_
> 直接向索引中插入一个条目，无需工作树中存在对应文件。

**-z**
> 配合 **--stdin** 或 **--index-info** 使用时，以 NUL 作为行结束符。

**--ignore-submodules**
> 与 **--refresh** 搭配使用时跳过子模块检查。

**--split-index**, **--no-split-index**
> 启用或禁用面向大型仓库的 split-index 特性。

**--untracked-cache**, **--no-untracked-cache**
> 启用或禁用对未跟踪文件信息的缓存，以加速 **git status**。

# DESCRIPTION

**git update-index** 将工作树中的文件内容登记到索引。它是一个底层（plumbing）命令，`git add` 内部就依赖它。

最常见的用法是 `--assume-unchanged` 标志，它告诉 Git 暂时忽略某个被跟踪文件的改动。`--skip-worktree` 标志用途类似，但面向的是由稀疏检出管理的文件。

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

[git-add](/man/git-add)(1), [git-rm](/man/git-rm)(1), [git-ls-files](/man/git-ls-files)(1)

# RESOURCES

```[Documentation](https://git-scm.com/docs/git-update-index)```

```[Source code](https://github.com/git/git)```

<!-- verified: 2026-07-17 -->
