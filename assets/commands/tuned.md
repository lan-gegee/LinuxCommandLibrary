# TAGLINE

动态系统性能调优守护进程

# TLDR

**启动 tuned 守护进程**

```sudo systemctl start tuned```

**设置 tuned 开机自启**

```sudo systemctl enable tuned```

**列出可用配置**

```tuned-adm list```

**显示当前激活的配置**

```tuned-adm active```

**应用性能配置**

```sudo tuned-adm profile [throughput-performance]```

**获取推荐配置**

```tuned-adm recommend```

**禁用调优**

```sudo tuned-adm off```

# SYNOPSIS

**tuned** [_options_]

**tuned-adm** _command_ [_arguments_]

# PROFILES

**balanced**：通用场景；平衡性能与功耗。

**throughput-performance**：面向服务器的最大吞吐量。

**latency-performance**：为实时工作负载最小化延迟。

**powersave**：降低功耗。

**virtual-guest**：针对虚拟机客户机优化。

**virtual-host**：针对虚拟化宿主机优化。

**network-latency**：低延迟网络调优。

**network-throughput**：高网络吞吐量。

# TUNED-ADM COMMANDS

**list**：显示可用配置。

**active**：显示当前激活的配置。

**profile** _name_：激活指定配置。

**recommend**：为系统建议最优配置。

**off**：禁用所有调优。

**verify**：检查当前设置是否与配置一致。

# DESCRIPTION

**tuned** 是一个监控系统使用情况并动态调整系统设置以优化性能的守护进程。它使用各种配置文件来设置 CPU 调频策略、磁盘 I/O 调度器、内核参数和电源管理设置。

守护进程可以静态模式（应用配置中的固定设置）或动态模式（根据实时系统活动调整设置）运行。配置存储在 /etc/tuned/ 和 /usr/lib/tuned/ 中。

管理通过 tuned-adm 完成，它与守护进程通信以切换配置和查询状态。可以通过扩展现有配置或定义新的调优规则来创建自定义配置。

# CONFIGURATION

**/etc/tuned/tuned-main.conf**
> 守护进程主配置，控制动态调优、更新间隔和日志。

**/etc/tuned/**_profile_**/tuned.conf**
> 自定义配置定义，包含内核、磁盘和 CPU 调优参数。

**/usr/lib/tuned/**
> 系统提供的默认配置目录。

# CAVEATS

在 RHEL 上动态调优默认禁用。配置更改立即生效，但若不启用该服务则不会在重启后保留。某些设置可能与其他系统管理工具冲突。

# HISTORY

**tuned** 由 Red Hat 为企业级 Linux 系统开发，旨在简化性能优化。它从手动内核调优实践演变为基于工作负载类型应用最佳实践的自动化系统，降低了对系统优化专业经验的要求。

# INSTALL

```dnf: sudo dnf install tuned```

```pacman: sudo pacman -S tuned```

```apk: sudo apk add tuned```

```zypper: sudo zypper install tuned```

```nix: nix profile install nixpkgs#tuned```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tuned-adm](/man/tuned-adm)(8), [cpupower](/man/cpupower)(1), [sysctl](/man/sysctl)(8), [ionice](/man/ionice)(1)
