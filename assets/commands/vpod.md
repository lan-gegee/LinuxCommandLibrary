# TAGLINE

运行在 WASM RISC-V 虚拟机上的即时 Linux 沙箱

# TLDR

使用默认快照**启动交互式 Shell**

```vpod```

从指定快照**启动 Shell**

```vpod start [alpine:latest]```

**下载快照**使其在本地可用

```vpod pull [alpine:latest]```

**列出**已有的可用快照

```vpod list```

使用官方脚本**安装**

```curl -fsSL https://install.vpod.sh | sh```

# SYNOPSIS

**vpod** [_command_] [_snapshot_]

# DESCRIPTION

**vpod** 为不受信任的进程提供一个即开即用、用完即弃的 Linux 环境。每个 vpod 都是一台被编译为 WebAssembly 的 RISC-V 虚拟机（RV64GC 指令集），因此整个沙箱运行在可移植的 WASM 运行时内，而不依赖宿主内核、容器或硬件虚拟化。

启动时，vpod 从一个快照（保存好的虚拟机状态）引导，不到一秒即可就绪，并让用户进入交互式 Shell。由于执行始终处于 WebAssembly 沙箱之内，在 vpod 中运行的代码与宿主相互隔离，并且在 Linux、macOS 和 Windows 上行为一致，无需按平台做额外设置。

除了命令行工具，该项目还提供 Python SDK（可通过 **pip install vpod** 安装），能以编程方式创建持久化沙箱，目标是安全地运行 AI 智能体生成的或其他不受信任的代码。

# PARAMETERS

**start** _SNAPSHOT_
> 从指定快照而不是默认快照启动交互式 Shell。

**pull** _SNAPSHOT_
> 下载快照并保存在本地供以后使用。

**list**
> 列出本地可用的快照。

# CAVEATS

没有硬件加速，CPU 密集型负载的运行速度会慢于本地执行。沙箱内部无法访问 GPU 和加速器接口（CUDA、Metal、ML 加速器）。

# HISTORY

**vpod** 由 capsulerun 开发，以 Apache License 2.0 发布。它主要使用 Rust 编写，RISC-V 客户机通过 WebAssembly 运行时执行。

# SEE ALSO

[bubblewrap](/man/bubblewrap)(1), [docker](/man/docker)(1), [firejail](/man/firejail)(1), [qemu](/man/qemu)(1), [wasmtime](/man/wasmtime)(1)

# RESOURCES

```[Source code](https://github.com/capsulerun/vpod)```

<!-- verified: 2026-06-18 -->
