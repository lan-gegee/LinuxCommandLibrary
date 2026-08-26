# TAGLINE

将失败或已完成的 pueue 任务重新入队

# TLDR

**重启失败的任务**

```pueue restart [task_id]```

**以新参数重启**

```pueue restart --edit [task_id]```

**重启所有失败的任务**

```pueue restart --all-failed```

**原位重启**

```pueue restart --in-place [task_id]```

# SYNOPSIS

**pueue** **restart** [_options_] _task_ids_...

# PARAMETERS

**--edit**
> 重启前编辑命令。

**--in-place**
> 在相同的任务槽位中重启。

**--all-failed**
> 重启所有失败的任务。

**--stashed**
> 以暂存状态重启。

**-g**, **--group** _name_
> 按分组过滤。

# DESCRIPTION

**pueue restart** 将失败或已完成的任务重新排队执行。可以在重启前修改命令。适合以修改后的参数重试失败的操作。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-start](/man/pueue-start)(1)
