# TAGLINE

交换两个 pueue 任务的队列位置

# TLDR

**交换任务在队列中的位置**

```pueue switch [task_id1] [task_id2]```

# SYNOPSIS

**pueue** **switch** _task_id_1_ _task_id_2_

# DESCRIPTION

**pueue switch** 交换两个任务的队列位置。两个任务都必须处于排队或暂存状态（不能是运行中或已完成）。适用于在不删除并重新添加任务的情况下调整任务执行优先级。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-status](/man/pueue-status)(1), [pueue-enqueue](/man/pueue-enqueue)(1), [pueue-stash](/man/pueue-stash)(1)
