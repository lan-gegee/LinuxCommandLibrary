# TAGLINE

面向大语言模型和多模态模型的低比特量化工具包

# TLDR

使用默认配方**量化模型**

```auto-round --model [Qwen/Qwen3-0.6B] --scheme "[W4A16]" --format "[auto_round]"```

**使用 best 配方**（更慢，精度更高）

```auto-round-best --model [model_id] --scheme "[W4A16]"```

**使用 light 配方**（更快）

```auto-round-light --model [model_id] --scheme "[W4A16]"```

**量化为 4-bit** 并以多种格式导出

```auto-round --model [model_id] --bits 4 --group_size 128 --format "[auto_round,auto_awq,auto_gptq]" --output_dir [path/to/output]```

无需校准的 RTN 模式

```auto-round --model [model_id] --bits 4 --iters 0```

**多 GPU** 量化

```auto-round --model [model_id] --device_map "[0,1,2,3]"```

**评估**已量化的模型

```auto-round --model [path/to/quantized] --eval --tasks [mmlu,lambada_openai]```

# SYNOPSIS

**auto-round** **--model** _MODEL_ [_options_]

**auto-round-best** **--model** _MODEL_ [_options_]

**auto-round-light** **--model** _MODEL_ [_options_]

# DESCRIPTION

**auto-round** 是由 **Intel** 开发的面向 **LLM** 和 **VLM** 的仅权重量化训练后（PTQ）工具包。它采用符号梯度下降联合优化权重取整和裁剪范围，能在超低比特宽度（低至 2 bit）下以极短的校准时间获得高精度。

该工具包支持 CPU、Intel GPU（XPU）、HPU 和 CUDA 后端，并可导出为多种流行的量化格式，包括 **auto_round**、**auto_awq**、**auto_gptq** 和 **gguf**，因此模型可以通过 Transformers、vLLM、SGLang 或 llm-compressor 直接服务，无需重新量化。

提供三种配方：**auto-round**（默认均衡）、**auto-round-best**（最慢、精度最高，慢 4–5 倍）和 **auto-round-light**（最快，提速 2–3 倍）。

# PARAMETERS

**--model** _MODEL_
> 模型标识符或本地路径（如 _Qwen/Qwen3-0.6B_）。

**--scheme** _SCHEME_
> 量化方案，如 _W4A16_、_W2A16_、_W8A16_。

**--bits** _N_
> 权重位宽：2、3、4 或 8。

**--group_size** _N_
> 量化分组大小（如 32、64、128）。

**--format** _FORMAT_
> 导出格式，逗号分隔：_auto_round_、_auto_gptq_、_auto_awq_、_gguf:q4_k_m_ 等。

**--output_dir** _PATH_
> 量化模型的输出目录。

**--dataset** _SPEC_
> 校准数据（本地路径或 HuggingFace 数据集）。支持 _name:num=N_、_:concat=True_、_:apply_chat_template_ 以及逗号分隔列表。

**--iters** _N_
> 调优迭代次数（RTN 为 _0_，默认 _200_，追求最佳精度可达 _1000_）。

**--bs** _N_
> 批大小（默认 8）。

**--seqlen** _N_
> 校准序列长度（默认 2048）。

**--nsamples** _N_
> 校准样本数（默认 128，best 配方最多 512）。

**--lr** _RATE_
> 学习率。

**--device_map** _SPEC_
> GPU 分配，如 _auto_ 或 _0,1,2,3_。

**--low_gpu_mem_usage**
> 以更多时间为代价减少显存占用。

**--enable_torch_compile**
> 使用 **torch.compile**（需要 PyTorch 2.6+）。

**--quant_lm_head**
> 同时量化语言模型头（仅限 auto_round 格式）。

**--adam**
> 用 **AdamW** 优化器替代符号梯度下降。

**--eval**
> 量化后评估模型。

**--eval_backend** _BACKEND_
> 评估引擎，_vllm_ 或默认的 Hugging Face。

**--tasks** _LIST_
> 逗号分隔的 lm-eval-harness 任务（如 _mmlu,lambada_openai_）。

# DESCRIPTION OF FORMATS

**auto_round**
> AutoRound 原生格式，支持 lm-head 量化。

**auto_gptq**
> 兼容 GPTQ 的格式。

**auto_awq**
> 兼容 AWQ 的格式。

**gguf:q4_k_m**, **gguf:q2_k_s**
> 用于 llama.cpp / Ollama 类运行时的 GGUF 格式。

# CAVEATS

校准效果对数据集质量和长度敏感；使用领域不匹配的校准数据可能降低精度。更低的比特宽度（2-3 bit）可能需要 **best** 配方才能恢复精度。某些导出格式会限制功能组合（例如 **--quant_lm_head** 仅支持 auto_round 格式）。

# HISTORY

**AutoRound** 由 **Intel** 作为其 LLM 量化技术栈的一部分推出。它区别于 **GPTQ** 和 **AWQ** 等较早 PTQ 方法的地方在于：用符号梯度下降联合优化取整和裁剪，在保持仅需校准的同时，缩小了低比特宽度下与 QAT 的精度差距。

# SEE ALSO

[python](/man/python)(1), [llama.cpp](/man/llama.cpp)(1)
