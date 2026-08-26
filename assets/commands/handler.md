# TAGLINE

A2A 协议客户端 TUI 与 CLI

# TLDR

**启动交互式 TUI**

```handler tui```

**启动本地 A2A 服务器智能体**

```handler server```

**向智能体发送消息**

```handler send --url [agent_url] --message "[message]"```

**验证 A2A 智能体**

```handler validate --url [agent_url]```

# SYNOPSIS

**handler** _command_ [_options_]

# DESCRIPTION

**handler** 是面向 **A2A（Agent-to-Agent）协议**的客户端和开发者工具包，同时提供 TUI 与 CLI 两种界面，用于与符合 A2A 标准的智能体交互。它让开发者可以在终端中发送消息、验证智能体、管理任务，并与 AI 智能体交互式聊天。

该工具内置一个本地 A2A 服务器智能体（需要本地运行 **Ollama**），可用于测试和开发。

# PARAMETERS

**tui**
> 启动交互式终端用户界面

**server**
> 启动本地 A2A 服务器智能体

**send**
> 向智能体发送消息

**validate**
> 验证 A2A 智能体端点

**--url** _URL_
> 目标智能体的 URL

**--message** _TEXT_
> 要发送的消息

**--verbose**
> 启用详细输出

**--debug**
> 启用调试日志

# CAVEATS

内置的服务器智能体要求本地正在运行 **Ollama**。A2A 协议相对较新，不同实现之间的智能体兼容性可能存在差异。

# HISTORY

**handler** 由 **Al Duncanson** 创建，使用 **Python** 编写。它是为 Google 的 **Agent-to-Agent (A2A) Protocol** 开发的开发者工具包，该协议使来自不同框架的 AI 智能体能够相互通信。

# SEE ALSO

[curl](/man/curl)(1), [ollama](/man/ollama)(1)
