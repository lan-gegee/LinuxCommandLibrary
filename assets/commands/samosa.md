# TAGLINE

在 16 GB 内存的机器上本地运行 Qwen3.6-35B-A3B

# TLDR

在终端中**提问**

```samosa "explain how DNS works"```

**继续**已封存的对话

```samosa --continue "and which strategy does Python use?"```

启用通用**思考**模式

```samosa --think "solve this logic puzzle"```

在机器温度较低时**使用更多线程**

```samosa --fast "summarize this design"```

**检查**安装状态

```samosa doctor```

**启动**本地 Web 聊天应用

```samosa app```

# SYNOPSIS

**samosa** [_OPTIONS_] ["_prompt_"]

**samosa** **doctor** | **app** | **serve** [**--stop**]

# DESCRIPTION

**samosa**（Samosa Chat）将 **Qwen3.6-35B-A3B** 的文本部分完全运行在本地 CPU 上，无需云账号，也没有遥测。该模型是混合专家（MoE）模型（总参数 35B，每个 token 约 3B 激活）。共享权重常驻内存，专家权重则按需从 NVMe 流式读取，因此 16 GB 的机器也能运行（安装位于 ~/.samosa 下，建议预留约 30 GB 可用磁盘空间）。

主要界面是终端：传入提示词字符串即可流式输出答案。对话会封存到磁盘，使用 **--continue** 可按字节精确恢复，因此后续提问无需重新读取完整历史。**samosa app** / **samosa serve** 会在 **127.0.0.1:8642** 上启动仅限回环访问的 HTTP UI 和 OpenAI 兼容端点。

Apple Silicon 上的 macOS 是最快路径（16 GB M3 上大约 5–7 tok/s）；Linux 和 Windows 通常通过 Docker 运行，在 x86 SIMD 分发落地之前速度较慢。默认线程数为二，以保持较低的温度；当散热余量允许时，**--fast** 可提高并发度。

# PARAMETERS

_"prompt"_
> 要发送给模型的问题或指令

**--continue**
> 从最后一次封存的对话快照恢复

**--think**
> 通用推理模式（更高的温度 / 思考预算）

**--think-code**
> 精确编程配置文件，配备更大的思考预算

**--fast**
> 自适应多线程模式（发热更大）

**--seed** _n_
> 固定采样种子，使输出可复现

**--max-tokens** _n_
> 限制新答案的 token 数（外层上限为 8192）

**--thinking-budget** _n_
> 启用思考模式时限制内部推理的 token 数

**doctor**
> 校验安装路径、模型文件和环境

**app**
> 在后台启动服务器并打开聊天页面

**serve**
> 在前台运行本地服务器于 127.0.0.1:8642

**serve --stop**
> 停止后台服务器

# CAVEATS

需要约 **16 GB RAM**、一块高速 **NVMe SSD** 以及大量可用磁盘空间来存放权重。解码往往受限于 SSD 而非 GPU；目前尚无 Metal/CUDA 路径。对话总大小有上限（24,576 token）。目前仅支持文本（视觉权重可能随附，但运行时图像路径尚不完整）。在运行时 CPU 分发完成之前，x86 Docker 的性能远低于 Apple Silicon。不支持 Intel Mac 和内存不足 16 GB 的机器。

# HISTORY

由 Deepan Wadhwa 开发的独立 Apache-2.0 项目。其推理引擎和打包方式借鉴了 **colibrì** 和 Qwen3.6 模型家族的思想；Samosa 增加了 group-32 量化、按字节预算管理的专家缓存、封存式对话、安装器回滚以及本地服务器。

# SEE ALSO

[ollama](/man/ollama)(1), [llama-cli](/man/llama-cli)(1), [llamafile](/man/llamafile)(1), [llm](/man/llm)(1)

# RESOURCES

```[Source code](https://github.com/deepanwadhwa/samosa-chat)```

```[Documentation](https://github.com/deepanwadhwa/samosa-chat/blob/main/docs/USAGE.md)```

<!-- verified: 2026-07-17 -->
