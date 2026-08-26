# TAGLINE

通过 SSH 在本地和远程主机上运行任务

# TLDR

**初始化新的 sake 配置**

```sake init```

**在所有服务器上运行任务**

```sake run [ping] --all```

在所有服务器上执行命令并以表格输出

```sake exec --all --output table '[uptime]'```

**SSH 登录已定义的服务器**

```sake ssh [server]```

# SYNOPSIS

**sake** _command_ [_options_]

# PARAMETERS

**init**
> 创建新的 sake.yaml 配置文件。

**run** _TASK_
> 在目标服务器上运行定义的任务。

**exec** _COMMAND_
> 在目标服务器上执行临时 shell 命令。

**ssh** _SERVER_
> SSH 登录到已配置的服务器。

**list servers**, **list tasks**, **list tags**
> 列出已配置的服务器、任务或标签。

**describe** _servers_|_tasks_
> 显示已配置服务器或任务的详细信息。

**edit task** _TASK_, **edit server** _SERVER_
> 在 **$EDITOR** 中打开对应的 sake.yaml 条目。

**completion** _bash_|_zsh_|_fish_
> 输出 Shell 补全脚本。

**--all**
> 目标为所有服务器。

**--tags** _TAG_
> 目标为匹配一个或多个标签的服务器。

**--limit** _N_
> 将执行限制在前 _N_ 个匹配的服务器。

**--config** _FILE_
> 使用指定的配置文件，而不是自动发现 sake.yaml。

**--output** _FORMAT_
> 输出格式：**table**、**text**、**json**、**html** 或 **markdown**。

**--strategy** _free_|_row_|_column_
> 跨多台服务器的执行策略。

**--parallel**
> 在目标服务器上并发而非串行地运行任务。

# DESCRIPTION

**sake** 让你在 sake.yaml 配置文件中定义服务器和任务，然后通过 SSH 在本地或远程主机上运行这些任务。它支持任务、服务器和标签的自动补全、表格化输出、并行执行，还可以 SSH 进入 Docker 容器。

# HISTORY

**sake** 由 **Samir Alajmovic**（alajmo）创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S sake```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ansible](/man/ansible)(1), [ssh](/man/ssh)(1), [fabric](/man/fabric)(1)
