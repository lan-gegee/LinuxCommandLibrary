# TAGLINE

用于管理多个仓库的 CLI 工具

# TLDR

**初始化 mani 配置**

```mani init```

**同步（克隆）所有仓库**

```mani sync```

**在所有项目上执行命令**

```mani exec "[command]"```

**只在带有特定标签的项目上执行命令**

```mani exec --tags [frontend] "[command]"```

**运行预定义任务**

```mani run [task_name]```

**列出所有项目**

```mani list projects```

**列出所有可用任务**

```mani list tasks```

# SYNOPSIS

**mani** _command_ [_options_]

# PARAMETERS

**init**
> 在当前目录中初始化新的 mani 配置。

**sync**
> 克隆并更新配置中定义的所有仓库。

**exec** _command_
> 跨项目执行 shell 命令。

**run** _task_
> 运行配置中预定义的任务。

**list** _resource_
> 列出项目、标签或任务。

**--tags** _tags_
> 按标签筛选项目（逗号分隔）。

**--projects** _projects_
> 按项目名称筛选（逗号分隔）。

**--all-projects**
> 面向包括根目录在内的所有项目。

**--parallel**
> 跨项目并行执行命令。

**--output** _format_
> 输出格式：stream、table、markdown 或 html。

# DESCRIPTION

**mani** 是一个用于从中央工作区管理多个仓库的 CLI 工具。你在 **mani.yaml** 配置文件中定义仓库和命令，然后即可跨全部或部分项目执行命令。

其特性包括按名称、标签或路径灵活选择项目，多种输出格式（stream、table、markdown、HTML），跨项目并行执行，以及支持自定义命令的预定义任务。

# CONFIGURATION

**mani.yaml**
> 中央配置文件，定义仓库、标签和任务。

# CAVEATS

所有仓库必须能被运行 mani 的机器访问。克隆操作需要网络连接。

# HISTORY

**mani** 由 **alajmo** 创建，使用 **Go** 语言编写。

# INSTALL

```brew: brew install mani```

```nix: nix profile install nixpkgs#mani```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [mr](/man/mr)(1)
