# TAGLINE

实时系统进程监视器

# TLDR

启动 **top**

```top```

不显示任何**空闲或僵尸**进程

```top -i```

只显示**特定用户**拥有的进程

```top -u [username]```

按字段对进程**排序**

```top -o %MEM```

显示进程的单个**线程**

```top -Hp [process_id]```

监视**特定 PID**

```top -p [1234],[5678]```

以**批处理模式**运行以便脚本使用（单次快照）

```top -b -n 1```

将**刷新间隔**设为 5 秒

```top -d 5```

显示**完整命令行**而非程序名

```top -c```

# SYNOPSIS

**top** [_-b_] [_-c_] [_-d delay_] [_-H_] [_-i_] [_-n iterations_] [_-o field_] [_-p pid_] [_-S_] [_-u user_] [_-w width_]

# DESCRIPTION

**top** 提供正在运行的系统的动态实时视图。它显示系统概要信息以及当前由 Linux 内核管理的进程或线程列表。显示内容会定期更新，并且可以通过交互方式自定义。

# PARAMETERS

**-b**, **--batch**
> 以批处理模式（非交互式）运行，便于管道传输输出。

**-c**, **--cmdline-toggle**
> 在命令行和程序名显示之间切换。

**-d** _SECS_, **--delay=SECS**
> 设置屏幕刷新间隔（默认：3.0 秒）。

**-e**, **--scale-task-mem**
> 设置任务内存值的缩放单位（k/m/g/t/p）。

**-E**, **--scale-summary-mem**
> 设置概要内存值的缩放单位（k/m/g/t/p/e）。

**-H**, **--threads-show**
> 显示单个线程而不是进程。

**-i**, **--idle-toggle**
> 隐藏空闲和僵尸进程。

**-n** _NUMBER_, **--iterations=NUMBER**
> 设置退出前的最大迭代次数。

**-o** _FIELD_, **--sort-override=FIELD**
> 覆盖默认排序字段。加 + 或 - 前缀表示升序/降序。

**-p** _PIDLIST_, **--pid=PIDLIST**
> 只监视指定的进程 ID（逗号分隔）。

**-S**, **--accum-time-toggle**
> 切换累计时间模式，显示每个进程及其已终止子进程占用的 CPU 时间。

**-s**, **--secure-mode**
> 以安全模式启动 top，禁用有潜在危险的交互式命令。

**-u** _USER_, **--filter-only-euser=USER**
> 只显示指定有效用户的进程。

**-U** _USER_, **--filter-any-user=USER**
> 显示指定用户（实际、有效、保存及文件系统身份）的进程。

**-w** _WIDTH_, **--width=WIDTH**
> 在批处理模式下覆盖屏幕宽度（最小 80 字符）。

# INTERACTIVE COMMANDS

**h or ?**: 显示帮助屏幕
**q**: 退出 top
**d or s**: 更改刷新间隔
**k**: 终止进程（提示输入 PID 和信号）
**r**: 重新设置进程 nice 值（提示输入 PID 和 nice 值）
**f**: 管理显示的字段
**o**: 添加过滤表达式
**c**: 切换命令行/程序名
**V**: 切换森林视图模式
**1**: 在整体与逐个 CPU 状态之间切换
**m**: 循环切换内存显示模式
**t**: 循环切换 CPU 状态显示模式
**R**: 反转排序顺序
**P**: 按 CPU 使用率排序
**M**: 按内存使用率排序
**T**: 按累计时间排序
**< or >**: 左右移动排序列
**W**: 写入配置文件

# PROCESS STATUS CODES

**D**: 不可中断睡眠
**I**: 空闲内核线程
**R**: 运行中
**S**: 睡眠（可中断）
**T**: 被作业控制信号停止
**t**: 被调试器停止
**Z**: 僵尸

# CAVEATS

配置文件保存在 ~/.config/procps/toprc。编写脚本时建议使用批处理模式（-b），因为它会禁用交互功能并生成可解析的输出。默认刷新间隔为 3.0 秒。

# HISTORY

**top** 最初由 Roger Binns 编写，一直是 **procps**（现为 **procps-ng**）软件包的一部分。自 20 世纪 80 年代以来，它一直是类 Unix 系统上的标准系统监控工具。

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

[htop](/man/htop)(1), [atop](/man/atop)(1), [ps](/man/ps)(1), [free](/man/free)(1), [uptime](/man/uptime)(1), [vmstat](/man/vmstat)(1), [kill](/man/kill)(1)
