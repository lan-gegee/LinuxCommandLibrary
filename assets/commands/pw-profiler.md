# TAGLINE

分析 PipeWire 性能与延迟

# TLDR

对默认实例进行**性能分析**，记录到 profile.log

```pw-profiler```

更改**日志输出文件**

```pw-profiler -o path/to/file.log```

分析**远程**实例

```pw-profiler -r remote_name```

显示**帮助**

```pw-profiler -h```

# SYNOPSIS

**pw-profiler** [_options_]

# PARAMETERS

**-o**, **--output** _file_
> 指定输出日志文件（默认：profile.log）

**-r**, **--remote** _name_
> 分析远程 PipeWire 实例

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**pw-profiler** 对本地或远程 PipeWire 实例进行性能分析。它生成日志文件以及 gnuplot 数据文件和 HTML 可视化，用于分析 PipeWire 性能。

该分析器捕获计时信息、缓冲区使用情况和处理统计信息，有助于诊断音频延迟和性能问题。

# CAVEATS

性能分析会带来额外开销，只应用于诊断目的。长时间的分析会话可能产生很大的文件。

# HISTORY

**PipeWire**（Linux 上的现代多媒体框架）的一部分。为优化音频和视频管线提供性能分析工具。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [pw-top](/man/pw-top)(1), [pw-cli](/man/pw-cli)(1), [pw-dump](/man/pw-dump)(1), [pw-mon](/man/pw-mon)(1)
