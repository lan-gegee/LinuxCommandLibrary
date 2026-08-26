# TAGLINE

云端量子线路模拟器客户端

# TLDR

针对公共 API **运行 1000 量子比特的 GHZ** 演示

```qumulator demo```

**运行 Willow 布局基准测试**

```qumulator demo --willow```

**运行全息虫洞演示**

```qumulator demo --wormhole```

**运行任意子编织演示**

```qumulator demo --anyon```

**显示获取免费 API 密钥的说明**

```qumulator key```

**提交 QASM 线路并打印结果**

```qumulator run [circuit.qasm]```

**显式传入 API 密钥**

```qumulator run [circuit.qasm] --key [YOUR_KEY]```

# SYNOPSIS

**qumulator** _command_ [_options_]

# DESCRIPTION

**qumulator** 是 **Qumulator** 云 API 的命令行客户端。该 API 可在标准经典硬件上模拟量子线路、自旋系统、光子振幅和分子性质。本地 CLI 通过 HTTP 提交任务并打印结果；繁重的计算在云端运行（默认为 Google Cloud Run，4 vCPU、16 GB 内存）。

该模拟器面向结构化线路，最多可支持约 **1000 个量子比特**，无需 GPU 或量子硬件。CLI 随 **qumulator-sdk** Python 包一同分发，因此安装 SDK 后即可同时获得 Python 客户端和 **qumulator** 二进制文件。

# COMMANDS

**demo** [**--willow** | **--wormhole** | **--anyon**]
> 运行内置演示。不带标志时运行 1000 量子比特的 GHZ 线路。**--willow** 运行 105 量子比特的 Willow 布局基准测试，**--wormhole** 运行全息虫洞模拟，**--anyon** 运行任意子编织计算。

**key**
> 打印获取免费 API 密钥的说明。

**run** _circuit.qasm_
> 将 **QASM** 文件提交给 API 并打印结果。

# OPTIONS

**--key** _KEY_
> 直接传入 API 密钥，而不依赖环境变量。

# CONFIGURATION

**QUMULATOR_API_KEY**
> 未提供 **--key** 时所有子命令使用的环境变量。可通过 **qumulator key** 获取密钥。

# CAVEATS

由于线路在云端执行，**线路数据会离开本地机器**——请勿提交你认为结构需要保密的线路。网络延迟主导短任务的耗时，因此在微型线路上迭代会比在本地模拟器中运行慢得多。

# HISTORY

**Qumulator** 以 **qumulator-sdk** Python 包的形式发布。它的定位是通过托管 API 在普通经典硬件上运行超大规模但结构化的量子模拟，与付费的量子硬件机时相比，降低了试验量子算法的成本。

# SEE ALSO

[python](/man/python)(1), [pip](/man/pip)(1)
