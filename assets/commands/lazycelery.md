# TAGLINE

用于监控和管理 Celery worker 与任务的 TUI

# TLDR

**启动 Celery 监控器**

```lazycelery```

**运行交互式设置**

```lazycelery init```

**覆盖 broker URL**

```lazycelery --broker [redis://localhost:6379/0]```

**显示当前配置**

```lazycelery config```

**更新 broker URL**

```lazycelery set-broker [redis://localhost:6379/0]```

**设置刷新间隔**（毫秒）

```lazycelery set-refresh [1000]```

**使用自定义配置文件**

```lazycelery --config [~/.config/lazycelery/config.toml]```

# SYNOPSIS

**lazycelery** [_command_] [_options_]

# PARAMETERS

**--broker** _URL_
> 覆盖本次会话使用的 broker URL。

**--config** _FILE_
> 使用自定义的配置文件。

# DESCRIPTION

**lazycelery** 是一款用于监控和管理 Celery worker 与任务的终端 UI，其灵感来自 lazydocker 和 lazygit。它提供键盘驱动的界面，可以在 worker、队列和任务三种视图之间切换，显示每个队列中有多少任务、每个 worker 正在做什么。

功能包括实时监控 worker、附带消息计数的队列管理、附带状态跟踪的任务列表、搜索与过滤功能、任务重试和撤销（revoke），以及清空队列的操作。

# CAVEATS

目前仅支持基于 Redis 的 Celery broker。需要有正在运行的 Celery 基础设施才能连接。可通过 `cargo install lazycelery` 或 Homebrew 安装。

# HISTORY

**lazycelery** 由 **Fguedes90** 创建，使用 **Rust** 编写。

# SEE ALSO

[lazydocker](/man/lazydocker)(1)
