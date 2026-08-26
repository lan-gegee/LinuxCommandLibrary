# TAGLINE

设置进程的 CPU 亲和性

# TLDR

**获取**运行中进程按 PID 指定的 CPU 亲和性

```taskset -p -c [pid]```

**设置**运行中进程按 PID 指定的 CPU 亲和性

```taskset -p -c [cpu_id] [pid]```

**以单个 CPU 的亲和性启动**新进程

```taskset -c [cpu_id] [command]```

**以多个非连续 CPU 的亲和性启动**新进程

```taskset -c [cpu_id_1,cpu_id_2,cpu_id_3] [command]```

**以 CPU 1 到 4 的亲和性启动**新进程

```taskset -c [1-4] [command]```

**使用十六进制掩码设置亲和性**（CPU 0 和 1）

```taskset -p [0x3] [pid]```

**为进程的所有线程设置**亲和性

```taskset -a -p -c [0-3] [pid]```

# SYNOPSIS

**taskset** [_options_] [_mask_|_list_] [_pid_|_command_]

# PARAMETERS

**-p, --pid**
> 操作已存在的 PID

**-c, --cpu-list**
> 以列表而非位掩码的形式指定 CPU

**-a, --all-tasks**
> 设置/获取所有任务（线程）的亲和性

**-h, --help**
> 显示帮助信息

**-V, --version**
> 显示版本信息

# DESCRIPTION

**taskset** 用于获取或设置进程的 CPU 亲和性，即控制进程可以在哪些 CPU 上运行。CPU 亲和性可以用位掩码或逗号分隔的 CPU ID 列表来指定。

它适用于性能调优、把进程隔离到特定核心，或测试软件在受限 CPU 资源下的表现。

# CAVEATS

CPU ID 从 0 开始。设置亲和性未必能提升性能，操作不当反而可能造成性能下降。除非配置了 CPU 隔离，内核仍可能为负载均衡而迁移进程。CPU 列表支持步长语法（例如 0-10:2 表示 CPU 0、2、4、6、8、10）。该命令属于 util-linux 软件包。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chrt](/man/chrt)(1), [nice](/man/nice)(1), [renice](/man/renice)(1), [numactl](/man/numactl)(8)
