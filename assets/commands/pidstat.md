# TAGLINE

监视 Linux 内核管理的各个任务

# TLDR

以 2 秒间隔显示 **CPU 统计信息**，共 10 份报告

```pidstat 2 10```

显示**缺页错误**和内存利用率

```pidstat -r```

显示每个进程的 **I/O** 使用情况

```pidstat -d```

显示**特定 PID** 的信息

```pidstat -p 1234```

显示匹配模式的进程的**内存**统计信息

```pidstat -C "pattern" -r -p ALL```

显示**上下文切换**

```pidstat -w```

**执行并监视**特定程序

```pidstat -e [program] [args] 1```

以 **JSON** 格式显示输出

```pidstat -o JSON 1 5```

# SYNOPSIS

**pidstat** [_-d_] [_-H_] [_-h_] [_-I_] [_-l_] [_-R_] [_-r_] [_-s_] [_-t_] [_-U_ [_username_]] [_-u_] [_-v_] [_-w_] [_-C comm_] [_-G process_name_] [_--human_] [_-o JSON_] [_-p_ {_pid_|SELF|ALL}] [_-T_ {TASK|CHILD|ALL}] [_interval_] [_count_] [_-e program args_]

# DESCRIPTION

**pidstat** 用于监视 Linux 内核当前管理的各个任务。它报告所选进程或全部任务的 CPU 使用率、内存利用率、I/O 统计、上下文切换及其他资源使用情况。

# PARAMETERS

**-d**
> 显示 I/O 统计信息（磁盘读/写、I/O 延迟）

**-r**
> 报告缺页错误和内存利用率指标

**-u**
> 显示 CPU 使用率百分比（未指定选项时的默认值）

**-w**
> 显示自愿和非自愿上下文切换

**-s**
> 报告栈内存使用情况

**-t**
> 包含所选任务的线程统计信息

**-p {pid|SELF|ALL}**
> 选择特定进程、当前进程或所有任务

**-T {TASK|CHILD|ALL}**
> 监视单个任务、子任务或两者

**-C comm**
> 使用正则表达式模式按命令名过滤

**-G process_name**
> 显示匹配名称模式的进程

**-l**
> 显示带参数的完整命令名

**--human**
> 以人类可读的大小格式化输出（1.0k、1.2M）

**-e program args**
> 执行并监视特定程序

**-h**
> 将所有活动横向显示在一行内；省略报告末尾的平均统计

**-H**
> 显示自 epoch 起的秒数时间戳

**-I**
> 在 SMP 环境中，将 CPU 使用率除以处理器总数

**-o JSON**
> 以 JSON 格式输出统计信息

**-R**
> 报告实时优先级和调度策略信息

**-U** [_username_]
> 显示任务的真实用户名；可选按指定用户过滤

**-v**
> 报告内核表数值：线程数和文件描述符数

**--dec**={0|1|2}
> 指定使用的小数位数（默认：2）

# CAVEATS

使用 **-e** 运行并监视程序时，必须指定非零的 **interval** 值。**interval** 和 **count** 参数控制报告的频率和时长。

必须挂载 `/proc` 文件系统 pidstat 才能工作。将 interval 指定为 0 或省略它会报告自系统启动以来累计的统计信息。

# HISTORY

**pidstat** 属于 **sysstat** 软件包，由 Sebastien Godard 开发。它提供每个进程的统计信息，与 mpstat、iostat 等系统级工具相辅相成。

# INSTALL

```apt: sudo apt install sysstat```

```dnf: sudo dnf install sysstat```

```pacman: sudo pacman -S sysstat```

```apk: sudo apk add sysstat```

```zypper: sudo zypper install sysstat```

```brew: brew install sysstat```

```nix: nix profile install nixpkgs#sysstat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sar](/man/sar)(1), [top](/man/top)(1), [ps](/man/ps)(1), [mpstat](/man/mpstat)(1), [iostat](/man/iostat)(1), [vmstat](/man/vmstat)(1)
