# TAGLINE

从 pueue 队列中移除已完成的任务

# TLDR

**清理已完成的任务**

```pueue clean```

**只清理成功的任务**

```pueue clean --successful-only```

**清理特定分组**

```pueue clean --group [group]```

# SYNOPSIS

**pueue clean** [_options_]

# PARAMETERS

**--successful-only**
> 只移除成功完成的任务，保留失败的任务以便排查。

**--group** _NAME_
> 只清理特定分组的任务。

# DESCRIPTION

**pueue clean** 从 pueue 任务队列中移除已完成的任务（包括成功和失败的），使状态显示保持整洁。使用 **--successful-only** 可以在清理已完成任务的同时保留失败的任务供后续排查。

# CAVEATS

只移除已完成的任务（默认包括成功和失败的）。正在运行和排队的任务不受影响。pueue 的一部分。

# HISTORY

**pueue** 由 **Arne Beer**（Nukesor）使用 **Rust** 编写。**clean** 子命令提供队列清理功能，保持任务列表整洁。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-remove](/man/pueue-remove)(1), [pueue-status](/man/pueue-status)(1), [pueue-log](/man/pueue-log)(1)
