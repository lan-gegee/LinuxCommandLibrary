# TAGLINE

查询 systemd 用户态 OOM killer 的相关信息

# TLDR

显示 **systemd-oomd** 所存储的 cgroup 和系统上下文的当前状态

```oomctl dump```

# SYNOPSIS

**oomctl** [_OPTIONS_...] _COMMAND_

# PARAMETERS

**dump**
> 显示 systemd-oomd 监控的 cgroup 和系统上下文的当前状态

**-h**, **--help**
> 打印帮助文本并退出

**--version**
> 打印版本字符串并退出

**--no-pager**
> 不将输出通过管道送入分页器

# DESCRIPTION

**oomctl** 用于获取 systemd 用户态内存不足（OOM）killer **systemd-oomd** 读取的各类上下文信息。它显示 systemd-oomd 正在监控内存压力和交换分区用量的 cgroup 上下文。

systemd-oomd 服务监控启用了 ManagedOOMSwap 或 ManagedOOMMemoryPressure 的 cgroup，利用 PSI（压力失速信息）统计来判断内存压力何时超过配置阈值。一旦超过限制，它会选定一个 cgroup 并向其所有进程发送 SIGKILL 将其终止。

# CAVEATS

需要启用完整统一 cgroup 层级（cgroups-v2）和内存记账的 systemd。内核必须编译了 PSI 支持（Linux 4.20+）。系统应启用交换分区，systemd-oomd 才能发挥最佳效果；没有 swap 时，系统可能在 oomd 来得及响应之前就进入活锁状态。

# HISTORY

于 **systemd 版本 247**（2020 年）引入，是 systemd-oomd 用户态 OOM killer 实现的一部分。它借助 PSI 指标在系统失去响应之前主动管理内存压力，为内核 OOM killer 提供了更智能的替代方案。

# INSTALL

```apt: sudo apt install systemd-oomd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [journalctl](/man/journalctl)(1)
