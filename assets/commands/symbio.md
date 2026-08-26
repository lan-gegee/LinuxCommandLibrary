# TAGLINE

通过 LoRA 从纠错中学习的本地 AI 智能体 CLI（Apple Silicon / MLX）

# TLDR

**启动**交互式对话（首次运行会打开设置向导）

```symbio```

```symb```

**查看或修改**配置

```symb config```

```symb config get agent.temperature```

```symb config set agent.temperature 0.7```

用收集的数据**训练** LoRA 适配器

```symb train```

**管理技能**与闲置适配器

```symb skill list```

```symb skill new [name]```

```symb archive --dry-run```

**Telegram** 网关

```symb gateway status```

```symb gateway start```

# SYNOPSIS

**symbio** [_subcommand_] [_options_]

**symb** [_subcommand_] [_options_]

# DESCRIPTION

**symbio**（简短别名 **symb**）是一个本地 AI 助手：它在终端中（或通过 Telegram）对话，维护 markdown 笔记，运行沙箱化的工具，并把你的纠正转化为 **LoRA** 微调数据，让模型在设备端不断改进。

它使用 Apple 的 **MLX** / Metal 技术栈：当前版本面向 **Apple Silicon**（建议约 16 GB 统一内存）。核心流程不依赖任何云端 API。首次启动时，交互式向导会设置名称、模型预设和可选功能（浏览器、网页搜索、混合智能体调度、Telegram）。

纠正会被自动识别（如 "No, …" / "Actually …" 之类的措辞）并保存为错误笔记；当达到 **learn.mistake_threshold**（默认 5）时，会执行一次批量 LoRA 更新，并用**黄金基准集**校验，出现回退时自动回滚。可选的 **MOA** 模式把有边界的任务委托给更小的 worker 模型。技能以 markdown 流程起步，之后可以发展出专属适配器。

从克隆目录安装可用 **pip install -e .** 或 **pipx install .**，使 **symbio** / **symb** 进入 **$PATH**。

# PARAMETERS

**(no subcommand)** / **chat**
> 启动交互式对话会话。

**config** [**show** | **get** _key_ | **set** _key_ _value_]
> 查看或修改 **config.json**（show 输出中的机器人令牌会被遮蔽）。

**train**
> 运行 LoRA 微调（**lora.iters**）并重新加载适配器。

**skill list** | **skill new** _name_ | **skill rm** _role_
> 列出、创建或移除技能笔记/适配器。

**archive** [**--dry-run**] [**--restore** **note**|**adapter** _name_]
> 归档闲置的笔记/适配器，或恢复其中一项。

**gateway status** | **gateway start** | **gateway stop**
> 检查或控制 Telegram 机器人网关。

**setup**
> 重新运行交互式设置向导。

# CONFIGURATION

**config.json**（项目 / 安装目录）
> 模型名称、智能体限制、LoRA 超参数、学习阈值、Telegram 设置、调度（MOA）和工具组。机密信息优先使用 **symb config set**，而非手动编辑。

**SYMBIO_TELEGRAM_TOKEN**
> Telegram 机器人令牌；设置后覆盖配置文件中存储的值。

**notes/**、**training_data/**、**adapters/**
> Markdown 记忆、JSONL 训练语料和 LoRA 适配器权重（worker 位于 **workers/**_role_/ 下）。

# CAVEATS

推理和训练目前要求 **Apple Silicon + MLX**；CUDA/llama.cpp 后端属于路线图规划，并非生产默认项。shell/Python 沙箱是在你的用户权限下尽力而为的保护。Telegram 和浏览器功能需要额外配置，危险操作需显式批准。模型下载和 LoRA 训练非常消耗资源。

# HISTORY

**Symbio** 是一个开源本地智能体（Apache-2.0），专注于无需云订阅的、由纠错驱动的 LoRA 个性化。上游地址：**github.com/huyedits/Symbio**。

# SEE ALSO

[ollama](/man/ollama)(1), [pipx](/man/pipx)(1), [python](/man/python)(1), [claude](/man/claude)(1)

# RESOURCES

```[Source code](https://github.com/huyedits/Symbio)```

```[Homepage](https://huggingface.co/spaces/HuyEdits/symbio-demo)```

<!-- verified: 2026-08-02 -->
