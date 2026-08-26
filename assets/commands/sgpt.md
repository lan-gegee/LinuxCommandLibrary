# TAGLINE

基于 ChatGPT 的 AI Shell 助手

# TLDR

**提问**

```sgpt "[How do I list files?]"```

**生成 shell 命令**

```sgpt -s "[list all PDF files]"```

**执行 shell 命令**

```sgpt -se "[find large files]"```

**生成代码**

```sgpt -c "[python function to sort list]"```

**聊天模式**

```sgpt --chat [session_name] "[message]"```

**使用特定角色**

```sgpt --role [code] "[question]"```

**管道输入**

```cat [file.txt] | sgpt "[summarize this]"```

# SYNOPSIS

**sgpt** [_-s_] [_-c_] [_--chat name_] [_options_] _prompt_

# PARAMETERS

**-s**, **--shell**
> 生成 shell 命令。

**-se**
> 生成 shell 命令并执行。

**-c**, **--code**
> 生成代码。

**--chat** _NAME_
> 聊天会话。

**--role** _ROLE_
> 使用角色。

**--model** _MODEL_
> 指定模型。

**--temperature** _TEMP_
> 响应的随机性。

**--no-cache**
> 禁用缓存。

# DESCRIPTION

**sgpt**（Shell GPT）是一个用于与 OpenAI ChatGPT 模型交互的命令行界面，专为开发者和系统管理工作流优化。它有多种工作模式：用于快速回答的一般查询模式、用于生成可执行命令及其说明的 shell 模式（**-s**），以及能自动检测语言、生成编程解决方案的代码模式（**-c**）。

聊天会话在多次调用之间保持对话上下文，支持追问和迭代改进。角色可以针对特定任务定制 AI 的行为，既提供常见场景的预定义角色，也支持用户自定义角色。

该工具与 Unix 管道自然集成，可通过 stdin 接受输入，对文件内容、命令输出或任何流式数据进行 AI 分析。这使它适合总结日志、解释错误信息或从代码生成文档等任务。

# CONFIGURATION

**OPENAI_API_KEY**
> 提供用于身份验证的 OpenAI API 密钥的环境变量。

**~/.config/shell_gpt/.sgptrc**
> 配置文件，用于设置默认模型、temperature、缓存选项及其他偏好。

**~/.config/shell_gpt/roles/**
> 存放自定义角色定义文本文件的目录。

# CAVEATS

需要 OpenAI API 密钥。按 token 计费。需要互联网连接。

# HISTORY

**sgpt** 由 **Farkhod Sadykov** 创建，用于 AI 辅助的 Shell 使用。它将 ChatGPT 能力直接带到命令行。

# SEE ALSO

[chatgpt](/man/chatgpt)(1), [github-copilot-cli](/man/github-copilot-cli)(1)
