# TAGLINE

用于构建复杂批处理作业流水线的 Python 工作流引擎

# TLDR

**运行任务**

```luigi --module [mymodule] [MyTask]```

**带参数运行**

```luigi --module [mymodule] [MyTask] --[param]=[value]```

**运行本地调度器**

```luigid```

**以多个 worker 运行**

```luigi --module [mymodule] [MyTask] --workers [4]```

**使用本地调度器运行**（无需中央调度器）

```luigi --module [mymodule] [MyTask] --local-scheduler```

# SYNOPSIS

**luigi** [_options_] _task_ [_task-params_]

# PARAMETERS

**--module** _name_
> 包含任务的 Python 模块。

**--workers** _n_
> worker 数量。

**--local-scheduler**
> 使用本地调度器而非中央调度器。

**--scheduler-host** _host_
> 中央调度器主机名。

**--scheduler-port** _port_
> 中央调度器端口（默认 8082）。

**--log-level** _level_
> 日志级别（DEBUG、INFO、WARNING、ERROR、CRITICAL）。

**--help**
> 显示可用选项和任务参数。

# DESCRIPTION

**Luigi** 是一个 Python 工作流引擎，用于构建复杂的批处理作业流水线。它处理依赖解析、工作流管理、可视化和失败处理。

任务通过 requires() 定义依赖关系，Luigi 会确保任务按正确的顺序执行。

# TASK EXAMPLE

```python
import luigi

class MyTask(luigi.Task):
    param = luigi.Parameter()

    def requires(self):
        return UpstreamTask()

    def output(self):
        return luigi.LocalTarget('output.txt')

    def run(self):
        with self.output().open('w') as f:
            f.write(self.param)
```

# CAVEATS

生产环境建议使用中央调度器。没有内置的触发机制（可配合 cron）。Target 决定任务是否完成。需要 Python 3。带下划线的参数名在命令行上必须使用连字符（例如 my_parameter 对应 --my-parameter）。

# HISTORY

Luigi 由 **Spotify** 开发，于 **2012 年**开源，用于管理复杂的数据流水线和机器学习工作流。

# INSTALL

```nix: nix profile install nixpkgs#luigi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[airflow](/man/airflow)(1), [prefect](/man/prefect)(1)
