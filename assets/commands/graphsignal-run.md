# TAGLINE

面向 AI 推理工作负载的性能剖析启动器

# TLDR

**安装**支持 CUDA 12 的性能分析器

```pip install 'graphsignal[cu12]'```

通过包装启动命令来**剖析** vLLM 服务器

```GRAPHSIGNAL_API_KEY=[key] graphsignal-run vllm serve [model] --port [8001]```

**剖析**任意推理命令

```GRAPHSIGNAL_API_KEY=[key] graphsignal-run [command] [args...]```

为记录的数据**附加**任意标签

```GRAPHSIGNAL_TAG_DEPLOYMENT=[us-prod] GRAPHSIGNAL_API_KEY=[key] graphsignal-run [command]```

# SYNOPSIS

**graphsignal-run** _COMMAND_ [_ARGS_...]

# DESCRIPTION

**graphsignal-run** 是 **Graphsignal** 的启动器 CLI，后者是一个生产级规模的推理性能剖析平台。你在正常的模型服务或推理命令前加上 **graphsignal-run**，它会以 sidecar 进程的方式挂载，在不改动代码的情况下剖析被包装的工作负载。

它捕获连续、高分辨率的时间线，揭示各操作的耗时和资源利用率：CUDA kernel 活动、GPU 与系统级指标、逐步的 LLM 生成追踪、token 吞吐量以及错误监控。收集到的信号会被发送到 Graphsignal 平台，你可以在那里查看时间线，跨模型、引擎和加速器定位性能瓶颈。

它支持常见的推理技术栈，包括 **PyTorch**、**vLLM** 和 **SGLang**。

# CONFIGURATION

**GRAPHSIGNAL_API_KEY**

> 用于身份验证和上传剖析数据的账户 API 密钥。必需。

**GRAPHSIGNAL_TAG_**_KEY_**=**_VALUE_

> 为记录的信号附加任意标签（例如 **GRAPHSIGNAL_TAG_DEPLOYMENT=us-prod**）。可以使用不同的键多次设置。

# CAVEATS

该分析器会把遥测数据上传到 Graphsignal 的托管服务，并需要有效的 API 密钥，因此并非完全离线的工具。安装的 extra 必须与主机的 CUDA 版本匹配：CUDA 12.x 使用 **graphsignal[cu12]**，CUDA 13.x 使用 **graphsignal[cu13]**。

# HISTORY

由 **Graphsignal** 开发，于 **2026 年**发布，是其推理性能分析器的命令行入口。它在 PyPI 上作为 **graphsignal** 软件包的一部分分发，采用 Apache-2.0 许可证。

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1), [nvtop](/man/nvtop)(1), [py-spy](/man/py-spy)(1), [perf](/man/perf)(1)

# RESOURCES

```[Source code](https://github.com/graphsignal/graphsignal-profiler)```

```[Homepage](https://graphsignal.com)```

<!-- verified: 2026-06-24 -->
