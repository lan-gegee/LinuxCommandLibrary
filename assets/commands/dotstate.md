# TAGLINE

集成 Git 的现代 dotfile 管理器

# TLDR

**初始化**一个新的 dotstate 仓库

```dotstate init [directory]```

将文件**加入** dotstate 跟踪

```dotstate add [path/to/file]```

**同步** dotfiles 到当前系统

```dotstate sync```

**跟踪**并提交更改

```dotstate commit -m "message"```

# SYNOPSIS

**dotstate** [_command_] [_options_] [_arguments_]

# PARAMETERS

**-c, --config** _FILE_
> 配置文件路径

**-d, --dotfiles** _DIR_
> Dotfiles 仓库目录

**-v, --verbose**
> 启用详细输出

**--dry-run**
> 只显示将要执行的操作，不实际更改

**-h, --help**
> 显示帮助并退出

**--version**
> 显示版本并退出

# DESCRIPTION

**dotstate** 是一个现代 dotfile 管理器，使用 Git 进行版本控制，同时为常见的 dotfile 操作提供简化接口。它通过在 Git 仓库中跟踪配置文件，帮助用户在多台机器之间管理配置。

该工具提供初始化 dotfiles 仓库、添加文件进行跟踪、在系统间同步配置以及处理平台特定文件的命令。它在主目录中的实际 dotfiles 与仓库之间保持清晰的分离。

# COMMANDS

**init** [_DIRECTORY_]
> 初始化一个新的 dotstate 仓库

**add** _FILE_
> 将文件加入 dotstate 跟踪

**remove** _FILE_
> 停止跟踪某个文件

**sync**
> 将 dotfiles 同步到当前系统

**status**
> 显示仓库状态

**commit** [_-m_ _MESSAGE_]
> 提交更改到仓库

**push**
> 推送更改到远程

**pull**
> 从远程拉取更改

**list**
> 列出所有被跟踪的文件

# CAVEATS

需要已安装并配置 Git。同步期间可能覆盖现有文件——建议先备份。平台特定配置需手动处理。符号链接的处理因操作系统而异。

# HISTORY

**dotstate** 作为传统 dotfile 管理器的现代化替代品而创建，注重简洁与 Git 集成。它的目标是提供版本控制的强大能力，同时免去手动 Git 操作的复杂度。

# SEE ALSO

[git](/man/git)(1), [stow](/man/stow)(1), [chezmoi](/man/chezmoi)(1), [yadm](/man/yadm)(1)
