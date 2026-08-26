# TAGLINE

内存感知的 GGUF 语言模型推理 CLI

# TLDR

以一次性提示词**运行** GGUF 模型

```runNburn [path/to/model.gguf] "[prompt]"```

**启动**交互式聊天（省略提示词）

```runNburn [path/to/model.gguf]```

结合多轮历史和采样选项进行**聊天**

```runNburn chat --system "[prompt]" --max-tokens [n] [path/to/model.gguf]```

**提供** OpenAI 兼容的 HTTP API

```runNburn serve --host 127.0.0.1 --port 8000 --ram-budget 16GiB [path/to/model.gguf]```

**限制**主机工作集内存

```runNburn --ram-budget 16GiB [path/to/model.gguf] "[prompt]"```

# SYNOPSIS

**runNburn** [_options_] _model.gguf_ [_prompt_]

**runNburn** **chat** [_options_] _model.gguf_

**runNburn** **serve** [_options_] _model.gguf_

# DESCRIPTION

**runNburn**（包/crate 名称 **runNburn**；产品二进制文件通常为 **runNburn**）是一个 1.0 前版本的 Rust 推理运行时，面向超过可用高速内存的量化 GGUF 模型。权重尽可能保留文件映射驻留，主机内存占用由检测到的或显式指定的 RAM 预算限定，可选的 CUDA 或 Metal 路径可加速受支持的算子。

同一套产品路径覆盖一次性生成、交互式聊天以及本地 OpenAI 兼容 HTTP 服务器（**chat/completions**、**responses**、模型列表）。架构感知的支持范围包括 Llama/Phi、Gemma、Qwen 的稠密/混合/MoE 等系列；识别出架构并不保证每个社区 GGUF 变体都能被完全加速。

CPU 是默认后端。根据硬件使用 Cargo 特性标志构建（**cpu**、**cuda**、**metal**、实验性的 **vulkan**）。在不指定 **--ram-budget** 时，引擎会为操作系统预留约四分之一的物理 RAM，并将其余部分用作工作集预算。

# PARAMETERS

**--ram-budget** _size_

> 限制引擎占用的主机内存驻留量（例如 **16GiB**、**32GB**）。接受二进制和十进制后缀。直接的 CLI 选项必须出现在 GGUF 路径之前。

**chat** / **serve**

> 用于多轮 REPL 和 HTTP 服务的子命令。采样、缓存和绑定选项见 **runNburn chat --help** 与 **runNburn serve --help**。

**serve** 的常用选项包括 **--host**、**--port**、**--model-name**、**--response-cache-budget** 和 **--api-key-file**。绑定到非回环地址时需要 API key。

# CAVEATS

1.0 前版本；API 和后端覆盖范围会变化。**--ram-budget** 不是操作系统的 RSS 硬性上限。OpenAI 接口只是部分兼容，并非完整的 OpenAI API。Vulkan 和某些移动端路径是实验性的。二进制名称按项目发布形式使用混合大小写（**runNburn**）。

# SEE ALSO

[llama-cli](/man/llama-cli)(1), [ollama](/man/ollama)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/coderredlab/runNburn)```

<!-- verified: 2026-07-30 -->
