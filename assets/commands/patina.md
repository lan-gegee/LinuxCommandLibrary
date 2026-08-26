# TAGLINE

学习你判断方式的持久化认知后端

# TLDR

**初始化 Patina** 及其本地存储

```patina init```

**显示需要处理的事项**、新内容和待办项

```patina catch-up```

以习得的语气**开始交互式对话**

```patina chat```

**运行后台守护进程**，按间隔执行摄取和衰减

```patina heartbeat start --interval [30]```

为网关集成**启动 HTTP 服务器**

```patina serve --port [8321]```

# SYNOPSIS

**patina** _command_ [_options_]

# DESCRIPTION

**patina** 是一个本地优先的 **AI 后端**，它会随着时间推移建立用户模型：一个带上下文保留和渐进自治能力的 SQLite **信念图**，用得越多需要的指令就越少。它可以摄取消息（例如来自 Slack 导出），提取信念、跟踪优先级，并能以习得的沟通风格起草消息。

它由三层组成，共同支撑信念图：用于评分、衰减和查询的确定性逻辑（Tier 1，完全不依赖任何模型也能使用）；通过 **Ollama** 运行的本地模型（如 Qwen），负责提取和分类（Tier 2）；以及 Claude 等前沿模型，负责综合与起草（Tier 3）。所有数据都保存在本地 **~/.patina** 下。patina 还可以作为 MCP 服务器供 Claude Code 等宿主使用。

# COMMANDS

**init**
> 初始化 Patina 及其本地存储。

**ingest** [**--from-export** _file_]
> 从 Slack 导出或已配置的适配器导入数据。

**catch-up**
> 显示需要处理的事项、新内容和待办项的统一视图。

**priorities**
> 列出按优先级象限（Q1-Q4）排序的事项。

**draft** [**--to** _name_] [**--context** _text_]
> 以习得的语气生成消息。

**extract**
> 使用 LLM 从观察记录中提取信念。

**beliefs** [**--type** _entity_type_]
> 列出被跟踪的实体及其置信度计数。

**autonomy status**
> 显示当前自治级别和准确率指标。

**autonomy set-level** _N_
> 手动设置自治级别（0 到 6）。

**heartbeat start** [**--interval** _minutes_]
> 启动后台守护进程，定期运行摄取、衰减和升级周期。

**chat**
> 开始交互式对话（通过 Claude Agent SDK）。

**serve** [**--port** _port_]
> 启动用于网关集成的 HTTP 服务器。

# CONFIGURATION

状态保存在本地的 **~/.patina/store.db**（SQLite 信念图）和 **~/.patina/config.yaml** 中。Tier 2 通过 Ollama 使用本地模型；Tier 3 使用前沿模型，通过配置文件和环境变量设置。

# CAVEAT

Tier 1 无需模型即可工作，但信念提取和起草（Tier 2 和 Tier 3）需要配置本地和/或前沿 LLM。patina 是管理个人数据的早期软件，连接适配器前请先审查它会摄取哪些内容。

# HISTORY

**patina** 是由 **Sanctum Origo Systems** 用 **Python** 编写的开源项目，使用 **uv tool install patina** 安装。它以 **Apache-2.0** 许可证发布。

# SEE ALSO

[claude](/man/claude)(1), [ollama](/man/ollama)(1), [uv](/man/uv)(1)
