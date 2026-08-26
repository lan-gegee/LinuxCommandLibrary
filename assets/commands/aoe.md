# TAGLINE

Agent of Empires——并行 AI 编码代理的会话管理器

# TLDR

在当前目录**启动交互式 TUI**

```aoe```

**创建会话**并运行指定的代理 CLI

```aoe add --cmd [claude]```

在 worktree 分支上**添加会话**

```aoe add --cmd [claude] --branch [feature/login]```

**启动 Web 仪表盘**以便通过浏览器/手机访问

```aoe serve```

通过 HTTPS 配合二维码认证**公开暴露仪表盘**

```aoe serve --tunnel```

**查看调试日志**

```aoe logs```

**列出活动会话**（TUI 中也可查看）

```aoe list```

# SYNOPSIS

**aoe** [_command_] [_options_]

# PARAMETERS

**add**
> 创建新的代理会话。
> **--cmd** _name_：要启动的代理 CLI（claude、opencode、gemini、codex、copilot、cursor 等）。
> **--branch** _name_：在该分支上创建或关联一个 git worktree。
> **--sandbox**：在共享认证卷的 Docker 容器内运行会话。
> **--name** _label_：在 TUI 中显示的友好名称。

**list**
> 打印所有已知会话及其状态。

**attach** _name_
> 将当前终端附加到现有会话（等同于 tmux attach）。

**kill** _name_
> 终止会话并清理其 worktree。

**serve**
> 启动 Web 仪表盘。
> **--port** _n_：HTTP 端口（默认 8765）。
> **--tunnel**：通过 HTTPS 暴露仪表盘，支持基于二维码的手机配对。

**logs**
> 用最合适的查看器跟踪 AoE 守护进程日志。

**doctor**
> 打印环境诊断信息（检测到的 tmux、docker、代理可执行文件）。

**--help**, **-h**
> 打印帮助后退出。

**--version**
> 打印版本后退出。

# DESCRIPTION

**aoe**（Agent of Empires）是一款 Rust 编写的终端会话管理器，用于编排**并行运行的多个 AI 编码代理**。每个会话运行在自己的 **tmux** 窗口中——也可选择放入 **Docker** 沙箱——这样多个代理可以在同一仓库的不同分支上工作而互不干扰。默认调用会打开一个 **TUI**，显示所有会话及其当前状态（运行中、等待输入、空闲），并提供 diff 查看器，让你无需离开终端即可审查更改。

开箱即用，aoe 知道如何启动 **Claude Code**、**OpenCode**、**Gemini CLI**、**Codex CLI**、**Copilot CLI**、**Cursor CLI**、**Mistral Vibe**、**Pi.dev**、**Factory Droid**、**Hermes**、**Qwen Code** 和 **Kiro CLI**。由于底层 tmux 服务器保持它们存活，会话可在 SSH 断开、终端关闭和 aoe 重启后继续存在。独立的 **Web 仪表盘**（**aoe serve**）让同样的会话可以从浏览器访问，配合 **--tunnel** 还能通过 HTTPS 从手机访问。

# CONFIGURATION

**~/.config/aoe/**
> 用户配置：代理定义、默认分支命名、仪表盘认证。

**~/.local/share/aoe/**
> 各会话的状态、日志和 worktree 元数据。

**tmux**
> 必需的运行时依赖；每个会话都是一个 tmux 窗口。使用 **Ctrl+b d** 可分离回到 AoE TUI。

**Docker**
> 可选。使用 **--sandbox** 时必需；AoE 会绑定挂载代理的认证目录，使沙箱中的会话保持登录状态。

# CAVEATS

不支持原生 Windows——请改用 **WSL2**。必须安装 **tmux** 并位于 **PATH** 中。沙箱会话与主机共享认证卷，容器内的代理可以看到机密信息；请像在本地运行代理一样谨慎对待。Web 仪表盘处于 **beta** 阶段；如果要针对其 API 编写脚本，请固定版本号。

# HISTORY

**Agent of Empires** 由 **Mozilla.ai** 的 **Nate Brake** 创建并于 **2025 年末**发布，旨在解决在笔记本电脑或远程服务器上跨长生命周期会话同时运行多个编码代理的实际需求。它以 **Rust** 编写，通过 **Homebrew**、**Nix**、**Cargo** 和安装脚本分发，采用 **MIT** 许可证。

# INSTALL

```brew: brew install aoe```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[tmux](/man/tmux)(1), [claude](/man/claude)(1), [gemini](/man/gemini)(1), [git-worktree](/man/git-worktree)(1)
