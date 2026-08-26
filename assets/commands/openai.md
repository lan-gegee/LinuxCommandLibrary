# TAGLINE

聊天补全

# TLDR

**聊天补全**

```openai api chat.completions.create -m gpt-4 -g user "[prompt]"```

**创建嵌入**

```openai api embeddings.create -m text-embedding-ada-002 -i "[text]"```

**列出模型**

```openai api models.list```

**生成图像**

```openai api images.generate -p "[description]"```

# SYNOPSIS

**openai** [_command_] [_options_]

# PARAMETERS

**api** _ENDPOINT_
> API 命令。

**-m** _MODEL_
> 模型名称。

**-g** _ROLE_ _MESSAGE_
> 带角色的消息。

**-i** _INPUT_
> 输入文本。

**-p** _PROMPT_
> 提示词文本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**openai** 是 OpenAI 的 CLI。用于与 GPT 模型及其他 API 交互。

该工具提供命令行方式的 API 访问。需要 API 密钥。

# CAVEATS

需要 OPENAI_API_KEY。API 使用按量计费。存在速率限制。

# HISTORY

openai CLI 由 **OpenAI** 创建，用于命令行方式的 API 访问。

# SEE ALSO

[curl](/man/curl)(1), [ollama](/man/ollama)(1)
