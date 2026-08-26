# TAGLINE

测量命令执行时间

# TLDR

**测量命令的执行时间**

```time [command]```

**测量时间并输出详细信息**（GNU time）

```/usr/bin/time -v [command]```

**输出到文件**（GNU time）

```/usr/bin/time -o [time.log] [command]```

**自定义输出格式**（GNU time）

```/usr/bin/time -f "Real: %e User: %U Sys: %S" [command]```

**追加到输出文件**（GNU time）

```/usr/bin/time -a -o [time.log] [command]```

# SYNOPSIS

**time** [_command_ [_arguments_...]]

**/usr/bin/time** [**-v**] [**-o** _file_] [**-f** _format_] _command_ [_arguments_...]

# PARAMETERS (GNU TIME)

**-v**, **--verbose**
> 显示详细的资源使用情况

**-o** _file_, **--output**=_file_
> 将计时统计信息写入文件

**-a**, **--append**
> 追加到输出文件而不是覆盖

**-f** _format_, **--format**=_format_
> 使用指定的输出格式

**-p**, **--portability**
> 使用 POSIX 输出格式

# FORMAT SPECIFIERS (GNU TIME)

**%e**：实际经过时间（秒）
**%E**：实际经过时间（h:mm:ss）
**%U**：用户态 CPU 时间（秒）
**%S**：内核态 CPU 时间（秒）
**%P**：CPU 使用百分比（(U+S)/E）
**%M**：最大常驻内存集（KB）
**%x**：命令的退出状态
**%C**：命令及其参数

# DESCRIPTION

**time** 测量命令的执行时间，报告实际耗时（墙上时钟）、用户时间（用户态 CPU 时间）和系统时间（内核态 CPU 时间）。

它有两个版本：shell 内建命令（bash、zsh）和 GNU time（**/usr/bin/time**）。内建版本较简单；GNU time 提供更详细的资源统计和格式化选项。

实际时间是真正经过的时间。用户时间是执行用户代码的 CPU 时间。系统时间是内核调用中花费的 CPU 时间。在多核并行执行的系统中，User + System 可能大于 Real；若进程等待 I/O 则可能更少。

# CAVEATS

Shell 内建的 **time** 优先级更高。要使用功能完整的外部命令，请用 **/usr/bin/time** 或 **\time**。

要做准确的基准测试，需多次运行迭代并考虑系统负载。统计型基准测试可使用 **hyperfine** 等工具。

资源测量（内存、I/O）只在 GNU time 中可用，shell 内建版本不支持。

# INSTALL

```apt: sudo apt install time```

```dnf: sudo dnf install time```

```pacman: sudo pacman -S time```

```apk: sudo apk add time```

```zypper: sudo zypper install time```

```nix: nix profile install nixpkgs#time```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[timeout](/man/timeout)(1), [watch](/man/watch)(1), [hyperfine](/man/hyperfine)(1), [perf](/man/perf)(1)
