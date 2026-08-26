# TAGLINE

命令完成时触发通知

# TLDR

**命令完成时通知**

```noti [long-running-command]```

**使用自定义标题通知**

```noti -t "[Build]" [make]```

**使用自定义消息通知**

```noti -m "[Done!]" [command]```

**使用指定服务**

```noti --slack [command]```

**管道模式**

```[command] | noti```

**横幅通知**

```noti -b [command]```

**按 PID 监视正在运行的进程**

```noti -w [PID]```

# SYNOPSIS

**noti** [_options_] [_command_]

# PARAMETERS

_COMMAND_
> 要监视的命令。

**-t** _TITLE_
> 通知标题。

**-m** _MESSAGE_
> 通知消息。

**-b**
> 横幅通知。

**-s**
> 语音通知（文字转语音）。

**-w** _PID_
> 按 PID 监视正在运行的进程，在其结束时发出通知。

**--slack**
> 通过 Slack 发送通知。

**--pushover**
> 通过 Pushover 发送通知。

**--help**
> 显示帮助信息。

# DESCRIPTION

**noti** 会在命令完成时触发通知，支持多种服务。

该工具在任务完成时发出提醒，可与 Slack、Pushover 以及系统原生通知配合工作。

# CAVEATS

需要通知服务。跨平台。外部服务需另行配置。

# HISTORY

noti 的创建目的是在多个平台和服务之间提供**命令完成通知**。

# INSTALL

```brew: brew install noti```

```nix: nix profile install nixpkgs#noti```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[notify-send](/man/notify-send)(1), [terminal-notifier](/man/terminal-notifier)(1)
