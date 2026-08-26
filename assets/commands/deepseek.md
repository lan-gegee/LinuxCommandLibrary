# TAGLINE

基于 DeepSeek Coder 模型的 AI 编程助手

# TLDR

**启动交互模式**

```deepseek```

**运行单条提示**

```deepseek chat "[write a Python function for binary search]"```

**以指定模型启动**

```deepseek --model [deepseek-coder:6.7b]```

**配置本地环境**（Ollama）

```deepseek setup```

**强制 CLI 使用本地模式**

```deepseek --local```

**显示帮助**

```deepseek --help```

# SYNOPSIS

**deepseek** [_command_] [_options_]

# PARAMETERS

**chat** _prompt_
> 发送单条提示并打印响应。

**setup**
> 配置本地 Ollama 环境和模型。

**--model** _model_
> 要使用的模型（例如 deepseek-coder:6.7b、deepseek-coder:1.3b）。

**--local**
> 强制 CLI 使用本地 Ollama 模型而非云端 API。

**--help**
> 显示帮助信息。

# DESCRIPTION

**deepseek** 是一个命令行 AI 编程助手，借助 DeepSeek Coder 模型在多种编程语言中协助完成代码补全、生成、重构、调试和代码审查。

它有两种运行模式。推荐的本地模式使用 **Ollama** 在你自己的机器上运行 DeepSeek Coder 模型，保持代码私密并避免 API 费用。云模式使用 DeepSeek API，需要 API 密钥。

不带参数时启动交互式会话；**chat** 子命令执行单条提示后退出，便于编写脚本。

# CONFIGURATION

**DEEPSEEK_API_KEY**（环境变量）
> 云模式使用的 API 密钥。

**DEEPSEEK_USE_LOCAL**（环境变量）
> 设为 true/false 以选择本地或云模式。

# CAVEATS

本地模式需要 Ollama 和已下载的 DeepSeek Coder 模型（大小约 1GB 到 19GB 不等）。云模式需要 DeepSeek API 密钥并可能产生费用。通过 npm 安装为 `run-deepseek-cli` 软件包（需要 Node.js 18+）；这是一个社区项目，并非 DeepSeek 官方发布。

# SEE ALSO

[ollama](/man/ollama)(1), [claude](/man/claude)(1)

# RESOURCES

```[Source code](https://github.com/holasoymalva/deepseek-cli)```

<!-- verified: 2026-07-11 -->
