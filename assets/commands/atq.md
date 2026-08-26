# TAGLINE

列出 at 队列中待处理的作业

# TLDR

**列出**待处理的作业

```atq```

列出**指定队列**中的作业

```atq -q [a]```

为列出的作业指定自定义**时间格式**

```atq -o [%Y-%m-%d %H:%M]```

# SYNOPSIS

**atq** [_-V_] [_-q queue_] [_-o fmt_]

# DESCRIPTION

**atq** 列出 at 队列中待处理的作业。它显示已安排的一次性作业的编号、执行时间和队列标识。

这等价于 **at -l**。

# PARAMETERS

**-q** _queue_
> 仅显示指定队列中的作业。队列标识由单个字母（a-z 或 A-Z）组成。**at** 作业的默认队列为 **a**，**batch** 作业的默认队列为 **b**。

**-o** _fmt_
> 对列表中显示的日期和时间使用指定的 **strftime** 风格格式。

**-V**
> 将版本号打印到标准错误后退出。

# OUTPUT FORMAT

每行显示作业编号、计划执行的日期和时间、队列字母以及所属用户名。

# CAVEATS

非 root 用户只能看到自己的作业；超级用户可以看到所有人的作业。**atd** 守护进程未运行时作业不会执行，错过执行时机的过期作业仍会列在队列中，直到被移除为止。

# HISTORY

**atq** 是 at 命令套件的一部分，自 **1970 年代**起就在 Unix 中提供延迟命令执行功能。

# INSTALL

```apt: sudo apt install at```

```dnf: sudo dnf install at```

```pacman: sudo pacman -S at```

```apk: sudo apk add at```

```zypper: sudo zypper install at```

```nix: nix profile install nixpkgs#at```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[at](/man/at)(1), [atrm](/man/atrm)(1), [atd](/man/atd)(8), [cron](/man/cron)(8)

# RESOURCES

```[Source code](https://salsa.debian.org/debian/at)```

<!-- verified: 2026-06-17 -->
