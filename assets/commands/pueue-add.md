# TAGLINE

向 pueue 任务队列添加命令

# TLDR

**将命令加入队列**

```pueue add [command]```

**添加后立即启动**

```pueue add -i [command]```

**添加到特定分组**

```pueue add -g [group] [command]```

**延迟执行**

```pueue add --delay "10min" [command]```

**添加为暂存任务**

```pueue add --stashed [command]```

# SYNOPSIS

**pueue** **add** [_options_] _command_

# PARAMETERS

**-i**, **--immediate**
> 立即启动。

**-g**, **--group** _name_
> 添加到指定分组。

**--delay** _duration_
> 启动前的延迟时间。

**--stashed**
> 添加为暂存（暂停）任务。

**-l**, **--label** _label_
> 任务标签。

**-a**, **--after** _ids_
> 在其他任务之后启动。

**-p**, **--priority** _n_
> 任务优先级。

# DESCRIPTION

**pueue add** 向任务队列添加新命令。命令会按顺序排队执行。支持任务分组、依赖关系、优先级和延迟执行。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-status](/man/pueue-status)(1)
