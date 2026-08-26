# TAGLINE

面向 Slurm 的 OCI 容器运行时代理

# TLDR

**创建**新容器

```scrun create container_id```

**启动**容器

```scrun start container_id```

查询容器**状态**

```scrun state container_id```

**终止**容器（发送 SIGTERM）

```scrun kill container_id```

用**指定信号**终止

```scrun kill container_id SIGKILL```

**删除**容器

```scrun delete container_id```

启用**调试**日志

```scrun create container_id --debug```

# SYNOPSIS

**scrun** _command_ _container_id_ [_options_]

# PARAMETERS

**create**
> 创建新容器

**start**
> 启动已创建的容器

**state**
> 查询容器状态

**kill** [_signal_]
> 向容器发送信号

**delete**
> 删除容器并释放资源

**--debug**
> 启用调试日志

# DESCRIPTION

**scrun** 是面向 Slurm 的 OCI 运行时代理，以作业的形式运行容器。它允许容器编排系统将容器工作负载提交到 Slurm 集群。

容器作为 Slurm 作业执行，充分利用集群的资源管理和调度能力。

# CAVEATS

需要配置 Slurm 的容器支持。计算节点必须能够访问容器镜像。

# HISTORY

属于 **Slurm** 工作负载管理器，为 HPC 集群环境提供容器集成能力。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[srun](/man/srun)(1), [sbatch](/man/sbatch)(1), [podman](/man/podman)(1)
