# TAGLINE

输出当前进程可用的处理单元数量

# TLDR

**输出处理单元数量**

```nproc```

**输出所有已安装的处理器数**（忽略 cgroup）

```nproc --all```

**输出数量减去 N 后的结果**

```nproc --ignore [2]```

**在 make 中用于并行任务**

```make -j$(nproc)```

# SYNOPSIS

**nproc** [_--all_] [_--ignore=N_] [_options_]

# PARAMETERS

**--all**
> 输出已安装处理器的总数，忽略 cgroup 限制。

**--ignore=** _N_
> 从计数中排除 N 个处理器。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**nproc** 输出当前进程可用的处理单元数量。这对于并行化构建和其他工作负载非常有用。

默认情况下，nproc 会遵循 cgroup 限制，返回容器化环境中可用的 CPU 数量。这使它具备容器感知能力——一个被限制为 4 个 CPU 的容器将看到 4，而不是宿主机的全部 CPU 数量。

**--all** 选项忽略 cgroup 限制，返回已安装处理器的总数。当你需要了解实际硬件情况而不受容器化影响时，这个选项很有用。

结合 **--ignore** 使用，可以为系统任务预留 CPU。例如 `nproc --ignore=1` 会留出一个空闲核心。

常见用法是设置并行构建任务数：`make -j$(nproc)` 以每个可用处理器一个任务的方式进行编译，在遵守系统限制的同时最大化构建速度。

# CAVEATS

不考虑超线程——一个核心上的两个超线程会被计为两个处理器。可能不反映当前的 CPU 频率或热节流状态。SMT 兄弟线程被计为独立处理器。虚拟化环境中的结果可能有所不同。

# HISTORY

**nproc** 是 **GNU coreutils** 的一部分。加入它是为了提供一种可移植的 CPU 数量查询方式，取代各平台特定的方法。该命令已成为构建系统和并行处理脚本的重要工具，在各类系统上提供一致的行为。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lscpu](/man/lscpu)(1), [getconf](/man/getconf)(1), [parallel](/man/parallel)(1), [make](/man/make)(1)
