# TAGLINE

将暂存任务移入 pueue 队列

# TLDR

**将暂存任务入队**

```pueue enqueue [task_id]```

**将多个任务入队**

```pueue enqueue [id1] [id2] [id3]```

**延迟入队**

```pueue enqueue --delay "[30min]" [task_id]```

# SYNOPSIS

**pueue enqueue** [_options_] _task_ids_

# PARAMETERS

_TASK_IDS_
> 要入队的任务 ID。

**--delay** _DURATION_
> 执行前的延迟时间。

# DESCRIPTION

**pueue enqueue** 将暂存任务移入活动队列以执行。通过 **--stashed** 添加或用 **pueue stash** 移入暂存区的任务都可以用该命令激活。可选的 **--delay** 可将执行推迟指定时长。

# CAVEATS

任务必须处于暂存状态才能入队。使用 **pueue stash** 暂存正在运行或排队中的任务，或用 **pueue add --stashed** 直接创建暂存状态的任务。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-stash](/man/pueue-stash)(1), [pueue-add](/man/pueue-add)(1), [pueue-status](/man/pueue-status)(1)
