# TAGLINE

AI 驱动的自主开发助手

# TLDR

**带任务描述运行**

```ra-aid -m "[add unit tests for auth module]"```

**以研究模式运行**，先收集信息

```ra-aid -m "[understand the caching strategy]" --research-only```

**使用指定的提供商和模型**

```ra-aid -m "[fix the bug]" --provider [openai] --model [gpt-4]```

**以聊天模式运行**，进行交互式协作

```ra-aid -m "[help me design the API]" --chat```

**以牛仔模式运行**，跳过 Shell 命令批准提示

```ra-aid -m "[fix the linting errors]" --cowboy-mode```

# SYNOPSIS

**ra-aid** [_options_] **-m** _message_

# PARAMETERS

**-m**, **--message** _MESSAGE_
> 给智能体的任务描述。

**--provider** _PROVIDER_
> 要使用的 AI 提供商（anthropic、openai、openrouter、openai-compatible、makehub、gemini）。

**--model** _MODEL_
> 要使用的具体模型（非 Anthropic 提供商必填）。

**--research-only**
> 仅收集信息，不做更改。

**--chat**
> 启用支持直接人机交互的交互式聊天模式（隐含 --hil）。

**--hil**
> 启用人在回路模式，进行交互式审批。

**--cowboy-mode**
> 跳过 Shell 命令的交互式审批。

**--auto-test**
> 每次代码更改后自动运行测试。

**--test-cmd** _COMMAND_
> 运行测试的自定义命令。

**--recursion-limit** _N_
> 智能体操作的最大递归深度（默认：100）。

**--show-cost**
> 在智能体工作时显示费用信息。

**--max-cost** _USD_
> 以美元设置费用上限阈值。

**--verbose**
> 启用详细输出。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**ra-aid** 是一款基于 LangGraph 构建的自主 AI 开发助手，分三个阶段工作：研究、规划和实施。它能分析代码库、制定策略并以最少的人工干预执行多步骤开发任务。

它采用结构化工作流：首先调研代码库和任务需求，然后制定详细计划，最后实施更改。这种分阶段的方式提供了透明度，开发者可以在执行前审查计划。

ra-aid 支持多种 AI 提供商（Anthropic、OpenAI、OpenRouter、Gemini 等），并集成 Shell 命令、文件编辑和网页浏览能力来完成复杂的开发任务。--chat 模式支持交互式协作，你可以通过对话引导智能体完成任务。

# CAVEATS

需要 AI 提供商的 API 密钥。复杂的自主任务可能消耗大量 API token。使用 --show-cost 监控花费，用 --max-cost 设置限额。提交前务必审查自主模式下所做的更改。

# HISTORY

**ra-aid** 是一款开源自主编码智能体，构建于 **LangGraph** 基于智能体的任务执行框架之上。它的特色在于"研究—规划—实施"三阶段工作流，比单遍式编码智能体更加透明。

# SEE ALSO

[claude](/man/claude)(1), [aider](/man/aider)(1), [codex](/man/codex)(1), [forge](/man/forge)(1)
