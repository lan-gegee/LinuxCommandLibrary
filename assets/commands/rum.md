# TAGLINE

管理运行中后台任务的简单工具

# TLDR

**启动一个被跟踪的后台任务**

```rum [my_long_script.sh]```

**列出所有被跟踪的运行**

```rum --list```

**显示某次运行的输出日志**

```rum --log [id]```

**实时跟踪运行中任务的输出**

```rum --log --follow [id]```

**按 ID 移除被跟踪的运行**

```rum --remove [id]```

# SYNOPSIS

**rum** [_options_] [_command_...]

# PARAMETERS

**--list**
> 列出所有被跟踪的后台运行及其状态。

**--log** _ID_
> 显示某次被跟踪运行的输出日志。

**--follow**
> 与 --log 搭配使用，实时跟踪输出（类似 tail -f）。

**--remove** _ID_
> 按 ID 移除一次被跟踪的运行。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**rum** 让你能够运行并管理长时间运行的后台进程。在任何命令前加上 **rum** 即可开始跟踪它。每次运行都会获得一个用于管理的唯一 ID。输出会被捕获，之后可以用 --log 查看；对于简单的任务跟踪来说，这比 screen 或 tmux 更轻量，在可能断开的 SSH 会话中尤其有用。

# HISTORY

**rum** 由 **Daniel Csillag**（dccsillag）创建，使用 **Rust** 编写。

# INSTALL

```aur: yay -S rum```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[screen](/man/screen)(1), [tmux](/man/tmux)(1), [nohup](/man/nohup)(1), [disown](/man/disown)(1)
