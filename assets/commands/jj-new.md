# TAGLINE

在仓库中创建新变更

# TLDR

创建新变更

```jj new```

创建带描述的新变更

```jj new -m "[message]"```

在特定父修订上创建新变更

```jj new -r [rev]```

创建合并变更

```jj new [rev1] [rev2]```

在当前变更之前插入变更

```jj new --insert-before```

# SYNOPSIS

**jj new** [_options_] [_revisions_...]

# PARAMETERS

_REVISIONS_
> 父修订（多个时创建合并）。

**-m** _MESSAGE_
> 新变更的描述。

**-r** _REV_
> 父修订。

**--insert-before**
> 插入到当前变更之前。

**--insert-after**
> 插入到指定变更之后。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jj new** 在仓库中创建新变更。它会在指定父修订之上开启一个全新的工作副本状态。

该命令可用于创建分支点和合并点。多个父修订会创建合并变更。

# CAVEATS

jj 的子命令。当前变更会自动提交。不同于 Git 分支。

# HISTORY

jj new 是 **Jujutsu** 的一部分，是其"将所有变更视为一等修订"工作流的核心。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-describe](/man/jj-describe)(1), [jj-next](/man/jj-next)(1)
