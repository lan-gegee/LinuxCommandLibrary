# TAGLINE

纯文本 todo.txt 任务管理器

# TLDR

**添加任务**

```todo.sh add "[task text]"```

**列出所有任务**

```todo.sh list```

**按优先级列出**

```todo.sh listpri [A]```

**标记完成**

```todo.sh do [item-number]```

**添加优先级**

```todo.sh pri [item-number] [A]```

**归档已完成项**

```todo.sh archive```

# SYNOPSIS

**todo.sh** _command_ [_options_] [_args_]

# PARAMETERS

**add**
> 添加任务。

**list**, **ls**
> 列出任务。

**listpri**, **lsp**
> 按优先级列出。

**do**
> 完成任务。

**pri**
> 设置优先级。

**archive**
> 归档已完成项。

# DESCRIPTION

**todo.sh** 是一个 shell 脚本，用于管理 Gina Trapani 创建的 todo.txt 纯文本格式的任务。任务每行一条，支持优先级（A-Z）、项目标签（+project）和上下文标签（@context），使文件既便于人类阅读也易于解析。

该工具提供添加、完成、设置优先级和归档任务的命令。已完成的条目可移动到 done.txt 归档文件，保持活动列表整洁。纯文本格式确保了可移植性，可与任何文本编辑器或同步服务兼容。

# CAVEATS

需要 Bash。使用 todo.txt 格式。需要配置文件。

# HISTORY

**todo.sh** 由 **Gina Trapani** 创建，是 todo.txt 格式的一部分，用于简单、纯文本的任务管理。

# INSTALL

```apk: sudo apk add todo.txt-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[task](/man/task)(1), [todoman](/man/todoman)(1), [taskwarrior](/man/taskwarrior)(1)
