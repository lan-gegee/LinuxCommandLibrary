# TAGLINE

从命令行与 Claude AI 交互

# TLDR

向 Claude **发送简单消息**

```anthropic -g user "Hello, Claude!"```

使用指定模型**发送消息**

```anthropic -g user "[prompt]" -m [claude-opus-4-8]```

让 Claude **分析图像**

```anthropic -g user "Describe this image" -i [path/to/image.png]```

**设置系统提示词**以提供上下文

```anthropic -g user "[prompt]" -s "You are a helpful coding assistant"```

带助手回复的**多轮对话**

```anthropic -g user "Hello!" -g assistant "Hi there!" -g user "How are you?"```

**控制响应长度**与随机性

```anthropic -g user "[prompt]" -x [2048] -t [0.7]```

# SYNOPSIS

**anthropic** [**-g** _role_ _content_] [**-m** _model_] [**-s** _system_] [**-i** _image_] [**-t** _temp_] [**-x** _tokens_]

# PARAMETERS

**-g**, **--message** _role_ _content_
> 添加一条具有指定角色（user/assistant）和内容的消息。可重复使用以进行多轮对话。

**-m**, **--model** _model_
> 指定要使用的 Claude 模型。内置默认值是 claude-3-opus-20240229，该模型现已退役，因此请传入当前可用的模型，例如 claude-opus-4-8 或 claude-sonnet-4-6。

**-s**, **--system** _prompt_
> 为对话提供上下文或指令的系统消息。

**-i**, **--image** _path_
> 用于视觉任务的图像文件路径（PNG、JPEG 或 PDF）。

**-t**, **--temperature** _value_
> 控制响应的随机性。值越高输出越有创造性。

**-k**, **--top_k** _value_
> 将采样限制在概率最高的前 k 个 token 内。

**-p**, **--top_p** _value_
> 核采样；仅考虑累积概率高于阈值的 token。

**-x**, **--max_tokens** _count_
> 响应中的最大 token 数。默认：1024。

# DESCRIPTION

**anthropic** 是一个用于与 Anthropic 的 Claude AI 模型交互的命令行界面。它让用户可以从终端直接访问 Claude API，发送文本消息和图像进行分析。

该工具通过链式使用多个 **-g** 标志支持多轮对话，实现具备上下文感知能力的交互。它支持多种图像格式，包括 PNG、JPEG 和 PDF 文件，可用于视觉任务。此 CLI 与 Shell 管道集成良好，适合脚本编写和自动化工作流。

# CAVEATS

需要设置包含有效 API 凭据的 **ANTHROPIC_API_KEY** 环境变量。处理 PDF 需要系统上安装 **Poppler** 库（由 **pdf2image** 使用）；如果不传 PDF 则无需安装。硬编码的默认模型（claude-3-opus-20240229）已退役，因此需用 **-m** 提供当前可用的模型。API 使用会按 token 消耗量产生费用。

# HISTORY

anthropic-cli 是 **dvcrn** 开发的社区项目，提供访问 Anthropic Claude 模型的命令行途径。它封装了官方 Anthropic Python SDK，面向偏好终端工作流而非网页界面的开发者。它以 **anthropic-cli** 的名称发布在 PyPI 上，与 Anthropic 官方的 **claude**（Claude Code）和 **ant** 命令行工具无关。

# SEE ALSO

[claude](/man/claude)(1), [ollama](/man/ollama)(1), [llm](/man/llm)(1)

# RESOURCES

```[Source code](https://github.com/dvcrn/anthropic-cli)```

<!-- verified: 2026-06-11 -->
