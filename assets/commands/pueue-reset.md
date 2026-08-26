# TAGLINE

将 pueue 守护进程重置为干净状态

# TLDR

**重置 pueue 状态**

```pueue reset```

**只重置特定分组**

```pueue reset --groups [group1] [group2]```

# SYNOPSIS

**pueue** **reset** [_options_]

# PARAMETERS

**--groups** _group_...
> 只重置特定分组，而非全部内容

# DESCRIPTION

**pueue reset** 会终止所有正在运行的任务、移除全部任务并重置任务 ID 计数器，使守护进程回到干净状态。如果存在正在运行的任务，会显示确认提示。

# CAVEATS

此命令会永久移除所有任务历史并终止运行中的任务。操作无法撤销。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-clean](/man/pueue-clean)(1), [pueue-kill](/man/pueue-kill)(1), [pueue-remove](/man/pueue-remove)(1)
