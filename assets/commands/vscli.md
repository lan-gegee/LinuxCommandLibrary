# TAGLINE

用于启动 VS Code 开发容器的 CLI/TUI 工具

# TLDR

**在 VS Code 中打开当前目录**

```vscli open```

**打开指定的项目目录**

```vscli open [path/to/project]```

**使用 Cursor 编辑器而非 VS Code 打开**

```vscli open --command cursor .```

**强制以开发容器方式打开**

```vscli open --behavior force-container```

**交互式浏览最近打开的项目**

```vscli recent```

**试运行查看将启动的内容而不实际打开**

```vscli open --dry-run```

# SYNOPSIS

**vscli** [_options_] _command_ [_arguments_]

# SUBCOMMANDS

**open** [_PATH_] [_ARGS_]
> 在 VS Code 中打开项目。自动检测开发容器配置。默认为当前目录。

**recent**
> 打开一个交互式的最近使用工作区列表。

# PARAMETERS

**--command** _EDITOR_
> 指定要使用的编辑器命令（例如 code、code-insiders、cursor）。

**--behavior** _BEHAVIOR_
> 更改启动行为：force-container 或 force-classic。

**-s**, **--history-path** _PATH_
> 覆盖历史文件的默认路径。

**-d**, **--dry-run**
> 显示将要启动的内容，但不实际打开编辑器。

**-v**, **--verbose**
> 提高日志详细程度。

**-q**, **--quiet**
> 降低日志详细程度。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**vscli** 简化了 VS Code 项目的启动，尤其专注于开发容器。它会自动检测项目是否使用开发容器并据此启动。当一个项目包含多个开发容器配置时，vscli 会提示你选择其中一个。它支持多种编辑器，包括 VS Code、VS Code Insiders 和 Cursor。它还会记录最近的项目，通过交互式 TUI 列表快速访问。

# HISTORY

**vscli** 由 **michidk** 创建，使用 **Rust** 编写。可通过 Cargo、Homebrew、Chocolatey 或 winget 安装。

# INSTALL

```brew: brew install vscli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[code](/man/code)(1)
