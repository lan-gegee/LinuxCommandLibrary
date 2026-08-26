# TAGLINE

显示 pueue 任务队列状态

# TLDR

**显示队列状态**

```pueue status```

**显示特定分组**

```pueue status -g [group]```

**以 JSON 格式显示**

```pueue status --json```

**显示完整任务详情**

```pueue status --full```

# SYNOPSIS

**pueue** **status** [_options_]

# PARAMETERS

**-g**, **--group** _name_
> 显示特定分组。

**--json**
> 以 JSON 输出。

**--full**
> 以展开的输出显示完整的任务信息。

# DESCRIPTION

**pueue status** 显示队列中所有任务的当前状态。列出排队、运行、完成和失败的任务及其任务 ID、命令、状态和执行时间。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-add](/man/pueue-add)(1), [pueue-log](/man/pueue-log)(1), [pueue-clean](/man/pueue-clean)(1), [pueue-follow](/man/pueue-follow)(1)
