# TAGLINE

录制并回放程序执行过程以辅助调试

# TLDR

**录制程序执行**

```rr record [./program]```

**回放录制内容**

```rr replay```

**列出录制记录**

```rr ls```

**回放指定的轨迹**

```rr replay [trace-directory]```

**以混乱模式录制**

```rr record --chaos [./program]```

**打包轨迹以便分享**

```rr pack [trace-directory]```

# SYNOPSIS

**rr** _command_ [_options_] [_program_] [_args_]

# PARAMETERS

**record**
> 录制执行过程。

**replay**
> 回放录制内容。

**ls**
> 列出轨迹。

**pack**
> 打包轨迹。

**--chaos**
> 随机化线程调度。

**-n**
> 进程数量。

**-h**
> 显示命令帮助。

# DESCRIPTION

**rr** 是一款面向 Linux 调试场景的轻量级录制与确定性回放工具。它会记录程序的全部执行过程——包括所有系统调用、信号和线程调度决策——因此可以将完全相同的执行反复回放任意次进行调试，每次运行的行为都完全一致。

在回放时，rr 与 GDB 集成，在标准调试界面的基础上增加了时间旅行（time-travel）能力。开发者可以在执行过程中反向单步、设置反向断点、跳转到已记录轨迹中的任意一点，这让定位难以复现的 bug 的根本原因变得轻松许多。

**--chaos** 标志会在录制时随机化线程调度，帮助暴露在正常调度下可能不会显现的并发缺陷和竞态条件。录制的开销很低，通常能以接近原生的速度运行，因此完全可以融入真实的调试工作流。

# CAVEATS

仅支持 Linux x86-64。需要 perf_event 访问权限。部分系统调用不受支持。

# HISTORY

**rr** 由 **Mozilla** 开发，最初用于调试 Firefox。它在 Linux 上提供录制与回放式调试能力。

# INSTALL

```apt: sudo apt install rr```

```dnf: sudo dnf install rr```

```zypper: sudo zypper install rr```

```nix: nix profile install nixpkgs#rr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdb](/man/gdb)(1), [strace](/man/strace)(1), [perf](/man/perf)(1)
