# TAGLINE

本地优先的文档数据提取 CLI

# TLDR


**启动**本地的 ParseHawk 服务栈

```parsehawk start```


**查看**服务状态

```parsehawk status```


**运行配置**健康检查

```parsehawk doctor```


**上传**文档

```parsehawk files upload [document.pdf]```


**使用提取器对文件执行一次性提取**

```parsehawk extract [document.pdf] --extractor [extractor_id]```


**用临时指令提取**并等待结果

```parsehawk extract [document.pdf] --instructions "[extract invoice total and date]" --wait```


**停止**正在运行的服务

```parsehawk stop```

# SYNOPSIS

**parsehawk** \<command\> [subcommand] [options]

# DESCRIPTION

ParseHawk 是一款本地优先的文档 AI 工具，能把文档（PDF、扫描件、图像、文本和 Markdown）转换为经过校验的结构化 JSON。默认情况下它完全在本地机器上运行，不调用任何第三方 API，使用由 vLLM 提供服务的量化提取模型。

该项目以单一后端之上的三个客户端形态发布：REST API、Web UI 以及这个命令行界面。CLI 既负责管理后端服务（**start**、**stop**、**status**），也负责驱动数据工作流（上传文件、定义提取器和 schema、运行提取作业）。提取是零样本或少样本式的：用户无需训练模型，只需提供一份 JSON Schema、自然语言指令和可选示例，模型就会返回符合该 schema 的 JSON。

大多数数据操作都要求后端栈处于运行状态，因此一次典型的会话以 **parsehawk start** 开始，以 **parsehawk stop** 结束。

# COMMANDS

**start**

> 启动 ParseHawk 服务栈。

**stop**

> 停止正在运行的服务。

**restart**

> 重启服务。

**status**

> 显示服务是否正在运行。

**doctor**

> 运行本地配置健康检查。

**dev**

> 以带热重载的开发模式启动。

**extract** \<file\>

> 对文件执行一次性提取，而不创建单独的作业。

**files upload** \<file\>

> 将文档上传到服务。

**files list**

> 列出已上传的文件。

**files delete** \<file_id\>

> 移除一个已上传的文件。

**schemas validate** \<schema.json\>

> 校验一个 JSON Schema 文件。

**extractors create**

> 定义一组新的提取规则。

**extractors list**

> 显示可用的提取器。

**extractors get** \<extractor_id\>

> 获取某个提取器的详细信息。

**extractors delete** \<extractor_id\>

> 移除某个提取器。

**jobs create**

> 启动一个提取作业。

**jobs get** \<job_id\>

> 获取某个作业的状态和结果。

**config list**

> 显示当前设置。

**config set** \<key\> \<value\>

> 更改某个配置值。

# PARAMETERS

**--extractor** \<id\>

> 选择要使用的提取器。

**--file-id** \<id\>

> 选择一个已上传的文件作为输入。

**--schema** \<file\>

> 提供描述期望输出的 JSON Schema。

**--instructions** \<text\>

> 给出自然语言的提取指令。

**--wait**

> 阻塞直到作业完成，而不是立即返回。

**--runtime none**

> 跳过本地模型推理。

# CONFIGURATION

行为可以通过环境变量调整，环境变量会覆盖默认值：

**PARSEHAWK_VLLM_MAX_MODEL_LEN**

> 模型的最大上下文长度（例如 16384）。

**PARSEHAWK_VLLM_GPU_MEMORY_UTILIZATION**

> 模型运行时可使用的 GPU 内存比例（例如 0.6）。

**PARSEHAWK_VLLM_MAX_NUM_SEQS**

> 并行处理的最大序列数。

**PARSEHAWK_TELEMETRY_DISABLED**

> 设为 1 即可退出匿名使用情况分析。

# CAVEATS

该 CLI 控制着一个持久化的后端服务，因此大多数操作都需要先执行过 **parsehawk start**。运行本地模型需要大量资源：macOS（Apple Silicon）上大约需要 16 GB 统一内存，配备 NVIDIA GPU 的 Linux 上大约需要 16 GB 显存，此外还需要 Docker。不支持 Windows。除非通过 **PARSEHAWK_TELEMETRY_DISABLED** 禁用，否则会发送匿名的使用情况分析数据。

# HISTORY

ParseHawk 使用 **Python** 构建（后端为 FastAPI），配有 **React**/**Vite** Web UI，并通过 **vLLM** 在本地运行其默认提取模型（NuExtract3）。它以 **Apache-2.0** 许可证发布。

# SEE ALSO

[tesseract](/man/tesseract)(1), [pdftotext](/man/pdftotext)(1), [jq](/man/jq)(1), [docker](/man/docker)(1)

# RESOURCES

```[Source code](https://github.com/parsehawk/parsehawk)```

<!-- verified: 2026-06-26 -->
