# TAGLINE

Mistral AI 命令行编程助手

# TLDR

**启动交互式会话**

```vibe```

**以初始提示词启动**

```vibe "[refactor the main function to be more modular]"```

**以非交互方式运行，便于脚本化**

```vibe --prompt "[add unit tests for the auth module]"```

**自动批准所有工具执行**

```vibe --auto-approve```

**使用自定义 agent 配置**

```vibe --agent [my_custom_agent]```

**恢复最近一次会话**

```vibe --continue```

**恢复特定会话**

```vibe --resume [session_id]```

**在非交互模式下限制轮次与费用**

```vibe --prompt "[fix lint errors]" --max-turns [10] --max-price [2.50]```

**在提示词中引用文件**

```vibe``` 然后 ```@[path/to/file.py] [explain this code]```

**直接执行 shell 命令**

```vibe``` 然后 ```![ls -la]```

# SYNOPSIS

**vibe** [_options_] [_prompt_]

# PARAMETERS

**--prompt** _TEXT_
> 以提供的提示词非交互运行（默认启用自动批准）。

**--auto-approve**
> 无需确认即自动批准所有工具执行。

**--agent** _NAME_
> 选择 agent 配置（内置：default、plan、accept-edits、auto-approve），或从 agents 目录加载自定义 TOML 文件。

**-c**, **--continue**
> 恢复最近一次会话。

**--resume** _SESSION_ID_
> 按 ID 恢复特定会话。

**--max-turns** _N_
> 限制非交互模式下助手轮次数量。

**--max-price** _DOLLARS_
> 费用超过指定金额时中止会话。

**--enabled-tools** _TOOL_
> 限制可用的内置工具（支持 glob 模式）。

**--output** _FORMAT_
> 输出格式：`text`、`json` 或 `stream`。

**--workdir** _PATH_
> 设置会话的工作目录。

**--setup**
> 运行交互式 API 密钥配置。

# INTERACTIVE CONTROLS

**Ctrl+J** 或 **Shift+Enter**
> 插入换行符，用于多行输入。

**Ctrl+G**
> 在外部编辑器中编辑当前输入。

**Ctrl+O**
> 切换工具输出视图。

**Ctrl+T**
> 切换待办列表视图。

**Ctrl+R**
> 开始语音录制（Escape 取消）。

**Shift+Tab**
> 开启/关闭自动批准模式。

**@**_filename_
> 在提示词中自动补全文件路径。

**!**_command_
> 直接执行 shell 命令，绕过 agent。

**/**_command_
> 运行内置或自定义斜杠命令（例如 `/help`）。

# BUILT-IN TOOLS

**read_file**, **write_file**, **search_replace**
> 用于读取、写入和修改代码的文件操作

**bash**
> 有状态的命令执行终端

**grep**
> 支持 ripgrep 的代码搜索

**todo**
> 任务跟踪与列表管理

# DESCRIPTION

**Mistral Vibe CLI** 是一个开源的命令行编程助手，由 Mistral 的 1230 亿参数编程模型 Devstral 2 驱动，拥有 256K 上下文窗口。它可以使用自然语言在整个代码库中探索、修改和执行变更。

该工具通过自动扫描你的文件结构和 Git 状态提供项目感知上下文。功能包括支持 @ 自动补全的智能文件引用、通过 ! 执行 shell 命令，以及能理解整个代码库的多文件编排。它支持 Agent Communication Protocol（ACP）以便集成到 IDE。

Vibe 默认以交互式聊天模式运行，提供一个将复杂任务拆解为可执行步骤的对话式 AI 智能体。非交互模式则支持脚本化和自动化工作流。

# CAVEATS

需要通过 **MISTRAL_API_KEY** 环境变量设置 Mistral API 密钥，或将其存储在 **~/.vibe/.env** 中（可用 **VIBE_HOME** 覆盖配置主目录）。可通过 `curl -LsSf https://mistral.ai/vibe/install.sh | bash`、`uv tool install mistral-vibe` 或 `pip install mistral-vibe` 安装。Linux 和 macOS 是主要平台；Windows 受支持但属次要。自动批准模式会在不确认的情况下执行命令，可能具有破坏性 —— 若需先审后行的流程，建议使用 **plan** agent。

# HISTORY

Mistral Vibe CLI 由 **Mistral AI** 于 **2025 年 12 月 9 日**与 Devstral 2 一同发布。它以 Apache 2.0 许可证发布，使用 Python 构建。Mistral 在 2025 年 12 月前提供 Devstral 2 的免费 API 访问，自 2026 年 1 月起开始收费。该工具可作为扩展集成到 Zed IDE。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [gemini](/man/gemini)(1), [aider](/man/aider)(1)
