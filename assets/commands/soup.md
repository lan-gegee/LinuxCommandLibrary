# TAGLINE

从一个 YAML 配置对大语言模型进行微调与后训练

# TLDR

**安装**轻量版 CLI（不含 PyTorch）或完整训练套件

```pip install soup-cli```

```pip install "soup-cli[train]"```

从**模板**创建配置

```soup init --template chat```

根据 YAML 配置**训练**

```soup train --config soup.yaml```

与微调后的模型或适配器**对话**

```soup chat --model ./output```

运行**批量推理**

```soup infer --model ./output --input prompts.jsonl```

**导出**为 GGUF 以供 Ollama / llama.cpp 使用

```soup export --model ./output --format gguf --quant q4_k_m```

启动 **OpenAI 兼容**服务器

```soup serve --model ./output --port 8000```

检查 GPU、依赖和环境

```soup doctor```

# SYNOPSIS

**soup** [_global-options_] _command_ [_args_]

# PARAMETERS

**init** [**--template** _name_]
> 以交互方式或基于模板（**chat**、**code**、**tool-calling**、**medical**、**reasoning**、**vision**、合规模板如 **hipaa** / **soc2** 等）创建 **soup.yaml** 配置。

**train** **--config** _file_
> 根据 YAML 运行监督微调或偏好微调（SFT、DPO、KTO、ORPO、SimPO、GRPO、PPO 等）。安装 **[train]** 附加组件后可处理 LoRA/QLoRA、批大小、量化和多 GPU。可选的层流式加载（**stream_layers: true**）可将冻结的基础模型移出显存，适合小显存 GPU。

**chat** **--model** _path_
> 与本地模型或适配器目录进行交互式对话。

**infer** **--model** _path_ **--input** _file_
> 对提示词进行批量推理（JSONL 及相关格式）。

**serve** **--model** _path_ [**--port** _n_] [**--backend** _name_]
> 提供 OpenAI 兼容的 HTTP API（可选后端包括 **vllm**、**sglang**）。

**merge** **--adapter** _path_
> 将 LoRA 适配器合并进基础模型权重。

**export** **--model** _path_ **--format** _fmt_
> 导出以便部署（**gguf**、**onnx**、**tensorrt**、**awq**、**gptq** 等）。

**push** **--model** _path_ **--repo** _user/name_
> 将模型或适配器上传到 Hugging Face Hub。

**data** _subcommand_ ...
> 数据集工具：**inspect**、**validate**、**convert**、**dedup**、**split**、**generate**、**forge**，以及许多质量 / PII / 污染检测辅助命令。

**eval** _subcommand_ ...
> 评估：基准测试、自定义 JSONL 任务、LLM 作为裁判（LLM-as-judge）、门禁和对比。

**ship** **--base** _model_ **--adapter** _path_ **--task-eval** _file_
> 输出 SHIP / DON'T-SHIP 门禁判定（任务胜出率加回归测试套件）。退出码：**0** 可发布，**2** 不发布，**3** 参数错误，**1** 运行时错误。

**doctor**
> 诊断 GPU、驱动、Python 软件包和环境。

**recipes** **list**|**show**|**use**|**search**
> 浏览并生成现成的训练配方。

**version** [**--full**] [**--json**]
> 打印已安装的 Soup 版本。

**--log-level** **quiet**|**normal**|**verbose**|**debug**
> 全局日志详细程度（Rich 格式化输出）。

# DESCRIPTION

**soup** 是 **Soup** 的命令行界面（PyPI 包名为 **soup-cli**）：一个 Python 工具包，将 LLM 微调简化为一个配置文件加几个子命令。你在 **soup.yaml** 中描述基础模型、数据、任务类型和训练参数，然后运行 **soup train**。同一个二进制文件还涵盖数据准备、评估、导出、本地服务、适配器管理和发布门禁。

默认的 **pip install soup-cli** 刻意保持轻量（仅包含 CLI、配置和数据工具，不含 PyTorch）。微调需要 **pip install "soup-cli[train]"**（或使用 **[all]** 安装全部可选组件）。训练可在 CUDA GPU、Apple Silicon（MPS）上运行，也可用 CPU 做冒烟测试；可选附加组件启用 Unsloth、MLX、服务后端、UI 等。

支持的数据格式包括 Alpaca、ShareGPT、ChatML、偏好对（DPO 风格）、KTO、视觉、音频和预训练文本。模型通过 Hugging Face **AutoModelForCausalLM** 加载，因此 Hub 上大多数文本生成检查点无需自定义胶水代码即可使用。

# CONFIGURATION

主要文件：**soup.yaml**（路径通过 **--config** 传入）。核心字段包括 **base**（模型 ID 或路径）、**task**（例如 **sft**）、**data.train** / format / split、**training**（轮数、学习率、LoRA、量化、可选 **stream_layers**）以及 **output**。Schema 详情见项目文档中的 **docs/** 目录和 **config/schema.py**。

# CAVEATS

微调需要大量磁盘和内存，最好有 GPU；在不使用层流式加载的情况下，8B QLoRA 训练通常需要约 8 GB 以上显存。未安装 **[train]** 附加组件前，纯 **soup-cli** 无法训练。层流式加载仍标记为 BETA。在会把 **[train]** 当作通配符展开的 Shell 中，建议给附加组件加双引号（**pip install "soup-cli[train]"**）。部分高级命令需要可选附加组件（**[serve]**、**[ui]**、**[mcp]** 等）。

# HISTORY

**Soup** 是一个 Apache-2.0 开源项目，在 PyPI 上以 **soup-cli** 维护。近期版本专注于低显存训练（让 8B 模型在约 4 GB 显存的笔记本 GPU 上训练）、在此路径上的偏好训练损失函数，以及用于 CI 的发布 / 评估门禁。

# SEE ALSO

[ollama](/man/ollama)(1), [llama](/man/llama)(1), [huggingface-cli](/man/huggingface-cli)(1), [pip](/man/pip)(1)

# RESOURCES

```[Source code](https://github.com/MakazhanAlpamys/Soup)```

```[Homepage](https://trysoup.dev)```

```[Documentation](https://github.com/MakazhanAlpamys/Soup/tree/main/docs)```

<!-- verified: 2026-08-04 -->
