# TAGLINE

以指定的 NUMA 调度或内存放置策略运行进程

# TLDR

在**节点 0** 上运行命令，内存分配到节点 0 和 1

```numactl --cpunodebind=0 --membind=0,1 -- command```

在**指定 CPU** 上运行命令

```numactl --physcpubind=0-4,8-12 -- command```

以内存在所有节点间**交叉存取**的方式运行

```numactl --interleave=all -- command```

显示**当前 NUMA 策略**

```numactl --show```

显示**硬件 NUMA 配置**

```numactl --hardware```

优先在**特定节点**上分配内存

```numactl --preferred=0 -- command```

# SYNOPSIS

**numactl** [_--interleave=nodes_] [_--membind=nodes_] [_--cpunodebind=nodes_] [_--physcpubind=cpus_] [_--_] _command_ [_arguments_]

# DESCRIPTION

**numactl** 以特定的 NUMA（非一致性内存访问）调度或内存放置策略运行进程。策略针对命令设置，并被其所有子进程继承。它还可以管理共享内存段的策略。

# PARAMETERS

**-a, --all**
> 禁用 cpuset 感知，获得更广泛的 CPU/节点访问能力

**-i, --interleave=nodes**
> 在指定节点间轮询分配内存

**-m, --membind=nodes**
> 将内存分配限制在指定节点

**-N, --cpunodebind=nodes**
> 将 CPU 执行限制在指定节点的处理器上

**-C, --physcpubind=cpus**
> 将进程绑定到特定物理 CPU

**-l, --localalloc**
> 优先在当前节点分配，失败时回退

**-p, --preferred=node**
> 优先在单一节点分配，失败时回退

**-P, --preferred-many=nodes**
> 基于邻近性优先使用多个节点

**-b, --balancing**
> 启用内核 NUMA 平衡

**-s, --show**
> 显示当前 NUMA 策略设置

**-H, --hardware**
> 显示可用节点和 CPU

**--huge**
> 对 SYSV 共享内存使用大页

**--shm, --shmid**
> 指定共享内存段

**--touch**
> 立即强制应用策略而不是等到访问时

**--strict**
> 若页面已因冲突策略发生缺页则报错

**-V, --version**
> 打印版本信息并退出

# CAVEATS

NUMA 策略只在多节点系统上有意义。节点编号从 0 开始。特殊值 "all" 可用于表示所有节点。

# HISTORY

**numactl** 属于 Linux NUMA 系统的 **numactl** 软件包。它提供对 NUMA 内存和 CPU 策略的用户态控制，与内核自动 NUMA 平衡相辅相成。

# INSTALL

```apt: sudo apt install numactl```

```dnf: sudo dnf install numactl```

```pacman: sudo pacman -S numactl```

```apk: sudo apk add numactl-tools```

```zypper: sudo zypper install numactl```

```brew: brew install numactl```

```nix: nix profile install nixpkgs#numactl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[migratepages](/man/migratepages)(8), [numastat](/man/numastat)(8), [mbind](/man/mbind)(2)
