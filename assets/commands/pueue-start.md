# TAGLINE

恢复已暂停的 pueue 任务或分组

# TLDR

**启动暂停的任务**

```pueue start [task_id]```

**启动所有任务**

```pueue start --all```

**启动分组**

```pueue start --group [group_name]```

**启动多个特定任务**

```pueue start [task_id_1] [task_id_2] [task_id_3]```

# SYNOPSIS

**pueue start** [_options_] [_task_ids_]

# PARAMETERS

**--all**, **-a**
> 启动所有任务。

**--group**, **-g** _name_
> 启动特定分组。

# DESCRIPTION

**pueue start** 恢复 pueue 任务队列中已暂停的任务或分组。用 pueue pause 暂停的任务可以恢复并继续执行。

# CAVEATS

任务必须处于暂停或排队状态。启动前请使用 **pueue status** 检查任务状态。pueue 守护进程必须正在运行。

# HISTORY

**pueue start** 是 **Arne Beer** 开发的 **pueue** 的一部分——一款支持顺序和并行执行的命令行任务管理器。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-pause](/man/pueue-pause)(1), [pueue-add](/man/pueue-add)(1), [pueue-status](/man/pueue-status)(1)
