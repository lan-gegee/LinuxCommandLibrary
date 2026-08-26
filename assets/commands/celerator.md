# TAGLINE

Celery 任务的 TUI 监视与调试器

# TLDR

**启动 celerator** 并连接 Redis broker

```celerator --broker=redis://localhost:6379/0```

**启动 celerator** 并连接 RabbitMQ broker

```celerator --broker=amqp://guest:guest@localhost:5672//```

# SYNOPSIS

**celerator** **--broker=**_URI_

# PARAMETERS

**--broker** _URI_
> Celery broker URI（必需）。支持 Redis、RabbitMQ 及其他兼容 Celery 的 broker。

# DESCRIPTION

**celerator** 是一款用于实时调试和监控 Celery 任务的 TUI 应用。它连接到 Celery broker，通过 Celery 内置的事件系统监听任务生命周期事件，并以基于 Textual 框架构建的交互式终端界面呈现这些事件。

功能包括：实时事件监控并捕获任务数据、一键重试任务（可使用原始参数或自定义参数）、用于查看 args、kwargs、异常和 traceback 的详细调试面板，以及完整的键盘导航以便高效检查任务。

Celery worker **必须** 以 **--events** 标志启动，celerator 才能接收到任务数据。

# KEY BINDINGS

```
r        Retry selected task
Ctrl+r   Retry with custom arguments
c        Clear task table
q        Quit application
Enter    Display traceback/task details
Up/Down  Navigate task list
```

# CAVEATS

Celery worker 必须以 **--events** 标志启动，否则 celerator 将收不到任何任务数据。需要 Python 以及 **celery>=5.5.2**、**textual>=3.2.0** 和 **redis>=6.0.0**。被监控的应用程序无需修改代码。

# HISTORY

**celerator** 由 **Fardin Allahverdi** 开发，首个版本 v0.1.0 发布于 **2025 年 5 月**。其名称是 "Celery" 和 "accelerator" 的合成词。它的定位是作为 Flower 等基于 Web 的 Celery 监控工具的轻量级、终端原生替代品，利用 Textual 框架构建 TUI。

# SEE ALSO

[redis-cli](/man/redis-cli)(1)
