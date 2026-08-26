# TAGLINE

实时显示 PipeWire 性能统计

# TLDR

显示**交互式**视图

```pw-top```

监控**远程**实例

```pw-top -r [remote_name]```

以**批处理（batch）**模式运行

```pw-top -b```

带**迭代次数**上限的批处理模式

```pw-top -b -n [5]```

# SYNOPSIS

**pw-top** [**-r** _remote_] [**-b**] [**-n** _iterations_] [**-V**]

# PARAMETERS

**-r, --remote=_name_**
> 要监控的远程实例名称。未指定时连接到默认的 PipeWire 实例

**-b, --batch-mode**
> 以周期性打印代替交互模式

**-n, --iterations=_num_**
> 在完成指定次数的批处理迭代后退出。仅在批处理模式下使用

**-V, --version**
> 显示版本信息

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**pw-top** 提供 PipeWire 节点和设备统计信息的动态实时视图。它以层级结构显示 Driver 节点与 follower 节点，在类似 top 的界面中展示 CPU 使用率、缓冲区统计、延迟、xrun 及其他性能指标。

该工具对诊断音频性能问题、定位 xrun 以及监控 PipeWire 在负载下的行为至关重要。按 **q** 退出，按 **c** 清除错误计数器。

# CAVEATS

需要正在运行的 PipeWire 守护进程。统计刷新频率取决于系统负载。某些指标可能并非对所有节点可用。

# HISTORY

**pw-top** 是 **PipeWire** 的一部分，提供类似于 top 但专用于音频子系统的性能监控。它有助于诊断延迟和性能问题。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pw-cli](/man/pw-cli)(1), [pw-dump](/man/pw-dump)(1), [pw-profiler](/man/pw-profiler)(1), [pipewire](/man/pipewire)(1)
