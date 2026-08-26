# TAGLINE

在终端中通过 Ubuntu 推理 snap 运行本地大语言模型

# TLDR

用所选模型启动一个对话会话

```inference-snaps chat```

查看引擎和服务器状态

```inference-snaps status```

切换到其他执行引擎（如 CUDA）

```sudo inference-snaps use-engine cuda```

显示硬件信息（内存、架构、GPU）

```sudo inference-snaps show-machine```

# SYNOPSIS

**inference-snaps** [_command_] [_options_]

# DESCRIPTION

**inference-snaps**（以及 `deepseek-r1`、`gemma3`、`gemma4` 等关联的模型 snap）提供了一种简单方式，无需编写代码或管理 Python 环境，就能在 Ubuntu 上本地运行强大的开放权重 LLM。

这些 snap 打包了模型权重、推理引擎（CPU、CUDA、ROCm 等）和一个轻量聊天服务器。启动后，你可以在终端中与模型对话，或将其他工具连接到本地 HTTP API。

支持的模型（截至 2026 年）包括 DeepSeek R1、Google Gemma 3/4、Nemotron、Qwen-VL 等。每个模型 snap 会安装自己的命令，用法与 `inference-snaps` 相同。

# COMMANDS

**chat**  
> 启动交互式对话（首次使用时会拉起后台服务器）

**status**  
> 显示当前激活的模型/引擎，以及聊天服务器是否正在运行

**use-engine** _engine_  
> 切换执行后端（cpu、cuda、rocm 等），并在需要时下载匹配的模型变体

**show-machine**  
> 打印与 LLM 推理相关的详细硬件信息

**get** / **set**  
> 读取或修改配置项（host、port 等）

# CAVEATS

- 这些是 Ubuntu Snap 软件包，在 Ubuntu 及其衍生发行版上效果最佳。
- 大型模型需要大量内存和/或受支持的 GPU。
- 首次运行模型会下载数 GB 的权重文件。

# SEE ALSO

[ollama](/man/ollama)(1), [huggingface-cli](/man/huggingface-cli)(1)
