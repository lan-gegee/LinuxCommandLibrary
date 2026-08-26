# TAGLINE

跨提供商并行运行 AI 编程智能体的统一 CLI

# TLDR

**启动本地守护进程**，用于托管运行中的智能体

```paseo daemon start```

以指定的提供商和提示词**启动一个智能体**

```paseo run --provider [claude/opus-4.6] "[implement user authentication]"```

在独立的 git worktree 中**启动智能体**，使其编辑保持隔离

```paseo run --worktree [feature-branch] --provider [codex] "[refactor the payment module]"```

**列出守护进程管理的当前运行中的智能体**

```paseo ls```

按 ID **流式查看运行中智能体的实时输出**

```paseo attach [agent_id]```

向活动中的智能体**发送后续指令**

```paseo send [agent_id] "[also add unit tests]"```

**指定远程守护进程**而非本地守护进程

```paseo run --host [host:port] --provider [opencode] "[review the diff]"```

# SYNOPSIS

**paseo** _subcommand_ [_options_]

**paseo** **run** **--provider** _PROVIDER_ [**--worktree** _BRANCH_] [**--host** _HOST_] _prompt_

**paseo** **ls**

**paseo** **attach** _agent_id_

**paseo** **send** _agent_id_ _message_

**paseo** **daemon** **start** | **stop** | **status**

# DESCRIPTION

**paseo** 是一个命令行客户端和本地守护进程，通过单一界面编排多个 AI 编程智能体。每次调用 **paseo run** 都会在受支持的提供商（Claude Code、Codex、GitHub Copilot、OpenCode、Pi）之一下启动一个智能体进程，并向守护进程注册；守护进程让智能体跨终端会话保持存活，并使其可接收后续消息或被实时附加。

典型工作流是先用 **paseo daemon start** 启动一次守护进程，然后针对不同的提示词或分支并行发起多个智能体，用 **paseo ls** 查看它们的状态和 ID，再通过 **attach** 或 **send** 与需要关注的智能体交互。由于每个智能体都可以绑定到自己的 git worktree，并行的智能体可以在相互隔离的分支上工作，不会互相覆盖编辑内容。

守护进程模式还支持跨设备使用：工作站上运行的守护进程可以通过 **--host** 从笔记本访问，因此长时间运行的智能体会话可以超越任何单个 shell 或设备而存在。Paseo 将自身定位为底层编程智能体 CLI 之上的轻量协调层，而不是独立的 AI：模型选择和提示词会直接交给所选的提供商。

# PARAMETERS

**--provider** _PROVIDER_

> **paseo run** 必需。选择底层的编程智能体，例如 **claude/opus-4.6**、**codex**、**copilot**、**opencode**、**pi**。适用时请使用提供商自己的模型标识符。

**--worktree** _BRANCH_

> 在 _BRANCH_ 上专用的 git worktree 中运行智能体，使其文件编辑与其他并行智能体保持隔离。

**--host** _HOST_

> 将命令路由到 _HOST_ 处（例如 **host:port**）的远程 Paseo 守护进程，而不是本地的守护进程。

# SUBCOMMANDS

**run**

> 在所选提供商下以给定提示词启动一个新智能体。

**ls**

> 列出正在运行的智能体及其 ID、提供商和状态。

**attach** _id_

> 流式查看智能体的实时输出。分离后智能体继续运行。

**send** _id_ _message_

> 向已在运行的智能体发送后续消息。

**daemon start | stop | status**

> 管理托管运行中智能体的本地 Paseo 守护进程。

# INSTALLATION

```
npm install -g @getpaseo/cli
```

安装后，先运行一次 **paseo daemon start** 以启动本地守护进程。

# CAVEATS

**paseo** 只是一个薄封装：它不替代底层的提供商 CLI，每个提供商都必须单独安装并进行身份验证。API 费用和速率限制照常按提供商计算。

守护进程会让智能体在后台保持存活。忘记执行 **paseo ls** 或 **paseo daemon stop** 可能导致长期运行的智能体进程（及其 token 消耗）悄然累积。

使用 **--worktree** 创建的 worktree 在智能体退出后会保留在磁盘上。不再需要时，可用 **git worktree remove** 清理。

# HISTORY

**paseo** 是 **getpaseo** 团队的较新项目（2026 年首次公开发布），采用 **AGPL-3.0** 许可证发布。它伴随多智能体编程工作流的兴起趋势而生，旨在为同时运行 Claude Code、Codex、Copilot、OpenCode 和 Pi 的用户提供统一界面、统一历史和统一守护进程。

# INSTALL

```aur: yay -S paseo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [copilot](/man/copilot)(1), [git-worktree](/man/git-worktree)(1)
