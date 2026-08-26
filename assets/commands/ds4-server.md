# TAGLINE

DwarfStar LLM 推理的本地 OpenAI/Anthropic 兼容 HTTP 服务器

# TLDR

加载 GGUF 模型**启动 API**（默认绑定 127.0.0.1:8000）

```ds4-server -m [ds4flash.gguf]```

以**大上下文和 Metal 后端**提供服务

```ds4-server -m [ds4flash.gguf] --metal --ctx [100000]```

**监听自定义主机与端口**

```ds4-server -m [ds4flash.gguf] --host [127.0.0.1] --port [8000]```

为浏览器客户端**启用 CORS**

```ds4-server -m [ds4flash.gguf] --cors```

当模型放不进内存时**从 SSD 流式读取模型权重**

```ds4-server -m [ds4flash.gguf] --ssd-streaming --ctx [32768]```

在磁盘预算内**持久化 KV 缓存**

```ds4-server -m [ds4flash.gguf] --ctx [100000] --kv-disk-dir [~/.ds4/server-kv] --kv-disk-space-mb [8192]```

通过本地 API **列出模型**

```curl http://127.0.0.1:8000/v1/models```

**降低 GPU 占空比**以获得更好的散热表现

```ds4-server -m [ds4flash.gguf] --power [60]```

# SYNOPSIS

**ds4-server** [_options_]

# PARAMETERS

**-m**, **--model** _FILE_
> GGUF 模型路径。默认：**ds4flash.gguf**。

**--metal** | **--cuda** | **--rocm** | **--cpu**
> 显式选择推理后端。macOS 上首选 Metal；Linux 上视构建情况支持 CUDA/ROCm。

**-c**, **--ctx** _N_
> 分配的上下文长度（以 token 计）。

**-n**, **--tokens** _N_
> 客户端未设置上限时的默认最大输出 token 数。

**--host** _HOST_
> 绑定地址。默认：**127.0.0.1**。

**--port** _N_
> 绑定端口。默认：**8000**。

**--cors**
> 为浏览器 JavaScript 客户端添加 **Access-Control-Allow-*** 响应头。

**--power** _N_
> GPU 占空比目标，取值 1 到 100。默认：**100**。

**--ssd-streaming**
> 启用基于 SSD 的模型流式读取，替代完整的内存驻留。

**--ssd-streaming-cache-experts** _N_|_NGB_
> 路由专家缓存的大小（专家数量或 GiB，如 **32GB**）。

**--think** / **--think-max** / **--nothink**
> 聊天式请求的默认思考模式（服务器同时映射 OpenAI/Anthropic 的 effort 字段）。

**--kv-disk-dir** _DIR_
> 在 _DIR_ 中启用磁盘上的 KV 检查点。

**--kv-disk-space-mb** _N_
> 启用 KV 磁盘时的磁盘预算（MB）。默认：**4096**。

**--trace** _FILE_
> 将提示词、缓存决策、输出和工具调用写入轨迹文件。

**-t**, **--threads** _N_
> 用于宿主侧工作的 CPU 辅助线程数。

# DESCRIPTION

**ds4-server** 是 **DwarfStar**（由 **Salvatore Sanfilippo** / **antirez** 及贡献者发起的项目 **ds4**）的 HTTP API 前端。它加载项目专属的 **GGUF** 并提供 OpenAI 和 Anthropic 兼容端点，使本地工具、IDE 和编程智能体可以直接对接专用 DeepSeek V4（及相关）推理引擎，而无需调用云 API。

每个客户端连接由一个阻塞式请求线程处理；推理本身被串行化到持有活动会话和 KV 状态的唯一工作线程上。这一设计把会话复用、可选的磁盘 KV 检查点和计算图执行集中在同一处。端点包括 **/v1/chat/completions**、**/v1/responses**、**/v1/completions** 和 **/v1/messages**。**deepseek-v4-flash** 和 **deepseek-v4-pro** 等模型名称别名都指向当前加载的 GGUF。

与通用的 GGUF 运行器不同，DwarfStar 只针对一小批精心准备的权重（DeepSeek V4 Flash/PRO 以及面向其他 MoE 模型的实验分支）。请使用项目提供的下载脚本和发布的 GGUF；任意的社区 GGUF 文件预期无法运行。后端包括 **Metal**（Apple Silicon 上的首选）、**CUDA**（含 DGX Spark）和 **ROCm**（如 Strix Halo）。**--ssd-streaming** 通过从磁盘换入路由专家，让超出内存的模型仍可运行。

# CAVEATS

该软件明确处于 **beta** 阶段。仅支持 DwarfStar 准备的 GGUF。默认绑定为 localhost；只有在理解其没有内置鉴权的前提下才可暴露到网络。磁盘 KV 和大上下文需要充足的可用磁盘与内存。纯 CPU 构建主要用于诊断；生产使用应使用 Metal、CUDA 或 ROCm。交互式 CLI 二进制也叫 **ds4**，在 Linux 上与同名但无关的 DualShock 4 工具重名。

# HISTORY

**DwarfStar**（**ds4**）由 **Salvatore Sanfilippo**（**antirez**）创建，是一个小型自包含的本地推理技术栈，专为勉强塞进（或塞不进）消费级内存的大型开放权重 MoE 模型优化。**ds4-server** 提供该技术栈的 HTTP API 一侧，让编程智能体和 OpenAI 兼容客户端能使用与交互式 **ds4** CLI 相同的引擎。

# SEE ALSO

[ds4-agent](/man/ds4-agent)(1), [ds4-bench](/man/ds4-bench)(1), [ds4-eval](/man/ds4-eval)(1), [ollama](/man/ollama)(1), [llama-cli](/man/llama-cli)(1), [llama.cpp](/man/llama.cpp)(1)

# RESOURCES

```[Source code](https://github.com/antirez/ds4)```

```[Documentation](https://github.com/antirez/ds4/blob/main/docs/ENGINE_REFERENCE.md)```

<!-- verified: 2026-07-18 -->
