# TAGLINE

用于与大语言模型聊天的终端界面

# TLDR

**开始聊天会话**

```oatmeal```

**与特定模型聊天**

```oatmeal --model [model_name]```

**使用特定后端**

```oatmeal --backend [ollama|openai|claude]```

# SYNOPSIS

**oatmeal** [_options_]

# PARAMETERS

**--model** _MODEL_
> 指定要使用的模型。

**--backend** _BACKEND_
> 选择模型后端（ollama、openai、claude、gemini）。

# DESCRIPTION

**oatmeal** 是一款 TUI 工具，可使用不同的后端与大语言模型聊天。它与编辑器集成，让你可以读取编辑器中选中的代码，并将模型提供的代码提交回去。每个代码块都带有编号索引，便于引用。

支持的后端包括 Ollama（默认）、OpenAI、Claude 和 Gemini。编辑器集成包括剪贴板和 Neovim 插件支持。

# CAVEATS

需要运行中的模型后端（如 Ollama 服务器）或云服务的有效 API 密钥。

# HISTORY

**oatmeal** 由 **dustinblackman** 创建，使用 **Rust** 编写。

# SEE ALSO

[ollama](/man/ollama)(1), [claude](/man/claude)(1)
