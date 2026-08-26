# TAGLINE

在终端中与 AI 模型对话

# TLDR

**提问一个问题**

```aichat "[explain quicksort]"```

**通过管道传入内容进行分析**

```cat [file.py] | aichat "[review this code]"```

**使用指定模型**

```aichat --model [claude:claude-sonnet-4-20250514] "[question]"```

**从自然语言执行 shell 命令**

```aichat -e "[list large files in current directory]"```

**启动交互式聊天会话**

```aichat```

**使用角色/persona**

```aichat --role [shell] "[find duplicate files]"```

**处理一个文件**

```aichat --file [document.pdf] "[summarize this]"```

# SYNOPSIS

**aichat** [_options_] [_prompt_]

# PARAMETERS

**-m**, **--model** _MODEL_
> 要使用的模型（provider:model 格式）。

**-r**, **--role** _ROLE_
> 使用预定义的角色/persona。

**-e**, **--execute**
> 执行模式：将自然语言翻译为 shell 命令。

**--file** _FILE_
> 在对话中包含文件。

**-S**, **--no-stream**
> 禁用流式输出。

**--list-models**
> 列出可用模型。

**--list-roles**
> 列出可用角色。

**--info**
> 显示当前配置。

# DESCRIPTION

**aichat** 是一款一体化 AI 命令行工具，支持聊天、命令执行和 RAG（检索增强生成）。它兼容 20 多家 AI 提供商，包括 OpenAI、Claude、Gemini、Ollama、Azure 等。

在聊天模式下，它提供带对话历史、多行输入和语法高亮的 REPL。执行模式将自然语言描述翻译为 shell 命令并可选择运行它们。RAG 模式为文档建立索引，以便针对本地文件进行问答。

角色定义了可复用的 persona 和系统提示词。内置角色包括 %code%、%shell%、%explain-shell% 和 %functions%。自定义角色以单个文件的形式定义在 roles 配置目录中。

该工具支持函数调用，允许 AI 模型调用已定义的工具。会话可以在多次调用之间保留对话。可以同时配置多个提供商和模型。

可通过 `cargo install aichat`、Homebrew 安装，或下载二进制文件。

# CONFIGURATION

**~/.config/aichat/config.yaml**
> 主配置文件，用于模型设置、API 密钥、角色和默认参数。

**~/.config/aichat/roles/**
> 自定义角色定义目录，每个角色为一个单独的文件。

# CAVEATS

云提供商需要 API 密钥。多提供商配置需要配置文件。RAG 索引需要额外设置。Token 用量和费用因提供商和模型而异。

# HISTORY

**aichat** 由 **sigoden** 于 **2023** 年创建，作为与多个 AI 提供商交互的统一命令行工具。它从一个简单的聊天工具发展为具备执行模式、RAG 和代理能力的综合性 AI 终端工具集。

# INSTALL

```pacman: sudo pacman -S aichat```

```brew: brew install aichat```

```nix: nix profile install nixpkgs#aichat```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[mods](/man/mods)(1), [smartcat](/man/smartcat)(1), [ollama](/man/ollama)(1), [llm](/man/llm)(1)
