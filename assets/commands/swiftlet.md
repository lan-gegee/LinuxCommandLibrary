# TAGLINE

在 Apple Silicon 上以低内存流式运行大型 Qwen MoE 模型

# TLDR

**构建** release 二进制

```git clone https://github.com/leonickson1/Swiftlet.git && cd Swiftlet```

```swift build -c release```

从 Hugging Face **下载 / 重打包** 4-bit 模型容器

```.build/release/swiftlet-repack --from-hf Leonickson/Qwen3.6-35B-A3B-qpack --output ~/models/qwen3.6-35b.qpack```

带多轮历史进行**对话**

```swiftlet chat ~/models/qwen3.6-35b.qpack "[Who wrote One Hundred Years of Solitude?]" "[What language did he write it in?]"```

带统计信息的**一次性**生成

```swiftlet generate ~/models/qwen3.6-35b.qpack --gpu --chat --prompt "[Explain expert streaming in one paragraph.]"```

启动一个 **OpenAI 兼容**的本地服务器

```swiftlet-server --model ~/models/qwen3.6-35b.qpack --port 8080```

# SYNOPSIS

**swiftlet** **chat** _model.qpack_ [_prompt_...]

**swiftlet** **generate** _model.qpack_ [**--gpu**] [**--chat**] [**--prompt** _text_]

**swiftlet-repack** **--from-hf** _repo_ **--output** _path_

**swiftlet-server** **--model** _path_ [**--port** _n_]

# PARAMETERS

**chat** _model_ [_prompts_...]
> 交互式或脚本化的多轮对话。会应用模型聊天模板，可禁用推理块，并缓存对话状态，使后续提问只需预填充新一轮内容。

**generate** _model_ [**--gpu**] [**--chat**] [**--prompt** _text_]
> 一次性生成，支持可选的 GPU 路径和生成统计信息。

**swiftlet-repack** **--from-hf** _owner/repo_ **--output** _file.qpack_
> 将专家权重流式打包进固定步长的 **.qpack** 容器（支持断点续传）。也通过 **--source** 接受原始 MLX 检查点以及 Hugging Face MLX 社区仓库。

**swiftlet-server** **--model** _file.qpack_ [**--port** _n_]
> 与 OpenAI chat-completions 兼容的 HTTP 服务器（面向本机回环使用）。

# DESCRIPTION

**swiftlet** 是一个用于 **Apple Silicon** 上 **Qwen3-Next** 和 **Qwen3.5/3.6 MoE** 混合架构系列的 **Swift + Metal** 运行时。只有稠密核心常驻内存；路由到的混合专家权重通过 **pread** 从 SSD 流式读入一个容量受限的专家缓存。这一设计让 **Qwen3.6-35B-A3B**（峰值内存约 2.6 GB，磁盘占用约 18 GB）和 **Qwen3-Next-80B-A3B**（峰值内存约 4.3 GB，磁盘占用约 42 GB）等模型能以 4-bit 量化在普通 Mac 上运行，而且 35B 级别的模型可以在较新的 iPhone 上于配套 App 内运行。

该包提供三个可执行文件：**swiftlet**（chat / generate）、**swiftlet-repack**（构建 **.qpack** 容器）和 **swiftlet-server**（OpenAI 兼容 API）。**SwiftletCore** 同时也是一个库，可用于嵌入 macOS/iOS 应用。内核是运行时编译的 Metal 着色器；各层计算均对照 mlx-lm 参考基准做了验证。

# CAVEATS

仅限 **Apple Silicon**（macOS 14+ / iOS 17+）。需要足够的 SSD 空间存放完整容器（数十 GB）。每个 token 只激活几十亿参数，因此事实性回忆可能更接近较小的稠密模型，而非标称参数量。解码循环仍是性能优化的重点，报告的速度因芯片而异。模型权重需单独下载，并受其自身许可证约束（Qwen 模型：Apache-2.0）。不是通用的 Linux GPU 推理方案。

# HISTORY

**Swiftlet** 是一个 Apache-2.0 项目，将专家流式思想（精神上类似 TurboFieldfare 等工作）应用于采用 Gated DeltaNet 和稀疏专家路由的 Qwen 混合 MoE 架构，以 Swift 和 Metal 从零实现，并以 mlx-lm 作为正确性参考。

# SEE ALSO

[ollama](/man/ollama)(1), [mlx](/man/mlx)(1), [llama](/man/llama)(1)

# RESOURCES

```[Source code](https://github.com/leonickson1/Swiftlet)```

```[Homepage](https://github.com/leonickson1/Swiftlet)```

<!-- verified: 2026-08-04 -->
