# TAGLINE

设置 pueue 任务并发级别

# TLDR

**设置并行任务数**

```pueue parallel [4]```

**为特定分组设置**

```pueue parallel --group [group_name] [2]```

**不限并行**

```pueue parallel 0```

**一次只跑一个任务**

```pueue parallel 1```

# SYNOPSIS

**pueue parallel** [**-g** _group_] [_amount_]

# PARAMETERS

_amount_
> 目标分组中允许并行运行的任务数量。值为 **0** 表示不限制。省略 _amount_ 则查询当前值。

**-g**, **--group** _NAME_
> 将设置应用于指定分组而非 **default** 分组。

# DESCRIPTION

**pueue parallel** 设置一个 pueue 分组中可同时运行的任务数量。每个分组都有各自独立的并行度限制。若未给出 _amount_，pueue 会打印该分组的当前值。

更改只影响新任务的调度——降低上限时不会停止已在运行的任务。

# CAVEATS

设置为 0 会完全取消并发限制。使用 **pueue group** 列出分组，用 **pueue status** 查看当前限制。

# HISTORY

pueue parallel 是 **Arne Beer** 开发的 **pueue** 的一部分，提供带并发控制的任务队列管理。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-add](/man/pueue-add)(1), [pueue-group](/man/pueue-group)(1), [pueue-status](/man/pueue-status)(1)
