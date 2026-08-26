# TAGLINE

将分支硬重置为与其远程一致，并清理未跟踪文件

# TLDR

**将当前分支**与其上游同步

```git sync```

**与指定的远程和分支同步**

```git sync [origin] [main]```

**同步但保留未跟踪/被忽略的文件**

```git sync --soft```

**不弹出确认提示直接同步**

```git sync --force```

# SYNOPSIS

**git** **sync** [_remote_ _branch_] [_-s_ | _--soft_] [_-f_ | _--force_]

# PARAMETERS

_REMOTE_ _BRANCH_
> 要同步的远程和分支；默认为当前分支配置的上游。

**-s**, **--soft**
> 重置后跳过 `git clean -d -f -x`，保留未跟踪和被忽略的文件。

**-f**, **--force**
> 跳过确认提示。

**-h**, **--help**
> 显示用法信息。

# DESCRIPTION

**git sync** 是一个 git-extras 命令：先拉取给定（或上游跟踪）的远程分支，然后执行 `git reset --hard` 使当前分支与之完全一致。除非指定 `-s`/`--soft`，否则它随后还会运行 `git clean -d -f -x`，删除工作树中所有未跟踪和被忽略的文件。

除非传入 `-f`/`--force`，否则它在运行前会请求确认。

# CAVEATS

该操作具有破坏性：不在远程上的本地提交、未提交的改动，以及（不带 `-s` 时的）未跟踪/被忽略的文件都会被丢弃。它不是 fetch 后变基或 fetch 后合并；与 `git pull` 不同，分叉的本地工作会被直接抛弃而不是整合进来。

# INSTALL

```zypper: sudo zypper install git-sync```

```brew: brew install git-sync```

```nix: nix profile install nixpkgs#git-sync```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-fetch](/man/git-fetch)(1), [git-reset](/man/git-reset)(1), [git-clean](/man/git-clean)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-sync)```

<!-- verified: 2026-07-17 -->
