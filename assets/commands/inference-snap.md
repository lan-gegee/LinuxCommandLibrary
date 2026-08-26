# TAGLINE

通过 Ubuntu 推理 snap 进行本地生成式 AI 对话

# TLDR

**启动**交互式终端对话会话

```inference-snap chat```

**显示**当前引擎与聊天服务器状态

```inference-snap status```

**选择**硬件引擎及匹配的模型

```sudo inference-snap use-engine [cuda|cpu|...]```

**打印**主机硬件详情以便选择模型

```sudo inference-snap show-machine```

**读取**运行中的聊天服务器配置

```inference-snap get```

# SYNOPSIS

**inference-snap** **chat**

**inference-snap** **status**

**inference-snap** **get**

**sudo inference-snap** **use-engine** _engine_

**sudo inference-snap** **show-machine**

# DESCRIPTION

**inference-snap** 是 Ubuntu **Inference Snaps** 的命令行界面：这些打包好的生成式 AI 模型针对本地 CPU、GPU 或 NPU 硬件进行了调优。每个 snap 都自带模型权重和运行时，能自动检测主机并提供本地聊天 API。

**chat** 子命令会启动终端会话，并在首次使用时拉起后台聊天服务器。支持的模型家族包括 **deepseek-r1**、**gemma3**、**gemma4**、**nemotron3-nano** 和 **qwen-vl**，具体取决于安装了哪个推理 snap。

**use-engine** 用于切换执行后端（例如 NVIDIA GPU 上的 **cuda**），并下载适合该引擎的模型变体。**show-machine** 会报告内存、架构和设备详情，帮助选择引擎。**get** 打印服务器设置（如 **http.host** 和 **http.port**）；**status** 概括引擎选择与服务健康状况。

Inference snaps 还提供 OpenAI 兼容的 HTTP API 供 IDE 和其他工具使用，但 **inference-snap** 本身是用于聊天和管理的 snap 管理 CLI。

# CAVEATS

需要已通过 **snap** 安装受支持的 Ubuntu 推理 snap。切换引擎和检查硬件需要 **sudo**。首次启动 **chat** 可能要下载模型权重，耗时较明显。

# SEE ALSO

[snap](/man/snap)(8), [curl](/man/curl)(1)
