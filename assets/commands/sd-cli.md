# TAGLINE

Stable Diffusion 图像生成 CLI

# TLDR

**从文本提示词生成图像**

```sd-cli -m [model.safetensors] -p "[a photo of a cat]" -o [output.png]```

**以指定尺寸生成**

```sd-cli -m [model.safetensors] -p "[prompt]" --width [512] --height [512] -o [output.png]```

**设置生成参数**

```sd-cli -m [model.safetensors] -p "[prompt]" --steps [20] --cfg-scale [7.0] --seed [42] -o [output.png]```

**使用指定的采样方法**

```sd-cli -m [model.safetensors] -p "[prompt]" --sampling-method [euler_a] -o [output.png]```

**使用负向提示词生成**

```sd-cli -m [model.safetensors] -p "[prompt]" -n "[blurry, low quality]" -o [output.png]```

**图生图（img2img）**

```sd-cli -m [model.safetensors] --img2img [input.png] -p "[oil painting style]" --strength [0.75] -o [output.png]```

# SYNOPSIS

**sd-cli** **-m** _model_ **-p** _prompt_ [_options_] **-o** _output_

# PARAMETERS

**-m**, **--model** _FILE_
> 模型权重路径（.safetensors 或 .gguf）。

**-p**, **--prompt** _TEXT_
> 用于图像生成的文本提示词。

**-n**, **--negative-prompt** _TEXT_
> 引导模型避开的负向提示词。

**-o**, **--output** _FILE_
> 输出图像路径。

**--steps** _N_
> 采样步数（默认：20）。

**--cfg-scale** _FLOAT_
> Classifier-free guidance 强度（默认：7.0）。

**--seed** _INT_
> 随机数种子（-1 表示随机）。

**--width** _PX_
> 图像宽度（像素）。

**--height** _PX_
> 图像高度（像素）。

**--sampling-method** _METHOD_
> 采样方法：euler、euler_a、heun、dpm2、dpm++2s_a、dpm++2m、dpm++2mv2、lcm。

**--img2img** _FILE_
> 用于图生图的输入图像。

**--strength** _FLOAT_
> img2img 的去噪强度（0.0-1.0）。

**--threads** _N_
> CPU 线程数量。

**--rng** _TYPE_
> 随机数生成器类型：std_default、cuda。

# DESCRIPTION

**sd-cli** 是 **stable-diffusion.cpp** 的命令行界面，后者是基于 ggml 张量库的轻量级 Stable Diffusion C/C++ 实现。它可以在 CPU 和 GPU 上运行图像生成模型，无需 Python 或重量级的机器学习框架。

该工具支持 Stable Diffusion 1.x、2.x、SDXL 和 Flux 模型架构。safetensors 或 gguf（量化）格式的模型可以直接加载。量化模型能显著降低内存占用，同时保持合理的质量。

文生图根据提示词生成图像；图生图在提示词的引导下转换已有图像。strength 参数控制对原始图像的改动程度。

使用 CMake 从源码构建。可通过 CUDA、Metal 和 Vulkan 后端获得 GPU 加速。

# CAVEATS

必须从源码构建。需要大型模型文件（数 GB）。质量取决于模型选择和参数。GPU 加速需要针对特定后端的构建标志。SDXL 和 Flux 模型比 SD 1.x 需要更多内存。

# HISTORY

**stable-diffusion.cpp** 由 **leejet** 于 **2023 年**创建，其灵感来自 llama.cpp 以最少依赖将机器学习模型带入 C/C++ 的做法。它让 Stable Diffusion 推理得以运行在资源受限的环境和不支持 Python 的平台上。

# INSTALL

```aur: yay -S sd-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mflux](/man/mflux)(1), [comfyui](/man/comfyui)(1), [convert](/man/convert)(1)
