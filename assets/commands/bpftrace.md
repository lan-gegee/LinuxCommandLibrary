# TAGLINE

面向 Linux eBPF 的高级跟踪语言。

# TLDR

列出所有**可用的探测点**

```sudo bpftrace -l```

运行**单行程序**

```sudo bpftrace -e 'tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }'```

**从文件运行程序**

```sudo bpftrace [path/to/file]```

按 **PID** 跟踪某个程序

```sudo bpftrace -e 'tracepoint:raw_syscalls:sys_enter /pid == 123/ { @[comm] = count(); }'```

**跟踪子进程**命令直到其退出

```sudo bpftrace -c '[command]' -e 'tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }'```

进行**试运行**：只验证探测点而不执行

```sudo bpftrace --dry-run -e '[one_line_program]'```

**将输出写入**文件

```sudo bpftrace -o [output.txt] -e '[one_line_program]'```

显示**版本**

```bpftrace -V```

# SYNOPSIS

**bpftrace** [_options_] [_program_|_file_]

# DESCRIPTION

**bpftrace** 是一种面向 Linux eBPF 的高级跟踪语言。它为内核和用户态跟踪提供强大的脚本接口，类似于其他 Unix 系统上的 DTrace。

程序可以挂接到 tracepoint、kprobe、uprobe 及其他类型的探测点，实时收集并聚合系统行为数据。

# PARAMETERS

**-l** [_SEARCH_]
> 列出匹配搜索模式的探测点（支持通配符）。

**-e** _program_
> 执行单行程序。

**-d** _STAGE_
> 为指定的编译阶段输出调试信息（ast、codegen、dis、verifier 等）。

**--dry-run**
> 验证并编译程序，但不实际挂接探测点。

**-p** _PID_
> 挂接到某进程或按 PID 过滤动作。

**-c** _COMMAND_
> 以子进程方式运行命令；子进程结束时 bpftrace 也退出。

**-o** _FILENAME_
> 将跟踪输出写入文件而不是 stdout。

**-f** _FORMAT_
> 输出格式：`text`（默认）或 `json`。

**-B** _MODE_
> 输出的缓冲模式：`none`、`line`（默认）或 `full`。

**-I** _DIR_
> 将目录加入 C 头文件搜索路径（可重复使用）。

**-v**
> 详细输出。

**-q**
> 安静模式；不输出非错误消息。

**-V**, **--version**
> 显示版本信息。

**--unsafe**
> 允许 `system()` 调用等不安全操作。

**--info**
> 打印内核特性和 bpftrace 构建的相关信息。

# CAVEATS

需要 root 权限。内核必须启用 eBPF 和 BTF 支持。某些探测点可能并非在所有内核版本上都可用。性能影响因探测点类型和触发频率而异。

# HISTORY

**bpftrace** 由 Alastair Robertson 创建，于 **2018 年**首次发布。它受 DTrace 启发，旨在借助 eBPF 为 Linux 带来类似的高级跟踪能力。

# INSTALL

```apt: sudo apt install bpftrace```

```dnf: sudo dnf install bpftrace```

```pacman: sudo pacman -S bpftrace```

```apk: sudo apk add bpftrace```

```zypper: sudo zypper install bpftrace```

```nix: nix profile install nixpkgs#bpftrace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bpftool](/man/bpftool)(8), [perf](/man/perf)(1), [strace](/man/strace)(1)
