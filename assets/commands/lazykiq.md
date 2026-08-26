# TAGLINE

在终端中检查 Sidekiq 运行状况的 TUI

# TLDR

**启动 Sidekiq 监控器**

```lazykiq```

**连接到指定的 Redis URL**

```lazykiq --redis [redis://localhost:6379/0]```

# SYNOPSIS

**lazykiq** [_options_]

# PARAMETERS

**--redis** _URL_
> Redis 连接 URL（例如 redis://localhost:6379/0）。

# DESCRIPTION

**lazykiq** 是一个用于检查 Sidekiq 活动情况的终端 UI。它通过 Redis 建立连接，展示 Sidekiq 进程、正在运行的作业、队列内容、作业列表以及错误回溯。

功能包括 vim 风格导航、分页与列表过滤，以及在仪表盘、队列和指标视图之间的快速切换。作业详情会显示负载内容、时间戳、重试次数和异常跟踪。你可以查看重试中（retried）、忙碌（busy）、计划中（scheduled）和死亡（dead）状态的作业。支持 Nerd Fonts 以增强显示效果。

# CAVEATS

需要能够访问 Sidekiq 所使用的 Redis 实例。这是一款只读监控工具——不会修改 Sidekiq 的状态。

# HISTORY

**lazykiq** 由 **kpumuk** 创建，使用 **Go** 编写。

# SEE ALSO

[lazydocker](/man/lazydocker)(1), [lazygit](/man/lazygit)(1), [redis-cli](/man/redis-cli)(1)
