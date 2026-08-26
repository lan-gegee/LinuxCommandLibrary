# TAGLINE

安排命令在指定时间执行

# TLDR

交互式创建命令并在 **5 分钟后**执行

```at now + 5 minutes```

在**指定时间**执行来自 stdin 的命令

```echo "command" | at 1000```

在指定时间执行**文件**中的命令

```at -f [path/to/file] 9:30 PM Tue```

**列出**所有排队中的作业

```at -l```

**查看**指定作业

```at -c [job_number]```

从队列中**移除**一个作业

```atrm [job_number]```

# SYNOPSIS

**at** [_-q queue_] [_-f file_] [_-mMlv_] _timespec_

**at** [_-q queue_] [_-f file_] [_-mMkv_] [_-t time_]

**at** _-c_ _job_ ...

**at** [_-rd_] _job_ ...

# DESCRIPTION

**at** 在指定的时间执行命令。命令从标准输入或文件读取，稍后执行。结果会发送到用户的邮箱。必须有 **atd** 守护进程正在运行，作业才能执行。

# PARAMETERS

**-f file**
> 从文件而非标准输入读取命令

**-l**
> 列出所有排队中的作业（等价于 atq）

**-c job**
> 将指定作业的命令打印（cat）到标准输出

**-m**
> 作业完成时向用户发送邮件，即使没有任何输出

**-M**
> 从不向用户发送邮件

**-q queue**
> 使用指定的队列。队列是单个字母（a-z、A-Z）；字母顺序越靠后的队列以更高的 nice 值运行。"=" 队列保留给当前正在运行的作业。

**-t time**
> 以 [[CC]YY]MMDDhhmm[.ss] 格式在给定时间运行作业

**-r job**, **-d job**
> 删除指定的作业（等价于 atrm）

**-b**
> batch 的别名

**-v**
> 在读取作业前显示其将被执行的时间

# CONFIGURATION

**/etc/at.allow**
> 若该文件存在，则只有列于其中的用户才能用 at 安排作业。

**/etc/at.deny**
> 列于该文件中的用户被禁止使用 at。若 at.allow 存在，则忽略此文件。

# CAVEATS

需要 **atd** 守护进程正在运行。时间可用多种格式指定：HH:MM、midnight、noon、teatime（下午 4 点），或 "now + 5 minutes" 这类相对时间。

# HISTORY

属于传统 Unix 作业调度系统的一部分，早在 **1970 年代**的早期 Unix 中就已可用。现代 Linux 的 **at** 软件包主要由 Thomas Koenig 编写，此后由多位 Debian 贡献者维护。

# INSTALL

```apt: sudo apt install at```

```dnf: sudo dnf install at```

```pacman: sudo pacman -S at```

```apk: sudo apk add at```

```zypper: sudo zypper install at```

```nix: nix profile install nixpkgs#at```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[atq](/man/atq)(1), [atrm](/man/atrm)(1), [cron](/man/cron)(8), [batch](/man/batch)(1)

# RESOURCES

```[Source code](https://salsa.debian.org/debian/at)```

<!-- verified: 2026-06-17 -->
