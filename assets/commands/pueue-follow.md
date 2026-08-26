# TAGLINE

实时流式查看 pueue 任务输出

# TLDR

**跟踪任务输出**

```pueue follow [task_id]```

**跟踪最新任务**

```pueue follow```

**指定行数跟踪**

```pueue follow --lines [50] [task_id]```

# SYNOPSIS

**pueue follow** [_options_] [_task_id_]

# PARAMETERS

_TASK_ID_
> 要跟踪的任务。

**--lines** _N_
> 初始显示的行数。

# DESCRIPTION

**pueue follow** 实时流式输出正在运行的任务的 stdout 和 stderr，类似于 **tail -f**。不带任务 ID 时，它跟踪最近启动的任务。**--lines** 选项控制初始显示多少行已有输出。

# CAVEATS

仅适用于正在运行的任务。pueue 的一部分。

# HISTORY

pueue follow 提供**实时任务**输出流。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-log](/man/pueue-log)(1)
