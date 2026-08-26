# TAGLINE

在普通硬件上从磁盘运行大型 MoE LLM（如 GLM-5.2 744B）的微型纯 C 引擎

# TLDR

**构建**引擎

```cd c && ./setup.sh```

**转换**（或指向已转换的模型）并开始聊天

```COLI_MODEL=/path/to/glm52_i4 ./coli chat```

**加载前查看**规划的 RAM/VRAM 分层方案

```COLI_MODEL=/path/to/glm52_i4 ./coli plan```

**提供**兼容 OpenAI 的本地 API

```COLI_MODEL=/path/to/glm52_i4 ./coli serve --host 127.0.0.1 --port 8000```

**评测**质量

```./coli bench```

# SYNOPSIS

**coli** <command> [options]

# DESCRIPTION

coli（colibrì）是一个极简、零依赖的 C 推理引擎（核心为单文件），用于运行 GLM-5.2 这类超大规模混合专家模型：只将稠密部分常驻内存，专家权重则按需从磁盘流式读取，配合激进的缓存策略和可选的 MTP 投机解码。

在小机器上它有意以磁盘 I/O 为瓶颈进行设计，面向在消费级硬件上试验和本地使用前沿规模模型。运行时推理是纯 C 实现；Python 仅用于离线转换器和可选的 HTTP 网关。

# COMMANDS

**chat**
> 交互式聊天（支持采样参数、MTP、思考模式）。会话可在重启后恢复压缩的 KV 缓存。

**convert**
> 对模型分片进行一次性 FP8→int4 转换（可断点续传；每次下载一个分片）。

**plan**
> 仅凭 safetensors 头信息报告稠密部分与专家部分的占用、安全的专家缓存上限以及 VRAM 分层方案，无需加载张量。

**serve**
> 兼容 OpenAI 的 HTTP API（`/v1/chat/completions`、`/v1/models`、旧式 completions），支持可选的 API 密钥和请求排队。

**bench**
> 运行质量基准测试（HellaSwag、ARC、MMLU）。

**run**, **info**
> 单条提示生成与模型信息。

# PARAMETERS

环境变量和标志控制温度、topp、草稿深度（MTP）、内存预算、自动绑定（autopin）、CUDA 专家分层等。大多数操作都需要 `COLI_MODEL`（或 `--model`）。常用选项包括 `--temp`、`--topp`、`--ngen`、`DRAFT`、`THINK=1`、`PIN`/`PIN_GB` 以及 `--auto-tier`（将 plan 结果应用于 chat/run/serve）。完整列表见项目 README。

# CAVEATS

- 需要大量高速本地存储（示例模型约需 370 GB），且高速随机读取的 NVMe 带来的收益极为显著。
- 目前专门针对 GLM-5.2 架构；并非通用 LLM 运行器。
- 冷启动性能较低；预热缓存 + MTP 能显著改善响应速度。MTP 头应为 int8 才能让投机解码有效启用。

# SEE ALSO

[llama.cpp](/man/llama.cpp)(1)

# RESOURCES

```[Source code](https://github.com/JustVugg/colibri)```

```[Documentation](https://github.com/JustVugg/colibri#readme)```

<!-- verified: 2026-07-11 -->
