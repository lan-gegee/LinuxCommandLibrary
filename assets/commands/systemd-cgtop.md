# TAGLINE

监控 cgroup 资源使用情况

# TLDR

**启动**交互式视图

```systemd-cgtop```

**更改**排序方式

```systemd-cgtop --order [cpu|memory|path|tasks|io]```

按时间而非百分比**显示** CPU 占用

```systemd-cgtop --cpu=percentage```

**更改**刷新间隔

```systemd-cgtop -d [interval]```

**只**统计用户空间进程（不含内核线程）

```systemd-cgtop -P```

# SYNOPSIS

**systemd-cgtop** [_options_]

# PARAMETERS

**--order _field_**
> 按 cpu、memory、path、tasks 或 io 排序

**-d, --delay _interval_**
> 刷新间隔（支持 ms、us、min 后缀）

**-P**
> 只统计用户空间进程

**-k**
> 统计时包括内核线程

**-n, --iterations _n_**
> 运行 n 次迭代后退出

**-b, --batch**
> 以批处理模式运行（非交互式）

**-r, --raw**
> 输出不带单位的原始数字

**--depth _n_**
> 要显示的最大 cgroup 树深度

# DESCRIPTION

**systemd-cgtop** 按资源使用量显示占用最多的控制组，类似于 **top**，但按 cgroup 组织。它会显示每个控制组的 CPU、内存和 I/O 统计信息。

该工具适用于监控各服务的资源消耗，了解哪些 systemd 单元正在使用系统资源。交互模式支持通过键盘快捷键更改显示选项。

# CAVEATS

I/O 统计需要启用相应的 cgroup 控制器。某些资源统计信息可能因内核配置而不可用。属于 systemd 工具套件的一部分。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-cgls](/man/systemd-cgls)(1), [top](/man/top)(1), [systemctl](/man/systemctl)(1), [cgroups](/man/cgroups)(7)
