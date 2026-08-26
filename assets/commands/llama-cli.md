# TAGLINE

从命令行运行本地 LLM 推理（llama.cpp）

# TLDR

**加载模型并启动交互式聊天**

```llama-cli -m [path/to/model.gguf]```

**运行单个提示词并打印补全结果**

```llama-cli -m [path/to/model.gguf] -p "[prompt]" -no-cnv```

**设置提示词上下文大小**

```llama-cli -m [path/to/model.gguf] -c [4096]```

**将模型层卸载到 GPU**

```llama-cli -m [path/to/model.gguf] -ngl [all]```

**从 Hugging Face 下载并运行模型**

```llama-cli -hf [user/model:quant]```

**从文件读取首个提示词**

```llama-cli -m [path/to/model.gguf] -f [path/to/prompt.txt]```

**提供系统提示词**

```llama-cli -m [path/to/model.gguf] -sys "[You are a helpful assistant]"```

**用温度控制随机性**

```llama-cli -m [path/to/model.gguf] --temp [0.7]```

# SYNOPSIS

**llama-cli** **-m** _model.gguf_ [_options_]

**llama-cli** **-hf** _user/model[:quant]_ [_options_]

# DESCRIPTION

**llama-cli** 是 **llama.cpp** 项目的命令行推理工具。它加载 **GGUF** 格式的模型，可以交互式地来回聊天生成文本，也可以进行单次非交互式补全。它完全运行在本地硬件上，可使用 CPU、GPU（CUDA、Metal、Vulkan、ROCm）或两者的混合。

默认情况下，当模型自带聊天模板时，llama-cli 会进入对话模式，自动应用该模板并提供交互式提示。**-no-cnv** 标志会禁用此行为，将输入严格视为原始补全提示。模型可以通过 **-m** 提供本地文件，通过 **-hf** 从 Hugging Face 按需下载，或通过 **-dr** 从 Docker 仓库拉取。

该工具暴露了完整的采样器栈（温度、top-k、top-p、min-p、mirostat、DRY 等）、上下文管理选项（如上下文大小和上下文偏移），以及线程数和 GPU 层卸载等硬件控制选项。它与 **llama-server** 等其他 llama.cpp 工具共享参数解析器，因此大多数标志在各工具之间行为一致。

# PARAMETERS

**-m**, **--model** _FNAME_

> 要加载的 GGUF 模型文件路径。

**-hf**, **--hf-repo** _user/model[:quant]_

> 从 Hugging Face 仓库下载模型；quant 默认为 Q4_K_M。

**-p**, **--prompt** _PROMPT_

> 用于开始生成的提示词。系统消息请使用 **-sys**。

**-f**, **--file** _FNAME_

> 从文件读取提示词。

**-sys**, **--system-prompt** _PROMPT_

> 与模型配合使用的系统提示词（需聊天模板支持时有效）。

**-c**, **--ctx-size** _N_

> 提示词上下文的大小（默认：0，从模型加载）。

**-n**, **--predict** _N_

> 要预测的 token 数量（默认：-1，-1 = 无限）。

**-ngl**, **--n-gpu-layers** _N_

> 存入显存的最大层数。接受精确数字、**auto** 或 **all**。

**-t**, **--threads** _N_

> 生成期间使用的 CPU 线程数。

**-cnv**, **--conversation** / **-no-cnv**, **--no-conversation**

> 强制开启或关闭对话模式（存在聊天模板时自动启用）。

**--temp** _N_

> 采样温度（默认：0.80）。

**-co**, **--color** [on|off|auto]

> 为输出着色，以便区分提示词、输入与生成的文本。

**-i**, **--interactive**

> 以交互模式运行，遇到反向提示词时交还控制权。

**-r**, **--reverse-prompt** _PROMPT_

> 在 PROMPT 处停止生成，并在交互模式下交还控制权。

# CAVEAT

llama-cli 只读取 **GGUF** 文件；较旧的 GGML 模型文件必须转换或重新下载。性能和可达到的上下文大小在很大程度上取决于量化方式和可用显存：将 **-ngl** 设置得超出 GPU 显存容量会导致加载失败或回退到 CPU。该单个二进制文件历史上名为 **main**；旧指南中提到的 **./main** 描述的是同一个程序。

# HISTORY

**llama.cpp** 由 **Georgi Gerganov** 于 **2023 年 3 月**创建，是 Meta LLaMA 模型的纯 C/C++ 移植版本，目标是在没有 GPU 的消费级硬件上高效运行推理。后来成为 llama-cli 的示例程序最初叫 **main**；**2024 年**项目统一工具命名时更名为 **llama-cli**。该项目目前在 ggml-org 组织下持续开发，发布频繁。

# INSTALL

```apk: sudo apk add llama.cpp```

```brew: brew install llama.cpp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[llama.cpp](/man/llama.cpp)(1), [llamafile](/man/llamafile)(1), [ollama](/man/ollama)(1), [llm](/man/llm)(1)

# RESOURCES

```[Source code](https://github.com/ggml-org/llama.cpp)```

```[Documentation](https://github.com/ggml-org/llama.cpp/tree/master/tools/cli)```

<!-- verified: 2026-06-23 -->
