# TAGLINE

支持多提供商与离线运行的自包含终端编码代理

# TLDR

**启动交互式终端界面**

```ante```

**运行一次性无头任务**

```ante -p "[add error handling to src/main.rs]"```

**通过管道传入 diff 进行审查**

```git diff | ante -p "[review this for security issues]"```

**使用指定的提供商和模型**

```ante --provider [openai] --model [gpt-5.5] -p "[refactor the database module]"```

**配合本地 GGUF 模型完全离线运行**

```ante --offline-model [~/.ante/models/model.gguf] -p "[add tests]"```

**恢复已保存的会话**

```ante --resume [ses_...] -p "[now add tests]"```

**更新到最新版本**

```ante update```

# SYNOPSIS

**ante** [_options_] [**-p** _prompt_]

**ante** **serve**

**ante** **gateway**

**ante** **update** [_options_]

# PARAMETERS

**-p**, **--prompt** _PROMPT_
> 以无头模式运行给定提示词的任务，完成后退出

**-m**, **--model** _MODEL_
> 覆盖模型名称

**--provider** _PROVIDER_
> 覆盖 API 提供商（例如 anthropic、openai、gemini、xai、openrouter、local）

**--profile** _NAME_
> 使用 **~/.ante/**_NAME_**.settings.json** 代替默认设置；等价于环境变量 **ANTE_PROFILE**

**--effort** _LEVEL_
> 覆盖模型努力程度：min、low、medium、high、xhigh 或 max

**--yolo**
> 跳过所有交互式工具审批提示

**--output-format** _FORMAT_
> 无头输出格式：json、human 或 minimal（默认：minimal）

**--offline-model** _PATH_
> 本地 GGUF 模型文件的路径；启动内置本地推理引擎并使用 local 提供商

**-r**, **--resume** _SESSION_ID_
> 按 ID 恢复先前保存的会话

**--no-session-save**
> 不保存会话记录或可恢复的快照

**--check**
> 在主任务完成后对工作成果执行一轮验证

**--system-prompt** _PROMPT_
> 完全替换默认系统提示词

**--system-prompt-file** _PATH_
> 从 UTF-8 文件读取替代的系统提示词

**--append-system-prompt** _TEXT_
> 向系统提示词追加文本

**--no-skills**
> 跳过技能发现；不宣告也不调用任何技能

**--tools** _TOOLS_...
> 用恰好这些工具替换默认工具集

**--include-tools** _TOOLS_...
> 在默认或 **--tools** 工具集的基础上添加工具

**--exclude-tools** _TOOLS_...
> 在 **--tools** 和 **--include-tools** 处理之后再移除这些工具

# COMMANDS

**serve**
> 以结构化 JSONL 协议作为长期运行的守护进程，供编辑器插件和集成使用

**gateway**
> 将 Ante 作为 Slack 或 Discord 机器人运行

**update**
> 安装最新版本；支持 **--channel** 和 **--version**

# DESCRIPTION

**ante** 是 Antigma Labs 出品的一款自包含编码代理，运行于终端之中。它以单个 Rust 二进制文件分发（约 15MB），没有运行时语言依赖。日常使用是交互式 TUI（不带参数运行 **ante**）；无头一次性任务则使用 **-p** / **--prompt**。

它可通过 API 密钥或 OAuth 与多家云提供商协作（Anthropic、OpenAI、Gemini、Grok/xAI、Open Router 以及 OpenAI 兼容端点），也能借助内置推理引擎配合本地 GGUF 模型完全离线运行。配置存放在 **~/.ante/** 下（设置、目录以及可选的命名 profile）。

子命令涵盖程序化嵌入（**ante serve**）、聊天平台机器人（**ante gateway**）和自我更新（**ante update**）。功能包括多代理编排、技能、MCP 服务器以及跨会话的持久记忆。

# CAVEATS

Ante 处于 alpha/预览阶段：可能出现破坏性变更和功能不完整的情况。官方仅支持 macOS 和 Linux（Windows 用户请使用 WSL）。无头模式意味着自动批准所有工具调用（yolo）。云提供商需要凭据（如 **ANTHROPIC_API_KEY**、**OPENAI_API_KEY**）；离线模式需要本地 GGUF 模型。预构建二进制文件在 alpha 阶段依据单独的二进制条款免费使用；仓库中的开源部分采用 Apache-2.0 协议。请通过官方脚本安装（**curl -fsSL https://ante.run/install.sh | bash**）；发行版中名为 **ante** 的软件包通常是另一个项目（Ante 编程语言）。

# CONFIGURATION

默认设置：**~/.ante/settings.json**

命名 profile：**~/.ante/**_name_**.settings.json**（用 **--profile** 或 **ANTE_PROFILE** 选择）

提供商/模型目录覆盖：**~/.ante/catalog.json**

二进制安装位置默认为 **~/.ante/bin**（安装时可用 **ANTE_INSTALL_DIR** 覆盖）

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [opencode](/man/opencode)(1), [aider](/man/aider)(1), [goose](/man/goose)(1)

# RESOURCES

```[Source code](https://github.com/AntigmaLabs/ante)```

```[Homepage](https://antigma.ai)```

```[Documentation](https://docs.antigma.ai)```

<!-- verified: 2026-08-10 -->
