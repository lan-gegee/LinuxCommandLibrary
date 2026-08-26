# TAGLINE

用 C/CUDA 从零训练并运行 GPT-2 规模的语言模型

# TLDR

**训练**小型 CPU 演示模型（约 100 万参数）

```nanoeuler train```

**训练**较大的 CPU 模型（约 1000 万参数）

```nanoeuler train big```

在终端 REPL 中与训练好的 checkpoint **对话**

```nanoeuler chat```

通过梯度检查**验证**手写的反向传播

```make check```

从零开始**预训练**约 116M 参数的 GPU 模型

```./nanoeuler_cuda t```

# SYNOPSIS

**nanoeuler** _subcommand_ [_options_]

# PARAMETERS

**train** [_big_]
> 在 CPU 上运行训练循环。不带参数时训练小型演示模型；**big** 选择面向 GPU 级硬件的较大配置。

**chat**
> 启动交互式 REPL：输入提示词，模型会根据 **nanoeuler.bin** 或 **nanoeuler_chat.bin** 续写。

**make check**
> 构建并运行双精度梯度检查，将每个解析反向传播与有限差分结果进行比对验证。

**./nanoeuler_cuda t**
> 预训练完整的 GPU 流水线（约 116M 参数），每 5000 步保存一次 checkpoint 到 **nanoeuler.bin**。

**./nanoeuler_cuda tr**
> 从最新的 checkpoint 恢复 GPU 预训练。

**./nanoeuler_cuda s**
> 在 Alpaca 指令数据上对预训练基础模型进行监督微调；输出 **nanoeuler_chat.bin**。

**./nanoeuler_cuda c**
> 在 GPU 上与微调后的模型交互式对话。

**./nanoeuler_cuda i** _"prompt"_
> 在 GPU 上执行一次性自回归生成。

# DESCRIPTION

**nanoeuler** 是一个完全用 **C** 和 **CUDA** 从零构建的 **GPT-2 级仅解码器 transformer**——不用 PyTorch、不用自动微分、不用任何机器学习框架。前向和反向传播均为手写并经过验证。项目包含字节级 **BPE 分词器**、基于书籍和网络语料库的完整**预训练**流水线，以及将模型**监督微调**为聊天助手的过程。

CPU 二进制文件（**nanoeuler.c**）是面向小模型的独立演示。CUDA 引擎（**cuda/nanoeuler_cuda.cu**）增加了 **cuBLAS** 矩阵乘法和手写的 **FlashAttention**，可在单张消费级 GPU 上训练 **约 116M 参数**的模型。架构模块遵循现代实践：**RMSNorm**、**RoPE**、**SwiGLU** 前馈层、**分组查询注意力**和**多 token 预测**头。

名称源自残差网络的**前向欧拉（forward-Euler）**视角：每个块 **x = x + f(x)** 就是微分方程 **dx/dt = f(x)** 的一次积分步骤。这是一个研究与教学性质的成果——在这个规模下，模型只能生成看起来流畅但缺乏真实世界知识的英语文本，并非能力完备的助手。

# CAVEATS

GPU 训练需要 **NVIDIA GPU**、**nvcc** 和 **cuBLAS**；构建默认针对 **sm_89**（RTX 40 系列）。数据脚本会从 Project Gutenberg 和 Hugging Face 下载大型语料库。聊天模型用于展示预训练→SFT 流水线；质量高度依赖算力和数据规模。**DPO** 对齐已在计划中但尚未实现。

# HISTORY

由 **JustVugg** 创建，是一个公开的从零实现 LLM 的工程项目，展示了端到端训练过程——使用手动推导的梯度和完整、可审计的代码库，而非框架抽象。

# SEE ALSO

[make](/man/make)(1), [nvcc](/man/nvcc)(1), [python](/man/python)(1)

# RESOURCES

```[Source code](https://github.com/JustVugg/nanoeuler)```

<!-- verified: 2026-07-11 -->
