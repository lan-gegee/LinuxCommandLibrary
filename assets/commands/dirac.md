# TAGLINE

高效的 AI 编程代理 CLI

# TLDR

**通过提示词启动交互式编程任务**

```dirac "[describe the task]"```

**向** AI 提供商**认证**

```dirac auth```

**查看并恢复**之前的任务

```dirac history```

**以计划模式运行**，在执行前先展示策略

```dirac -p "[refactor the authentication module]"```

**自动批准**所有操作，无需确认（Yolo 模式）

```dirac -y "[fix all lint errors]"```

**将输入通过管道交给** Dirac 审查

```git diff | dirac "Review these changes"```

# SYNOPSIS

**dirac** [_options_] [_command_] [_prompt_]

# PARAMETERS

**-p**, **--plan**
> 计划模式：在执行任何操作之前先展示策略。

**-y**, **--yes**
> Yolo 模式：自动批准所有操作，不弹出确认提示。

**auth**
> 向配置的 AI 提供商进行认证。

**history**
> 列出之前的任务并可恢复其中任意任务。

# DESCRIPTION

**dirac** 是一个基于终端的 AI 编程代理，专为上下文效率和降低 API 成本而设计。它采用基于审批的工作流，可以读写文件、执行终端命令并驱动无头浏览器，同时让用户保持掌控。

该代理强调基于哈希锚定的编辑、AST 操作以及大规模并行操作，以最大限度减少每次变更消耗的 token。据项目方称，与同类代理相比，这可将 API 支出降低 50–80%，同时保持甚至提升代码质量。

Dirac 支持多个模型提供商，可通过环境变量选择，因此可以搭配 Anthropic、OpenAI、Google、xAI、Mistral、Groq、OpenRouter 或自托管后端使用。

# CONFIGURATION

API 密钥从环境变量读取：

```
ANTHROPIC_API_KEY
OPENAI_API_KEY
OPENROUTER_API_KEY
GEMINI_API_KEY
GROQ_API_KEY
MISTRAL_API_KEY
XAI_API_KEY
HF_TOKEN
```

启动 **dirac** 之前，请为你要使用的提供商设置相应的环境变量。当前使用的提供商会根据已设置的密钥自动确定。

# CAVEATS

审批提示可以用 **-y** 跳过，但这样做会允许未经确认的文件写入和 Shell 执行。请仅在可丢弃的环境或可信项目中使用。AI 代理在大规模重构时可能误解意图；提交前务必审查 diff。

# HISTORY

Dirac 通过 npm 以 **dirac-cli** 的形式分发。它结合哈希锚定编辑、AST 感知操作和积极的上下文管理，将自己定位为其他终端编程代理的更低成本替代品。

# INSTALL

```zypper: sudo zypper install dirac```

```brew: brew install dirac```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[claude](/man/claude)(1), [vtcode](/man/vtcode)(1), [aider](/man/aider)(1)
