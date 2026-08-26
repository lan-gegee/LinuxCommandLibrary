# TAGLINE

以文本格式显示系统的硬件拓扑，无需图形界面

# TLDR

以**树形格式**显示机器拓扑

```lstopo-no-graphics```

只显示**物理核心**（忽略逻辑处理器）

```lstopo-no-graphics --only pu```

使用**物理索引**显示拓扑

```lstopo-no-graphics -p```

显示**帮助**

```lstopo-no-graphics -h```

# SYNOPSIS

**lstopo-no-graphics** [_options_]

# PARAMETERS

**--only _type_**
> 只显示指定类型的对象（例如 pu 表示处理单元）

**-p, --physical**
> 显示物理索引而非逻辑索引

**-l, --logical**
> 显示逻辑索引（默认）

**--no-io**
> 在输出中隐藏 I/O 设备

**--no-bridges**
> 在输出中隐藏桥接设备

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**lstopo-no-graphics** 以文本格式显示系统的硬件拓扑，无需图形显示。它是 **hwloc**（Hardware Locality）软件包的一部分，展示 CPU、缓存、内存和 I/O 设备的层次结构。

输出以树状结构显示系统的 NUMA 节点、封装（插槽）、核心和处理单元（硬件线程）。这些信息有助于理解 CPU 架构、缓存共享和内存局部性，从而进行性能优化。

与 **lstopo** 不同，此变体可在没有 X11 或图形库的纯控制台环境中工作。

# CAVEATS

输出的详细程度取决于内核暴露的硬件信息。某些虚拟机或容器可能只显示有限的拓扑数据。必须安装 hwloc 库才能使用此命令。

# HISTORY

hwloc 项目由波尔多 Inria 和田纳西大学开发，于 2009 年左右首次发布。它在多种操作系统和架构上提供层次化拓扑信息的可移植抽象。

# INSTALL

```apt: sudo apt install hwloc```

```dnf: sudo dnf install hwloc```

```pacman: sudo pacman -S hwloc```

```apk: sudo apk add hwloc-tools```

```zypper: sudo zypper install hwloc```

```brew: brew install hwloc```

```nix: nix profile install nixpkgs#hwloc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lstopo](/man/lstopo)(1), [hwloc-ls](/man/hwloc-ls)(1), [lscpu](/man/lscpu)(1), [numactl](/man/numactl)(8)
