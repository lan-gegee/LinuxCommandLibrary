# TAGLINE

按 worktree 隔离的开发栈编排器

# TLDR

在当前 worktree 中**启动 lich.yaml 所描述的栈**

```lich up```

在当前 worktree 中**停止栈**

```lich down```

**跟踪运行中栈的日志**

```lich logs```

**列出跨 worktree 的所有运行中栈**

```lich stacks```

**销毁本机上的每一个栈**

```lich nuke```

# SYNOPSIS

**lich** _command_ [_options_]

# DESCRIPTION

**lich** 读取一个描述开发栈（Docker 容器、宿主机进程、环境变量和生命周期）的 **lich.yaml** 文件，并以 **worktree 级隔离**的方式将其启动。同一栈的多个副本可以在一台机器上同时运行，不会发生端口冲突或资源争用，这在并行处理多个 Git 分支或 worktree 时非常有用。

服务（services）是 lich 通过 Docker 管理的容器，而 **owned** 条目是由 lich 启动并监督的宿主机进程（例如开发服务器）。端口可以发布到环境变量中以便进程相互发现，取值支持模板插值，例如 **${services.postgres.host_port}**。

# COMMANDS

**up**
> 在当前 worktree 中启动开发栈。

**down**
> 停止当前 worktree 中的开发栈。

**logs**
> 跟踪运行中栈的日志。

**stacks**
> 列出跨 worktree 的所有运行中栈，包括状态、运行时长、服务数量和 URL。

**nuke**
> 销毁本机上的所有栈。

# CONFIGURATION

项目根目录下的 **lich.yaml** 文件描述了整个栈。顶层键包括：

**version**
> 配置模式版本（当前为 1）。必填。

**services**
> 要管理的 Docker 容器。每个条目设置一个镜像、端口映射（可通过 published_env 选择性暴露）和环境变量。

**owned**
> 要管理的宿主机进程。每个条目设置一个工作目录（cwd）、一条命令（cmd）、一个端口和环境变量，支持对服务值的模板插值。

可将 **LICH_TELEMETRY** 环境变量设为 0 以禁用匿名使用遥测。

# HISTORY

**lich** 是一个用 **TypeScript** 编写、构建于 **Bun** 运行时之上的开源 CLI，由 **RPate97** 创建。它以 **MIT** 许可证发布，文档见 lich.sh。

# SEE ALSO

[docker](/man/docker)(1), [docker-compose](/man/docker-compose)(1), [foreman](/man/foreman)(1), [git](/man/git)(1)
