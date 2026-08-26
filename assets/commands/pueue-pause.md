# TAGLINE

暂停 pueue 任务队列处理

# TLDR

**暂停所有任务**

```pueue pause```

**暂停特定任务**

```pueue pause [task_id]```

**暂停分组**

```pueue pause --group [group]```

**等待当前任务完成**

```pueue pause --wait```

# SYNOPSIS

**pueue pause** [_options_] [_task_ids_]

# PARAMETERS

_TASK_IDS_
> 要暂停的任务。

**--group** _NAME_
> 暂停特定分组。

**--wait**
> 等待正在运行的任务。

**--all**
> 暂停所有分组。

# DESCRIPTION

**pueue pause** 暂停任务队列，阻止新任务启动。正在运行的任务会继续执行至完成，除非被单独暂停。使用 **--wait** 让正在运行的任务完成后再生效暂停，或用 **--group** 只暂停特定的任务分组。

# CAVEATS

不影响运行中的任务。pueue 的一部分。

# HISTORY

pueue pause 提供**队列暂停**功能。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-start](/man/pueue-start)(1)
