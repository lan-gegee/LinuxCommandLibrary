# TAGLINE

重放已录制的终端会话输出

# TLDR

以原始速度**重放** typescript 文件

```scriptreplay path/to/timing_file path/to/typescript```

以**两倍速度**重放

```scriptreplay path/to/timing_file path/to/typescript 2```

以**一半速度**重放

```scriptreplay path/to/timing_file path/to/typescript 0.5```

# SYNOPSIS

**scriptreplay** _timing_file_ _typescript_ [_divisor_]

# PARAMETERS

_timing_file_
> 包含 script 生成的计时信息的文件

_typescript_
> 包含已录制终端输出的文件

_divisor_
> 速度倍率（2 表示两倍速，0.5 表示半速）

# DESCRIPTION

**scriptreplay** 重放由 script 命令录制的终端会话。它按原始计时显示输出，适用于演示和回顾会话。

计时文件包含每个输出块之间的延迟信息，从而实现准确的重放。

# CAVEATS

仅显示输出，不执行命令。需要 script 录制时生成的计时文件和 typescript 文件。

# HISTORY

属于 **util-linux** 软件包，与 script 配合实现终端会话的录制与回放。

# INSTALL

```apt: sudo apt install bsdutils```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[script](/man/script)(1), [scriptlive](/man/scriptlive)(1)
