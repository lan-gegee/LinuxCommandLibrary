# TAGLINE

监视 NVIDIA Jetson 设备上的内存与处理器使用情况

# TLDR

**循环打印系统统计信息**

```sudo tegrastats```

**设置自定义采样间隔（毫秒）**

```sudo tegrastats --interval [1000]```

**将输出写入日志文件**

```sudo tegrastats --logfile [filename]```

**在后台运行 tegrastats 并记录到文件**

```sudo tegrastats --start --logfile [filename]```

**停止后台运行的 tegrastats 进程**

```sudo tegrastats --stop```

**输出详细信息，包括读取失败的警告**

```sudo tegrastats --verbose```

# SYNOPSIS

**tegrastats** [**--interval** _millisec_] [**--logfile** _filename_] [**--start**] [**--stop**] [**--verbose**]

# DESCRIPTION

**tegrastats** 用于报告运行 Linux for Tegra（L4T）的 NVIDIA Jetson 设备的内存和处理器使用情况。它以固定间隔打印一行状态信息，汇总 RAM 和 swap 的使用量、每核 CPU 负载与频率、内存控制器和 GPU（GR3D）利用率、片上温度，并且在配备相应电源传感器的板卡上还会显示每条电源轨的瞬时与平均功耗。

由于桌面版的 **nvidia-smi** 工具不支持 Tegra 集成 GPU，tegrastats 成为观察 Jetson 负载的标准轻量工具。它的输出是紧凑且机器可解析的一行文本，因此非常适合把长时间运行的基准测试结果记录到文件供日后分析。

tegrastats 随 L4T BSP 一起发布，由 JetPack 安装在 **/usr/bin/tegrastats**。不带 **sudo** 运行时输出不完整，因为读取部分硬件计数器需要 root 权限。

# PARAMETERS

**--interval** _millisec_

> 每隔 _millisec_ 毫秒采样并打印一次统计信息。默认为 1000（一秒）。

**--logfile** _filename_

> 将输出发送到 _filename_ 而非标准输出。

**--start**

> 以后台进程方式运行 tegrastats。可与 **--logfile** 组合，在终端腾出来做其他工作的同时持续记录日志。

**--stop**

> 终止当前在后台运行的所有 tegrastats 进程。

**--verbose**

> 打印额外的诊断消息，例如传感器读取失败时的警告。

**--help**

> 打印用法摘要并退出。

# OUTPUT FIELDS

**RAM** _used_/_total_MB

> 主内存的已用量和总量，随后是可用的最大空闲块（**lfb**）。

**SWAP** _used_/_total_MB

> swap 的已用量和总量，以及缓存数量。

**CPU** [_load_%@_freq_,...]

> 每核利用率百分比与时钟频率；离线核心显示为 **off**。

**EMC_FREQ** _x_%@_freq_

> 外部内存控制器（DRAM）的利用率和频率。

**GR3D_FREQ** _x_%@_freq_

> GPU 3D 引擎的利用率和频率。

**CPU@_x_C, GPU@_x_C, ...**

> 片上热区报告的温度，单位为摄氏度。

**VDD_IN _x_/_y_, ...**

> 各电源轨的功率（毫瓦），显示为瞬时/平均，仅在配备 INA 功率监测器的板卡上提供。

# CAVEATS

请用 **sudo** 运行；没有 root 时某些计数器无法读取，输出会不完整。功耗读数仅在包含相应 INA 传感器的板卡上可用，字段的确切集合因 Jetson 模块（Nano、TX2、Xavier、Orin）和 L4T 版本而异。tegrastats 仅适用于 Tegra SoC，桌面版 NVIDIA GPU 上不可用。

# HISTORY

**tegrastats** 是 NVIDIA **Linux for Tegra (L4T)** 板级支持包的一部分，随面向 Jetson 产品线的 **JetPack** SDK 分发。长期以来它一直是监控 Jetson 系统负载的推荐内置方式，流行的第三方工具 **jtop**（jetson-stats）也在解析并利用它的输出。

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1), [nvtop](/man/nvtop)(1), [htop](/man/htop)(1), [free](/man/free)(1)

# RESOURCES

```[Homepage](https://developer.nvidia.com/embedded/jetson-linux)```

```[Documentation](https://docs.nvidia.com/jetson/archives/r35.4.1/DeveloperGuide/text/AT/JetsonLinuxDevelopmentTools/TegrastatsUtility.html)```

<!-- verified: 2026-06-13 -->
