# TAGLINE

与大语言模型交互的命令行工具

# TLDR

**使用默认模型对话**

```llm "[prompt]"```

**使用指定模型**

```llm -m [gpt-4o] "[prompt]"```

**交互式聊天会话**

```llm chat```

**继续最近一次对话**

```llm -c "[follow up]"```

**列出模型**（内置的和插件提供的）

```llm models```

向模型**管道输入**

```cat [file.txt] | llm "[summarize this]"```

**使用系统提示词**

```llm -s "[Reply as a pirate]" "[Hi there]"```

**设置 API 密钥**

```llm keys set [openai]```

**安装插件**（如 Claude 支持）

```llm install [llm-claude-3]```

# SYNOPSIS

**llm** [_options_] [_prompt_]

**llm** _subcommand_ [_options_]

# PARAMETERS

_PROMPT_
> 提供给模型的文本提示词。

**-m** _MODEL_, **--model** _MODEL_
> 要使用的模型（例如 **gpt-4o**、**claude-3-5-sonnet**、**llama2**）。

**-c**, **--continue**
> 继续最近一次的对话。

**--cid** _ID_
> 按 ID 继续指定的对话。

**-s** _PROMPT_, **--system** _PROMPT_
> 设置系统提示词。

**-t** _NAME_, **--template** _NAME_
> 使用命名的提示词模板。

**-o** _KEY_ _VALUE_, **--option** _KEY_ _VALUE_
> 传递模型特有的选项（例如 **-o temperature 0**）。

**-a** _PATH_, **--attachment** _PATH_
> 为支持附件的模型在提示词中附加文件（图像、PDF、音频）。

**--no-stream**
> 禁用 token 流式输出，只打印最终答案。

**--key** _KEY_
> 本次调用使用特定的 API 密钥。

# SUBCOMMANDS

**chat**
> 打开交互式聊天会话。

**models** [**list** | **default** _name_]
> 列出可用模型或设置默认模型。

**keys** [**set** _key_]
> 管理 API 密钥。

**logs**
> 显示或查询持久化的提示词与响应日志。

**templates**
> 管理可复用的提示词模板。

**install** _package_ / **uninstall** _package_
> 安装或移除 llm 插件（例如 **llm-claude-3**、**llm-ollama**）。

**embed**, **embed-multi**, **similar**
> 生成并搜索文本嵌入（embedding）。

# DESCRIPTION

**llm** 是一个用于与大语言模型交互的命令行工具和 Python 库。开箱即用即可对接 OpenAI 的 API；通过插件还能支持 Anthropic Claude、Google Gemini、Mistral、本地 **Ollama**、**llama.cpp** / GGUF 以及许多其他提供商和自托管模型。

每条提示词和响应都会记录到本地 **SQLite** 数据库中（Linux 上位于 **~/.config/io.datasette.llm/**，macOS 上位于 **~/Library/Application Support/io.datasette.llm/**），因此可以搜索、导出和回放以前的对话。该工具还支持提示词模板、系统提示词、嵌入、相似度搜索以及可插拔的后端。

# CAVEATS

云模型需要通过 **llm keys set** 存储 API 密钥。对话日志以明文形式存储在 SQLite 中，请注意提示词中的机密信息。OpenAI 之外的提供商需要安装额外插件（例如 **llm install llm-claude-3**）。

# HISTORY

**llm** 由 **Simon Willison** 创建，旨在为语言模型 API 和本地模型提供统一的命令行访问方式，并方便地记录和查询历史提示词。

# INSTALL

```brew: brew install llm```

```nix: nix profile install nixpkgs#llm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ollama](/man/ollama)(1), [chatgpt](/man/chatgpt)(1)
