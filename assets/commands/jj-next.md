# TAGLINE

将工作副本移动到子变更

# TLDR

移动到子变更

```jj next```

一次移动多步

```jj next [2]```

编辑目标变更

```jj next --edit```

沿特定分支移动

```jj next --branch [name]```

# SYNOPSIS

**jj next** [_options_] [_count_]

# PARAMETERS

_COUNT_
> 向前移动的变更数量。

**--edit**
> 编辑目标变更而不是创建新变更。

**--branch** _NAME_
> 沿指定分支前进。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jj next** 将工作副本移动到子变更。它在变更历史中向前导航。

该命令适合按顺序审阅变更。与 prev 配合使用可以在历史中前后导航。

# CAVEATS

jj 的子命令。需要存在子变更。存在多个子变更时可能有歧义。

# HISTORY

jj next 是 **Jujutsu** 的一部分，为以变更为中心的模型提供直观的历史导航。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-prev](/man/jj-prev)(1), [jj-edit](/man/jj-edit)(1)
