# TAGLINE

将当前 HEAD 重置到指定状态

# TLDR

**取消暂存文件**

```git reset [file]```

**软重置（保留改动在暂存区）**

```git reset --soft [commit]```

**混合重置（取消暂存改动）**

```git reset [commit]```

**硬重置（丢弃改动）**

```git reset --hard [commit]```

**重置到上游**

```git reset --hard @{u}```

**取消暂存所有文件**

```git reset HEAD```

**将单个文件重置到某提交**

```git reset [commit] -- [file]```

# SYNOPSIS

**git** **reset** [_options_] [_commit_] [_--_] [_files_...]

# PARAMETERS

**--soft**
> 保留改动在暂存区。

**--mixed**
> 取消暂存改动（默认）。

**--hard**
> 丢弃所有改动。

**--keep**
> 重置但保留本地改动。

**--merge**
> 重置到合并状态。

**-p**, **--patch**
> 交互式重置。

**--recurse-submodules**
> 更新子模块工作树以与父项目保持一致。

# DESCRIPTION

**git reset** 将当前 HEAD 移动到指定状态。根据所用的模式，它可以取消暂存文件、撤销提交，或完全丢弃改动。

三种主要模式是 `--soft`（保留改动在暂存区）、`--mixed`（取消暂存改动，默认）和 `--hard`（丢弃所有改动）。若给出文件路径，则只取消这些文件的暂存，而不移动 HEAD。

# CAVEATS

硬重置会永久丢弃改动。对未提交的工作使用 --hard 时务必小心。

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

[git-checkout](/man/git-checkout)(1), [git-revert](/man/git-revert)(1), [git-restore](/man/git-restore)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-reset)```

<!-- verified: 2026-07-17 -->
