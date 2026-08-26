# TAGLINE

从磁盘流式读取模型专家的本地 LLM 推理引擎

# TLDR

**构建**引擎和 CLI

```make```

对已转换的容器**运行**一次性提示词

```waste run [~/models/k3.waste] "[What is the capital of France?]" -n [32]```

**交互式多轮对话**

```waste chat [~/models/k3.waste]```

**显示下一个 token 的分布**

```waste eval [~/models/k3.waste] "[2 + 2 =]" --top-k [5]```

为容器**规划内存预算**

```waste plan [~/models/k3.waste] --budget [46G]```

**带图像输入运行**（多模态模型）

```waste run [~/models/k3.waste] "[What is in this picture?]" --image [photo.png]```

加载时**校验专家 CRC**

```waste run [~/models/k3.waste] "[prompt]" --verify```

# SYNOPSIS

**waste** _command_ [_options_] [_args_...]

# PARAMETERS

**run** _CONTAINER_ [_PROMPT_]
> 根据提示词（或 stdin）生成补全。常用标志：**-n** _count_（token 上限）、**--budget** _SIZE_、**--image** _FILE_、**--verify**。

**chat** _CONTAINER_
> 多轮交互式会话；会话状态保存在进程内。

**eval** _CONTAINER_ _PROMPT_
> 显示下一个 token 的分数/分布。支持 **--top-k**、**--json**、**--image**。

**plan** _CONTAINER_
> 报告本机可容纳的内存预算以及引擎会选择的值。

**info** _CONTAINER_
> 打印容器/模型元数据。

**bench** _CONTAINER_
> 运行内置的性能检测。

**tokenize** _CONTAINER_
> 对提示词分词或检查其布局（当前子标志见 **--help**）。

**--budget** _SIZE_
> 内存硬上限（例如 `46G`）。若省略，引擎会选择约物理内存 7/8 以下的预算，且绝不低于模型下限。

**--verify**
> 在缓存未命中时检查每个专家记录的 CRC（较慢；在复制/下载后很有用）。也可用 **WASTE_VERIFY=1**。

**--json**
> 为 eval/plan/info/bench 等命令提供机器可读输出。

**--help**
> 列出所有命令和标志。

# DESCRIPTION

**waste**（Weight-Aware Streaming Tensor Engine）是一个零依赖的 C 语言推理引擎和 CLI，用于在完整权重集无法装入内存时运行大型混合专家语言模型。它在内存中保留常驻的"主干"，从 NVMe 上的转换后 **.waste** 容器流式读取被激活的专家，并将剩余内存用作有界的专家缓存。

其标志性验证案例是开源权重模型 **Kimi K3**（约 2.78T 参数，容器约 982 GiB），在配备足够内存和内置 NVMe 的消费级硬件上以大约每秒半个 token 的速度运行。同一格式的较小模型（如 Kimi-Linear 48B）运行速度快得多，内存下限也低得多。

先使用仓库中的 Python 工具将公开的 safetensors 转换一次；运行时只需要 **waste** 二进制文件（以及 libc/pthreads）。`serve/` 目录下还有一个可选的 OpenAI 兼容 HTTP 服务器，通过 ctypes 使用同一个公共 C API。

# CAVEATS

K3 级别的模型需要数十 GB 内存（开启至少约 **29 GB**，达到实用吞吐量约需 **~64 GB**）以及 **fast 内置 NVMe** 上约 **1 TB** 的容器——USB 外接硬盘太慢。构建需要 C11 编译器和 **make**；转换需要 Python/torch。专家 CRC 校验默认关闭。对于转换器认识的模型（目前是 K3），聊天模板会完整填充；其他容器可能以原始提示词模式运行。它不是 **ollama** 这类通用多模型运行时的直接替代品。

# HISTORY

**WASTE** 由 **SQLite Cloud, Inc.**（sqliteai）开发，以 **Apache 2.0** 许可发布。它的定位是在单机上对前沿规模的 MoE 模型进行磁盘流式推理，而不是多 GPU 服务器。

# SEE ALSO

[ollama](/man/ollama)(1), [llama.cpp](/man/llama.cpp)(1)

# RESOURCES

```[Source code](https://github.com/sqliteai/waste)```

```[Documentation](https://github.com/sqliteai/waste/tree/main/docs)```

<!-- verified: 2026-08-01 -->
