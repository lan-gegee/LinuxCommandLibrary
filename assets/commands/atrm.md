# TAGLINE

从 at 队列中移除作业

# TLDR

**移除**已安排的作业

```atrm [job_number]```

移除**多个**作业

```atrm [1] [2] [3]```

# SYNOPSIS

**atrm** _job_ [_job_...]

# DESCRIPTION

**atrm** 从 at 队列中移除作业。作业通过 **atq** 显示的作业编号来标识。

用户只能移除自己的作业；root 可以移除任何作业。

# PARAMETERS

**job**
> 要移除的作业编号

# CAVEATS

无法移除已经在运行的作业。作业编号可通过 atq 查询。移除操作立即生效且不可撤销。

# HISTORY

**atrm** 是 **at** 命令套件（一次性作业调度）的一部分，自 1980 年代初期起就存在于 Unix 系统中。

# INSTALL

```apt: sudo apt install at```

```dnf: sudo dnf install at```

```pacman: sudo pacman -S at```

```apk: sudo apk add at```

```zypper: sudo zypper install at```

```nix: nix profile install nixpkgs#at```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[at](/man/at)(1), [atq](/man/atq)(1), [batch](/man/batch)(1)
