# TAGLINE

分布式 PyTorch 训练启动器

# TLDR

以默认配置**启动**训练脚本

```accelerate launch [train.py]```

针对你的硬件**配置** accelerate

```accelerate config```

以**指定 GPU** 配置启动

```accelerate launch --num_processes [4] --gpu_ids [0,1,2,3] [train.py]```

在**多台机器**上启动训练

```accelerate launch --num_machines [2] --machine_rank [0] --main_process_ip [192.168.1.1] [train.py]```

# SYNOPSIS

**accelerate** _command_ [_options_] [_script_] [_script_args_]

# DESCRIPTION

**accelerate** 是 Hugging Face 的库，只需极少的代码改动即可让 PyTorch 代码运行于任意分布式配置。它能处理跨多 GPU、TPU 和多机分布式训练的复杂性，同时保持训练代码简洁。

该工具抽象了混合精度训练、梯度累积和多设备并行所需的样板代码，并能自动检测可用硬件，相应地配置训练环境。

# PARAMETERS

**config**
> 运行配置向导来设置你的环境

**launch**
> 以已配置的设置启动训练脚本

**--num_processes** _n_
> 要启动的进程总数

**--gpu_ids** _ids_
> 以逗号分隔的要使用的 GPU ID

**--mixed_precision** _type_
> 启用混合精度：no、fp16、bf16

**--num_machines** _n_
> 分布式训练使用的机器数量

**--machine_rank** _n_
> 当前机器的序号（从 0 开始）

**--main_process_ip** _ip_
> 主机的 IP 地址

**--main_process_port** _port_
> 主机使用的端口（默认：29500）

**--use_deepspeed**
> 启用 DeepSpeed 进行训练

**--use_fsdp**
> 启用全分片数据并行（Fully Sharded Data Parallel）

**test**
> 测试你的 accelerate 配置

**env**
> 打印环境信息

# CONFIGURATION

运行 **accelerate config** 会在 **~/.cache/huggingface/accelerate/default_config.yaml** 创建一个 YAML 配置文件。该文件保存计算环境类型、分布式训练后端、进程数量、混合精度模式以及 DeepSpeed/FSDP 选项等设置。也可以按项目指定配置：将 **accelerate_config.yaml** 放入项目目录，或在 launch 命令中传入 **--config_file**。

# CAVEATS

需要已安装 PyTorch。配置应与实际硬件匹配；不匹配可能导致静默失败或崩溃。DeepSpeed 和 FSDP 有额外依赖。部分功能需要特定的 GPU 架构（例如 bf16 需要 Ampere 或更新的架构）。

# HISTORY

**accelerate** 由 Hugging Face 开发，首次发布于 **2021** 年。它的诞生是为了简化分布式训练和混合精度工作流程，降低在多样化硬件配置上训练大模型的门槛。

# SEE ALSO

[python](/man/python)(1), [torchrun](/man/torchrun)(1)

# RESOURCES

```[Source code](https://github.com/huggingface/accelerate)```

```[Documentation](https://huggingface.co/docs/accelerate)```

<!-- verified: 2026-06-10 -->
