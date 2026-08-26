# TAGLINE

启用和禁用单个 CPU

# TLDR

**禁用**一个或多个 CPU

```chcpu -d [1,3]```

**启用**一个或多个 CPU 范围

```chcpu -e [1-3,5-7]```

**配置** CPU（向 hypervisor 发起请求）

```chcpu -c [0,1,2]```

**取消配置** CPU（归还给 hypervisor）

```chcpu -g [3,4]```

**重新扫描**新 CPU

```chcpu -r```

**设置 CPU 分派模式**（polarization）

```chcpu -p [horizontal]```

# SYNOPSIS

**chcpu** [_options_]

# DESCRIPTION

**chcpu** 可以启用或禁用 CPU、扫描新 CPU、更改底层 hypervisor 的 CPU 分派模式，以及向 hypervisor 请求 CPU（configure）或将 CPU 归还给 hypervisor（deconfigure）。

CPU 通过逻辑 ID 指定，使用逗号分隔的 cpu-list，其中可以包含单个地址或范围（例如 `0,5,7,9-11`）。

# PARAMETERS

**-c**, **--configure** _cpu-list_
> 配置指定的 CPU。hypervisor 从 CPU 池中取出一个 CPU 并将其分配给你的内核所在的虚拟硬件。

**-d**, **--disable** _cpu-list_
> 禁用指定的 CPU。内核会将其置于离线状态。

**-e**, **--enable** _cpu-list_
> 启用指定的 CPU。内核会将其置于在线状态。CPU 必须先被配置才能启用。

**-g**, **--deconfigure** _cpu-list_
> 取消配置指定的 CPU。hypervisor 将该 CPU 从虚拟硬件上移除并归还给 CPU 池。

**-p**, **--dispatch** _mode_
> 设置 CPU 分派模式（polarization）。支持的模式有 `horizontal`（工作负载分布在所有 CPU 上）和 `vertical`（工作负载集中在少数 CPU 上）。仅当硬件架构和 hypervisor 支持 CPU polarization 时才有效。

**-r**, **--rescan**
> 触发 CPU 的重新扫描。重新扫描后，Linux 内核即可识别新的 CPU。

**-h**, **--help**
> 显示帮助文本并退出。

**-V**, **--version**
> 输出版本信息并退出。

# CAVEATS

在大多数系统上无法禁用 CPU 0。禁用 CPU 会将进程迁移到其余 CPU 上。需要 root 权限。并非所有硬件都支持 CPU 热插拔。`--dispatch` 与 `--configure`/`--deconfigure` 选项需要 hypervisor 支持。

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

[lscpu](/man/lscpu)(1), [taskset](/man/taskset)(1), [numactl](/man/numactl)(8), [nproc](/man/nproc)(1)
