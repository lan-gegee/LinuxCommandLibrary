# TAGLINE

编辑排队中的 pueue 任务属性

# TLDR

在默认编辑器中**编辑任务的命令**

```pueue edit [task_id]```

**编辑任务的工作目录**

```pueue edit --path [task_id]```

**编辑任务的标签**

```pueue edit --label [task_id]```

**编辑任务的优先级**

```pueue edit --priority [task_id]```

**一次编辑多个任务**

```pueue edit [task_id1] [task_id2]```

# SYNOPSIS

**pueue** **edit** [_options_] _task_id_...

# DESCRIPTION

**pueue edit** 用于修改排队或暂存的任务。它会在默认编辑器中打开任务属性（通过 EDITOR 或 VISUAL 环境变量设置）以进行修改。仅对尚未开始运行的任务有效。

可以提供多个任务 ID 来依次编辑多个任务。

# PARAMETERS

**--command**
> 编辑任务的命令。未指定标志时这是默认行为。

**--path**
> 编辑任务的工作目录。

**--label**
> 编辑任务的标签。

**--priority**
> 编辑任务的优先级值。

# CAVEATS

只有排队中或暂存的任务可以编辑。正在运行、已暂停或已完成的任务无法修改。使用的编辑器由 EDITOR 或 VISUAL 环境变量决定。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-add](/man/pueue-add)(1), [pueue-stash](/man/pueue-stash)(1), [pueue-status](/man/pueue-status)(1), [pueue-restart](/man/pueue-restart)(1)
