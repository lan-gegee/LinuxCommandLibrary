# TAGLINE

在系统负载允许时执行命令

# TLDR

**交互式**输入命令，然后按 Ctrl-D 将其加入队列

```batch```

将从标准输入读取的一条**命令**加入队列

```echo "./backup.sh" | batch```

将**文件**中的命令加入队列

```batch -f [path/to/script.sh]```

任务结束时发送**邮件**，即使没有任何输出

```echo "./backup.sh" | batch -m```

# SYNOPSIS

**batch** [**-f** _file_] [**-m**] [**-V**] [**-q** _queue_]

# DESCRIPTION

**batch** 在系统负载允许时执行命令。它将作业排入队列，待系统平均负载降至 **1.5** 以下（或启动 **atd** 时通过 **-l** 指定的值）后运行，适合把非紧急或资源密集型任务安排到低负载时段执行。

与在特定时间运行命令的 **at** 不同，**batch** 会等待有利的系统条件，一旦满足就立即运行作业。**batch** 等价于 `at -q b -m now`。命令从标准输入或 **-f** 指定的文件读取，任何输出都会在完成后以邮件形式发送给用户。必须运行 **atd** 守护进程才能处理队列中的作业。

# PARAMETERS

**-f** _file_
> 从 _file_ 而非标准输入读取作业。

**-m**
> 任务完成时向用户发送邮件，即使没有输出。

**-q** _queue_
> 使用指定的队列（单个字母）。batch 默认使用队列 **b**。

**-V**
> 将版本号输出到标准错误并退出。

未给出 **-f** 文件时，命令从标准输入读取。交互式输入命令时，按 Ctrl-D 结束输入。

# CAVEATS

batch 要正常工作必须运行 **atd** 守护进程。结果会发送到用户的邮箱。负载阈值默认为 1.5，可通过 **-l** 选项启动 **atd** 来修改。

# HISTORY

**batch** 是 **at** 软件包的一部分，为 Unix 系统提供作业调度工具。

# INSTALL

```apt: sudo apt install at```

```dnf: sudo dnf install at```

```pacman: sudo pacman -S at```

```apk: sudo apk add at```

```zypper: sudo zypper install at```

```nix: nix profile install nixpkgs#at```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[at](/man/at)(1), [atq](/man/atq)(1), [atrm](/man/atrm)(1), [cron](/man/cron)(1), [crontab](/man/crontab)(1)

# RESOURCES

```[Documentation](https://manpages.debian.org/bookworm/at/batch.1.en.html)```

<!-- verified: 2026-06-19 -->
