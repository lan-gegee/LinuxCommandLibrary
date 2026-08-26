# TAGLINE

AI 驱动的 Unix 管道文本处理器

# TLDR

**用 AI 处理文本**

```echo "[text]" | sc "[summarize this]"```

**转换管道输入**

```cat [file.txt] | sc "[translate to French]"```

配合命令输出使用

```git diff | sc "[write a commit message for these changes]"```

**指定自定义提示词模板**

```echo "[text]" | sc -c [my_template]```

**使用特定模型**

```echo "[text]" | sc -m [claude]```

**交互模式**

```sc -i "[explain Kubernetes networking]"```

# SYNOPSIS

**sc** [_options_] [_prompt_]

# PARAMETERS

_PROMPT_
> 处理输入的指令。

**-c**, **--config** _NAME_
> 使用命名的提示词模板。

**-m**, **--model** _NAME_
> 要使用的模型或 API。

**-i**, **--interactive**
> 交互式对话模式。

**-r**, **--repeat**
> 重复上一次的命令。

**-t**, **--temperature** _FLOAT_
> 采样温度。

**-s**, **--system-message** _TEXT_
> 系统消息/人设。

**--list-models**
> 列出已配置的模型。

**--list-configs**
> 列出提示词模板。

# DESCRIPTION

**smartcat**（命令为 **sc**）在 Unix 管道后面装上了 AI 大脑。它从 stdin 读取内容，用语言模型处理后把结果写到 stdout，自然地融入 Unix 管道体系。

该工具面向基于流的文本转换：摘要、翻译、重新排版、代码审查、生成提交信息，以及任何其他文本处理任务。它遵循 Unix 哲学，专注做好一件事，并能与其他工具组合。

提示词模板定义了可复用的转换。模板保存在配置文件中，通过 `-c` 按名称调用。这使 AI 文本处理保持一致且可重复。

支持多个提供商：OpenAI、Anthropic、Mistral、Ollama 以及 OpenAI 兼容 API。配置通过 `~/.config/smartcat/` 下的 TOML 文件完成。

通过 `cargo install smartcat` 安装。命令名为 `sc`，便于快速输入。

# CONFIGURATION

**~/.config/smartcat/conversation.toml**
> 主配置文件，定义 API 密钥、默认模型、提示词模板和提供商设置。

**OPENAI_API_KEY**
> OpenAI 提供商的 API 密钥。

**ANTHROPIC_API_KEY**
> Anthropic 提供商的 API 密钥。

# CAVEATS

云提供商需要 API 密钥。管道模式必须提供 stdin。大输入可能超出模型的上下文限制。流式输出未必对所有下游命令有效。

# HISTORY

**smartcat** 由 **Emilien Fugier** 于 **2023 年**创建，宣传语是"给 `cat` 装上大脑"。它的设计目标是成为 Unix 命令行上一个极简、可组合的 AI 工具，优先考虑与现有 shell 工作流的集成而非功能堆砌。

# INSTALL

```pacman: sudo pacman -S smartcat```

```nix: nix profile install nixpkgs#smartcat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mods](/man/mods)(1), [aichat](/man/aichat)(1), [llm](/man/llm)(1), [cat](/man/cat)(1)
