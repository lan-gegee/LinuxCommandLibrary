# TAGLINE

可在本地或私有服务器上运行的开源自主 AI 智能体

# TLDR

**运行首次设置向导**

```openclaw onboard```

**启动网关以实现持久运行**

```openclaw gateway```

**将网关安装为系统守护进程**

```openclaw gateway install```

**向智能体发送任务**

```openclaw agent --message "[task]"```

**列出并管理已安装的技能**

```openclaw skills```

**检查系统健康状态与已连接的服务**

```openclaw status```

# SYNOPSIS

**openclaw** [_command_] [_options_]

**openclaw** **gateway** [_options_]

**openclaw** **agent** [_options_]

# PARAMETERS

**onboard**
> 运行交互式设置向导，配置消息平台并安装网关守护进程。

**gateway**
> 启动 Gateway 服务器以实现持久运行（默认端口：18789）。

**gateway install**
> 将 Gateway 安装为系统守护进程（macOS 上为 launchd，Linux 上为 systemd）。

**gateway start**
> 启动已安装的 Gateway 守护进程。

**gateway stop**
> 停止正在运行的 Gateway 守护进程。

**gateway restart**
> 重启 Gateway 守护进程。

**agent --message** _MESSAGE_
> 向 AI 智能体发送自然语言任务或指令。

**config get** _PATH_
> 获取某个配置值。

**config set** _PATH_ _VALUE_
> 设置某个配置值。

**skills**
> 列出并管理来自技能注册表的已安装技能。

**status**
> 显示系统健康状态、已连接的服务和活动会话。

**doctor**
> 运行诊断以发现配置或连接问题。

**cron**
> 管理定时循环任务。

**sessions**
> 列出活动及历史的智能体会话。

**--port** _PORT_
> 网关的端口号（默认：18789）。

**--verbose**
> 启用详细日志输出。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**OpenClaw** 是一个免费开源（MIT 许可证）的自主 AI 智能体，可在本地或私有服务器上运行。它使用 TypeScript 编写并通过 npm 安装，利用大语言模型通过消息平台自主执行任务。支持的渠道包括 WhatsApp、Telegram、Signal、Slack、Discord、Google Chat、iMessage、Microsoft Teams、Matrix 和 WebChat，可从任何设备进行语音和文字交互。

该智能体通过 Gateway 架构运行，提供持久的后台运行能力。Gateway 在多个端口上监听其控制平面、消息中继和其他服务。任务通过消息平台或 CLI 分派给智能体，智能体可以执行多步骤工作流、管理日历、起草电子邮件、发送消息以及自动化系统命令。

OpenClaw 支持借助 Ollama 等本地 LLM 后端实现完全本地化运行，让所有推理和任务执行都在设备上完成，不向外部服务发送任何数据。它也可以连接外部 AI API 以获得更强的能力。其技能框架内置 50 多种技能，并提供社区注册表（ClaHub），为日历、电子邮件、智能家居系统等提供可扩展的集成。

# CAVEATS

消息平台集成需要相应平台的 API 令牌或凭据。使用本地模型运行需要有足够的计算资源进行 LLM 推理。引导向导会指导你完成消息渠道的初始配置和守护进程安装。将 Gateway 暴露给外部网络时，请确保网络安全措施到位。

# HISTORY

OpenClaw 由 PSPDFKit 联合创始人兼前 CEO **Peter Steinberger** 于 2025 年 11 月创建。该项目最初名为 **Clawdbot**，从一开始就是开源的。2026 年 1 月，Anthropic 以 “Clawd” 与 “Claude” 商标相似为由威胁采取法律行动，促使项目更名为 **Moltbot**。仅仅三天后，由于加密货币骗子劫持了与 Moltbot 名称相关联的被弃用社交媒体账号，项目再次更名为 **OpenClaw**。该项目增长迅速，成为 GitHub 历史上增长最快的仓库之一，并在 84 天内突破 20 万星标。2026 年 2 月，Steinberger 宣布加入 OpenAI 领导下一代个人 AI 智能体的开发，同时成立了 OpenClaw 基金会来管理这一开源项目。

# INSTALL

```dnf: sudo dnf install openclaw```

```nix: nix profile install nixpkgs#openclaw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[claude](/man/claude)(1), [ollama](/man/ollama)(1), [llm](/man/llm)(1)
