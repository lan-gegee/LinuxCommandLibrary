# TAGLINE

原生构建于 Apple MLX 框架之上的 Flux 图像生成工具

# TLDR

**根据文本提示词生成图像**

```mflux-generate --model [schnell] --prompt "[a sunset over mountains]"```

**使用更高质量的 dev 模型和更多步数生成**

```mflux-generate --model [dev] --prompt "[prompt]" --steps [25] --seed [42]```

**指定图像尺寸**

```mflux-generate --model [schnell] --prompt "[prompt]" --width [1024] --height [768]```

**保存到指定的输出路径**

```mflux-generate --model [schnell] --prompt "[prompt]" --output [output.png]```

**使用量化模型以降低内存占用**

```mflux-generate --model [schnell] --prompt "[prompt]" --quantize [8]```

**使用初始图像进行图生图**

```mflux-generate --model [dev] --prompt "[prompt]" --image-path [input.png] --image-strength [0.4]```

**应用 LoRA 适配器权重**

```mflux-generate --model [dev] --prompt "[prompt]" --lora-paths [adapter.safetensors]```

**在本地保存一份量化的模型权重副本**

```mflux-save --model [schnell] --quantize [8] --path [path/to/save]```

# SYNOPSIS

**mflux-generate** **--model** _name_ **--prompt** _text_ [_options_]

**mflux-save** **--model** _name_ **--path** _dir_ [_options_]

# PARAMETERS

**--model**, **-m** _NAME_
> 要使用的模型（schnell、dev，或 HuggingFace 仓库/本地路径）。

**--prompt** _TEXT_
> 用于图像生成的文本提示词。使用 - 从标准输入读取。

**--output** _FILE_
> 输出图像路径。

**--width** _PX_
> 图像宽度（像素）。

**--height** _PX_
> 图像高度（像素）。

**--steps** _N_
> 推理步数。

**--seed** _INT_
> 用于可复现性的随机种子。

**--quantize**, **-q** _BITS_
> 量化级别（4 位或 8 位）。

**--guidance** _FLOAT_
> 引导系数（guidance scale）。

**--negative-prompt** _TEXT_
> 描述模型不应生成内容的文本提示词。

**--image-path** _FILE_
> 用于图生图生成的初始图像路径。

**--image-strength** _FLOAT_
> 初始图像对输出的影响强度（默认：0.4，0.0 = 无影响）。

**--lora-paths** _FILE_...
> 一个或多个 LoRA 适配器权重的路径。

**--lora-scales** _FLOAT_...
> 每个 LoRA 适配器的缩放系数。

**--metadata**
> 在图像旁导出一个包含生成元数据的 JSON 文件。

**--low-ram**
> 通过限制 MLX 缓存并在使用后释放组件来降低 GPU 内存占用。

**--base-model** _NAME_
> 从本地路径加载时指定架构（schnell、dev）。

# DESCRIPTION

**mflux** 是一个原生构建于 Apple **MLX** 框架之上的 Flux 图像生成工具，针对 Apple Silicon（M1/M2/M3/M4）优化。它使用 Flux 模型在本地生成图像，无需 GPU 服务器或云端 API。该软件包提供多个 CLI 命令：用于图像生成的 **mflux-generate**、用于在本地保存量化模型权重的 **mflux-save**，以及用于查看图像元数据的 **mflux-info**。

通过 pip 安装（`pip install mflux`）。模型权重在首次使用时从 HuggingFace 下载并缓存在本地。自定义模型也可以从本地路径或 HuggingFace 仓库加载。

**schnell** 更快且所需步数少（2-4 步）。**dev** 质量更高但需要更多步数（20-25 步）。量化（4 位或 8 位）可降低统一内存有限的机器的内存占用。**--low-ram** 标志通过在使用后释放组件进一步降低内存占用。

LoRA 适配器允许在基础模型之上应用经过微调的风格和概念。图生图生成可通过 **--image-path** 和 **--image-strength** 支持。

# CAVEATS

仅支持 Apple Silicon（M 系列 Mac）。需要 Python 3.10 及以上版本。模型下载数 GB。内存占用取决于模型和量化级别。**--low-ram** 标志有助于在内存受限的系统上运行，但会将生成限制为单张图像。

# HISTORY

**mflux** 由 **Filip Strand** 于 **2024 年**创建，旨在借助 MLX 框架为 Apple Silicon 带来原生的 Flux 图像生成能力。此后它扩展到支持 Flux 之外的多种模型架构，包括从 HuggingFace 仓库和本地路径加载的模型。

# SEE ALSO

[sd-cli](/man/sd-cli)(1), [comfyui](/man/comfyui)(1)
