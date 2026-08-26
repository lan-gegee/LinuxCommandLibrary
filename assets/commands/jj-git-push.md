# TAGLINE

将变更推送到 Git 远程仓库

# TLDR

推送当前书签

```jj git push```

推送特定书签

```jj git push --bookmark [name]```

推送所有书签

```jj git push --all```

推送到特定远程

```jj git push --remote [origin]```

通过自动创建书签来推送某个变更

```jj git push --change [change_id]```

试运行

```jj git push --dry-run```

推送已跟踪的书签并删除已移除的

```jj git push --tracked --deleted```

# SYNOPSIS

**jj git push** [_options_]

# PARAMETERS

**-b**, **--bookmark** _NAME_
> 要推送的书签（可重复）。

**--all**
> 推送所有书签。

**--tracked**
> 推送所有已跟踪的书签。

**--deleted**
> 推送那些已在本地删除的书签。

**-c**, **--change** _CHANGE_
> 基于变更 ID 创建书签并推送该变更。

**-r**, **--revisions** _REVISIONS_
> 推送指向指定修订的书签。

**--remote** _NAME_
> 目标远程（默认：origin）。

**--dry-run**
> 显示将要推送的内容但不实际推送。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**jj git push** 将变更推送到 Git 远程仓库。它将 jj 书签转换为 Git 分支进行推送。从远程当前位置到书签目标提交（含）范围内的所有提交都会被推送。

**--change** 标志便于在不手动创建和管理书签的情况下推送单个变更。

# CAVEATS

要推送的变更上需要有书签。远程必须已经配置。空修订被加上书签时会产生警告。

# HISTORY

jj git push 是 **Jujutsu** 的一部分，可通过 Git 托管服务开展协作。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-git](/man/jj-git)(1), [git-push](/man/git-push)(1)
