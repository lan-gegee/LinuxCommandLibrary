# TAGLINE

按名称和属性向进程发送信号

# TLDR

按名称匹配并**杀死所有进程**

```pkill [process_name]```

**精确名称匹配并杀死进程**

```pkill -x [exact_name]```

**杀死特定用户拥有的进程**

```pkill -u [username] [process_name]```

**向进程发送指定信号**

```pkill -[SIGTERM] [process_name]```

**杀死匹配模式的进程**（不区分大小写）

```pkill -i [pattern]```

**杀死最近启动的**匹配进程

```pkill -n [process_name]```

**杀死最旧的**匹配进程

```pkill -o [process_name]```

# SYNOPSIS

**pkill** [_-signal_] [_-fvx_] [_-n|-o_] [_-P ppid,..._] [_-g pgrp,..._] [_-s sid,..._] [_-u euid,..._] [_-U uid,..._] [_-G gid,..._] [_-t term,..._] [_pattern_]

# PARAMETERS

**-** _signal_, **--signal** _signal_
> 要发送的信号（默认：SIGTERM）。可用名称或编号

**-f**, **--full**
> 匹配完整命令行，而不仅是进程名

**-x**, **--exact**
> 要求进程名完全匹配

**-n**, **--newest**
> 只选择最近启动的匹配进程

**-o**, **--oldest**
> 只选择最旧的匹配进程

**-P** _ppid_, **--parent** _ppid_
> 只匹配父进程为指定值的进程

**-u** _euid_, **--euid** _euid_
> 只匹配具有指定有效用户 ID 的进程

**-U** _uid_, **--uid** _uid_
> 只匹配具有指定真实用户 ID 的进程

**-g** _pgrp_, **--pgroup** _pgrp_
> 只匹配位于指定进程组的进程

**-G** _gid_, **--group** _gid_
> 只匹配具有指定真实组 ID 的进程

**-t** _term_, **--terminal** _term_
> 只匹配在指定终端上的进程

**-i**, **--ignore-case**
> 不区分大小写的模式匹配

**-v**, **--inverse**
> 反转匹配（排除匹配的进程）

# DESCRIPTION

**pkill** 根据进程名称和其他属性向进程发送信号。与需要进程 ID 的 **kill** 不同，pkill 使用模式匹配来识别目标进程，让常见的进程管理任务更加方便。

默认情况下，pkill 发送 SIGTERM（信号 15）以优雅地终止进程。模式会与进程名（可执行文件名）匹配，但配合 **-f** 时则匹配包含参数在内的完整命令行。

该命令特别适合在脚本中使用，也适合快速终止进程而无需先用 **ps** 或 **pgrep** 查找其 PID。多个选择条件可以组合使用，从而精确定位特定进程。

# CAVEATS

模式匹配可能意外杀死无关进程。请先用相同的模式运行 **pgrep** 验证哪些进程会受影响。若不小心，**-f** 选项可能匹配到 pkill 命令自身。处于不可中断睡眠（D 状态）的进程即使 SIGKILL 也无法杀死。普通用户只能杀死自己的进程。

# HISTORY

**pkill** 于 **1998 年**随 **Solaris 7** 推出，是与 **pgrep** 同属一套的进程工具之一。它随后被移植到其他类 Unix 系统，Linux 实现由 **procps**（或 **procps-ng**）软件包提供。该命令已成为现代类 Unix 系统上的标准工具，相比传统的 **ps | grep | kill** 管道方式更为便利。

# INSTALL

```apt: sudo apt install procps```

```dnf: sudo dnf install procps-ng```

```pacman: sudo pacman -S procps-ng```

```apk: sudo apk add procps-ng```

```zypper: sudo zypper install procps```

```brew: brew install procps```

```nix: nix profile install nixpkgs#procps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pgrep](/man/pgrep)(1), [kill](/man/kill)(1), [killall](/man/killall)(1), [ps](/man/ps)(1), [top](/man/top)(1)
