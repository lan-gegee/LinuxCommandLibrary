# TAGLINE

在 git worktree 中运行的分层智能体循环

# TLDR

从 PyPI **安装** CLI

```pip install plasma-fractal```

为已初始化的项目**打开**实时 TUI 仪表盘

```fractal open```

将内置的智能体技能**安装**到你的 agent 配置中

```fractal install```

**显示**顶层帮助

```fractal --help```

以浅色配色方案**打开**仪表盘

```fractal open --light```

# SYNOPSIS

**fractal** [_command_] [_options_]

# DESCRIPTION

**fractal**（Python 软件包 **plasma-fractal**）运行可自我组织成树状结构的分层自主智能体循环。每个节点在自己的 **git worktree** 内朝目标迭代，并可以为可拆分的子任务派生子节点，因此树会随问题规模生长，而不是遵循固定计划。

硬性上限（迭代次数、深度、子节点数、成本、时间）约束着每一个循环；操作者可以随时引导或停止工作。包括成本在内的运行元数据存储在本地 **SQLite** 数据库中，可在终端 UI（**fractal open**）中实时查看。智能体运行在 **tmux** 会话中。

支持的智能体后端包括 Claude Code（**claude**）、Codex（**codex**）、Grok Build（**grok**）、OpenCode（**opencode**）和 Oh My Pi（**omp**），可通过 **--agent** 为每个节点选择。当设置了 **OPENROUTER_API_KEY** 时，Claude 和 Codex 可通过 **--provider=openrouter** 经由 OpenRouter 路由。

节点通常通过 **/fractal** 智能体技能（插件市场或 **fractal install**）派生，该技能会引导设置节点参数并在 tmux 中启动工作。也可以直接使用 CLI；运行 **fractal \<command\> --help** 查看各命令的选项。

# PARAMETERS

**open** [**--light**]
> 从已初始化为 fractal 的项目根目录打开 TUI 仪表盘。**--light** 适合浅色终端主题。

**install** [**--link**] [**--project**]
> 将 fractal 与 wiki 技能复制或符号链接到 agent 技能目录（**~/.claude/skills**、**~/.agents/skills**）。**--link** 用符号链接代替复制；**--project** 将安装范围限定在当前项目。

其他子命令用于管理节点生命周期、运行和配置（见 **fractal --help** 和 **fractal \<command\> --help**）。派生节点时的常用参数包括 **name**、**path**、**base** 分支、**agent**、**provider**、**model**、**max-iters**、**max-depth**、**max-children**、**timeout**、**max-cost** 以及相关的预算/时间限制。

# CAVEATS

需要 git 仓库；若要实时智能体会话，还需要 **tmux** 以及位于 **PATH** 中的所选智能体 CLI。成本上限与 provider 路由依赖于正确的 API 凭据。通过 **pipx**/**uv tool** 安装时可能需要同时安装 **plasma-wiki**，以便 **wiki** 辅助工具可用。节点名称受到限制（在技能工作流中只允许字母、数字和 **_**）。

# HISTORY

**fractal** 是 Plasma AI 的 Apache-2.0 项目，用于具有本地可观测性的递归多智能体 worktree。

# INSTALL

```dnf: sudo dnf install fractal```

```pacman: sudo pacman -S fractal```

```apk: sudo apk add fractal```

```zypper: sudo zypper install fractal```

```nix: nix profile install nixpkgs#fractal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [git](/man/git)(1), [git-worktree](/man/git-worktree)(1)

# RESOURCES

```[Source code](https://github.com/plasma-ai/fractal)```

```[Documentation](https://docs.plasma.ai/fractal)```

<!-- verified: 2026-07-22 -->
