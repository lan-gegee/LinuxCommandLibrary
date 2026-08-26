# TAGLINE

PyTorch 分布式训练启动器

# TLDR

在单节点 4 GPU 上**运行分布式训练**

```torchrun --standalone --nproc_per_node=4 [train.py]```

使用 2 个节点、每节点 4 GPU **运行多节点训练**

```torchrun --nnodes=2 --nproc_per_node=4 --rdzv_endpoint=[master_ip:29500] [train.py]```

以指定的 rendezvous 后端**运行**

```torchrun --nnodes=2 --nproc_per_node=4 --rdzv_backend=c10d --rdzv_endpoint=[master_ip:29500] [train.py]```

以支持重启的容错模式**运行**

```torchrun --nnodes=2 --nproc_per_node=4 --max_restarts=3 --rdzv_endpoint=[master_ip:29500] [train.py]```

**运行单 GPU 训练**（等同于普通 python）

```torchrun --standalone --nproc_per_node=1 [train.py]```

# SYNOPSIS

**torchrun** [**--nnodes** _N_] [**--nproc_per_node** _N_] [**--rdzv_backend** _backend_] [**--rdzv_endpoint** _host:port_] [**--standalone**] _script.py_ [_script_args_]

# PARAMETERS

**--nnodes** _min_:max_ or _N_
> 参与训练的节点数量。弹性训练时可指定范围。

**--nproc_per_node** _N_
> 每个节点要派生的进程数。通常等于 GPU 数量。

**--standalone**
> 单节点模式，无需外部 rendezvous。自动建立本地 rendezvous。

**--rdzv_backend** _backend_
> Rendezvous 后端：c10d（默认）、etcd、etcd-v2 或 static。

**--rdzv_endpoint** _host:port_
> Rendezvous 端点地址。对于 c10d，即主节点的 IP 和端口。

**--rdzv_id** _id_
> 用户定义的 rendezvous 组 ID。所有节点必须使用相同的 ID。

**--max_restarts** _N_
> 工作组失败后重启的最大次数。默认为 0。

**--node_rank** _N_
> 本节点的编号（用于静态 rendezvous）。

**--master_addr** _addr_
> 主节点地址（旧式用法，请改用 --rdzv_endpoint）。

**--master_port** _port_
> 主节点端口（旧式用法，请改用 --rdzv_endpoint）。

**--local-addr** _addr_
> 要绑定的本地地址。默认为 localhost。

**--redirects** _N_
> 将每个工作进程的 stdout 和 stderr 重定向到日志文件。格式：0:1,1:2 表示将工作进程 0 的 stdout 重定向到文件 1，依此类推。

**--tee** _N_
> 将 stdout/stderr 同时输出到控制台和日志文件。格式与 --redirects 相同。

**--log-dir** _dir_
> 使用 --redirects 或 --tee 时日志文件的存放目录。

# DESCRIPTION

**torchrun** 是 PyTorch 的分布式训练启动器，用于取代已弃用的 torch.distributed.launch。它在多个 GPU 和节点上派生进程，为大规模神经网络训练搭建分布式环境。

该启动器支持多种分布式策略，包括数据分布式并行（DDP）、全分片数据并行（FSDP）、张量并行以及混合方案。它会自动设置 RANK、WORLD_SIZE、LOCAL_RANK、MASTER_ADDR 和 MASTER_PORT 等环境变量以支持分布式通信。

单节点多 GPU 训练请使用 **--standalone** 模式。多节点训练时，所有节点必须指定相同的 rendezvous 端点以相互协调。该启动器支持节点数量可动态变化的弹性训练，以及在 worker 失败时自动重启的容错能力。

# CAVEATS

训练脚本必须基于 torch.distributed 编写以处理分布式初始化。GPU 训练时每个节点的进程数不应超过可用 GPU 数量。同一分布式作业中的所有节点必须使用兼容的 PyTorch 版本和 NCCL 配置。网络防火墙必须放行 rendezvous 端口上的通信。

# HISTORY

**torchrun** 作为 TorchElastic 项目的一部分于 **PyTorch 1.10**（2021 年 10 月）引入，取代了较旧的 torch.distributed.launch 模块，旨在提供弹性且容错的分布式训练能力。从 **PyTorch 2.0**（2023 年 3 月）起，命令行参数风格由下划线改为连字符（--local-rank 取代 --local_rank）。

# INSTALL

```apt: sudo apt install python3-torch```

```dnf: sudo dnf install python3-torch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [nvidia-smi](/man/nvidia-smi)(1)
