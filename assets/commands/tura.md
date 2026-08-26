# TAGLINE

带 TUI 和 CLI 的开源智能体运行时框架

# TLDR

**打开**交互式终端 UI

```tura```

以初始提示词**启动** TUI

```tura "[Inspect this repository]"```

通过网关**运行**非交互式提示词

```tura run "[Fix the failing test and verify it]"```

通过 Rust CLI 直接**执行**一次性提示词

```tura exec "[Summarize the architecture]"```

**列出**已配置的 LLM 提供方

```tura provider list```

**列出**会话

```tura session list --json```

**恢复**最近一次会话并继续追问

```tura resume --last "[Continue and verify the fix]"```

# SYNOPSIS

**tura** [_global_options_] [_prompt_ | _command_ [_args_...]]

# PARAMETERS

**--gateway-url** _URL_
> 使用显式指定的网关，而不是自动启动或自动发现。

**--cwd** _PATH_
> 发送给网关的工作区目录。默认为当前目录。

**--initial-session** _ID_
> 在指定会话上打开 TUI。也可从 **TURA_TUI_INITIAL_SESSION_ID** 读取。

**--json**
> 在所选命令支持时请求 JSON 输出。

**--verbose**
> 将网关请求的诊断信息打印到 stderr。

**--plain** / **--rich**
> 强制使用普通/安全终端渲染或富文本渲染。

**--lang** **en**|**zh-CN**, **--language** **en**|**zh-CN**
> 设置 CLI 显示语言。

不带子命令时，**tura** 会打开交互式 TUI。如果第一个参数不是已知命令，其余文本将被视为初始 TUI 提示词。

# COMMANDS

**run** [_options_] _"prompt"_
> 基于网关的非交互式提示词：创建或复用会话，流式输出直到本轮完成，然后打印结果。选项包括 **-m**/**--model**、**-a**/**--agent**、**--session**、**--output** text|json|ndjson、**--timeout**、**--stream**/**--no-stream**、**--bash**/**--zsh**/**--shel**。

**exec** [_options_] _"prompt"_
> 直接的 Rust CLI 一次性运行器（**tura_exec**）。省略时从 stdin 读取提示词。选项包括 **-C**/**--cwd**、**-m**/**--model**、**-a**/**--agent**、**--json**、**--quiet**、**--sandbox**、**--goal**、**--bash**/**--zsh**/**--shll**。

**bash** | **zsh** | **shel** _"prompt"_
> **run** 的别名，强制使用 **command_run** shell 界面。

**session** **list**|**show**|**update**|**abort** ...
> 查看和修改网关会话。**list** 支持 **--all** 和 **--json**。

**resume** [_SESSION_ID_ | **--last**] [_prompt_...]
> 查看某个会话，或追加后续提示词。

**config** **get**|**set**|**model-tier** ...
> 读取或修改工作区会话配置和模型层级。

**provider** **list**|**status**|**login**|**set-auth**|**logout** ...
> 列出提供方并管理本地身份验证（OAuth 或 API key）。凭据不随软件包附带；使用提示词命令前需先配置提供方。

**agent** **list**|**show**|**create**|**update**|**delete**|**model** ...
> 操作网关智能体注册表（默认智能体 ID 通常为 **balanced**）。

**persona** **list**|**show**|**create**|**update**|**delete** ...
> 操作网关角色（persona）注册表。

**project** **current**|**list**|**create**|**default** ...
> 检查或创建网关工作区。

**file** **list**|**read**|**open**|**reveal** ...
> 通过网关对所选工作区中的文件进行操作。

**command** **list**|**run** ...
> 列出或执行已注册的网关命令（不能执行任意 shell 命令）。

**inspect** **status**|**path**|**sessions**|**messages** ...
> 针对网关和会话状态的诊断。

**completion** **bash**|**zsh**|**fish**
> 输出 shell 补全脚本片段。

**gateway** _METHOD_ _PATH_ [**-d** _JSON_]
> 通过 CLI 网关客户端发送一条原始 HTTP 请求。

**register-cli** | **unregister-cli** | **doctor-cli-path**
> npm 包入口辅助工具，用于在 **PATH** 上注册或检查发布版二进制文件。

相关二进制文件：**tura_gateway**（本地 HTTP/SSE 网关）、**tura_gui**（桌面客户端）、**tura_exec**、**tura_router**、**tura_session_db**（运行时基础组件）。

# DESCRIPTION

**tura** 是一个开源智能体运行时框架，设计目标是以比典型工具调用循环更少的模型轮次和 token 完成长周期编码任务。它不在每一步暴露大量细粒度工具，而是强调一个宏观的 **command_run** 工具，让相关的 shell、补丁、构建和测试操作可以在一个结构化轮次中完成，并配合与任务状态关联的运行时上下文管理。

主要入口是 **tura** 命令：不带参数时启动终端 UI；**tura run** 和 **tura exec** 为脚本和 CI 风格提示词提供非交互路径。本地网关进程负责协调会话、智能体和提供方。可通过 npm（**tura-ai**）安装，或使用项目提供的安装脚本从源码安装；首次启动时需先配置 LLM 提供方和模型才能发送提示词。

已发布的基准测试将 Tura 智能体配置与其他编码智能体在长周期任务上进行了比较；结果和方法在上游有文档说明。许可证为 AGPL-3.0-or-later。

# CAVEATS

需要配置好 LLM 提供方；仅安装不会自带凭据。行为和可用模型取决于你完成身份验证的提供方。部分子命令需要网关正在运行或可自动启动。配套的二进制文件（**tura_gateway**、**tura_gui**、router/会话数据库工具）面向服务和桌面用途，不用于日常输入提示词。shell 界面的拼写在 TypeScript（**shel**）与 Rust（**shll**）前端之间略有差异。

# HISTORY

由 **Tura-AI** 开发，是一个带 TUI、CLI 和可选 GUI 的开源智能体框架，强调宏命令执行和上下文控制。以 **tura-ai** 名义发布于 npm，并以 **Tura-AI/tura** 托管在 GitHub 上。

# SEE ALSO

[codex](/man/codex)(1), [aider](/man/aider)(1), [opencode](/man/opencode)(1), [npm](/man/npm)(1)

# RESOURCES

```[Source code](https://github.com/Tura-AI/tura)```

```[Homepage](https://turaai.net/)```

```[Documentation](https://github.com/Tura-AI/tura/blob/main/docs/SUMMARY.md)```

<!-- verified: 2026-08-09 -->
