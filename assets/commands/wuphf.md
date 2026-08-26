# TAGLINE

面向 AI 编程助手的多智能体协作办公室

# TLDR

**启动** WUPHF 办公室并打开 Web UI

```npx wuphf```

使用指定的智能体提供方**运行**

```npx wuphf --provider [codex]```

**使用**基于 tmux 的终端 UI 而不是 Web 界面

```npx wuphf --tui```

**选择**预定义的智能体团队包

```npx wuphf --pack [coding-team]```

**选择**记忆后端

```npx wuphf --memory-backend [markdown]```

与特定智能体**开启一对一**会话

```npx wuphf --1o1 [ceo]```

**运行**时不自动打开浏览器

```npx wuphf --no-open```

**使用自定义的** Web UI 端口

```npx wuphf --web-port [7891]```

# SYNOPSIS

**wuphf** [_options_] [_subcommand_]

# PARAMETERS

**--memory-backend** _name_
> 选择共享记忆后端：**nex**、**gbrain**、**markdown**（默认）或 **none**。

**--pack** _name_
> 选择预配置的智能体团队：**starter**、**founding-team**、**coding-team**、**lead-gen-agency** 或 **revops**。

**--provider** _name_
> 驱动各智能体的 LLM CLI：**claude-code**（默认）、**codex** 或 **openclaw**。

**--tui**
> 使用基于 tmux 的终端 UI 而不是 Web UI。

**--no-nex**
> 禁用 Nex 后端，同时保留本地集成。

**--no-open**
> Web UI 启动时不打开默认浏览器。

**--opus-ceo**
> 将 CEO 智能体从 Sonnet 升级为 Opus。

**--collab**
> 启用协作模式（默认）。

**--unsafe**
> 绕过智能体权限检查；仅限本地实验环境使用。

**--web-port** _N_
> Web UI 端口（默认 **7891**）。

**--1o1** [_agent_]
> 与 CEO 开启一对一聊天；若给出名称则与指定智能体聊天。

**init**
> 运行初始设置并写入配置文件。

**shred**
> 终止当前办公室会话并清理本地状态。

# DESCRIPTION

**wuphf** 是"AI 员工版 Slack"——一个多智能体协作层，它会组建一个由角色化智能体（CEO、PM、工程师、设计师、CMO、CRO）组成的小型办公室，共享统一的记忆存储和聊天式频道。wuphf 不让每个 AI 助手孤立运行，而是让它们看到彼此的消息、认领任务、协作完成工作，并在会话之间保持上下文。

在底层，wuphf 将每个智能体委派给现有的 CLI，例如 **claude-code**、**codex** 或 **openclaw**，并默认在 **http://localhost:7891** 提供 Web UI，其中包含团队名册、共享频道和消息编辑器。**--tui** 模式则在 tmux 会话中呈现同一个办公室，适合纯终端环境。

记忆可通过 **--memory-backend** 插拔切换：**markdown** 后端在磁盘上维护一份人类可读的 Markdown 大脑，而 **nex** 和 **gbrain** 则对接托管服务。智能体名册由 **--pack** 选项描述，自定义团队包可以在配置中定义。

# CONFIGURATION

运行 **wuphf init** 后，配置会存储在本地并在每次启动时读取。必需的运行时依赖包括 **node** / **npx**、**python3**、**curl**、**tmux**（**--tui** 模式所需），以及 PATH 上至少一个受支持的 LLM CLI（**claude**、**codex** 或 **openclaw**）。API 密钥取自底层 CLI 自身的配置——wuphf 本身不存储密钥。

# CAVEATS

wuphf 是一个早期阶段的编排层，标志名称和团队包内容在不同版本间可能变化。**--unsafe** 标志会禁用每个智能体的权限检查，切勿在隔离的一次性环境之外使用。由于智能体会调用外部 LLM CLI，费用和速率限制取决于每个 CLI 背后的提供商账户。

# HISTORY

**wuphf** 由 **Nex** 开发，发布于 **github.com/nex-crm/wuphf**。其名字致敬美剧 *Parks and Recreation* 中虚构的通知服务。它通过 **npm** 分发，可用 **npx wuphf** 免全局安装运行。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [tmux](/man/tmux)(1), [npx](/man/npx)(1)
