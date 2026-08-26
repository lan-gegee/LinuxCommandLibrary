# TAGLINE

运行和管理后台进程

# TLDR

**在后台运行命令**

```hap run [command]```

**列出所有被跟踪的进程**

```hap```

**查看特定进程的状态**

```hap status [id]```

**查看进程的日志**

```hap logs [id]```

**实时查看进程日志输出**

```hap logs -f [id]```

**暂停正在运行的进程**

```hap pause [id]```

**恢复已暂停的进程**

```hap resume [id]```

# SYNOPSIS

**hap** _command_ [_options_] [_arguments_]

# DESCRIPTION

**hapless** 是一个轻量级命令行工具，用于运行和管理后台进程。它会包装命令以跟踪其执行期间及之后的状态，不需要守护进程或配置文件。只要在任何命令前面加上 **hap run**，就能把它启动到后台并获得自动日志记录和状态跟踪。

该工具提供所有被跟踪进程的总览，包括当前状态、退出码和运行时长。stdout 与 stderr 的日志都会被自动捕获，可随时查看。

# PARAMETERS

**run** _command_
> 在后台运行命令

**status** _id_
> 查看特定进程的状态

**logs** _id_
> 查看进程日志（-f 表示跟随模式）

**pause** _id_
> 暂停正在运行的进程

**resume** _id_
> 恢复已暂停的进程

**kill** _id_
> 终止进程

**clean**
> 从列表中移除已完成的进程

# CAVEATS

不会跨系统重启保留。进程跟踪依赖存储在本地的 PID 文件。需要终端输入的交互式命令无法在后台运行。

# HISTORY

**hapless** 由 **Misha Behersky**（bmwant）创建，使用 **Python** 编写。它被设计成 **screen**、**tmux** 或 **nohup** 等工具在基础后台进程管理场景下的更简单替代品，目标是零配置。

# INSTALL

```brew: brew install hapless```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nohup](/man/nohup)(1), [screen](/man/screen)(1), [tmux](/man/tmux)(1), [bg](/man/bg)(1)
