# TAGLINE

ChatGPT 命令行界面

# TLDR

**启动交互式聊天**

```chatgpt```

**发送单条提示词**

```chatgpt "[Your question here]"```

**与指定模型对话**

```chatgpt -m [gpt-4] "[prompt]"```

**设置系统提示词**

```chatgpt -s "[You are a helpful assistant]" "[prompt]"```

**将输入通过管道传给 ChatGPT**

```cat [file.txt] | chatgpt "[Summarize this]"```

**以指定温度运行**

```chatgpt -t [0.7] "[prompt]"```

**流式输出响应**

```chatgpt --stream "[prompt]"```

# SYNOPSIS

**chatgpt** [_options_] [_prompt_]

# PARAMETERS

**-m**, **--model** _name_
> 使用的模型（gpt-4、gpt-3.5-turbo 等）。

**-s**, **--system** _prompt_
> 用于设定上下文的系统提示词。

**-t**, **--temperature** _value_
> 采样温度（0-2，默认 1）。

**--max-tokens** _n_
> 响应的最大 token 数。

**--stream**
> 以流式方式逐段输出生成的响应。

**-c**, **--continue**
> 继续上一次对话。

**--api-key** _key_
> OpenAI API 密钥（或设置 OPENAI_API_KEY）。

**--no-markdown**
> 禁用 markdown 渲染。

**-o**, **--output** _file_
> 将响应写入文件。

**-i**, **--interactive**
> 启动交互模式。

# DESCRIPTION

**chatgpt-cli** 提供访问 OpenAI ChatGPT 模型的命令行途径。它让你能在终端中进行对话式 AI 交互，既支持交互式会话，也支持单次查询的脚本化用法。

该工具维护对话上下文，允许在交互模式下进行多轮对话。输入可以来自参数、stdin（管道）或交互式提示。默认用 markdown 格式渲染响应以提高可读性。

与 shell 管道的结合带来了强大的工作流：分析文件、转换文本、生成代码和自动化内容创作。流式选项会在生成过程中实时显示响应。

# CONFIGURATION

**OPENAI_API_KEY**
> 存放 OpenAI API 密钥的环境变量，在未提供 --api-key 时使用。

# CAVEATS

需要有可用额度的 OpenAI API 密钥。API 使用按 token 计费。较大的上下文窗口可能产生可观费用。响应质量因模型而异；GPT-4 能力更强但比 GPT-3.5 更贵。API 调用可能受速率限制。

# HISTORY

OpenAI 于 **2023 年 3 月** 发布 ChatGPT API 后，出现了多种 **chatgpt-cli** 实现。这些社区工具填补了用户想在终端访问 ChatGPT 而不用 Web 界面的空白。存在多种语言（Python、Go、Rust）的实现，目标相似但功能各异。

# INSTALL

```nix: nix profile install nixpkgs#chatgpt-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[llm](/man/llm)(1), [ollama](/man/ollama)(1), [sgpt](/man/sgpt)(1), [aichat](/man/aichat)(1)
