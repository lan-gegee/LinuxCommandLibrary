# TAGLINE

Elixir 构建工具和任务运行器

# TLDR

**创建新项目**

```mix new [project_name]```

**获取依赖**

```mix deps.get```

**编译项目**

```mix compile```

**运行测试**

```mix test```

**启动加载了项目的交互式 Shell**

```iex -S mix```

**格式化源文件**

```mix format```

**构建生产版本**

```mix release```

**列出所有可用任务**

```mix help```

# SYNOPSIS

**mix** [_task_] [_options_]

# PARAMETERS

**new** _NAME_
> 在名为 _NAME_ 的目录中创建新的 Elixir 项目。

**deps.get**
> 获取 `mix.exs` 中列出的所有项目依赖。

**deps.compile**
> 编译已获取的依赖。

**deps.update** _DEP_
> 更新指定依赖（或用 `--all` 更新全部）。

**compile**
> 编译当前项目及其依赖。

**test**
> 运行项目的测试套件。

**format**
> 按标准格式化器格式化 Elixir 源文件。

**run** _FILE_
> 在项目上下文中执行脚本或表达式。

**clean**
> 移除构建产物。

**release**
> 组装用于部署的自包含发行版。

**do** _task1_, _task2_
> 在一条命令中按顺序运行多个任务。

**help** [_TASK_]
> 列出所有可用任务，或显示特定任务的帮助。

# DESCRIPTION

**mix** 是 Elixir 自带的构建工具。它管理项目创建、依赖解析、编译、测试、代码格式化和发行版。所有功能通过基于任务的系统暴露，每个 `mix task` 对应一个 Mix.Task 模块。

依赖在 `mix.exs` 中声明，并从 Hex 软件包管理器获取。当前环境由 `MIX_ENV` 变量控制，默认为 `dev`（运行 `mix test` 时为 `test`）。自定义任务可以通过在 `Mix.Tasks.*` 下定义模块来创建。

# CAVEATS

需要安装 Elixir。安装软件包需要 Hex（`mix local.hex`）。`MIX_ENV` 环境变量控制激活的配置（`dev`、`test`、`prod`）。

# HISTORY

Mix 由 **José Valim** 创建，是 **Elixir** 的标准构建工具，随每个 Elixir 安装一起提供。

# INSTALL

```apt: sudo apt install elixir```

```dnf: sudo dnf install elixir```

```pacman: sudo pacman -S elixir```

```apk: sudo apk add elixir```

```zypper: sudo zypper install elixir```

```brew: brew install elixir```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[elixir](/man/elixir)(1), [iex](/man/iex)(1)
