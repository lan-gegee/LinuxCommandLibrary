# TAGLINE

向运行中的 pueue 任务发送 stdin 输入

# TLDR

**向运行中的任务发送输入**

```pueue send [task_id] "[input]"```

**向提示符发送 yes 响应**

```pueue send [task_id] "yes"```

**发送换行（空行）**

```pueue send [task_id] ""```

**发送转义序列（解释反斜杠转义）**

```pueue send -e [task_id] "line1\nline2"```

# SYNOPSIS

**pueue send** [_-e_] _task_id_ _input_

# PARAMETERS

_TASK_ID_
> 要接收输入的运行中任务的数字 ID。

_INPUT_
> 写入任务 stdin 的字符串。末尾会自动附加换行符。

**-e**, **--escape**
> 解释 `\n`、`\t`、`\\` 等反斜杠转义。

# DESCRIPTION

**pueue send** 将文本写入 **pueue** 队列中某个运行中任务的标准输入，可与提示用户输入的命令交互。适用于确认提示、提供密码短语（passphrase），或向守护进程监管的长时间运行任务输送数据。

目标任务的启动方式必须附带 stdin（**pueue add** 的默认行为），且当前必须处于运行状态。

# CAVEATS

任务必须正在运行；排队、暂停或已完成的任务无法接收输入。每次调用都会附加换行符。敏感输入（密码、令牌）会在 shell 历史记录和进程参数中可见。

# HISTORY

**pueue** 是 **Arne Beer** 用 Rust 编写的命令行任务队列管理器。添加 **send** 子命令是为了让非交互式队列也能处理偶尔需要 stdin 的程序。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-add](/man/pueue-add)(1), [pueue-follow](/man/pueue-follow)(1), [pueue-log](/man/pueue-log)(1), [pueue-status](/man/pueue-status)(1)
