# TAGLINE

OpenAI 语言模型的命令行界面

# TLDR

**启动交互式聊天**会话

```chatgpt```

**发送单条提示词**并获取响应

```chatgpt "[What is the capital of France?]"```

**将输入通过管道传给** ChatGPT

```cat [file.txt] | chatgpt "[Summarize this text]"```

**使用指定模型**

```chatgpt --model [gpt-4] "[prompt]"```

**继续上一次对话**

```chatgpt --continue "[follow-up question]"```

**设置系统提示词**提供上下文

```chatgpt --system "[You are a helpful coding assistant]" "[prompt]"```

**将响应输出到文件**

```chatgpt "[prompt]" > [response.txt]```

**设置温度**控制响应创造性

```chatgpt --temperature [0.7] "[prompt]"```

# SYNOPSIS

**chatgpt** [_options_] [_prompt_]

# PARAMETERS

**--model**, **-m** _model_
> 指定要使用的模型（gpt-4、gpt-3.5-turbo 等）。

**--system**, **-s** _prompt_
> 设置系统提示词以定义助手行为。

**--continue**, **-c**
> 继续上一次对话。

**--temperature**, **-t** _value_
> 控制随机性（0.0-2.0，默认：1.0）。

**--max-tokens** _n_
> 响应的最大 token 数。

**--top-p** _value_
> 核采样（nucleus sampling）参数。

**--stream**
> 在生成过程中流式输出响应。

**--no-stream**
> 等待完整响应后再显示。

**--api-key** _key_
> OpenAI API 密钥（或设置 OPENAI_API_KEY 环境变量）。

**--config** _file_
> 配置文件路径。

**--list-models**
> 列出可用模型。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**chatgpt** 是与 OpenAI ChatGPT 模型交互的命令行界面。它通过终端访问 GPT 语言模型，可用于文本生成、编程辅助、分析和一般性对话。

该工具同时支持来回对话的交互模式和快速查询的单提示词模式。输入可以通过管道来自其他命令或文件，因此适合在 shell 管道中处理文本任务。

配置可以通过命令行标志、环境变量或配置文件设置。**OPENAI_API_KEY** 环境变量是提供凭证的标准方式。不同模型在能力、速度和价格上各有差异。

系统提示词可以自定义助手的行为和专长领域。温度控制响应的创造性——值越低响应越聚焦，值越高变化越多。流式选项会在生成过程中逐 token 显示响应。

# CAVEATS

需要已开通计费的 OpenAI API 密钥。API 使用按 token 消耗计费。响应质量和能力因模型而异。需要网络连接。上下文长度受模型限制。发送敏感数据前应考虑隐私影响。

# HISTORY

OpenAI 于 **2023 年 3 月** 发布 ChatGPT API 后不久，各种 ChatGPT 命令行界面便相继出现。多种语言的 CLI 实现并存（Python、Go、Rust 等），功能集各不相同。这些工具把 GPT 能力带入了以终端为中心的工作流，使其能与 shell 脚本和开发流水线集成。

# INSTALL

```nix: nix profile install nixpkgs#chatgpt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chatgpt-cli](/man/chatgpt-cli)(1), [curl](/man/curl)(1), [jq](/man/jq)(1), [claude](/man/claude)(1), [ollama](/man/ollama)(1)
