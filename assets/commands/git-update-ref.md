# TAGLINE

安全地更新 Git 引用的值

# TLDR

**将引用更新为新值**

```git update-ref [refs/heads/branch] [commit]```

**删除引用**

```git update-ref -d [refs/heads/branch]```

**创建符号引用**

```git update-ref --symbolic-ref [ref] [target]```

**更新时校验旧值**

```git update-ref [ref] [new] [old]```

# SYNOPSIS

**git** **update-ref** [_options_] _ref_ _newvalue_ [_oldvalue_]

# PARAMETERS

**-d**
> 删除引用。

**--create-reflog**
> 创建引用日志（reflog）。

**--no-deref**
> 不解引用符号引用。

**-m** _reason_
> 引用日志信息。

**--stdin**
> 从标准输入读取更新指令（update、create、delete、verify、symref-update 等），并将其作为一个原子事务一起应用。

**-z**
> 配合 **--stdin** 使用时，参数以 NUL 结尾而不是带引号、以空白符结束的字符串。

**--batch-updates**
> 配合 **--stdin** 使用时，允许事务中的个别更新失败而不中止其他更新。

# DESCRIPTION

**git update-ref** 安全地更新仓库中存储的引用名。它提供原子的引用更新以及可选的旧值校验，确保只有当引用当前指向预期值时才会被修改。

这是一个底层（plumbing）命令，`git branch` 和 `git tag` 等上层命令在内部都会使用它。借助 **--stdin**，多个引用更新可以批量合并为单个原子事务。

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

[git-symbolic-ref](/man/git-symbolic-ref)(1), [git-branch](/man/git-branch)(1), [git-tag](/man/git-tag)(1)

# RESOURCES

```[Documentation](https://git-scm.com/docs/git-update-ref)```

```[Source code](https://github.com/git/git)```

<!-- verified: 2026-07-17 -->
