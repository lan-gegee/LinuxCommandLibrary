# TAGLINE

DwarfStar 本地 LLM 推理的交互式编程智能体

# TLDR

以大上下文**启动智能体**并加载模型

```ds4-agent -m [ds4flash.gguf] --ctx [100000]```

**运行单个非交互式轮次**

```ds4-agent -m [ds4flash.gguf] --non-interactive -p "[fix the failing test]"```

**降低 GPU 功率**以获得更安静的运行

```ds4-agent -m [ds4flash.gguf] --power [50]```

将提示词和工具调用的调试轨迹**写入文件**

```ds4-agent -m [ds4flash.gguf] --trace [agent.trace]```

在加载资源前**更改工作目录**

```ds4-agent -m [ds4flash.gguf] --chdir [/path/to/project]```

**禁用思考**以获得直接回答

```ds4-agent -m [ds4flash.gguf] --nothink```

# SYNOPSIS

**ds4-agent** [_options_]

# PARAMETERS

**-m**, **--model** _FILE_
> GGUF 模型路径。默认：**ds4flash.gguf**。

**-c**, **--ctx** _N_
> 分配的上下文长度（以 token 计）。

**-p**, **--prompt** _TEXT_
> 启动后提交初始提示词（配合 **--non-interactive** 时为单轮对话）。

**--non-interactive**
> 不带 TUI 运行。有 **-p**：执行一轮后退出；无 **-p**：从标准输入重复读取提示词。

**-sys**, **--system** _TEXT_
> 额外的系统提示词文本。传空字符串可禁用额外文本。

**--trace** _FILE_
> 写出提示词、token 和 DSML 工具调用的调试输出。

**--chdir** _DIR_
> 加载运行时资源前先切换工作目录（让相对项目路径能正确解析时很有用）。

**--power** _N_
> GPU 占空比目标，取值 1 到 100。默认：**100**。

**--metal** | **--cuda** | **--rocm** | **--cpu**
> 显式选择推理后端。

**--ssd-streaming**
> 当完整驻留放不下时，从 SSD 流式读取模型权重。

**--think** / **--think-max** / **--nothink**
> 控制模型的思考/推理模式。

# DESCRIPTION

**ds4-agent** 是随 **DwarfStar**（**ds4**）发布的集成编程智能体。它加载与交互式 **ds4** CLI 和 **ds4-server** 相同的专用 GGUF 模型，然后运行一个使用工具的智能体循环，面向本地开发工作（读取文件、编辑、经由模型的 DSML 工具协议执行命令）。

在交互式 TUI 中，你可以用斜杠命令管理长期会话：**/save** 与 **/list** / **/switch** 用于在 **~/.ds4/kvcache** 下持久化会话，**/compact** 压缩上下文，还有 **/history**、**/new** 和 **/power**。该智能体设计为与本项目的端到端本地技术栈协作，而非通用的智能体框架。

# CAVEATS

上游将其标记为 **alpha** 质量，逊于 DwarfStar 其余部分。需要 DwarfStar 兼容的 GGUF 以及合适的 GPU 后端才能达到实用速度。工具使用和长会话可能消耗大量上下文和磁盘空间来存放 KV 检查点。同系列的交互式推理二进制也叫 **ds4**，与同名但无关的 DualShock 4 工具重名。

# HISTORY

**ds4-agent** 是在核心推理 CLI 和 HTTP 服务器之后加入 **DwarfStar** 项目的，属于"模型 + 引擎 + 智能体"一体交付目标的一部分，面向高内存机器和 SSD 流式配置上的本地编程工作流。

# SEE ALSO

[ds4-server](/man/ds4-server)(1), [ds4-bench](/man/ds4-bench)(1), [ds4-eval](/man/ds4-eval)(1), [ollama](/man/ollama)(1), [llama-cli](/man/llama-cli)(1)

# RESOURCES

```[Source code](https://github.com/antirez/ds4)```

```[Documentation](https://github.com/antirez/ds4/blob/main/docs/ENGINE_REFERENCE.md)```

<!-- verified: 2026-07-18 -->
