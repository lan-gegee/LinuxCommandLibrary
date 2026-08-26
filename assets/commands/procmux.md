# TAGLINE

以可切换终端并行运行多个命令的 TUI 工具

# TLDR

**使用默认配置启动 procmux**

```procmux```

**使用指定的配置文件启动**

```procmux --config [path/to/procmux.yaml]```

**使用配置文件和覆盖文件启动**

```procmux --config [path/to/procmux.yaml] --config-override [path/to/override.yaml]```

**通过信号停止指定名称的进程**

```procmux signal-stop --name '[process-name]' --config [path/to/procmux.yaml]```

**通过信号启动指定名称的进程**

```procmux signal-start --name '[process-name]' --config [path/to/procmux.yaml]```

**列出所有已配置的进程**

```procmux signal-list --config [path/to/procmux.yaml]```

# SYNOPSIS

**procmux** [_options_]
**procmux** _signal-command_ **--name** _name_ **--config** _file_

# PARAMETERS

**--config** _FILE_
> procmux YAML 配置文件的路径。

**--config-override** _FILE_
> 用于覆盖主配置中各项值的 YAML 文件路径。

**signal-start** **--name** _NAME_ **--config** _FILE_
> 启动指定名称的进程。

**signal-stop** **--name** _NAME_ **--config** _FILE_
> 停止指定名称的进程。

**signal-restart** **--name** _NAME_ **--config** _FILE_
> 重启指定名称的进程。

**signal-stop-running** **--config** _FILE_
> 停止当前所有正在运行的进程。

**signal-restart-running** **--config** _FILE_
> 重启当前所有正在运行的进程。

**signal-list** **--config** _FILE_
> 列出所有已配置的进程。

# DESCRIPTION

**procmux** 是一个 TUI 工具，用于在易于切换的终端窗格中并行运行多个命令。它旨在帮助项目新手浏览和运行必要的命令，同时减少为长时间运行的进程手动管理多个终端会话的需要。配置通过 YAML 文件定义。

当配置中启用了 signal 服务器时，procmux 会启动一个 HTTP 服务器，允许通过 signal 子命令远程控制进程。该应用支持进程过滤、自动启动选项、描述和元标签。

# CAVEATS

依赖插值（配置的提示输入）的进程无法通过 signal 子命令启动或重启，因为所需的输入值只在交互式 TUI 中可用。

# HISTORY

**procmux** 由 **napisani** 创建，使用 **Python** 编写。

# SEE ALSO

[tmux](/man/tmux)(1), [mprocs](/man/mprocs)(1), [process-compose](/man/process-compose)(1), [screen](/man/screen)(1)
