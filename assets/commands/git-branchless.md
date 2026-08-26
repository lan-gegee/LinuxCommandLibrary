# TAGLINE

面向高速度 Git 工作流的工具集，提供 smartlog 和撤销功能

# TLDR

在仓库中**初始化 git-branchless**

```git branchless init```

**显示 smart log** 可视化图

```git sl```

**撤销上一次 git 操作**

```git undo```

**将所有本地分支**与上游同步

```git sync```

**将一个提交移到**不同的父节点

```git move -s [commit] -d [destination]```

**导航到堆栈中的下一个提交**

```git next```

**导航到堆栈中的上一个提交**

```git prev```

在 smartlog 中**显示隐藏的提交**

```git sl --hidden```

# SYNOPSIS

**git branchless** [_options_] _command_ [_args_...]

# COMMANDS

**init**
> 在仓库中初始化 git-branchless。

**smartlog**, **sl**
> 渲染你正在处理的提交的可视化图。

**undo**
> 通用的撤销功能，可撤销任何 git 操作。

**sync**
> 变基所有本地提交堆栈和分支。

**move** **-s** _source_ **-d** _dest_
> 将提交移动到 DAG 中的其他位置。

**next** [_n_]
> 检出堆栈中的下一个提交。

**prev** [_n_]
> 检出堆栈中的上一个提交。

**restack**
> 在父提交被更改后重新应用提交。

**hide** _commit_
> 从 smartlog 中隐藏一个提交。

**unhide** _commit_
> 取消隐藏先前隐藏的提交。

**submit**
> 为提交堆栈创建或更新拉取请求。

**test**
> 对堆栈中的提交运行测试。

**query** _revset_
> 使用 revset 表达式查询提交。

**install-man-pages**
> 生成并安装 man page。

# PARAMETERS

**-C** _path_
> 以指定的目录作为启动目录运行。

**--color** _when_
> 控制彩色输出：always、never、auto。

**--hidden**
> 显示隐藏的提交（配合 smartlog 使用）。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本号。

# DESCRIPTION

**git-branchless** 是一套增强 Git 的工具，面向高速度、monorepo 规模的工作流。它借鉴了 Mercurial 等其他版本控制系统以及 Meta 内部工具的理念。

**smartlog**（**git sl**）以直观的方式可视化你的提交图，只显示相关的提交。与 git log 不同，它关注的是进行中的工作而非完整历史。

**undo** 命令几乎可以撤销任何 Git 操作，包括硬重置、变基和修改提交。它通过一个隐藏日志来维护仓库状态的历史。

Git-branchless 使用 **revset 表达式**，这是一种类似于 Mercurial 的声明式提交指定语言。由此可以进行强大的查询，例如 **stack()**（当前堆栈中的所有提交）或 **draft()**（本地未发布的提交）。

**move** 命令可以在不影响工作副本的情况下重新安置整个提交子树，并自动清理过时的分支。

# CONFIGURATION

**.git/hooks/**
> git-branchless init 会安装自定义钩子（post-commit、post-rewrite 等），用于跟踪提交可见性和 DAG 变化。

**.git/config**
> 在 [branchless] 部分存储 branchless 专属设置，包括默认 revset 查询和显示偏好。

# CAVEATS

需要在每个仓库中先执行 **git branchless init** 进行初始化。部分功能会修改 Git 钩子和配置。并非与所有 Git 图形界面工具兼容。对只用过 Git 的用户来说，学习 revset 语法有一定门槛。

# HISTORY

Git-branchless 由 **Waleed Khan** 创建，灵感来自 Meta 的内部 Git 工具和 Mercurial 的 evolve 扩展。项目于 **2021 年**前后开始开发，目标是为 Git 带来堆叠式差异工作流和更强的撤销能力。该项目将提交演化、提交可见性等概念引入标准 Git 仓库。

# INSTALL

```pacman: sudo pacman -S git-branchless```

```apk: sudo apk add git-branchless```

```brew: brew install git-branchless```

```nix: nix profile install nixpkgs#git-branchless```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [git-absorb](/man/git-absorb)(1), [lazygit](/man/lazygit)(1), [tig](/man/tig)(1)

# RESOURCES

```[Source code](https://github.com/arxanas/git-branchless)```

```[Documentation](https://github.com/arxanas/git-branchless/wiki)```

<!-- verified: 2026-07-17 -->
