# TAGLINE

从 pueue 队列中移除任务

# TLDR

**移除任务**

```pueue remove [task_id]```

**移除多个任务**

```pueue remove [id1] [id2]```

**强制移除运行中的任务**

```pueue kill [task_id] && pueue remove [task_id]```

# SYNOPSIS

**pueue remove** [_options_] _task_ids_

# PARAMETERS

_TASK_IDS_
> 要移除的任务。

# DESCRIPTION

**pueue remove** 按任务 ID 从 pueue 队列中删除特定任务。只有排队中、暂存或已完成的任务可以移除；运行中的任务必须先用 **pueue kill** 终止后才能删除。若要批量删除所有已完成的任务，请使用 **pueue clean**。

# CAVEATS

运行中的任务无法直接移除；请先使用 **pueue kill**。移除任务会永久删除其日志输出。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-clean](/man/pueue-clean)(1), [pueue-kill](/man/pueue-kill)(1)
