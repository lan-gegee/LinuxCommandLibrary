# TAGLINE

基于终端的自动文件整理工具

# TLDR

**启动 TUI 管理规则**

```hazelnut```

**启动后台守护进程监视文件夹**

```hazelnutd```

**初始化新配置**

```hazelnut init```

**列出所有已配置的规则**

```hazelnut list```

**对目录试运行规则**

```hazelnut run --dir [~/Downloads]```

**对目录应用规则**

```hazelnut run --dir [~/Downloads] --apply```

**使用自定义配置文件**

```hazelnut --config [path/to/config.toml]```

# SYNOPSIS

**hazelnut** [_command_] [_options_]

**hazelnutd** [_options_]

# PARAMETERS

**init**
> 初始化新的配置文件。

**list**
> 列出所有已配置的规则。

**run**
> 对目录试运行或应用规则。

**update**
> 检查更新。

**--config** _path_
> 指定自定义配置文件。

**--dir** _path_
> 指定要处理的目录（与 run 搭配使用）。

**--apply**
> 应用规则而非试运行（与 run 搭配使用）。

# DESCRIPTION

**hazelnut** 是一款基于终端的自动文件整理工具，灵感来自 macOS 上的 **Hazel**。它监视文件夹并按照用户定义的规则整理文件。该工具由两个组件构成：交互式创建和管理规则的 **TUI**，以及在后台持续应用规则的**守护进程**（hazelnutd）。

规则定义在人类可读的 **TOML** 配置文件中，可以对匹配的文件触发移动、复制、重命名、归档、删除、移入废纸篓或执行自定义命令等操作。匹配条件包括文件扩展名、名称模式、大小和文件年龄。

# CONFIGURATION

规则存储在 TOML 配置文件中。每条规则指定一个监视文件夹、文件匹配条件（按扩展名、名称模式、大小、年龄）以及要执行的操作。多条规则可以匹配同一个文件，所有匹配的规则按顺序依次执行。

# CAVEATS

守护进程（hazelnutd）仅在 **macOS** 和 **Linux** 上可用；Windows 上只有 TUI 可用。文件监视依赖操作系统级的文件系统通知 API，在某些文件系统上可能有局限。

# HISTORY

**hazelnut** 由 **Ricardo Dantas** 创建，使用 **Rust** 和 **Ratatui** TUI 库编写。它的灵感来自广受欢迎的 macOS 自动化应用 Hazel，将类似的文件整理能力带到了终端。

# INSTALL

```pacman: sudo pacman -S hazelnut```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[watch](/man/watch)(1), [find](/man/find)(1), [mv](/man/mv)(1)
