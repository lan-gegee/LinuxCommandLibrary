# TAGLINE

Slurm 工作负载管理器的 TUI

# TLDR

**启动 Slurm 作业 TUI**

```turm```

**只显示自己的作业**

```turm -u $USER```

**按分区过滤**

```turm --partition [gpu]```

# SYNOPSIS

**turm** [_squeue-options_]

# DESCRIPTION

**turm** 为管理 Slurm 集群作业提供了便捷的终端用户界面。它解析 squeue 的输出来展示作业信息，每两秒刷新一次队列，并通过基于 inotify 的实时更新显示日志文件。它接受与 squeue 相同的选项。

# HISTORY

**turm** 由 **Karim Abou Zeid**（kabouzeid）创建，用 **Python** 编写。

# SEE ALSO

[squeue](/man/squeue)(1), [scontrol](/man/scontrol)(1), [sacct](/man/sacct)(1)
