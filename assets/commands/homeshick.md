# TAGLINE

用 Bash 编写的基于 Git 的 dotfile 同步器

# TLDR

**创建**新的 castle（dotfiles 仓库）

```homeshick generate [castle_name]```

**跟踪** castle 中的文件

```homeshick track [castle_name] [path/to/file]```

**进入**某个 castle 目录

```homeshick cd [castle_name]```

**从 GitHub 克隆** castle

```homeshick clone [github_username]/[repository_name]```

**符号链接** castle 中的所有文件

```homeshick link [castle_name]```

**列出**已安装的 castle

```homeshick list```

**从远程更新**所有 castle

```homeshick pull```

# SYNOPSIS

**homeshick** [_options_] _command_ [_arguments_]

# PARAMETERS

**generate** _CASTLE_ [_CASTLE_...]
> 创建新的 castle（dotfiles 仓库）

**track** _CASTLE_ _FILE_ [_FILE_...]
> 将文件/文件夹移入 castle 并用符号链接替换原位置

**cd** _CASTLE_
> 切换到某个 castle 的仓库目录，便于直接运行 git 命令

**clone** _URL_...
> 从 Git 仓库克隆 castle（支持 GitHub "user/repo" 简写）

**link**, **symlink** [_CASTLE_...]
> 将给定 castle（或全部 castle）home 文件夹中的所有文件符号链接到 $HOME

**pull** [_CASTLE_...]
> 对给定 castle（或全部 castle）及其子模块运行 git pull

**check**, **updates** [_CASTLE_...]
> 检查各 castle 相对远程是落后、领先还是已最新

**refresh**
> 检查远程是否有更新，跳过最近一周内检查过的 castle

**list**, **ls**
> 列出所有已安装的 castle

**-q**, **--quiet**
> 抑制状态输出，仅在需要输入时显示

**-s**, **--skip**
> 跳过 $HOME 中冲突的文件而不覆盖它们

**-f**, **--force**
> 自动覆盖 $HOME 中冲突的文件

**-b**, **--batch**
> 以非交互方式运行，接受默认答案

**-v**, **--verbose**
> 打印额外的诊断信息

# DESCRIPTION

**homeshick** 是一个用 Bash 编写的、基于 Git 的 dotfile 同步器。它使用 "castle"（Git 仓库）来管理 dotfiles，通过符号链接把仓库中的文件链接到家目录。

每个 castle 都是保存在 **~/.homesick/repos/** 下的一个 Git 仓库。被跟踪进 castle 的文件（通过 **track**）会移动到仓库中，原位置则替换为指向仓库副本的符号链接。这样可以进行版本控制并方便地跨机器同步。多个 castle 可以并存，让你把自己的 dotfile 集合与共享的集合（例如 oh-my-zsh castle）组合起来。

# CAVEATS

需要 Bash 3+ 和 Git 1.5+。在某些文件系统或容器中符号链接可能无法正常工作。当多个 castle 包含同一文件时会产生冲突；可使用 **-f/--force** 或 **-s/--skip** 以非交互方式解决。

# HISTORY

homeshick 由 **Anders Ingemann** 创建，仓库历史可追溯到 **2012 年**，作为 homesick（一个 Ruby gem）的纯 Bash 替代品。其名称结合了 "home"（dotfiles）和 "shell"（Bash 实现）。

# INSTALL

```zypper: sudo zypper install homeshick```

```brew: brew install homeshick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chezmoi](/man/chezmoi)(1), [stow](/man/stow)(8), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/andsens/homeshick)```

```[Documentation](https://github.com/andsens/homeshick/wiki)```

<!-- verified: 2026-07-19 -->
