# TAGLINE

面向多个 Get-Shit-Done 工作流项目的终端仪表盘

# TLDR

**启动 TUI**，显示所有已注册的 GSD 项目

```gsd-meta-manager```

将项目目录**注册到全局注册表**

```gsd-meta-manager add [path/to/project]```

以自定义别名**注册**

```gsd-meta-manager add [path/to/project] [alias]```

按名称或别名从注册表中**移除项目**

```gsd-meta-manager remove [project]```

将所有已注册的项目**列出**到 stdout

```gsd-meta-manager list```

**使用非默认配置文件**

```gsd-meta-manager --config [path/to/config.json]```

**显示版本号**

```gsd-meta-manager --version```

# SYNOPSIS

**gsd-meta-manager** [_--config FILE_] [_subcommand_] [_args_]

**gsd-meta-manager add** _PATH_ [_ALIAS_]

**gsd-meta-manager remove** _PROJECT_

**gsd-meta-manager list**

# PARAMETERS

**--config** _FILE_
> 覆盖默认配置文件位置。

**--version**
> 打印版本号并退出。

**--help**
> 显示帮助信息。

# SUBCOMMANDS

**add** _PATH_ [_ALIAS_]
> 将 _PATH_ 处的 GSD 项目注册到全局注册表。_ALIAS_ 设置自定义显示名称。

**remove** _PROJECT_
> 从注册表中移除一个项目，通过别名或路径标识。

**list**
> 打印所有已注册的项目。

**help** [_SUBCOMMAND_]
> 显示特定子命令的帮助。

# KEY BINDINGS

**j**, **k**
> 在项目列表中下移或上移。

**Enter**
> 打开所选项目的详情视图。

**Tab**, **Shift+Tab**
> 在详情标签页之间切换。

**/**
> 激活搜索与过滤模式。

**a**
> 交互式添加新项目。

**n**
> 创建全新的 GSD 项目。

**d**
> 从注册表中删除所选项目。

**?**
> 显示应用内帮助。

**q**
> 退出应用程序。

# DESCRIPTION

**gsd-meta-manager** 是一个 Rust 终端 UI，它将多个 GSD（"Get Shit Done"）工作流项目的状态汇总到单一仪表盘中。它直接从磁盘读取项目状态，自动检测绑定到 GSD 项目的 Claude Code 会话，无需任何后台守护进程即可展示进度。

每个已注册的项目都可以通过包含 10 个标签页的详情视图查看：**Phases**、**Roadmap**（渲染为 ASCII DAG）、**Backlog**、**Git History**、**Pipeline**、**Queue**、**Sessions**、**Archive**、**Config** 和 **Docs**。其设计意图是让多项目状态成为默认视图，而不是靠人手在许多终端间拼凑出来。

# CONFIGURATION

**~/.config/gsd-meta-manager/config.json**
> 默认注册表文件。存储已注册项目路径和别名的列表。可用 **--config** 覆盖。

# CAVEATS

该工具只反映磁盘上各项目中已有的状态；它不会运行流水线、编辑代码或推送提交。项目必须已经遵循 GSD 布局，**Phases** 和 **Roadmap** 等标签页才能渲染出有意义的内容。

# HISTORY

**gsd-meta-manager** 由 **bitcreed** 于 2026 年以 MIT 许可证发布。它通过 **crates.io** 分发，从源码构建需要 Rust 1.85 或更新版本。

# SEE ALSO

[cargo](/man/cargo)(1), [git](/man/git)(1), [tmux](/man/tmux)(1)
