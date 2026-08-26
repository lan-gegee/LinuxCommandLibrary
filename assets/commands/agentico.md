# TAGLINE

面向长时间运行 AI 编码代理的 TUI 编排器

# TLDR

**启动仪表盘**并在终端中管理特性

```agentico```

**就地安装或更新**二进制文件

```agentico update```

**仅以指定的 AI 提供方**启动

```agentico --providers claude,codex```

# SYNOPSIS

**agentico** [_options_]

# DESCRIPTION

**agentico** 是 Agentic Orchestrator 的命令行界面。Agentic Orchestrator 是一款基于终端的工作流管理器，能把高层次的特性需求转化为持续推进的工程流水线。它借助彼此隔离的 Git worktree、结构化的规划产物、实现循环、代码评审和拉取请求发布来协调 AI 编码代理，因此多个复杂特性可以并行推进而不会混淆状态。

首次启动时，agentico 会走一遍欢迎流程让你选择工作区目录，随后打开交互式仪表盘。在这里你可以创建特性、观察进行中的工作、回应审批提示并查看检查点。编排器会把各阶段路由给已安装提供方 CLI（如 **claude**、**codex**、**opencode**）中最合适的可用模型，仓库与拉取请求操作则由 **git** 和 **gh** 负责。

流水线深度按特性选择：Medium 对小改动省去前期调研；Large 增加知识库、问询、调研和设计阶段；Moonshot 深度相同但评审关卡更严格。人工检查点可在问询、调研、设计、路线图和发布等决策环节暂停等待确认。

# PARAMETERS

**--providers** _LIST_
> 将编排限制在特定的提供方 CLI（逗号分隔），例如 `claude`、`codex` 或 `opencode`。

**update**
> 按最初使用的安装方式（Homebrew、发布的二进制或 Go install）更新 agentico。

# CAVEATS

agentico 需要 **git** 以及完成 GitHub 认证的 **gh** CLI。必须至少安装并认证一款受支持且版本足够新的 AI 提供方 CLI；缺失或过旧的提供方会在启动时被跳过并给出提示。该工具围绕多仓库 Git worktree 和长期运行的代理会话设计，因此在大型并行工作负载下，磁盘空间、API 配额和提供方可用性都很重要。

# HISTORY

Agentic Orchestrator 由 **DoorDash OSS** 于 2026 年开源，是一个基于 Go 的 TUI，用于监督代理式编码工作流。面向用户的二进制文件命名为 **agentico**，以区分本地 CLI 与整个编排系统。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [gh](/man/gh)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/doordash-oss/agentic-orchestrator)```

<!-- verified: 2026-06-30 -->
