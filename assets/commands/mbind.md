# TAGLINE

为指定内存范围设置 NUMA 内存策略的系统调用

# TLDR

**为内存范围设置 NUMA 策略（C 代码）**

```mbind([addr], [length], MPOL_BIND, [&nodemask], [maxnode], 0)```

**将内存绑定到特定节点**

```mbind([ptr], [size], MPOL_BIND, [&mask], [maxnode], MPOL_MF_MOVE)```

**在节点间交错分配内存**

```mbind([addr], [len], MPOL_INTERLEAVE, [&nodemask], [maxnode], 0)```

# SYNOPSIS

**long mbind**(void *_addr_, unsigned long _len_, int _mode_, const unsigned long *_nodemask_, unsigned long _maxnode_, unsigned _flags_)

# PARAMETERS

**addr**
> 内存范围的起始地址。

**len**
> 内存范围的长度。

**mode**
> MPOL_DEFAULT、MPOL_BIND、MPOL_INTERLEAVE、MPOL_PREFERRED。

**nodemask**
> NUMA 节点的位掩码。

**maxnode**
> 最大节点编号 + 1。

**flags**
> MPOL_MF_STRICT、MPOL_MF_MOVE、MPOL_MF_MOVE_ALL。

# DESCRIPTION

**mbind** 是一个系统调用，用于为指定的内存范围设置 NUMA 内存策略。它控制该范围内内存分配使用哪些 NUMA 节点。

它通过控制内存局部性，在 NUMA 系统上实现性能优化。

# POLICIES

```
MPOL_DEFAULT    - Use process default
MPOL_BIND       - Strict binding to nodes
MPOL_INTERLEAVE - Round-robin across nodes
MPOL_PREFERRED  - Prefer specified node
```

# CAVEATS

需要 NUMA 硬件。除非 flags 指定迁移，否则仅影响未来的分配。特权标志可能需要 CAP_SYS_NICE。

# HISTORY

mbind 在 Linux 内核 **2.6.7** 中作为 NUMA 内存策略支持的一部分加入，主要由 SUSE 的 **Andi Kleen** 开发。

# SEE ALSO

[numactl](/man/numactl)(8), [numastat](/man/numastat)(8)
