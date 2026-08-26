# TAGLINE

记录并恢复引用的移动历史

# TLDR

**显示 reflog**

```git reflog```

**显示分支的 reflog**

```git reflog [branch]```

**带时间戳显示**

```git reflog --date=relative```

**使旧条目过期**

```git reflog expire --expire=[90.days] --all```

**删除特定条目**

```git reflog delete HEAD@{2}```

# SYNOPSIS

**git reflog** [_command_] [_options_]

# PARAMETERS

**show** _REF_
> 显示引用的 reflog（默认）。

**expire**
> 清除过期的 reflog 条目。

**delete**
> 删除特定条目。

**--all**
> 处理所有引用。

**--expire** _TIME_
> 使早于该时间的条目过期。

**--date** _FORMAT_
> 日期格式。

**-n** _NUM_
> 限制显示的条目数。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git reflog** 记录引用（如 HEAD 和分支末端）何时被更新，为找回丢失的提交提供安全保障。在误操作 reset、rebase 或删除分支之后，reflog 能显示这些引用之前指向的位置，从而恢复原本已不可达的提交。

条目会在可配置的时间后过期：可达条目保留 90 天（`gc.reflogExpire`），不可达条目保留 30 天（`gc.reflogExpireUnreachable`）。reflog 仅存在于本地，不会在仓库之间共享。

# CAVEATS

仅限本地，不会被推送。条目会过期（默认可达条目 90 天、不可达条目 30 天）。若 gc 已删除底层对象，reflog 也无能为力。

# HISTORY

git reflog 是 **Git** 的核心安全特性，提供引用移动的本地历史，使用户能从破坏性操作中恢复。

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

[git-log](/man/git-log)(1), [git-reset](/man/git-reset)(1), [git-gc](/man/git-gc)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-reflog)```

<!-- verified: 2026-07-17 -->
