# TAGLINE

对能在你的硬件上流畅运行的本地 LLM 进行排名

# TLDR

**检测硬件并列出**最适合的本地模型

```whichllm```

**仅显示检测到的硬件**

```whichllm hardware```

**将排名限制在仅用 CPU** 的机器上

```whichllm --cpu-only```

**模拟特定 GPU** 以便规划购买

```whichllm --gpu "[RTX 4090]"```

**反向规划**：运行给定模型需要什么 GPU

```whichllm plan [model_name]```

**下载模型并交互式对话**

```whichllm run [model_name]```

**打印使用模型的 Python 代码片段**

```whichllm snippet [model_name]```

**输出 JSON** 供脚本使用

```whichllm --json```

# SYNOPSIS

**whichllm** [_command_] [_options_]

# PARAMETERS

**hardware**
> 打印检测到的 GPU、CPU、内存、操作系统信息，不对模型排名。

**run** _model_
> 通过 Ollama 下载 _model_ 并启动交互式聊天会话。

**plan** _model_
> 反向查询：估算以可用速度运行 _model_ 需要哪一档 GPU 或内存。

**snippet** _model_
> 打印一段可直接粘贴的 Python 代码，用于从 HuggingFace 或 Ollama 加载 _model_。

**--gpu** _name_
> 覆盖硬件检测，按指定的 GPU（如 "RTX 4090"）进行排名。

**--cpu-only**
> 将排名限制在没有 GPU 也能可接受速度运行的模型。

**--top** _N_
> 显示排名前 _N_ 的模型，而非默认的精简列表。

**--quant** _type_
> 按量化方式过滤结果（如 _Q4_K_M_、_Q5_K_M_、_Q8_0_、_fp16_）。

**--profile** _use_case_
> 使排名偏向特定用途（_coding_ 编程、_vision_ 视觉、_math_ 数学、_general_ 通用）。

**--json**
> 输出机器可读的 JSON 而非格式化表格。

**--refresh**
> 绕过本地缓存并重新拉取基准测试数据。

**--version**
> 打印版本并退出。

**--help**
> 打印帮助并退出。

# DESCRIPTION

**whichllm** 会检测本地硬件（GPU 型号与显存、CPU、内存、操作系统），并对来自 **HuggingFace** 和 **Ollama** 的开放权重大型语言模型进行排名，衡量它们在这台机器上的实际运行效果。它并非只把"能否塞进显存"当作唯一标准，而是将适配性检查与来自 **LiveBench**、**Artificial Analysis**、**Aider** 和 **Chatbot Arena** ELO 排行榜等来源的**考虑时效性的基准测试**分数相结合，并对量化、部分卸载和 MoE 架构施加惩罚。

该工具面向常见的实际问题——"今晚该下载哪个模型"，而不是营销宣传。默认调用会打印一个简短的排名表；子命令扩展了同一引擎，可用于启动交互式会话、规划硬件升级，或输出便于直接集成的代码片段。

# CONFIGURATION

**~/.cache/whichllm/**
> 缓存的基准测试快照；可通过 **--refresh** 清除。

**Ollama**
> 如果存在，**whichllm run** 会把模型下载与服务交给本地 Ollama 守护进程处理。

# CAVEATS

排名依赖第三方基准测试；新模型会在其分数稳定之前出现，如果缺少近期发布的模型请使用 **--refresh**。硬件检测在 NVIDIA、AMD 和 Apple Silicon 上效果最佳；特殊加速器可能会退回到仅 CPU 的估算。该工具只推荐模型——它不会对建议的权重强制执行许可约束。

# HISTORY

**whichllm** 由 **Andyyyy64** 于 **2025 年**发布，是一个通过 **uv**、**pip** 和 **Homebrew** 分发的 Python 工具。它的诞生源于本地 LLM 生态在 HuggingFace、Ollama 和数十种量化格式之间的碎片化，彼时仅仅查看显存大小已不足以挑选出可用的模型。截至 **v0.5.x**（2026 年），该项目仍在持续跟踪新发布和基准测试更新。

# INSTALL

```nix: nix profile install nixpkgs#whichllm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ollama](/man/ollama)(1), [llm](/man/llm)(1), [huggingface-cli](/man/huggingface-cli)(1)
