# TAGLINE

对 Proxmox 主机性能进行基准测试

# TLDR

对**根文件系统**性能进行基准测试

```pveperf```

对**指定挂载点**进行基准测试

```pveperf [/mnt/storage]```

# SYNOPSIS

**pveperf** [_path_]

# PARAMETERS

_path_
> 要测试的挂载点（默认：/）

# DESCRIPTION

**pveperf** 运行一个快速基准测试，衡量 Proxmox VE 主机的 CPU 和存储性能。它报告 CPU BOGOMIPS、正则处理速度（REGEX/SECOND）、硬盘大小、缓冲读取速度、平均寻道时间、fsync 速率（FSYNCS/SECOND）以及 DNS 解析时间（外部和内部）。

结果有助于识别潜在的性能瓶颈，并验证存储是否满足虚拟化工作负载的最低要求。fsync 速率对数据库和 VM 磁盘性能尤为重要。默认测试在根文件系统挂载点上运行。

# CAVEATS

基准测试结果是近似值，各次运行之间可能存在差异。要进行精确的存储基准测试，请考虑使用 [fio](/man/fio)(1) 等专用工具。应结合工作负载需求来解读结果。需要 root 权限。

# HISTORY

属于 **Proxmox VE**，提供快速的系统性能验证。适用于初始硬件评估以及虚拟化环境中的性能问题排查。

# SEE ALSO

[pveversion](/man/pveversion)(1), [pvesh](/man/pvesh)(1)
