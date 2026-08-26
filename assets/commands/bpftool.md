# TAGLINE

检查和管理 eBPF 程序与映射。

# TLDR

列出已加载的 **eBPF 程序**信息

```bpftool prog list```

列出**网络子系统**中的 eBPF 程序挂接

```bpftool net list```

列出所有**活动链接**

```bpftool link list```

列出所有 **tracepoint 和 kprobe** 挂接

```bpftool perf list```

列出 **BPF Type Format (BTF)** 数据

```bpftool btf list```

列出已加载的**映射（map）**信息

```bpftool map list```

**探测**网络设备支持的 eBPF 特性

```bpftool feature probe dev [eth0]```

以**批处理模式**从文件运行命令

```bpftool batch file [myfile]```

# SYNOPSIS

**bpftool** [_object_] _command_ [_options_]

# DESCRIPTION

**bpftool** 用于检查和操作 eBPF（extended Berkeley Packet Filter）程序和映射。它让你能够查看已加载的 BPF 程序、它们的挂接点以及所使用的数据结构。

eBPF 是一项强大的 Linux 内核技术，用于网络、安全、跟踪和性能分析。bpftool 是调试和管理基于 eBPF 的工具的必备工具。

# OBJECTS

**prog**
> 管理 BPF 程序。

**map**
> 管理 BPF 映射。

**link**
> 管理 BPF 链接。

**net**
> 检查与网络相关的 BPF 挂接。

**perf**
> 检查与 perf 相关的 BPF 挂接。

**btf**
> 管理 BTF（BPF Type Format）数据。

**cgroup**
> 在 cgroup 上显示、挂接和分离 BPF 程序。

**feature**
> 探测内核/设备对 BPF 特性的支持情况。

**gen**
> 从目标文件生成骨架 C 头文件和 BTF 数据。

**struct_ops**
> 注册、注销并检视 BPF struct_ops。

**iter**
> 创建并固定（pin）BPF 迭代器。

# OPTIONS

**-j**, **--json**
> 生成 JSON 输出。

**-p**, **--pretty**
> 生成易读的 JSON 输出（隐含 **-j**）。

**-d**, **--debug**
> 将 libbpf 调试消息打印到 stderr。

**-f**, **--bpffs**
> 显示程序时同时显示已固定对象的文件名。

**-V**, **--version**
> 打印版本号和支持的特性。

# CAVEATS

需要 root 权限或 CAP_BPF 能力。输出格式可能因内核版本而异。某些特性需要特定的内核配置选项。

# HISTORY

**bpftool** 在 Linux 内核源码树的 **tools/bpf/bpftool** 下开发，随内核一起发布。它会定期同步到由 libbpf 项目维护的独立构建镜像中，后者将其独立于完整内核树打包。

# INSTALL

```apt: sudo apt install bpftool```

```dnf: sudo dnf install bpftool```

```apk: sudo apk add bpftool```

```zypper: sudo zypper install bpftool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bpftrace](/man/bpftrace)(8), [tc](/man/tc)(8), [perf](/man/perf)(1)

# RESOURCES

```[Source code](https://github.com/libbpf/bpftool)```

```[Documentation](https://docs.kernel.org/bpf/index.html)```

<!-- verified: 2026-06-19 -->
