# TAGLINE

将 Meta 的 LLaMA 模型移植到 C/C++ 以实现高效的 CPU 和 GPU 推理

# TLDR

**运行交互式聊天**

```./main -m [model.gguf] -i```

**根据提示词生成文本**

```./main -m [model.gguf] -p "[Your prompt here]"```

**设置上下文大小**

```./main -m [model.gguf] -c [4096] -p "[prompt]"```

**使用多线程**

```./main -m [model.gguf] -t [8] -p "[prompt]"```

**运行服务器模式**

```./server -m [model.gguf] --port [8080]```

**量化模型**

```./quantize [model.gguf] [output.gguf] [q4_0]```

# SYNOPSIS

**main** [_options_] -m _model_ -p _prompt_

# PARAMETERS

**-m** _model_
> GGUF 模型文件的路径。

**-p** _prompt_
> 输入提示词。

**-i**
> 交互模式。

**-c** _size_
> 上下文大小。

**-t** _threads_
> 线程数。

**-n** _tokens_
> 要生成的 token 数量。

**--temp** _temp_
> 采样温度。

**-ngl** _layers_
> 要卸载到 GPU 的层数。

# DESCRIPTION

**llama.cpp** 是 Meta 的 LLaMA 模型向 C/C++ 的移植版本，可实现高效的 CPU 和 GPU 推理。它支持多种量化格式，可在消费级硬件上运行大语言模型。

该项目包含模型转换、量化和服务部署等工具。

# SUPPORTED FORMATS

```
GGUF - Current format
Quantizations: q4_0, q4_1, q5_0, q5_1, q8_0
GPU: CUDA, Metal, OpenCL
```

# CAVEATS

模型必须转换为 GGUF 格式。内存需求取决于模型大小和量化方式。GPU 支持因后端而异。

# HISTORY

llama.cpp 由 **Georgi Gerganov** 在 Meta 发布 LLaMA 权重后于 **2023 年 3 月**创建，让本地 LLM 推理成为可能。

# INSTALL

```brew: brew install llama.cpp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[llamafile](/man/llamafile)(1), [ollama](/man/ollama)(1)
