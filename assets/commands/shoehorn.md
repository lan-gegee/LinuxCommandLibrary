# TAGLINE

量化 GGUF 模型以填满可用 VRAM，然后用 llama.cpp 运行它

# TLDR

将 Hugging Face BF16 GGUF **适配**到本机并对外**提供服务**

```shoehorn fit [unsloth/Qwen3-4B-GGUF] --serve```

**打印**检测到的 GPU 工作集大小（Metal）

```shoehorn vram```

在不写入文件的情况下**预览**每个张量的混合方案

```shoehorn plan -m [model-bf16.gguf] -i [model.imatrix] --ctx [4096] --budget [8GiB]```

按给定内存包络**量化**并写出 GGUF

```shoehorn quantize -m [model-bf16.gguf] -i [model.imatrix] --ctx [4096] --budget [1.75GiB] -o [fitted.gguf]```

通过 llama-server **运行**适配后的模型（**--** 之后的额外参数）

```shoehorn run -m [fitted.gguf] --ctx [4096] -- --port [8080]```

按另一台 Mac 的 RAM 大小计算**预算**

```shoehorn quantize -m [model-bf16.gguf] --target [16GB] -o [fitted.gguf]```

# SYNOPSIS

**shoehorn** **fit** _path_|_owner/repo_|_url_ [**-i** _imatrix_] [fit-flags] [**-o** _out.gguf_] [**--serve**]

**shoehorn** **plan** **-m** _model.gguf_ [**-i** _imatrix_] [fit-flags]

**shoehorn** **quantize** **-m** _model.gguf_ [**-i** _imatrix_] [fit-flags] **-o** _out.gguf_

**shoehorn** **run** **-m** _model.gguf_ [**--ctx** _N_] [**--kv** _type_] [**--** _llama-server-args_...]

**shoehorn** **vram**

# DESCRIPTION

**shoehorn** 对 BF16（或 F16/F32）**GGUF** 进行量化，使权重填满一个内存包络，而不是使用 **Q4_K_M** 这类固定预设。它会从目标 VRAM 中扣除 KV 缓存和估算的计算缓冲区开销，然后求解一个逐张量混合精度分配问题（拉格朗日背包加贪心补足），在给定字节预算下最小化 imatrix 加权误差。编码器由本项目实现；输出是标准 GGUF v3，任何 llama.cpp 构建都可以加载。

**fit** 是一条龙路径：解析本地文件、Hugging Face 仓库 ID 或 URL，把 BF16 GGUF 下载到 **~/.cache/shoehorn**（支持断点续传），获取已发布的 imatrix 或用 **llama-imatrix** 生成一个，求解并写出 **<stem>-fit.gguf**，还可以选择执行 **llama-server**。**plan** 只打印混合方案。**quantize** 写出文件。**run** 执行 **llama-server -m** _model_ **-c** _ctx_ **-ngl 99**。**vram** 打印 Metal 的 **recommendedMaxWorkingSetSize**。

在 Apple Silicon 上默认包络来自 Metal 工作集探测。在其他平台（或要面向另一台机器时）请传入 **--budget** 或 **--target**。推理和 imatrix 生成委托给 **PATH** 上的 **llama.cpp** 工具。

# COMMANDS

**fit** _source_

> 拉取或打开 _source_，取得 imatrix，按包络量化并写出 GGUF。**--serve** 会对结果启动 **llama-server**。

**plan**

> 求解并打印逐张量表、类型汇总、预算利用率和预计 VRAM。不写文件。

**quantize**

> 与 **plan** 相同的求解过程，随后编码并写出 **-o** _out.gguf_。

**run**

> 以完全 GPU 卸载方式执行 **llama-server**。**--** 之后的参数原样透传。

**vram**

> 打印检测到的 Metal 设备及可用工作集大小。探测不可用时打印 **no Metal device found**。

# PARAMETERS

**-m**, **--model** _path_
> 源 GGUF（BF16/F16/F32，或已在进程内解码的已量化文件）。**plan**、**quantize** 和 **run** 必需。

**-i**, **--imatrix** _path_
> 重要性矩阵（旧版二进制格式或 GGUF 格式的 **llama-imatrix** 输出）。若省略，**fit** 可以生成一个；**plan**/**quantize** 会退回到与激活无关的权重并给出警告。

**-o**, **--output** _path_
> 输出 GGUF。**quantize** 必须提供。**fit** 默认写到当前目录下的 **<model-stem>-fit.gguf**。

**--ctx** _N_
> 用于 KV 预算和 **run** 的上下文长度（默认 **8192**）。

**--budget** _size_
> 总内存包络（**18GiB**、**800MB**、**4.5G** 或字节数）。覆盖 Metal 探测结果。

**--target** _size_
> 面向另一台 Mac 的包络，近似为给定 RAM 的 **74%**。与 **--budget** 冲突。

**--kv** _type_
> 用于预算和运行的 KV 缓存类型：**f16**（默认）、**q8_0** 或 **q4_0**。

**--reserve** _size_
> 从包络中扣除的安全余量（默认 **512MiB**，使用 **--calibrate** 时为 **160MiB**）。

**--calibrate**
> 第一次写出后，在 **llama-cli** 中加载模型，读取真实的 KV/计算缓冲区大小，重新求解并重写可复用的张量。

**--exact-errors**
> 对每一行都评分，而不是每张量采样 128 行。

**--serve**
> 配合 **fit** 使用，对写出的文件执行 **llama-server**。

# CAVEATS

Metal VRAM 探测仅限 Apple Silicon；没有可用设备时必须传入 **--budget**（或 **--target**）。**metal** crate 是构建依赖，因此 Linux 上 **cargo install** 可能失败，尽管文档说明 **--budget** 在任何平台都能工作。

从 Hugging Face 拉取时，**fit** 会拒绝分片 GGUF。计算缓冲区项只是启发式估计；**--reserve** 和 **--calibrate** 可以吸收这部分误差。对外服务和自动生成 imatrix 需要 **PATH** 上有 **llama-server** / **llama-imatrix** / **llama-cli**。IQ1 格式未实现（下限为 **IQ2_XXS**）。**token_embd.weight** 和 **output.weight** 的下限为 4 位。

# SEE ALSO

[llama.cpp](/man/llama.cpp)(1), [llama-cli](/man/llama-cli)(1), [auto-round](/man/auto-round)(1), [ollama](/man/ollama)(1)

# RESOURCES

```[Source code](https://github.com/notactuallytreyanastasio/shoehorn)```

<!-- verified: 2026-08-14 -->
