# TAGLINE

将 pueue 任务移入暂存状态

# TLDR

**暂存排队中的任务**

```pueue stash [task_id]```

**暂存多个任务**

```pueue stash [id1] [id2] [id3]```

**暂存分组内的所有任务**

```pueue stash --group [group_name]```

**取消暂存（入队）某个暂存任务**

```pueue enqueue [task_id]```

**将新任务直接加入暂存区**

```pueue add --stashed "[command]"```

# SYNOPSIS

**pueue stash** [_options_] [_task_ids_...]

# PARAMETERS

_task_ids_
> 要暂存的一个或多个任务 ID。

**--group** _name_
> 暂存指定分组中的所有任务。

**--all**
> 暂存所有排队的任务。

# DESCRIPTION

**pueue stash** 将排队中的任务移入暂存状态，阻止其被自动启动。暂存任务仍保留在 pueue 中，但在用 **pueue enqueue** 显式入队之前不会运行。这适合准备稍后运行的任务，或在保留任务的前提下暂时挂起它们。

# STASH VS PAUSE

```
Stash  - Remove from queue entirely, won't auto-start
Pause  - Stop execution but keep in queue position
```

# CAVEATS

暂存任务重新入队时不会保留原有的队列位置。只有排队中（非运行中）的任务可以暂存。

# HISTORY

pueue stash 是 **Arne Beer** 开发的 **pueue** 的一部分，用于管理任务队列状态。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-enqueue](/man/pueue-enqueue)(1), [pueue-add](/man/pueue-add)(1), [pueue-status](/man/pueue-status)(1)
