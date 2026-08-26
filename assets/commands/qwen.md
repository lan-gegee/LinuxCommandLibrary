# TAGLINE

阿里 Qwen AI 模型的 CLI

# TLDR

**与 Qwen 对话**

```qwen```

**发送提示词**

```qwen "[prompt]"```

**使用指定模型**

```qwen --model [qwen-turbo] "[prompt]"```

# SYNOPSIS

**qwen** [_options_] [_prompt_]

# PARAMETERS

_PROMPT_
> 要发送的消息。

**--model** _MODEL_
> 要使用的模型。

**--temperature** _TEMP_
> 采样温度。

# DESCRIPTION

**qwen** 是用于与阿里云 Qwen 系列大语言模型交互的命令行界面。它直接在终端提供交互式聊天体验，既支持多轮对话提示词，也支持单次快速查询。

该工具连接阿里的 DashScope API 以访问多种 Qwen 模型变体，包括响应迅速的 Qwen Turbo 以及适合更复杂推理任务的更大模型。温度等采样参数可以调整，从而控制回复的创造性与确定性。

# CAVEATS

需要 API 访问权限。属于阿里云服务。

# HISTORY

Qwen 是**阿里**的大语言模型系列。

# SEE ALSO

[ollama](/man/ollama)(1), [llm](/man/llm)(1)
