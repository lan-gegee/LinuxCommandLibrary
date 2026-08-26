# TAGLINE

附加到正在运行的 Slurm 作业步骤

# TLDR

**附加**到某个作业步骤

```sattach jobid.stepid```

为特定任务附加**输入过滤器**

```sattach --input-filter 0 jobid.stepid```

为特定任务附加**输出过滤器**

```sattach --output-filter 0 jobid.stepid```

为特定任务附加**错误过滤器**

```sattach --error-filter 0 jobid.stepid```

# SYNOPSIS

**sattach** [_options_] _jobid.stepid_

# DESCRIPTION

**sattach** 附加到 Slurm 作业步骤的输入/输出流，让你能够与正在运行的作业交互。它将 Slurm 作业步骤的 stdout、stderr 和 stdin 重定向到当前终端。

# PARAMETERS

**jobid.stepid**
> 要附加到的作业 ID 和步骤 ID（格式：jobid.stepid）

**--input-filter TASK**
> 将当前控制台的输入作为指定任务的 stdin

**--output-filter TASK**
> 只重定向指定任务的 stdout

**--error-filter TASK**
> 只重定向指定任务的 stderr

**-l, --label**
> 在输出的每行前面加上任务编号

**-Q, --quiet**
> 抑制提示性消息

**-v, --verbose**
> 增加消息的详细程度

**--pty**
> 在伪终端中执行任务零。与过滤选项不兼容

**--layout**
> 打印任务布局信息后退出，不进行附加

**-V, --version**
> 显示 Slurm 版本号并退出

# CAVEATS

只有作业所有者才能附加到作业步骤。作业必须处于运行状态。并非所有 MPI 实现都支持附加。

# HISTORY

**sattach** 属于 **Slurm** 工作负载管理器，为 HPC 集群提供作业调度和资源管理。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[srun](/man/srun)(1), [sbatch](/man/sbatch)(1), [squeue](/man/squeue)(1), [scontrol](/man/scontrol)(1), [scancel](/man/scancel)(1)
