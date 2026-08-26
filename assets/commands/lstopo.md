# TAGLINE

显示包括 CPU、缓存、内存和 I/O 设备在内的硬件拓扑

# TLDR

**显示硬件拓扑**

```lstopo```

**在终端中显示**（文本模式）

```lstopo-no-graphics```

**输出为图片**

```lstopo [topology.png]```

**输出为 PDF**

```lstopo [topology.pdf]```

**输出为 XML**

```lstopo [topology.xml]```

**只显示 CPU 信息**

```lstopo --only core```

**连同 PCI 设备一起显示**

```lstopo --whole-io```

**显示物理索引**

```lstopo -p```

# SYNOPSIS

**lstopo** [_--of format_] [_--only type_] [_--whole-io_] [_options_] [_output_]

# PARAMETERS

**--of** _FORMAT_
> 输出格式（png、pdf、svg、xml、txt、console）。

**--only** _TYPE_
> 只显示特定类型的对象。

**--whole-io**
> 显示所有 I/O 设备。

**--no-io**
> 隐藏 I/O 设备。

**-p**, **--physical**
> 显示物理/OS 索引。

**-l**, **--logical**
> 显示逻辑索引。

**--merge**
> 合并相同的对象。

**--no-legend**
> 隐藏图例。

**--no-caches**
> 隐藏缓存信息。

**-v**, **--verbose**
> 详细输出。

**--input** _FILE_
> 从 XML 文件读取拓扑。

**--version**
> 打印版本号。

# DESCRIPTION

**lstopo** 显示包括 CPU、缓存、内存和 I/O 设备在内的硬件拓扑。它将系统从整机级别到单个核心和线程的层次结构可视化。

输出显示 NUMA 节点、封装（插槽）、核心和处理单元（线程）。缓存级别（L1、L2、L3）会连同其大小以及核心间的共享情况一并显示。

图形输出会生成展示拓扑树的图片。文本模式（lstopo-no-graphics）可在不支持图形的终端中使用。

理解拓扑对性能优化很重要。它能显示哪些核心共享缓存、哪些位于同一 NUMA 节点，以及内存的组织方式。

该工具可以从 XML 文件加载拓扑，支持离线分析或在不同系统间进行比较。

# CAVEATS

图形输出需要 Cairo/X11 库。某些虚拟环境可能显示错误的拓扑。获取完整的 I/O 设备信息可能需要 root 权限。

# HISTORY

**lstopo** 是 **hwloc**（Hardware Locality）的一部分，由 **Open MPI** 项目自 **2009 年**左右开始开发。hwloc 为不同操作系统的硬件拓扑提供可移植抽象。lstopo 由该项目早期的工具演化而来。

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

[lscpu](/man/lscpu)(1), [numactl](/man/numactl)(8)
