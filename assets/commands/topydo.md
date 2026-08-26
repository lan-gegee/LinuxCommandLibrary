# TAGLINE

功能丰富的 todo.txt 任务管理器

# TLDR

**列出任务**

```topydo ls```

**添加任务**

```topydo add "[task description]"```

**完成任务**

```topydo do [number]```

**设置优先级**

```topydo pri [number] [A]```

**推迟任务**

```topydo postpone [number] [1w]```

**交互模式**

```topydo prompt```

# SYNOPSIS

**topydo** _command_ [_options_] [_args_]

# PARAMETERS

**ls**
> 列出任务。

**add**
> 添加任务。

**do**
> 完成任务。

**pri**
> 设置优先级。

**postpone**
> 推迟任务。

**prompt**
> 交互模式。

# DESCRIPTION

**topydo** 是一个功能丰富的命令行待办事项管理器，使用 todo.txt 格式，同时增加了循环任务、相对日期处理和任务依赖等功能。它与其他 todo.txt 工具和客户端保持完全兼容。

交互式 **prompt** 模式提供连续会话，无需重启工具即可持续管理任务。可以使用相对日期表达式推迟任务，例如 "1w" 表示一周；循环任务在完成后会自动创建新的实例。

# CAVEATS

需要 Python。使用 todo.txt 格式。建议进行配置。

# HISTORY

**topydo** 的定位是一个基于 Python、支持循环任务的功能丰富的 todo.txt 客户端。

# INSTALL

```brew: brew install topydo```

```nix: nix profile install nixpkgs#topydo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[todo.sh](/man/todo.sh)(1), [task](/man/task)(1), [todoman](/man/todoman)(1)
