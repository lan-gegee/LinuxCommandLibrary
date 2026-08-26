# TAGLINE

执行由 at 安排的作业的守护进程

# TLDR

**启动 at 守护进程**

```atd```

**前台运行**以便调试

```atd -f```

向 stderr **输出调试消息**

```atd -d```

设置 batch 作业之间的**最小间隔**（秒）

```atd -b [120]```

仅在负载均值低于某值时才允许 batch 作业运行

```atd -l [1.5]```

**处理一次队列**后退出

```atd -s```

# SYNOPSIS

**atd** [**-d**] [**-f**] [**-s**] [**-l** _load_avg_] [**-b** _interval_]

# PARAMETERS

**-d**
> 调试模式；将错误输出到 stderr 而非 syslog（隐含 -f）

**-f**
> 前台运行而不守护进程化

**-s**
> 处理一次 at/batch 队列后退出。等价于旧的 atrun 命令。

**-l** _load_avg_
> 仅当系统负载低于该值时才执行 batch 作业（默认：0.8）

**-b** _interval_
> 启动 batch 作业的最小间隔秒数（默认：60）

# DESCRIPTION

**atd** 是执行由 **at** 命令安排的作业的守护进程。它在后台运行，定期检查 **/var/spool/at/** 中的待处理作业，并在其预定时间执行。

作业通过 **at** 提交可按特定时间调度，或通过 **batch** 按系统负载执行。守护进程代表安排作业的用户运行作业，继承该用户的环境和权限。

访问控制通过 **/etc/at.allow** 和 **/etc/at.deny** 管理。若存在 at.allow，则只有列出的用户可以安排作业。若只存在 at.deny，则除列出用户之外的所有用户都可以安排作业。若两者都不存在，则只有 root 能使用 at。

相关命令：
- **at** - 在特定时间安排一个作业
- **atq** - 列出待处理的作业
- **atrm** - 移除待处理的作业
- **batch** - 在系统负载允许时安排作业

# CONFIGURATION

**/etc/at.allow**
> 若该文件存在，则只有列于其中的用户才能用 at 安排作业。

**/etc/at.deny**
> 列于该文件中的用户被禁止使用 at。若 at.allow 存在，则忽略此文件。

# CAVEATS

atd 的 spool 目录（**/var/spool/at/**）通过 NFS 挂载时无法正常工作，即使启用了 no_root_squash 也是如此。作业继承的是被安排时的环境，而非当前环境。必须有守护进程正在运行，计划中的作业才会执行。

# HISTORY

**at** 命令及其守护进程源自早期 Unix 系统，可追溯至 **1979** 年的 **Version 7 Unix**。延迟执行命令的理念是 Unix 原始作业控制思想的一部分。现代实现还包含面向负载敏感调度的 **batch** 命令，适合让资源密集型任务在低负载时段运行。

# INSTALL

```apt: sudo apt install at```

```dnf: sudo dnf install at```

```pacman: sudo pacman -S at```

```apk: sudo apk add at```

```zypper: sudo zypper install at```

```nix: nix profile install nixpkgs#at```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[at](/man/at)(1), [atq](/man/atq)(1), [atrm](/man/atrm)(1), [batch](/man/batch)(1), [cron](/man/cron)(8), [crontab](/man/crontab)(1)

# RESOURCES

```[Source code](https://salsa.debian.org/debian/at)```

<!-- verified: 2026-06-17 -->
