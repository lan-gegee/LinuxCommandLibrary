# TAGLINE

DwarfStar 的 prefill 与生成速度基准测试

# TLDR

**在多个上下文边界上扫测 prefill/生成速度**

```ds4-bench --prompt-file [long.txt] --ctx-max [32768]```

**将结果写为 CSV**

```ds4-bench --prompt-file [long.txt] --ctx-max [32768] --csv [speed.csv]```

**仅测 prefill**（不生成 token）

```ds4-bench --prompt-file [long.txt] --gen-tokens [0]```

**在降低 GPU 功率下测量**

```ds4-bench --prompt-file [long.txt] --power [70]```

**对聊天渲染的提示词进行基准测试**

```ds4-bench --chat-prompt-file [prompt.txt] --ctx-max [16384]```

在内存受限机器上运行 **SSD 流式模型**

```ds4-bench -m [ds4flash.gguf] --ssd-streaming --prompt-file [long.txt]```

# SYNOPSIS

**ds4-bench** [_options_]

# PARAMETERS

**-m**, **--model** _FILE_
> GGUF 模型路径。默认：**ds4flash.gguf**。

**--prompt-file** _FILE_
> 用于基准测试的原始文本；token 序列会在每个测量边界处切片。

**--chat-prompt-file** _FILE_
> 将 _FILE_ 渲染为一条无思考模式的聊天用户消息，而非原始文本。

**-sys**, **--system** _TEXT_
> 系统提示词，仅在配合 **--chat-prompt-file** 时使用。

**--ctx-start** _N_
> 首个测量上下文边界。默认：**2048**。

**--ctx-max** _N_
> 最后一个测量上下文边界。默认：**32768**。

**--ctx-alloc** _N_
> 分配的上下文大小。默认：**ctx-max + gen-tokens + 1**。

**--step-incr** _N_
> 当 **--step-mul** 为 1 时各边界之间的线性步长。默认：**2048**。

**--step-mul** _F_
> 各边界之间的乘性步长。默认：**1**（线性）。

**--gen-tokens** _N_
> 每个边界的贪心解码 token 数。**0** 表示纯 prefill。默认：**128**。

**--csv** _FILE_
> 将 CSV 写入 _FILE_ 而非标准输出。

**--power** _N_
> GPU 占空比目标，取值 1 到 100。

**--metal** | **--cuda** | **--rocm** | **--cpu**
> 显式选择推理后端。

**--ssd-streaming**
> 本次基准运行启用基于 SSD 的模型流式读取。

# DESCRIPTION

**ds4-bench** 测量 **DwarfStar**（**ds4**）推理引擎在一系列上下文长度下的 prefill 和生成吞吐。你提供一个长提示词文件；工具先将其分词一次，然后在每个边界处运行 prefill（及可选的贪心解码），让你可以对比上下文增大时的 tokens/s。

它是该项目在 Metal、CUDA 和 ROCm 路径上的标准速度基准入口，也用于比较完整驻留与 **--ssd-streaming** 两种配置。结果可打印到终端，或写成 CSV 以便在 **speed-bench/** 工作流中绘图和跟踪回归。

# CAVEATS

需要 DwarfStar 兼容的 GGUF 以及足够的内存（或 SSD 带宽）来支撑所选的 **--ctx-alloc**。计时结果高度依赖后端、功率限制、散热状态以及专家缓存的冷热；单次运行只能作参考，不能当作跨硬件的绝对排名。纯 prefill 模式（**--gen-tokens 0**）不会经过解码路径。

# HISTORY

**ds4-bench** 是 **Salvatore Sanfilippo**（**antirez**）及其他贡献者的 **DwarfStar** 工具集的一部分，用于把关大型 MoE 模型（DeepSeek V4 Flash/PRO 及实验分支）的性能工作——这类模型的长上下文 prefill 成本占主导地位。

# SEE ALSO

[ds4-server](/man/ds4-server)(1), [ds4-eval](/man/ds4-eval)(1), [ds4-agent](/man/ds4-agent)(1), [llama-cli](/man/llama-cli)(1)

# RESOURCES

```[Source code](https://github.com/antirez/ds4)```

```[Documentation](https://github.com/antirez/ds4/tree/main/speed-bench)```

<!-- verified: 2026-07-18 -->
