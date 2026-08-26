# TAGLINE

命令完成时发送桌面通知

# TLDR

**命令结束时通知**

```ntfyme [command]```

**运行命令并发送通知**

```ntfyme -c "[command]"```

**自定义通知消息**

```ntfyme -m "[message]" [command]```

**跟踪长时间运行的进程**

```ntfyme --pid [process_id]```

# SYNOPSIS

**ntfyme** [_options_] [_command_]

# PARAMETERS

**-c** _COMMAND_
> 要执行的命令。

**-m** _MESSAGE_
> 自定义通知消息。

**--pid** _PID_
> 等待指定的进程 ID。

**--sound**
> 播放通知音效。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ntfyme** 在命令完成时发送桌面通知，监控耗时较长的任务。

该工具用通知包装命令，适用于漫长的操作过程。

# CAVEATS

需要通知守护进程。因系统而异。可能需要配置。

# HISTORY

ntfyme 为终端工作流提供**命令完成通知**功能。

# INSTALL

```aur: yay -S ntfyme```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[notify-send](/man/notify-send)(1), [nohup](/man/nohup)(1), [time](/man/time)(1)
