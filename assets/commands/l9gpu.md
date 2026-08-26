# TAGLINE

具备 Kubernetes 与 Slurm 工作负载归因能力的 GPU 可观测性代理

# TLDR

**安装** Python 软件包

```pip install l9gpu```

**监控 NVIDIA GPU** 并输出 OTLP 遥测数据

```l9gpu nvml_monitor --sink otel --cluster my-cluster```

不发送数据的**快速测试**

```l9gpu nvml_monitor --sink stdout --once```

**监控 AMD GPU**

```l9gpu amd_monitor --sink otel --cluster my-cluster```

**监控 Intel Gaudi**

```l9gpu gaudi_monitor --sink otel --cluster my-cluster```

通过 systemd **运行**或以 Kubernetes DaemonSet 方式部署（参见 Helm）

# SYNOPSIS

**l9gpu** _subcommand_ [options]

常用子命令：nvml_monitor、amd_monitor、gaudi_monitor、slurm_monitor 等。

# DESCRIPTION

**l9gpu** 是 Last9 GPU Telemetry 的核心 CLI。它以单节点代理的形式运行，从 GPU 收集硬件指标（NVML、amdsmi、hl-smi），为其附加来自 Kubernetes 或 Slurm 的工作负载上下文，然后导出标准的 OpenTelemetry（OTLP）指标和日志。

由此无需构建定制管道，即可实现按 Pod、按作业、按用户的 GPU 用量核算。它支持 NVIDIA、AMD 和 Intel Gaudi GPU，并可与任何兼容 OTLP 的后端集成。

该软件包还提供相关的健康检查工具。

# PARAMETERS

**--sink** _otel|stdout|file_

> 遥测数据的输出目标（生产环境推荐 otel）。

**--cluster** _name_

> 附加到输出数据上的集群标识符。

**--once**

> 仅运行一个采集周期后退出（适合测试）。

其他选项和子命令可通过 `l9gpu --help` 查看。

也可以通过 TOML 文件提供配置。

# CAVEATS

需要相应的厂商库或工具（如 NVIDIA 的 NVML），并要求 Python 3.10+。主要面向集群运维人员，无法替代 DCGM 或功能完备的 Prometheus 导出器。它输出 OTLP；下游通常由采集器负责存储与可视化。

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1)

# RESOURCES

```[Source code](https://github.com/last9/gpu-telemetry)```

```[Homepage](https://last9.io/gpu-observability/)```

```[Documentation](https://last9.io/docs/)```

<!-- verified: 2026-07-11 -->
