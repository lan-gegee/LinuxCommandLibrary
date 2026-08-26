# TAGLINE

在一个终端里监控你所有的编程智能体会话

# TLDR

**启动**监控所有智能体的终端 UI

```lazyagent```

仅**监控** Claude Code 会话

```lazyagent --agent claude```

仅**监控** Cursor 会话

```lazyagent --agent cursor```

**启动** HTTP API 服务器

```lazyagent --api```

在自定义地址上**启动 API**

```lazyagent --api --host [":8080"]```

以 macOS 菜单栏应用形式**启动**

```lazyagent --gui```

**同时运行全部三种**界面

```lazyagent --tui --gui --api```

# SYNOPSIS

**lazyagent** [_options_]

# PARAMETERS

**--agent** _name_
> 过滤指定的智能体：claude、cursor、opencode、pi、codex、amp 或 all（默认：all）

**--tui**
> 启动终端 UI（未指定任何界面时的默认行为）

**--gui**
> 以 macOS 菜单栏应用形式启动

**--api**
> 启动带 Server-Sent Events 的 HTTP API 服务器，实现实时更新

**--host** _address_
> 自定义 API 监听地址（默认：:3333）

**--help**
> 显示帮助信息

# DESCRIPTION

**lazyagent** 是一个终端 UI、macOS 菜单栏应用兼 HTTP API，用于监控机器上所有正在运行的编程智能体实例。它支持 **Claude Code**、**Cursor**、**OpenCode**、**pi**、**Codex CLI** 和 **Amp**。

与其他工具不同，lazyagent 既不取代也不修改你的工作流——它纯粹起观察作用。你可以在任何地方启动智能体（终端、IDE、桌面应用），lazyagent 会观察会话数据来判断每个会话正在进行的工作。无需对任何智能体做任何改动。

HTTP API 提供只读的 REST 接口，并借助 Server-Sent Events 实现实时推送更新，方便构建自定义仪表盘、移动应用，或与现有工具集成。

# CAVEATS

macOS 菜单栏应用（**--gui**）仅在 macOS 上可用；TUI 则可跨平台运行。lazyagent 是只读的，无法控制或修改智能体的行为。从源码构建需要 **Go 1.25+**，前端组件还需要 **Node.js 18+**。

# HISTORY

lazyagent 由 **Illegal Studio** 创建，主体使用 **Go** 编写，菜单栏应用的前端采用 **Svelte**。它于 **2025 年**首次发布，旨在满足开发者同时运行多个 AI 编程智能体时对统一监控视图日益增长的需求。

# SEE ALSO

[tmux](/man/tmux)(1), [htop](/man/htop)(1), [lazygit](/man/lazygit)(1)
