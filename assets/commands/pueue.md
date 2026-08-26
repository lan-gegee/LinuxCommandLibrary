# TAGLINE

命令行任务队列管理器

# TLDR

**将命令加入队列**

```pueue add -- [command]```

**将任务加入特定分组**

```pueue add -g [group_name] -- [command]```

**列出所有任务及其状态**

```pueue status```

**开始处理队列**或恢复特定任务

```pueue start [task_id]```

**暂停队列**或特定任务

```pueue pause [task_id]```

**实时跟踪任务输出**

```pueue follow [task_id]```

**查看任务输出日志**

```pueue log [task_id]```

**从列表移除已完成的任务**

```pueue remove [task_id]```

**终止运行中的任务**

```pueue kill [task_id]```

**重启失败或已完成任务**

```pueue restart [task_id]```

# SYNOPSIS

**pueue** _command_ [_options_]

# PARAMETERS

**add** [_options_] **--** _CMD_
> 将任务加入队列。用 **-g** _group_ 指定分组，用 **-d** 以暂停状态启动，用 **-a** _ID_ 建立对其他任务的依赖，用 **-l** _label_ 指定标签。

**status** [_-j_]
> 显示队列状态。用 **-j** 输出 JSON。

**start** [_ID_]
> 恢复特定的暂停任务；未指定 ID 时启动整个 default 分组。

**pause** [_ID_]
> 暂停特定任务；未指定 ID 时暂停整个 default 分组。

**remove** _ID_
> 从列表移除任务（仅限已完成或排队中的任务）。

**follow** _ID_
> 实时流式查看任务输出。

**log** [_ID_]
> 显示已完成任务捕获的输出。

**kill** [_ID_]
> 终止运行中的任务或某分组内的所有任务。

**restart** _ID_
> 重启已完成或失败的任务。

**clean**
> 从列表移除所有已完成的任务。

**reset**
> 终止所有任务并清空一切。

**group** [_add_|_remove_] _name_
> 管理任务分组。分组支持相互独立的并行队列。

**parallel** _N_ [_-g group_]
> 设置并行运行的任务数量（默认：1）。

# DESCRIPTION

**pueue** 是一款命令行任务队列管理器，可在后台按顺序或并行调度和运行 shell 命令。任务加入队列后由 **pueued** 守护进程执行，该守护进程独立于终端会话存在，并在系统重启后依然保留任务状态。

该工具提供任务生命周期管理，包括暂停、恢复、终止和重启任务。任务输出会被捕获，可用 **follow** 实时跟踪，也可事后用 **log** 查看。分组允许将任务组织到多个队列中，各自拥有独立的并行度设置。

# CONFIGURATION

**~/.config/pueue/pueue.yml**
> 客户端与守护进程的配置文件，定义默认并行度、回调命令和守护进程套接字路径。

# CAVEATS

需要 **pueued** 守护进程正在运行。使用 **pueued -d**（守护进程化）启动它。任务状态跨终端会话和守护进程重启持久保存。

# HISTORY

Pueue（德语"队列"之意）由 **Arne Beer** 创建，用于在后台管理长时间运行的 shell 命令。使用 Rust 编写。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nohup](/man/nohup)(1), [screen](/man/screen)(1), [tmux](/man/tmux)(1), [at](/man/at)(1), [batch](/man/batch)(1), [task](/man/task)(1)
