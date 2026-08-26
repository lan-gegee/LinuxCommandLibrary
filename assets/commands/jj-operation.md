# TAGLINE

管理 Jujutsu 的操作日志

# TLDR

列出操作

```jj operation log```

撤销上一次操作

```jj operation undo```

恢复到特定操作

```jj operation restore [operation-id]```

显示操作详情

```jj operation show [operation-id]```

# SYNOPSIS

**jj** **operation** _subcommand_ [_options_]

# PARAMETERS

**log**
> 列出操作历史。

**undo**
> 撤销上一次操作。

**restore** _id_
> 将仓库恢复到某操作时的状态。

**show** _id_
> 显示操作详情。

**abandon** _id_
> 废弃旧的操作。

# DESCRIPTION

**jj operation** 管理 Jujutsu 的操作日志。对仓库的每一次更改都会被记录为一个操作，从而支持撤销和时间回溯。操作会跟踪运行过哪些命令及其效果。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-undo](/man/jj-undo)(1)
