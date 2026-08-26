# TAGLINE

将进程的物理内存页从一组 NUMA 节点迁移到另一组

# TLDR

**将页从一个节点迁移到另一个节点**

```migratepages [pid] [from_node] [to_node]```

**将所有页迁移到指定节点**

```migratepages [pid] all [2]```

**迁移到最近的节点**

```migratepages [pid] [0] best```

# SYNOPSIS

**migratepages** _pid_ _from-nodes_ _to-nodes_

# PARAMETERS

**pid**
> 进程 ID。

**from-nodes**
> 源 NUMA 节点（或 'all'）。

**to-nodes**
> 目标 NUMA 节点（或 'best'）。

# DESCRIPTION

**migratepages** 将进程的物理内存页从一组 NUMA 节点迁移到另一组。这可用于在 NUMA 系统上优化内存布局。

该命令作用于正在运行的进程，可以通过迁移页来改善内存局部性。
# Migrate PID 1234 from node 0 to node 1
migratepages 1234 0 1

# Migrate from all nodes to node 2
migratepages 1234 all 2

# Let kernel choose best destination
migratepages 1234 0 best
```

# CAVEATS

需要 numactl 软件包。进程必须处于运行状态。迁移可能较慢。可能需要 root 权限。仅在 NUMA 系统上有效。

# HISTORY

migratepages 是 **numactl** 软件包的一部分，该软件包用于控制 Linux 系统上的 NUMA 内存策略。

# SEE ALSO

[numactl](/man/numactl)(8), [numastat](/man/numastat)(8), [mbind](/man/mbind)(2)

# INSTALL

```apt: sudo apt install numactl```

```dnf: sudo dnf install numactl```

```pacman: sudo pacman -S numactl```

```apk: sudo apk add numactl-tools```

```zypper: sudo zypper install numactl```

```brew: brew install numactl```

```nix: nix profile install nixpkgs#numactl```

<!-- packages: 2026-07-22 -->
